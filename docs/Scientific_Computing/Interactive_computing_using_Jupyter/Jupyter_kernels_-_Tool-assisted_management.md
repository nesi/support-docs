---
created_at: '2022-01-31T21:28:03Z'
hidden: false
label_names: []
position: 4
title: Jupyter kernels - Tool-assisted management
vote_count: 1
vote_sum: 1
zendesk_article_id: 4414958674831
zendesk_section_id: 360001189255
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h1 id="01H7EGCRSG9389SGGS98HZYGPE">Introduction</h1>
<p>Jupyter can execute code in different computing environments using <em>kernels</em>. Some kernels are provided by default (Python, R, etc.) but you may want to register your computing environment to use it in notebooks. For example, you may want to load a specific environment module in your kernel or use a Conda environment.</p>
<p>To register a Jupyter kernel, you can follow the steps highlighted in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/4414951820559" target="_blank" rel="noopener">Jupyter kernels - Manual management</a> or use the <code>nesi-add-kernel</code> tool provided on Jupyter on NeSI service. This page details the latter option, which we recommend.</p>
<h1 id="01H7EGCRSGR39X0FERXZP9C3ZT">Getting started</h1>
<p>First you need to open a terminal. It can be from a session on Jupyter on NeSI or from a regular ssh connection on Mahuika login node. If you use the ssh option, make sure to load the JupyterLab module to have access to the <code>nesi-add-kernel</code> tool:</p>
<pre><code>module purge  # remove all previously loaded modules<br>module load JupyterLab
</code></pre>
<p>Then, to list all available options, use the <code>-h</code> or <code>--help</code> options as follows:</p>
<pre><code>nesi-add-kernel --help</code></pre>
<p>Here is an example to add a TensorFlow kernel, using NeSI’s module:</p>
<pre><code>nesi-add-kernel tf_kernel </code>TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5</pre>
<p>and to share the kernel with other members of your NeSI project:</p>
<pre><code>nesi-add-kernel --shared tf_kernel_shared TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5 </code></pre>
<p>To list all the installed kernels, use the following command:</p>
<pre><code>jupyter-kernelspec list</code></pre>
<p>and to delete a specific kernel:</p>
<pre><code>jupyter-kernelspec remove &lt;kernel_name&gt;</code></pre>
<p>where <code>&lt;kernel_name&gt;</code> stands for the name of the kernel to delete.</p>
<h1 id="conda-environment">Conda environment</h1>
<p>First, make sure the <code>JupyterLab</code> module is loaded:</p>
<pre><code>module purge
module load JupyterLab</code></pre>
<p>To add a Conda environment created using <code>conda create -p &lt;conda_env_path&gt;</code>, use:</p>
<pre><code>nesi-add-kernel my_conda_env -p &lt;conda_env_path&gt;</code></pre>
<p>otherwise if created using <code>conda create -n &lt;conda_env_name&gt;</code>, use:</p>
<pre><code>nesi-add-kernel my_conda_env -n &lt;conda_env_name&gt;</code></pre>
<h1 id="virtual-environment">Virtual environment</h1>
<p>If you want to use a Python virtual environment, don’t forget to specify which Python module you used to create it.</p>
<p>For example, if we create a virtual environment named <code>my_test_venv</code> using Python 3.10.5:</p>
<pre><code>module purge
module load Python/3.10.5-gimkl-2022a
python -m venv my_test_venv</code></pre>
<p>to create the corresponding <code>my_test_kernel</code> kernel, we need to use the command:</p>
<pre><code>module purge<br>module load JupyterLab<br>nesi-add-kernel my_test_kernel Python/3.10.5-gimkl-2022a --venv my_test_venv</code></pre>
<h1 id="singularity-container">Singularity container</h1>
<p>To use a Singularity container, use the <code>-c</code> or <code>--container</code> options as follows:</p>
<pre><code>module purge<br>module load JupyterLab<br>nesi-add-kernel my_test_kernel -c &lt;container_image.sif&gt;</code></pre>
<p>where <code>&lt;container_image.sif&gt;</code> is a path to your container image.</p>
<p>Note that your container <strong>must</strong> have the <code>ipykernel</code> Python package installed in it to be able to work as a Jupyter kernel.</p>
<p>Additionally, you can use the <code>--container-args</code> option to pass more arguments to the <code>singularity exec</code> command used to instantiate the kernel.</p>
<p>Here is an example instantiating a NVIDIA NGC container as a kernel. First, we need to pull the container:</p>
<pre><code>module purge
module load Singularity/3.11.3
singularity pull nvidia_tf.sif docker://nvcr.io/nvidia/tensorflow:21.07-tf2-py3</code></pre>
<p>then we can instantiate the kernel, using the <code>--nv</code> singularity flag to ensure that the GPU will be found at runtime (assuming our Jupyter session has access to a GPU):</p>
<pre><code>module purge<br>module load JupyterLab<br>nesi-add-kernel nvidia_tf -c nvidia_tf.sif --container-args "'--nv'"</code></pre>
<p>Note that the double-quoting of <code>--nv</code> is needed to properly pass the options to <code>singularity exec</code>.</p>