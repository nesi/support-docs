---
created_at: '2021-01-05T20:28:08Z'
hidden: false
label_names: []
position: 8
title: Lambda Stack
vote_count: 1
vote_sum: 1
zendesk_article_id: 360002558216
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h1>Introduction</h1>
<p><a href="https://lambdalabs.com/lambda-stack-deep-learning-software" target="_blank" rel="noopener">Lambda Stack</a> is an AI software stack from Lambda containing PyTorch, TensorFlow, CUDA, cuDNN and more. On NeSI you can run Lambda Stack via <a href="https://sylabs.io/guides/3.7/user-guide/" target="_blank" rel="noopener">Singularity</a> (based on the official <a href="https://github.com/lambdal/lambda-stack-dockerfiles/" target="_blank" rel="noopener">Dockerfiles</a>). We have provided some prebuilt Singularity images (under <em>/opt/nesi/containers/lambda-stack/</em>) or you can build your own (see the guide below). In the following sections, we will show you how to run Lambda Stack in a Slurm job or interactively via <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615-Jupyter-on-NeSI" target="_blank" rel="noopener">JupyterLab</a>.</p>
<p>You can list the available Lambda Stack version on NeSI by running:</p>
<pre>$ ls /opt/nesi/containers/lambda-stack<br>lambda-stack-focal-20201130.sif<br>lambda-stack-focal-20201221.sif<br>lambda-stack-focal-20210105.sif<br>lambda-stack-focal-latest.sif<br>README</pre>
<p>In the filenames above, the dates correspond to the date the image was built and the file with <em>-latest</em> will correspond to the most recent version.</p>
<h1>Building the Singularity image (optional)</h1>
<p>This step is optional; if you choose to use the prebuilt Singularity images under <em>/opt/nesi/containers/lambda-stack/</em> you can skip this step.</p>
<p>Note that Singularity images are immutable, so the versions of packages in the image are a snapshot of the available versions from when the image was built. If you need more recent versions of packages, you can't just update them within the image, instead you must build a new Singularity image with the required versions.</p>
<p>Official <a href="https://github.com/lambdal/lambda-stack-dockerfiles/" target="_blank" rel="noopener">Dockerfiles</a> are provided for Lambda Stack but Docker can't be used on NeSI for security reasons, hence the need to create a Singularity image. Both Docker and Singularity require root access to build images (but Singularity does not require root to run them), so you will need to build the images somewhere you have admin rights (e.g. your laptop). These steps should work on Linux; if you run another operating system you could try installing an Ubuntu VM in <a href="https://www.virtualbox.org/wiki/Downloads" target="_blank" rel="noopener">VirtualBox</a>.</p>
<p>Make sure you have <a href="https://docs.docker.com/get-docker/" target="_blank" rel="noopener">Docker</a> and <a href="https://sylabs.io/guides/3.7/user-guide/quick_start.html#quick-installation-steps" target="_blank" rel="noopener">Singularity</a> installed first and then follow the steps below.</p>
<pre># clone the lambda stack Dockerfiles repo<br>git clone https://github.com/lambdal/lambda-stack-dockerfiles.git<br>cd lambda-stack-dockerfiles<br><br># build the Docker image<br>sudo docker build -t lambda-stack:20.04 -f Dockerfile.focal .<br><br># build the Singularity image from the Docker image<br>sudo singularity build lambda-stack-focal-$(date +%Y%m%d).sif docker-daemon:lambda-stack:20.04</pre>
<p>Note that the Docker build will require a lot of disk space during the build (~40GB) and the final image will be ~14GB. The Singularity image will be ~5GB and will also require a lot of space during the build. If you don't have enough space in <em>/tmp</em> for the Singularity build you could try running the following script (updating paths first) as root (e.g. using <em>sudo</em>):</p>
<pre>#!/bin/bash<br>export SINGULARITY_TMPDIR=/path/to/somewhere/with/lots/of/space<br>export SINGULARITY_CACHEDIR=/path/to/somewhere/else/with/lots/of/space<br>singularity build lambda-stack-focal-$(date +%Y%m%d).sif docker-daemon:lambda-stack:20.04</pre>
<p> </p>
<h1>Lambda Stack via Slurm</h1>
<p>The following Slurm script can be used as a template for running jobs using Lambda Stack.</p>
<pre>#!/bin/bash<br>#SBATCH --job-name=lambdastack<br>#SBATCH --time=00:15:00     # required walltime<br>#SBATCH --ntasks=1          # number of MPI tasks<br>#SBATCH --cpus-per-task=1   # number of threads per MPI task<br>#SBATCH --gpus-per-task=1   # optional, only if a GPU is required<br><br># path to the singularity image file (optionally replace with your own)<br>SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif<br><br># load environment modules (these are always required)<br>module purge<br>module load Singularity<br><br># for convenience store the singularity command in an environment variable<br># feel free to add additional binds if you need them <br>SINGULARITY="singularity exec --nv -B ${PWD} ${SIF}"<br><br># run a command in the container<br>${SINGULARITY} echo "Hello World"</pre>
<h1>Lambda Stack via Jupyter</h1>
<p>The following steps will create a custom Lambda Stack kernel that can be accessed via NeSI's Jupyter service (based on the instructions <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615-Jupyter-on-NeSI#adding_a_custom_python_kernel" target="_blank" rel="noopener">here</a>).</p>
<p>First, we need to create a kernel definition and wrapper that will launch the Singularity image. Run the following commands on the Mahuika login node:</p>
<pre># load the Singularity envioronment module<br>module load Singularity<br><br># path to the singularity image file (optionally replace with your own)<br>export SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif<br><br># create a jupyter kernel using the Python within the Singularity image<br>singularity exec -B $HOME $SIF python -m ipykernel install --user \<br>        --name lambdastack --display-name="Lambda Stack Python 3"</pre>
<p>If successful this should report that a kernelspec has been installed. Change to the kernelspec directory:</p>
<pre>cd $HOME/.local/share/jupyter/kernels/lambdastack</pre>
<p>and create a wrapper script for launching the kernel, named wrapper.sh:</p>
<pre>#!/usr/bin/env bash<br><br># path to the singularity image file (optionally replace with your own)<br>SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif<br><br># load environment modules (these are always required)<br>module purge<br>module load Singularity<br><br># unfortunately $HOME is not the canonical path to your home directory,<br># we need to bind in canonical home path too so jupyter can find kernel<br># connection file<br>homefull=$(readlink -e $HOME)<br><br># for convenience store the singularity command in an environment variable<br># feel free to add additional binds if you need them <br>SINGULARITY="singularity exec --nv -B ${HOME},${homefull},${PWD} ${SIF}"<br><br># run a command in the container<br>echo ${SINGULARITY} python3 $@<br>${SINGULARITY} python3 $@</pre>
<p>Make the wrapper script executable:</p>
<pre>chmod +x wrapper.sh</pre>
<p><span>Next, edit the </span><em>kernel.json</em><span> to change the first element of the argv list to point to the wrapper script we just created. The file should look like this (change &lt;username&gt; to your NeSI username):</span></p>
<pre><span>{<br>"argv": [<br>"/home/&lt;username&gt;/.local/share/jupyter/kernels/lambdastack/wrapper.sh",<br>"-m",<br>"ipykernel_launcher",<br>"-f",<br>"{connection_file}"<br>],<br>"display_name": "Lambda Stack Python 3",<br>"language": "python"<br>}<br></span></pre>
<p>After refreshing the <a href="https://jupyter.nesi.org.nz/" target="_blank" rel="noopener">NeSI JupyterLab</a> your Lambda Stack Python kernel should show up as "Lambda Stack Python 3".</p>
<h1>Example: running Transformers benchmarks</h1>
<p>Here we give an example showing using Lambda Stack to run the <a href="https://huggingface.co/transformers/" target="_blank" rel="noopener">Transformers</a> library benchmarks. Transformers is a natural language processing library that uses either TensorFlow or PyTorch underneath. While both PyTorch and TensorFlow are included in the Lambda Stack distribution, the Transformers library is not, so the first thing we do is create a virtual environment and install transformers into it:</p>
<pre># load the Singularity environment module<br>module load Singularity<br><br># create a directory and change to it<br>mkdir /nesi/project/&lt;project_code&gt;/transformers-benchmarks<br>cd /nesi/project/&lt;project_code&gt;/transformers-benchmarks<br><br># path to the singularity image file (optionally replace with your own)<br>export SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif<br><br># launch a bash shell in the Singularity image<br>singularity exec -B $PWD $SIF bash</pre>
<p>After executing the above command your prompt should have changed to <em>Singularity&gt;</em>, the following commands are all executed at this prompt (i.e. within the container):</p>
<pre>virtualenv --system-site-packages transenv<br>source transenv/bin/activate<br>pip install transformers psutil py3nvml<br><br># exit the Singularity container bash prompt<br>exit</pre>
<p>Note we used <em>--system-site-packages</em> so that we can use the Lambda Stack installed TensorFlow, PyTorch, etc., instead of installing them separately.</p>
<p>Now clone the transformers git repo so we can run the benchmark script (these commands run outside the container):</p>
<pre>git clone https://github.com/huggingface/transformers.git</pre>
<p>Create the following script for running the benchmarks, named <em>run-benchmark-torch.sh</em>:</p>
<pre>#!/bin/bash -e<br><br># load the virtual environment with transformers installed<br>source transenv/bin/activate<br><br># path to transformers benchmark script<br>BENCH_SCRIPT=transformers/examples/pytorch/benchmarking/run_benchmark.py<br><br># run the benchmarks<br>python ${BENCH_SCRIPT} --no_multi_process --training --no_memory \<br>                       --save_to_csv --env_print \<br>                       --models bert-base-cased bert-large-cased \<br>                                bert-large-uncased gpt2 \<br>                                gpt2-large gpt2-xl \<br>                       --batch_sizes 8 \<br>                       --sequence_lengths 8 32 128 512</pre>
<p>Now create a Slurm script that will launch the job, names <em>run-benchmark-torch.sl</em>:</p>
<pre>#!/bin/bash<br>#SBATCH --job-name=lambdastack<br>#SBATCH --time=00:30:00<br>#SBATCH --ntasks=1<br>#SBATCH --cpus-per-task=1<br>#SBATCH --gpus-per-task=1<br>#SBATCH --mem=12G<br><br># path to the singularity image file (optionally replace with your own)<br>SIF=/opt/nesi/containers/lambda-stack/lambda-stack-focal-latest.sif<br><br># load environment modules (these are always required)<br>module purge<br>module load Singularity<br><br># for convenience store the singularity command in an environment variable<br>SINGULARITY="singularity exec --nv -B ${PWD} ${SIF}"<br><br># print PyTorch version and number of GPUs detected<br>${SINGULARITY} python3 -c "import torch; print('torch version', torch.__version__)"<br>${SINGULARITY} python3 -c "import torch; print('num devices', torch.cuda.device_count())"<br><br># run the benchmark script we created<br>${SINGULARITY} bash ./run-benchmark-torch.sh</pre>
<p>Submit this job to Slurm and then wait for the benchmarks to run:</p>
<pre>sbatch run-benchmark-torch.sl</pre>
<p> </p>
<p> </p>
<p> </p>