---
created_at: '2022-01-31T20:45:43Z'
hidden: false
label_names: []
position: 5
title: Jupyter kernels - Manual management
vote_count: 1
vote_sum: 1
zendesk_article_id: 4414951820559
zendesk_section_id: 360001189255
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h1>Introduction</h1>
<p>Jupyter kernels execute the code that you write. The following Jupyter kernels are installed by default and can be selected from the Launcher:</p>
<ul>
<li>Python 3.8.2</li>
<li>Python 3.8.1</li>
<li>Python 3.7.3</li>
<li>Anaconda3</li>
<li>R 4.0.1</li>
<li>R 3.6.1</li>
</ul>
<p>Many packages are preinstalled in our default Python and R environments and these can be extended further as described on the <a href="https://support.nesi.org.nz/hc/en-gb/articles/207782537" target="_self">Python</a> and <a href="https://support.nesi.org.nz/hc/en-gb/articles/209338087" target="_self">R</a> support pages.</p>
<h1>Adding a custom Python kernel</h1>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">See also</h3>
<p>See the <a href="https://support.nesi.org.nz/hc/en-gb/articles/4414958674831" target="_blank" rel="noopener">Jupyter kernels - Tool-assisted management</a> page for the <strong>preferred</strong> way to register kernels, which uses the <code>nesi-add-kernel</code> command line tool to automate most of these manual steps.</p>
</blockquote>
<p>You can configure custom Python kernels for running your Jupyter notebooks. This could be necessary and/or recommended in some situations, including:</p>
<ul>
<li>if you wish to load a different combination of environment modules than those we load in our default kernels</li>
<li>if you would like to activate a virtual environment or conda environment before launching the kernel</li>
</ul>
<p>The following example will create a custom kernel based on the Miniconda3 environment module (but applies to other environment modules too).</p>
<p>In a terminal run the following commands to load a Miniconda environment module:</p>
<pre>$ module purge<br>$ module load Miniconda3/4.8.2</pre>
<p>Now create a conda environment named "my-conda-env" using Python 3.6. The <em>ipykernel</em> Python package is required but you can change the names of the environment, version of Python and install other Python packages as required.</p>
<pre>$ conda create --name my-conda-env python=3.6<br>$ source $(conda info --base)/etc/profile.d/conda.sh<br>$ conda activate my-conda-env<br>$ conda install ipykernel<br>$ # you can pip/conda install other packages here too</pre>
<p>Now create a Jupyter kernel based on your new conda environment:</p>
<pre>$ python -m ipykernel install --user --name my-conda-env --display-name="My Conda Env"</pre>
<p>We must now edit the kernel to load the required NeSI environment modules before the kernel is launched. Change to the directory the kernelspec was installed to (~/.local/share/jupyter/kernels/my-conda-env,<em> </em>assuming you kept <em>--name my-conda-env</em> in the above command):</p>
<pre>$ cd ~/.local/share/jupyter/kernels/my-conda-env</pre>
<p>Now create a wrapper script, called <em>wrapper.sh</em>, with the following contents:</p>
<pre>#!/usr/bin/env bash<br><br># load required modules here<br>module purge<br>module load Miniconda3/4.8.2<br><br># activate conda environment<br>source $(conda info --base)/etc/profile.d/conda.sh <br>conda deactivate  # workaround for https://github.com/conda/conda/issues/9392<br>conda activate my-conda-env<br><br># run the kernel<br><span class="pl-c1">exec</span> python <span class="pl-smi">$@</span></pre>
<p>Make the wrapper script executable:</p>
<pre>$ chmod +x wrapper.sh</pre>
<p>Next edit the <em>kernel.json</em> to change the first element of the argv list to point to the wrapper script we just created. The file should look like this (change &lt;username&gt; to your NeSI username):</p>
<pre>{<br> "argv": [<br> "/home/&lt;username&gt;/.local/share/jupyter/kernels/my-conda-env/wrapper.sh",<br> "-m",<br> "ipykernel_launcher",<br> "-f",<br> "{connection_file}"<br> ],<br> "display_name": "My Conda Env",<br> "language": "python"<br>}</pre>
<p>After refreshing JupyterLab your new kernel should show up in the Launcher as "My Conda Env".</p>
<h1>Sharing a Python kernel with your project team members</h1>
<p>You can also configure a shared Python kernel that others with access to the same NeSI project will be able to load. If this kernel is based on a Python virtual environment, Conda environment or similar, you must make sure it also exists in a shared location (other users cannot see your home directory).</p>
<p>The example below shows creating a shared Python kernel based on the <em>Python/3.8.2-gimkl-2020a</em> module and also loads the <em>ETE/3.1.1-gimkl-2020a-Python-3.8.2</em> module.</p>
<p>In a terminal run the following commands to load the Python and ETE environment modules:</p>
<pre>$ module purge<br>$ module load Python/3.8.2-gimkl-2020a<br>$ module load ETE/3.1.1-gimkl-2020a-Python-3.8.2</pre>
<p>Now create a Jupyter kernel within your project directory, based on your new virtual environment:</p>
<pre>$ python -m ipykernel install --prefix=/nesi/project/&lt;project_code&gt;/.jupyter --name shared-ete-env --display-name="Shared ETE Env"</pre>
<p>Next change to the kernel directory, which for the above command would be:</p>
<pre>$ cd /nesi/project/&lt;project_code&gt;/.jupyter/share/jupyter/kernels/shared-ete-env</pre>
<p>Create a wrapper script, <em>wrapper.sh</em>, with the following contents:</p>
<pre>#!/usr/bin/env bash<br><br># load necessary modules here<br>module purge<br>module load Python/3.8.2-gimkl-2020a<br>module load ETE/3.1.1-gimkl-2020a-Python-3.8.2<br><br># run the kernel<br><span class="pl-c1">exec</span> python <span class="pl-smi">$@</span></pre>
<p>Note we also load the ETE module so that we can use that from our kernel.</p>
<p>Make the wrapper script executable:</p>
<pre>chmod +x wrapper.sh</pre>
<p>Next, edit the <em>kernel.json</em> to change the first element of the argv list to point to the wrapper script we just created. The file should look like this (change &lt;project_code&gt; to your NeSI project code):</p>
<pre>{<br> "argv": [<br> "/nesi/project/&lt;project_code&gt;/.jupyter/share/jupyter/kernels/shared-ete-env/wrapper.sh",<br> "-m",<br> "ipykernel_launcher",<br> "-f",<br> "{connection_file}"<br> ],<br> "display_name": "Shared Conda Env",<br> "language": "python"<br>}</pre>
<p>After refreshing JupyterLab your new kernel should show up in the Launcher as "Shared Virtual Env".</p>
<h1>Custom kernel in a Singularity container</h1>
<p>An example showing setting up a custom kernel running in a Singularity container can be found on our <a href="https://support.nesi.org.nz/hc/en-gb/articles/360002558216-Lambda-Stack#lambda_stack_via_jupyter" target="_blank" rel="noopener">Lambda Stack</a> support page.</p>
<h1>Adding a custom R kernel</h1>
<p>You can configure custom R kernels for running your Jupyter notebooks. The following example will create a custom kernel based on the R/3.6.2-gimkl-2020a environment module and will additionally load an MPFR environment module (e.g. if you wanted to load the Rmpfr package).</p>
<p>In a terminal run the following commands to load the required environment modules:</p>
<pre>$ module purge<br>$ module load IRkernel/1.1.1-gimkl-2020a-R-3.6.2<br>$ module load Python/3.8.2-gimkl-2020a</pre>
<p>The IRkernel module loads the R module as a dependency and provides the R kernel for Jupyter. Python is required to install the kernel (since Jupyter is written in Python).</p>
<p>Now create an R Jupyter kernel based on your new conda environment:</p>
<pre>$ R -e "IRkernel::installspec(name='myrwithmpfr', displayname = 'R with MPFR', user = TRUE)"</pre>
<p>We must now to edit the kernel to load the required NeSI environment modules when the kernel is launched. Change to the directory the kernelspec was installed to (~/.local/share/jupyter/kernels/myrwithmpfr,<em> </em>assuming you kept <em>--name myrwithmpfr</em> in the above command):</p>
<pre>$ cd ~/.local/share/jupyter/kernels/myrwithmpfr</pre>
<p>Now create a wrapper script in that directory, called <em>wrapper.sh</em>, with the following contents:</p>
<pre>#!/usr/bin/env bash<br><br># load required modules here<br>module purge<br>module load MPFR/4.0.2-GCCcore-9.2.0<br>module load IRkernel/1.1.1-gimkl-2020a-R-3.6.2<br><br># run the kernel<br><span class="pl-c1">exec</span> R <span class="pl-smi">$@</span></pre>
<p>Make the wrapper script executable:</p>
<pre>$ chmod +x wrapper.sh</pre>
<p>Next edit the <em>kernel.json</em> to change the first element of the argv list to point to the wrapper script we just created. The file should look something like this (change &lt;username&gt; to your NeSI username):</p>
<pre>{<br> "argv": [<br> "/home/&lt;username&gt;/.local/share/jupyter/kernels/myrwithmpfr/wrapper.sh",<br> "--slave",<br> "-e",<br> "IRkernel::main()",<br> "--args",<br> "{connection_file}"<br> ],<br> "display_name": "R with MPFR",<br> "language": "R"<br>}</pre>
<p>After refreshing JupyterLab your new R kernel should show up in the Launcher as "R with MPFR".</p>
<h1>Spark</h1>
<p>At the time of writing, the latest stable version of Spark does not support Python 3.8. If you wish to use Spark (e.g. PySpark) make sure you select one of our Python 3.7.3 or Anaconda3 kernels.</p>