Introduction
============

[Lambda
Stack](https://lambdalabs.com/lambda-stack-deep-learning-software) is an
AI software stack from Lambda containing PyTorch, TensorFlow, CUDA,
cuDNN and more. On NeSI you can run Lambda Stack via
[Singularity](https://sylabs.io/guides/3.7/user-guide/) (based on the
official
[Dockerfiles](https://github.com/lambdal/lambda-stack-dockerfiles/)). We
have provided some prebuilt Singularity images (under
*/opt/nesi/containers/lambda-stack/*) or you can build your own (see the
guide below). In the following sections, we will show you how to run
Lambda Stack in a Slurm job or interactively via
[JupyterLab](https://support.nesi.org.nz/hc/en-gb/articles/360001555615-Jupyter-on-NeSI).

You can list the available Lambda Stack version on NeSI by running:

    $ ls /opt/nesi/containers/lambda-stack
    lambda-stack-focal-20201130.sif
    lambda-stack-focal-20201221.sif
    lambda-stack-focal-20210105.sif
    lambda-stack-focal-latest.sif
    README

In the filenames above, the dates correspond to the date the image was
built and the file with *-latest* will correspond to the most recent
version.

Building the Singularity image (optional)
=========================================

This step is optional; if you choose to use the prebuilt Singularity
images under */opt/nesi/containers/lambda-stack/* you can skip this
step.

Note that Singularity images are immutable, so the versions of packages
in the image are a snapshot of the available versions from when the
image was built. If you need more recent versions of packages, you
can\'t just update them within the image, instead you must build a new
Singularity image with the required versions.

Official
[Dockerfiles](https://github.com/lambdal/lambda-stack-dockerfiles/) are
provided for Lambda Stack but Docker can\'t be used on NeSI for security
reasons, hence the need to create a Singularity image. Both Docker and
Singularity require root access to build images (but Singularity does
not require root to run them), so you will need to build the images
somewhere you have admin rights (e.g. your laptop). These steps should
work on Linux; if you run another operating system you could try
installing an Ubuntu VM in
[VirtualBox](https://www.virtualbox.org/wiki/Downloads).

Make sure you have [Docker](https://docs.docker.com/get-docker/) and
[Singularity](https://sylabs.io/guides/3.7/user-guide/quick_start.html#quick-installation-steps)
installed first and then follow the steps below.

    # clone the lambda stack Dockerfiles repo
    git clone https://github.com/lambdal/lambda-stack-dockerfiles.git
    cd lambda-stack-dockerfiles

    # build the Docker image
    sudo docker build -t lambda-stack:20.04 -f Dockerfile.focal .

    # build the Singularity image from the Docker image
    sudo singularity build lambda-stack-focal-$(date +%Y%m%d).sif docker-daemon:lambda-stack:20.04

Note that the Docker build will require a lot of disk space during the
build (\~40GB) and the final image will be \~14GB. The Singularity image
will be \~5GB and will also require a lot of space during the build. If
you don\'t have enough space in */tmp* for the Singularity build you
could try running the following script (updating paths first) as root
(e.g. using *sudo*):

    #!/bin/bash
    export SINGULARITY_TMPDIR=/path/to/somewhere/with/lots/of/space
    export SINGULARITY_CACHEDIR=/path/to/somewhere/else/with/lots/of/space
    singularity build lambda-stack-focal-$(date +%Y%m%d).sif docker-daemon:lambda-stack:20.04

 

Lambda Stack via Slurm
======================

The following Slurm script can be used as a template for running jobs
using Lambda Stack.

    #!/bin/bash
    #SBATCH --job-name=lambdastack
    #SBATCH --time=00:15:00     # required walltime
    #SBATCH --ntasks=1          # number of MPI tasks
    #SBATCH --cpus-per-task=1   # number of threads per MPI task
    #SBATCH --gpus-per-task=1   # optional, only if a GPU is required

    # path to the singularity image file (optionally replace with your own)
    SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

    # load environment modules (these are always required)
    ml purge
    ml Singularity

    # for convenience store the singularity command in an environment variable
    # feel free to add additional binds if you need them 
    SINGULARITY="singularity exec --nv -B ${PWD} ${SIF}"

    # run a command in the container
    ${SINGULARITY} echo "Hello World"

Lambda Stack via Jupyter
========================

The following steps will create a custom Lambda Stack kernel that can be
accessed via NeSI\'s Jupyter service (based on the instructions
[here](https://support.nesi.org.nz/hc/en-gb/articles/360001555615-Jupyter-on-NeSI#adding_a_custom_python_kernel)).

First, we need to create a kernel definition and wrapper that will
launch the Singularity image. Run the following commands on the Mahuika
login node:

    # load the Singularity envioronment module
    ml Singularity

    # path to the singularity image file (optionally replace with your own)
    export SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

    # create a jupyter kernel using the Python within the Singularity image
    singularity exec -B $HOME $SIF python -m ipykernel install --user \
            --name lambdastack --display-name="Lambda Stack Python 3"

If successful this should report that a kernelspec has been installed.
Change to the kernelspec directory:

    cd $HOME/.local/share/jupyter/kernels/lambdastack

and create a wrapper script for launching the kernel, named wrapper.sh:

    #!/usr/bin/env bash

    # path to the singularity image file (optionally replace with your own)
    SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

    # load environment modules (these are always required)
    ml purge
    ml Singularity

    # unfortunately $HOME is not the canonical path to your home directory,
    # we need to bind in canonical home path too so jupyter can find kernel
    # connection file
    homefull=$(readlink -e $HOME)

    # for convenience store the singularity command in an environment variable
    # feel free to add additional binds if you need them 
    SINGULARITY="singularity exec --nv -B ${HOME},${homefull},${PWD} ${SIF}"

    # run a command in the container
    echo ${SINGULARITY} python3 $@
    ${SINGULARITY} python3 $@

Make the wrapper script executable:

    chmod +x wrapper.sh

Next, edit the *kernel.json* to change the first element of the argv
list to point to the wrapper script we just created. The file should
look like this (change \<username\> to your NeSI username):

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

After refreshing the [NeSI JupyterLab](https://jupyter.nesi.org.nz/)
your Lambda Stack Python kernel should show up as \"Lambda Stack Python
3\".

Example: running Transformers benchmarks
========================================

Here we give an example showing using Lambda Stack to run the
[Transformers](https://huggingface.co/transformers/) library benchmarks.
Transformers is a natural language processing library that uses either
TensorFlow or PyTorch underneath. While both PyTorch and TensorFlow are
included in the Lambda Stack distribution, the Transformers library is
not, so the first thing we do is create a virtual environment and
install transformers into it:

    # load the Singularity environment module
    ml Singularity

    # create a directory and change to it
    mkdir /nesi/project/<project_code>/transformers-benchmarks
    cd /nesi/project/<project_code>/transformers-benchmarks

    # path to the singularity image file (optionally replace with your own)
    export SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

    # launch a bash shell in the Singularity image
    singularity exec -B $PWD $SIF bash

After executing the above command your prompt should have changed to
*Singularity\>*, the following commands are all executed at this prompt
(i.e. within the container):

    virtualenv --system-site-packages transenv
    source transenv/bin/activate
    pip install transformers psutil py3nvml

    # exit the Singularity container bash prompt
    exit

Note we used *\--system-site-packages* so that we can use the Lambda
Stack installed TensorFlow, PyTorch, etc., instead of installing them
separately.

Now clone the transformers git repo so we can run the benchmark script
(these commands run outside the container):

    git clone https://github.com/huggingface/transformers.git

Create the following script for running the benchmarks, named
*run-benchmark-torch.sh*:

    #!/bin/bash -e

    # load the virtual environment with transformers installed
    source transenv/bin/activate

    # path to transformers benchmark script
    BENCH_SCRIPT=transformers/examples/benchmarking/run_benchmark.py

    # run the benchmarks
    python ${BENCH_SCRIPT} --no_multi_process --training --no_memory \
                           --save_to_csv --env_print \
                           --models bert-base-cased bert-large-cased \
                                    bert-large-uncased gpt2 \
                                    gpt2-large gpt2-xl \
                           --batch_sizes 8 \
                           --sequence_lengths 8 32 128 512

Now create a Slurm script that will launch the job, names
*run-benchmark-torch.sl*:

    #!/bin/bash
    #SBATCH --job-name=lambdastack
    #SBATCH --time=00:30:00
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --gpus-per-task=1
    #SBATCH --mem=12G

    # path to the singularity image file (optionally replace with your own)
    SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif

    # load environment modules (these are always required)
    ml purge
    ml Singularity

    # for convenience store the singularity command in an environment variable
    SINGULARITY="singularity exec --nv -B ${PWD} ${SIF}"

    # print PyTorch version and number of GPUs detected
    ${SINGULARITY} python3 -c "import torch; print('torch version', torch.__version__)"
    ${SINGULARITY} python3 -c "import torch; print('num devices', torch.cuda.device_count())"

    # run the benchmark script we created
    ${SINGULARITY} bash ./run-benchmark-torch.sh

Submit this job to Slurm and then wait for the benchmarks to run:

    sbatch run-benchmark-torch.sl

 

 

 
