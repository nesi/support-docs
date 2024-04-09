---
created_at: '2019-06-14T05:35:45Z'
tags: []
title: TensorFlow on CPUs
vote_count: 2

vote_sum: 2
zendesk_article_id: 360000997675
zendesk_section_id: 360000040076
---

{% set app_name = "TensorFlow" %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

TensorFlow is a popular software library for machine learning
applications, see our
[TensorFlow](../../Scientific_Computing/Supported_Applications/TensorFlow_on_GPUs.md)
article for further information. It is often used with GPUs, as runtimes
of the computationally demanding training and inference steps are often
shorter compared to multicore CPUs. However, running TensorFlow on CPUs
can nonetheless be attractive for projects where:

- Runtime is dominated by IO, so that computational performance of
    GPUs does not provide much advantage with respect to overall runtime
    and core-hour charges
- The workflow can benefit from parallel execution on many nodes with
    large aggregated IO bandwidth (e.g., running an inference task on a
    very large dataset, or training a large ensemble of models)

Tests with a machine learning application based on the Inception v3
network for image classification  using a Nvidia P100 GPU and 18 Intel
Broadwell cores on Mahuika (1/2 node) resulted in the following
GPU-vs-CPU speedups (based on full task runtimes including IO):

- 4x for training
- 2.6x for inference

Keep in mind that these numbers will depend strongly on the
application - they are only intended as an example.

## Choosing the right Python package

It is very important to choose the right TensorFlow package for optimal
performance. Intel provide [optimised TensorFlow
packages](https://software.intel.com/en-us/articles/intel-optimization-for-tensorflow-installation-guide)
with [Intel oneDNN](https://github.com/oneapi-src/oneDNN) (previously
called MKL-DNN) support for the conda package manager. It is not
recommended to build your own package, unless you need a specific
feature - if you do need to build TensorFlow yourself, make sure that
you include oneDNN.

All TensorFlow modules on Mahuika are GPU-optimised releases. To install
a CPU-optimised TensorFlow release on Mahuika, run

``` sh
module load Miniconda3
conda create -p /nesi/project/<project ID>/conda_envs/tf_cpu tensorflow-mkl
source activate /nesi/project/<project ID>/conda_envs/tf_cpu
```

To install TensorFlow on Māui Ancil, run

``` sh
module load Anaconda3
conda create -p /nesi/project/<project ID>/conda_envs/tf_cpu tensorflow-mkl
source activate /nesi/project/<project ID>/conda_envs/tf_cpu
```

Conda will create a new environment in your project directory with an
optimised CPU version of TensorFlow. You can choose a specific version
as well using the syntax "tensorflow-mkl==x.y.z".

When the installation is complete, import TensorFlow in Python as usual,

``` sh
python -c "import tensorflow"
```

**Important:** It is safe to ignore warning messages of the kind "The
TensorFlow library was not compiled to use \[...\] instructions \[...\]"
at runtime - Intel oneMKL will automatically use optimal processor
capabilities.

## Setting up Slurm on Mahuika

Runtime environment setup has a significant influence on performance.
The following Slurm script should work well as a starting point for a
TensorFlow job on a single Mahuika node:

``` sl
#!/bin/bash -e

#SBATCH --job-name=tensorflow
#SBATCH --account=<your NeSI account ID>
#SBATCH --time=<overall runtime estimate>
#SBATCH --mem=<overall memory consumption>
#SBATCH --partition=long
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=<number of threads>
#SBATCH --hint=nomultithread                    # No hyperthreading

# Allow threads to transition quickly
export KMP_BLOCKTIME=0
# Bind threads to cores
export KMP_AFFINITY=granularity=fine,compact,0,0

module load Miniconda3
source activate /nesi/project/<project ID>/conda_envs/tf_cpu
srun python my_tensorflow_program.py
```

If you are unsure about setting up the memory and runtime parameters,
have a look at our article [Ascertaining job
dimensions](../../Getting_Started/Next_Steps/Job_Scaling_Ascertaining_job_dimensions.md).
Please also read the section on operator parallelisation below before
you choose a number of CPUs.

Environment variables "KMP\_BLOCKTIME" and "KMP\_AFFINITY" configure
threading behaviour of the Intel oneDNN library. While these settings
should work well for a lot of applications, it is worth trying out
different setups (e.g., longer blocktimes) and compare runtimes. Please
see our article on [Thread Placement and Thread
Affinity](../../Scientific_Computing/HPC_Software_Environment/Thread_Placement_and_Thread_Affinity.md)
as well as this [Intel
article](https://software.intel.com/en-us/articles/tensorflow-optimizations-on-modern-intel-architecture)
for further information and tips for improving peformance on CPUs.

## Setting up operator parallelisation in TensorFlow 1.x

TensorFlow has the ability to execute a given operator using multiple
threads ("intra-operator parallelisation"), as well as different
operators in parallel ("inter-operator parallelisation"). Although
TensorFlow will try and guess values for these parameters, it can be
worth setting them up explicitly to maximise performance. Note that
these instructions are only valid for TensorFlow 1.x.

Insert the following code at the beginning of your program:

``` py
import os

# Get number of threads from Slurm
numThreads = int(os.getenv('SLURM_CPUS_PER_TASK',1))

# Set number of threads for inter-operator parallelism,
# start with a single thread
numInterOpThreads = 1

# The total number of threads must be an integer multiple
# of numInterOpThreads to make sure that all cores are used
assert numThreads % numInterOpThreads == 0

# Compute the number of intra-operator threads; the number
# of OpenMP threads for low-level libraries must be set to
# the same value for optimal performance
numIntraOpThreads = numThreads // numInterOpThreads
os.environ['OMP_NUM_THREADS'] = str(numIntraOpThreads)

# Import TensorFlow after setting OMP_NUM_THREADS to make sure
# that low-level libraries are initialised correctly
import tensorflow as tf

# Configure TensorFlow
config = tf.ConfigProto()
config.inter_op_parallelism_threads = numInterOpThreads
config.intra_op_parallelism_threads = numIntraOpThreads
tf.Session(config=config)
```

It depends on your application how beneficial each operator
parallelisation strategy is, so it is worth testing different
configurations.
