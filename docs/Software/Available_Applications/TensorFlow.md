---
created_at: '2019-06-03T23:54:50Z'
tags:
- gpu
---

{% set app_name = "TensorFlow" %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

TensorFlow is an open source library for machine learning. TensorFlow
can train and run deep neural networks. It can also serve as a backend
for other techniques requiring automatic differentiation and GPU
acceleration.

TensorFlow is callable from Python with the numerically intensive parts
of the algorithms implemented in C++ for efficiency, and can run on both
CPUs and GPUs. It includes Keras, the high-level API used to build and
train most TensorFlow models. This page covers how to load TensorFlow,
then how to run it on CPUs and on GPUs.

## How to load TensorFlow

There are several ways to make TensorFlow available, whether you intend to
run on CPUs or GPUs: load it from an environment module, install it into
your own Python virtual environment or conda environment, or run it from
an Apptainer container.

### Loading TensorFlow from modules

TensorFlow is available on Mahuika as an [environment module](index.md):

``` sh
module load TensorFlow/2.13.0-gimkl-2022a-Python-3.11.3
```

List the available versions with:

``` sh
module spider TensorFlow
```

The module automatically loads the matching CUDA and cuDNN modules needed
to run TensorFlow on GPUs.

### Installing TensorFlow in a Python virtual environment

A virtual environment keeps your project's packages separate and lets you
install additional Python packages alongside TensorFlow:

``` sh
# Load python
module purge
module load Python/3.11.6-foss-2023a
export PYTHONNOUSERSITE=1

# Move into your folder for python virtual environments in project
mkdir -p /nesi/project/<project id>/${USER}/py_virtual_envs
cd /nesi/project/<project id>/${USER}/py_virtual_envs

# Make your python virtual environment
python3 -m venv my_tf_venv

# Activate your python virtual environment
source /nesi/project/<project id>/${USER}/py_virtual_envs/my_tf_venv/bin/activate
```

Then install the build you need. The default `tensorflow` package is
CPU-only; for GPU support install `tensorflow[and-cuda]`, which bundles
the required CUDA libraries (so you do not need to load CUDA/cuDNN
modules):

``` sh
pip install --upgrade pip           # Update pip
pip install tensorflow              # CPU-only
pip install 'tensorflow[and-cuda]'  # GPU (CUDA included)
```

Set `export PYTHONNOUSERSITE=1` so the environment stays isolated from
packages in your home folder. Activate it again before running your
scripts in a Slurm job:

``` sh
source /nesi/project/<project id>/${USER}/py_virtual_envs/my_tf_venv/bin/activate
```

### Installing TensorFlow in a conda environment

A conda environment lets you pick a specific version of Python and
TensorFlow. On Mahuika, use the [Miniforge3 module](Miniforge3.md):

``` sh
# Load conda
module purge && module load Miniforge3
source $(conda info --base)/etc/profile.d/conda.sh
export PYTHONNOUSERSITE=1

# Move into your folder for conda environments in project
mkdir -p /nesi/project/<project id>/${USER}/conda_envs
cd /nesi/project/<project id>/${USER}/conda_envs

# Make your conda environment
conda create -p ./my_tf_conda_venv python=3.11

# Activate your conda environment
conda activate ./my_tf_conda_venv
```

Then install the build you need with `pip`. As above, the default package
is CPU-only and `tensorflow[and-cuda]` adds GPU support with CUDA bundled:

``` sh
pip install --upgrade pip           # Update pip
pip install tensorflow              # CPU-only
pip install 'tensorflow[and-cuda]'  # GPU (CUDA included)
```

### Apptainer containers

You can use containers to run your application on the Mahuika platform. We
provide support for [Apptainer](Apptainer.md)
containers, that can be run by users without requiring additional
privileges. Note that Docker containers can be converted into
Apptainer containers.

For TensorFlow, we recommend using the [official container provided by
NVIDIA](https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow).
More information about using Apptainer with GPU enabled containers is
available on the [NVIDIA GPU Containers](../Containers/NVIDIA_GPU_Containers.md)
support page.

## TensorFlow on CPUs

TensorFlow usually runs faster on GPUs, but CPUs can be the better choice
when:

1. Your workflow is I/O-bound, or
2. Your workflow can spread across many nodes for aggregate bandwidth, or
3. Your workflow trains a large ensemble of small models.

These are cases where GPU compute gives little benefit for the core-hour
cost.

### Slurm script

The following is a good starting point for a single-node CPU job:

``` sl
#!/bin/bash -e

#SBATCH --job-name=tensorflow
#SBATCH --account=<your Mahuika project ID>
#SBATCH --time=<overall runtime estimate>
#SBATCH --mem=<overall memory consumption>
#SBATCH --cpus-per-task=<number of threads>

# Pin threads to cores for consistent performance
export OMP_PROC_BIND=true
export OMP_PLACES=cores

module purge
module load Python/3.11.6-foss-2023a
source /nesi/project/<project id>/${USER}/py_virtual_envs/my_tf_venv/bin/activate
srun python my_tensorflow_program.py
```

Pinning threads with `OMP_PROC_BIND` and `OMP_PLACES` gives more consistent timings
because nodes are shared between jobs — see [Thread Placement and Thread
Affinity](../Parallel_Computing/Thread_Placement_and_Thread_Affinity.md).
For help sizing `--mem` and
`--time`, see [Ascertaining job
dimensions](../Profiling_and_Debugging/Job_Scaling_Ascertaining_job_dimensions.md).

### Controlling thread parallelism

TensorFlow can run a single operator across multiple threads ("intra-op"
parallelism) and run independent operators concurrently ("inter-op"
parallelism). It chooses defaults automatically, but setting them
explicitly can improve performance. Add the following to the start of your
program, before any operations run:

``` py
import os
import tensorflow as tf

# Total threads available from Slurm
numThreads = int(os.getenv('SLURM_CPUS_PER_TASK', 1))

# Start with a single inter-op thread; the remainder go to intra-op
numInterOpThreads = 1
assert numThreads % numInterOpThreads == 0
numIntraOpThreads = numThreads // numInterOpThreads

tf.config.threading.set_inter_op_parallelism_threads(numInterOpThreads)
tf.config.threading.set_intra_op_parallelism_threads(numIntraOpThreads)
```

The best split depends on your model, so it is worth testing a few
configurations.

## TensorFlow on GPUs

To run on a GPU, set up TensorFlow using any of the methods in [How to
load TensorFlow](#how-to-load-tensorflow) — when installing with `pip`,
use the `tensorflow[and-cuda]` package — and request a GPU in your Slurm
script with `--gpus-per-node` (see [GPU use on
Mahuika](../../Batch_Computing/Using_GPUs.md)).

You can confirm that TensorFlow can see the GPU with:

``` sh
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

### Example: training a Keras model on a GPU

This example trains a small convolutional neural network, built with
Keras, to classify the MNIST handwritten digits on a single GPU. It uses
the GPU-optimised TensorFlow module, which loads the matching CUDA and
cuDNN libraries automatically.

1. Save the following training script as `mnist_cnn.py`:

    ``` py
    import tensorflow as tf

    # Confirm TensorFlow can see the GPU
    print("GPUs available:", tf.config.list_physical_devices("GPU"))

    # Load and normalise the MNIST handwritten-digit dataset
    # (downloaded and cached under ~/.keras/datasets on first run)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train[..., None] / 255.0
    x_test = x_test[..., None] / 255.0

    # Build a small convolutional network with Keras
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(28, 28, 1)),
        tf.keras.layers.Conv2D(32, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ])
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    # Train, then evaluate on the held-out test set
    model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.1)
    model.evaluate(x_test, y_test)
    ```

2. Save the following job submission script as `mnist.sl`:

    ``` sl
    #!/bin/bash -e
    #SBATCH --job-name=tensorflow-mnist
    #SBATCH --account=<your Mahuika project ID>
    #SBATCH --gpus-per-node=L4:1
    #SBATCH --cpus-per-task=2
    #SBATCH --mem=8G
    #SBATCH --time=00:10:00
    #SBATCH --output=slurm-%j.out       # standard output (%j = job ID)
    #SBATCH --error=slurm-%j.err        # standard error

    module purge
    module load TensorFlow/2.13.0-gimkl-2022a-Python-3.11.3

    python mnist_cnn.py
    ```

3. Submit the job:

    ``` sh
    sbatch mnist.sl
    ```

When the job finishes, the per-epoch training and validation accuracy, and
the final test accuracy, are written to the standard output file
`slurm-<JOBID>.out` (where `<JOBID>` is the Slurm job ID). Near the top of
that file you should also see the GPU that TensorFlow detected. TensorFlow's
own log messages and any warnings go to the matching `slurm-<JOBID>.err`
file.
