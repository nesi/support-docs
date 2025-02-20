---
created_at: '2019-06-03T23:54:50Z'
tags:
- gpu
title: TensorFlow on GPUs
vote_count: 2

vote_sum: 2
zendesk_article_id: 360000990436
zendesk_section_id: 360000040076
---

{% set app_name = "TensorFlow" %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

TensorFlow is an open source library for machine learning. TensorFlow
can train and run deep neural networks. It can also serve as a backend
for other techniques requiring automatic differentiation and GPU
acceleration.

TensorFlow is callable from Python with the numerically intensive parts
of the algorithms implemented in C++ for efficiency. This page focus on
running TensorFlow with GPU support.

!!! tip "See also"
     -   To request GPU resources using `--gpus-per-node` option of Slurm,
         see the [GPU use on NeSI](GPU_use_on_NeSI.md)
         documentation page.
     -   To run TensorFlow on CPUs instead, have a look at our article
         [TensorFlow on CPUs](TensorFlow_on_CPUs.md)
         for tips on how to configure TensorFlow and Slurm for optimal
         performance.

## Use NeSI modules

TensorFlow is available on Mahuika as an [environment module](The_HPC_environment.md)

``` sh
module load TensorFlow/2.4.1-gimkl-2020a-Python-3.8.2
```

Note this will automatically load the right versions of CUDA and cuDNN
modules needed to run TensorFlow on GPUs.

You can list the available versions of the module using:

``` sh
module spider TensorFlow
```

To install additional Python packages for your project, you can either:

1. install packages in your home folder,
2. install packages in a dedicated Python virtual environment for your
    project.

The first option is easy but will consume space in your home folder and
can create conflicts if you have multiple projects with different
versions requirements. To install packages this way, you need to
use`pip install --user`. For example, to install the SciKeras package:

``` sh
pip install --user scikeras
```

The second option provides a better separation between projects.
Additionally, it saves space in your home folder if you create your
virtual environments in the project or nobackup folder. The following
example illustrates how to create a virtual environment, activate it and
install the SciKeras package in it with `pip`:

``` sh
$ export PYTHONNOUSERSITE=1
$ python3 -m venv --system-site-packages my_venv
$ source my_venv/bin/activate
(my_venv) $ pip install scikeras
```

where `my_venv` is the path of the virtual environment folder.

The `--system-site-packages` option allows the virtual environment to
access the TensorFlow package provided by the environment module
previously loaded:

``` sh
$ module load TensorFlow/2.4.1-gimkl-2020a-Python-3.8.2
$ source my_venv/bin/activate
(my_venv) $ python -c "import tensorflow as tf; print(tf.__version__)"
[...]
2.4.1
```

Don't forget to activate the virtual environment *before* calling your
Python scripts in a Slurm submission script, using:

``` sh
source <path_to_virtual_environment>/bin/activate
```

!!! warning "Virtual environment isolation"
     Use `export PYTHONNOUSERSITE=1` to ensure that your virtual
     environment is isolated from packages installed in your home folder
     `~/.local/lib/python3.8/site-packages/`.

## Conda environments

As an alternative, you can also create *conda* environments to install a
specific version of Python, TensorFlow and any additional packages
required for your project. On Mahuika, use the Miniconda3 module:

``` sh
export PYTHONNOUSERSITE=1
module load Miniconda3/4.9.2
conda create -p my_conda_venv python=3.8
```

Note that here we use the `-p` option to create the conda environment in
a local `my_conda_venv` folder. Use a subfolder in your project or
nobackup folder to save space in your home folder.

Then activate the conda environment and install TensorFlow using
`conda install` or `pip install`, depending on your preferences:

``` sh
source $(conda info --base)/etc/profile.d/conda.sh  # if you didn't use "conda init" to set your .bashrc
conda activate ./my_conda_venv
pip install tensorflow==2.5.0
```

To use TensorFlow on GPUs, you also need to load cuDNN/CUDA modules with
the proper versions. See the official documentation about [tested configurations](https://www.tensorflow.org/install/source#gpu) for
compatibilities. For example, Tensorflow 2.5.0 requires you to load the
`cuDNN/8.1.1.33-CUDA-11.2.0` module:

``` sh
module load cuDNN/8.1.1.33-CUDA-11.2.0  # for Tensorflow 2.5
```

You can list the available versions of cuDNN (and associated CUDA
module) using:

``` sh
module spider cuDNN
```

Please contact us at [support@nesi.org.nz](mailto:support@nesi.org.nz) if you need a version not
available on the platform.

!!! note "Māui Ancillary Nodes"
     -   Load the Anaconda3 module instead of Miniconda3 to manipulate
         conda environments:  
         ``` sl
         module load Anaconda3/2020.02-GCC-7.1.0
         ```
     -   Use `module avail` to list available versions of modules, e.g.
         ``` sl
         module avail cuDNN
         ```

Additionnally, depending your version of TensorFlow, you may need to
take into consideration the following:

- install the `tensorflow-gpu` Python package if your are using
    TensorFlow 1,
- make sure to use a supported version of Python when creating the
    conda environment (e.g. TensorFlow 1.14.0 requires Python 3.3 to
    3.7),
- use `conda install` (not `pip install`) if your version of
    TensorFlow relies on GCC 4.8 (TensorFlow &lt; 1.15).

!!! tip
     Make sure to use `module purge` before loading Miniconda3, to ensure
     that no other Python module is loaded and could interfere with your
     conda environment.

    ``` sh
    module purge
    module load Miniconda3/4.9.2
    export PYTHONNOUSERSITE=1
    source $(conda info --base)/etc/profile.d/conda.sh  # if you didn't use "conda init" to set your .bashrc
    conda ...  # any conda commands (create, activate, install...)
    ```

## Singularity containers

You can use containers to run your application on the NeSI platform. We
provide support for
[Singularity](Singularity.md)
containers, that can be run by users without requiring additional
privileges. Note that Docker containers can be converted into
Singularity containers.

For TensorFlow, we recommend using the [official container provided by NVIDIA](https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow).
More information about using Singularity with GPU enabled containers is
available on the [NVIDIA GPU Containers](NVIDIA_GPU_Containers.md)
support page.

## Specific versions for A100

Here are the recommended options to run TensorFlow on the A100 GPUs:

- If you use TensorFlow 1, use the TF1 [container provided by NVIDIA](https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow),
    which comes with a version of TensorFlow 1.15 compiled specifically
    to support the A100 GPUs (Ampere architecture). Other official
    Python packages won't support the A100, triggering various crashes
    and slowdowns.
- If you use TensorFlow 2, any version from 2.4 and above will provide
    support for the A100 GPUs.

## Example Slurm script

In the following example, we will use the
[make\_image\_classifier](https://github.com/tensorflow/hub/blob/r0.12/tensorflow_hub/tools/make_image_classifier/make_image_classifier.py)
provided by [TensorFlow Hub](https://www.tensorflow.org/hub) to
illustrate a training workflow. The example task consists in retraining
the last layers of an already trained deep neural network in order to
make it classify pictures of flowers. This type of task is known as
"transfer learning".

1. Create a virtual environment to install the
    `tensorflow-hub[make_image_classifier]` package:

    ``` sh
    module purge  # start from a clean environment
    module load TensorFlow/2.4.1-gimkl-2020a-Python-3.8.2
    export PYTHONNOUSERSITE=1
    python3 -m venv --system-site-packages tf_hub_venv
    source tf_hub_venv/bin/activate
    pip install tensorflow-hub[make_image_classifier]~=0.12
    ```

2. Download and uncompress the example dataset containing labelled
    photos of flowers (daisies, dandelions, roses, sunflowers and
    tulips):

    ``` sl
    wget http://download.tensorflow.org/example_images/flower_photos.tgz -O - | tar -xz
    ```

3. Copy the following code in a job submission script named
    `flowers.sl`:

    ``` sl
    #!/bin/bash -e
    #SBATCH --job-name=flowers-example
    #SBATCH --gpus-per-node=1
    #SBATCH --cpus-per-task=2
    #SBATCH --time 00:10:00
    #SBATCH --mem 4G

    # load TensorFlow module and activate the virtual environment
    module purge
    module load TensorFlow/2.4.1-gimkl-2020a-Python-3.8.2
    export PYTHONNOUSERSITE=1
    source tf_hub_venv/bin/activate

    # select a model to train, here MobileNetV2
    MODEL_URL="https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"

    # run the training script
    make_image_classifier \
      --image_dir flower_photos \
      --tfhub_module "$MODEL_URL" \
      --image_size 224 \
      --saved_model_dir "model-${SLURM_JOBID}"
    ```

4. Submit the job:

    ``` sh
    sbatch flowers.sl
    ```

Once the job has finished, the trained model will be saved in a
`results-JOBID` folder, where `JOBID` is the Slurm job ID number.

All messages printed by TensorFlow during the training, including
training and validation accuracies, are captured in the Slurm output
file, named `slurm-JOBID.out` by default.

!!! tip
     While your job is running, you can monitor the progress of model
     training using `tail -f` on the Slurm output file:
     ``` sl
     tail -f slurm-JOBID.out  # replace JOBID with an actual number
     ```
     Press CTRL+C to get the bash prompt back.
