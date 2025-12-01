---
created_at: '2021-01-05T20:28:08Z'
tags:
- ai
- machine learning
- software
description: Information about using Lambda Stack
status: []
---

## Introduction

[Lambda
Stack](https://lambdalabs.com/lambda-stack-deep-learning-software) is an
AI software stack from Lambda containing PyTorch, TensorFlow, CUDA,
cuDNN and more. On the HPC you can run Lambda Stack via
[Apptainer](Apptainer.md) (based on the
official
[Dockerfiles](https://github.com/lambdal/lambda-stack-dockerfiles/)). We
have provided some pre-built container images (under
*/opt/nesi/containers/lambda-stack/*) or you can build your own. In the following sections, we will show you how to run
Lambda Stack in a Slurm job or interactively via
[JupyterLab](../../Scientific_Computing/Interactive_computing_with_OnDemand/Apps/JupyterLab/index.md).

You can list the available Lambda Stack version on NeSI by running:

``` sh
$ ls /opt/nesi/containers/lambda-stack
lambda-stack-focal-20201130.sif
lambda-stack-focal-20201221.sif
lambda-stack-focal-20210105.sif
lambda-stack-focal-latest.sif
README
```

In the filenames above, the dates correspond to the date the image was
built and the file with *-latest* will correspond to the most recent
version.

## Lambda Stack via Slurm

The following Slurm script can be used as a template for running jobs
using Lambda Stack.

``` sl
#!/bin/bash -e

#SBATCH --account               nesi12345
#SBATCH --job-name              lambdastack
#SBATCH --time                  00:15:00     # required walltime
#SBATCH --ntasks                1          # number of MPI tasks
#SBATCH --cpus-per-task         1   # number of threads per MPI task
#SBATCH --gpus-per-task         1   # optional, only if a GPU is required

# path to the container image file (optionally replace with your own)
SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

# clean environment
module purge

# for convenience store the apptainer command in an environment variable
# feel free to add additional binds if you need them 
CONTAINER="apptainer exec --nv -B ${PWD} ${SIF}"

# run a command in the container
${CONTAINER} echo "Hello World"
```

## Lambda Stack via Jupyter

The following steps will create a custom Lambda Stack kernel that can be
accessed via NeSI's Jupyter service (based on the instructions at
[Jupyter_on_NeSI](../../Interactive_Computing/OnDemand/Apps/JupyterLab/Jupyter_kernels_Tool_assisted_management.md)).

First, we need to create a kernel definition and wrapper that will
launch the container image. Run the following commands on the Mahuika
login node:

``` sh
# path to the container image file (optionally replace with your own)
export SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

# create a jupyter kernel using the Python within the container image
apptainer exec -B $HOME $SIF python -m ipykernel install --user \
        --name lambdastack --display-name="Lambda Stack Python 3"
```

If successful this should report that a `kernelspec` has been installed.
Change to the `kernelspec` directory:

``` sh
cd $HOME/.local/share/jupyter/kernels/lambdastack
```

and create a wrapper script for launching the kernel, named wrapper.sh:

``` sh
#!/usr/bin/env bash

# path to the container image file (optionally replace with your own)
SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

# clean environment
module purge

# unfortunately $HOME is not the canonical path to your home directory,
# we need to bind in canonical home path too so jupyter can find kernel
# connection file
homefull=$(readlink -e $HOME)

# for convenience store the container command in an environment variable
# feel free to add additional binds if you need them 
CONTAINER="apptainer exec --nv -B ${HOME},${homefull},${PWD} ${SIF}"

# run a command in the container
echo ${CONTAINER} python3 $@
${CONTAINER} python3 $@
```

Make the wrapper script executable:

``` sh
chmod +x wrapper.sh
```

Next, edit the *kernel.json* to change the first element of the `argv`
list to point to the wrapper script we just created. The file should
look like this (change &lt;username&gt; to your NeSI username):

``` json
{
"argv": [
"/home/<username>/.local/share/jupyter/kernels/lambdastack/wrapper.sh",
"-m",
"ipykernel_launcher",
"-f",
"{connection_file}"
],
"display_name": "Lambda Stack Python 3",
"language": "python"
}
```

After refreshing the [NeSI JupyterLab](https://jupyter.nesi.org.nz/)
your Lambda Stack Python kernel should show up as "Lambda Stack Python
3".

<!-- 
NOTE: The following information is out of date and doesn't seem essential to update
## Example: running Transformers benchmarks

Here we give an example showing using Lambda Stack to run the
[Transformers](https://huggingface.co/transformers/) library benchmarks.
Transformers is a natural language processing library that uses either
TensorFlow or PyTorch underneath. While both PyTorch and TensorFlow are
included in the Lambda Stack distribution, the Transformers library is
not, so the first thing we do is create a virtual environment and
install transformers into it:

``` sh
# create a directory and change to it
mkdir /nesi/project/<project_code>/transformers-benchmarks
cd /nesi/project/<project_code>/transformers-benchmarks

# path to the container image file (optionally replace with your own)
export SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

# launch a bash shell in the container image
apptainer exec -B $PWD $SIF bash
```

After executing the above command your prompt should have changed to
*Singularity&gt;*, the following commands are all executed at this
prompt (i.e. within the container):

``` sh
virtualenv --system-site-packages transenv
source transenv/bin/activate
pip install transformers psutil py3nvml

# exit the container bash prompt
exit
```

Note we used `--system-site-packages`` so that we can use the Lambda
Stack installed TensorFlow, PyTorch, etc., instead of installing them
separately.

Now clone the transformers git repo so we can run the benchmark script
(these commands run outside the container):

``` sh
git clone https://github.com/huggingface/transformers.git
```

Create the following script for running the benchmarks, named
*run-benchmark-torch.sh*:

``` sh
#!/bin/bash -e

# load the virtual environment with transformers installed
source transenv/bin/activate

# path to transformers benchmark script
BENCH_SCRIPT=transformers/examples/pytorch/benchmarking/run_benchmark.py

# run the benchmarks
python ${BENCH_SCRIPT} --no_multi_process --training --no_memory \
                       --save_to_csv --env_print \
                       --models bert-base-cased bert-large-cased \
                                bert-large-uncased gpt2 \
                                gpt2-large gpt2-xl \
                       --batch_sizes 8 \
                       --sequence_lengths 8 32 128 512
```

Now create a Slurm script that will launch the job, names
*run-benchmark-torch.sl*:

``` sl
#!/bin/bash -e

#SBATCH --account               nesi12345
#SBATCH --job-name              lambdastack
#SBATCH --time                  00:30:00
#SBATCH --ntasks                1
#SBATCH --cpus-per-task         1
#SBATCH --gpus-per-task         1
#SBATCH --mem                   12G

# path to the container image file (optionally replace with your own)
SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

# clean environment
module purge

# for convenience store the container command in an environment variable
CONTAINER="apptainer exec --nv -B ${PWD} ${SIF}"

# print PyTorch version and number of GPUs detected
${CONTAINER} python3 -c "import torch; print('torch version', torch.__version__)"
${CONTAINER} python3 -c "import torch; print('num devices', torch.cuda.device_count())"

# run the benchmark script we created
${CONTAINER} bash ./run-benchmark-torch.sh
```

Submit this job to Slurm and then wait for the benchmarks to run:

``` sh
sbatch run-benchmark-torch.sl
``` -->
