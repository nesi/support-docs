---
created_at: '2020-06-23T23:10:13Z'
hidden: false
label_names: []
position: 12
title: Miniconda3
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001580415
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>The <code>Miniconda3</code> environment module provides the <a href="https://docs.conda.io/projects/conda/en/latest/">Conda</a> package and environment manager. Conda lets you install packages and their dependencies in dedicated environment, giving you more freedom to install software yourself at the expense of possibly less optimized packages and no curation by the NeSI team.</p>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Alternatives</h3>
<ul>
<li>If you want a more reproducible and isolated environment, we recommend using the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001107916-Singularity">Singularity containers</a>.</li>
<li>If you only need access to Python and standard numerical libraries (numpy, scipy, matplotlib, etc.), you can use the <a href="https://support.nesi.org.nz/hc/en-gb/articles/207782537-Python">Python environment module</a>.</li>
</ul>
</blockquote>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Māui Ancillary Nodes</h3>
On Māui Ancillary Nodes, you can also use the <code>Anaconda3</code> module, which provides a default environment pre-installed with a set of numerical libraries (numpy, scipy, matplotlib, etc.).</blockquote>
<h1 id="module-loading-and-conda-environments-isolation">Module loading and conda environments isolation</h1>
<p>When using the Miniconda3 module, we recommend using the following snippet to ensure that your conda environments can be activated and are isolated as possible from the rest of the system:</p>
<pre><code>module purge &amp;&amp; module load Miniconda3
source $(conda info --base)/etc/profile.d/conda.sh
export PYTHONNOUSERSITE=1</code></pre>
<p>Here are the explanations for each line of this snippet:</p>
<ul>
<li>
<code>module purge &amp;&amp; module load Miniconda3</code> ensures that no other environment module can affect your conda environments. In particular, the Python environment module change the <code>PYTHONPATH</code> variable, breaking the isolation of the conda environments. If you need other environment modules, make sure to load them after this line.</li>
<li>
<code>source $(conda info --base)/etc/profile.d/conda.sh</code> ensures that you can use the <code>conda activate</code> command.</li>
<li>
<code>export PYTHONNOUSERSITE=1</code> makes sure that local packages installed in your home folder <code>~/.local/lib/pythonX.Y/site-packages/</code> (where <code>X.Y</code> is the Python version, e.g. 3.8) by <code>pip install --user</code> are excluded from your conda environments.</li>
</ul>
<blockquote class="blockquote-warning">
<h3 id="octopus-warning">Do not use <code>conda init</code>
</h3>
We <strong>strongly</strong> recommend against using <code>conda init</code>. It inserts a snippet in your <code>~/.bashrc</code> file that will freeze the version of conda used, bypassing the environment module system.</blockquote>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Māui Ancillary Nodes</h3>
On Māui Ancillary Nodes, you need to (re)load the <code>NeSI</code> module after using <code>module purge</code>:
<pre><code>module purge &amp;&amp; module load NeSI Miniconda3
source $(conda info --base)/etc/profile.d/conda.sh
export PYTHONNOUSERSITE=1</code></pre>
</blockquote>
<h1 id="prevent-conda-from-using-home-storage">Prevent conda from using /home storage</h1>
<p>Conda environments and the conda packages cache can take a lot of storage space. By default, Conda use <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas">/home storage</a>, which is restricted to 20GB on NeSI. Here are some techniques to avoid running out of space when using Conda.</p>
<p>First, we recommend that you move the cache folder used for downloaded packages on the <code>nobackup</code> folder of your project:</p>
<pre><code>conda config --add pkgs_dirs /nesi/nobackup/&lt;project_code&gt;/$USER/conda_pkgs</code></pre>
<p>where <code>&lt;project_code&gt;</code> should be replace with your project code. This setting is saved in your <code>~/.condarc</code> configuration file.</p>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Note</h3>
<p>Your package cache will be subject to the nobackup autodelete process (details available in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001162856-Automatic-cleaning-of-nobackup-file-system" target="_blank" rel="noopener">Nobackup autodelete</a> support page). The package cache folder is for temporary storage so it is safe if files within the cache folder are removed.</p>
</blockquote>
<p>Next, we recommend using the <code>-p</code> or <code>--prefix</code> options when creating new conda environments, instead of <code>-n</code> or <code>--name</code> options. Using <code>-p</code> or <code>--prefix</code>, you can specify the conda environment folder location, ideally in your project folder. For example:</p>
<pre><code>conda create --prefix /nesi/project/&lt;project_code&gt;/my_conda_env python=3.8</code></pre>
<p>Then use the path of the conda environment to activate it:</p>
<pre><code>conda activate /nesi/project/&lt;project_code&gt;/my_conda_env</code></pre>
<p>Note that <code>-p</code> and <code>--prefix</code> options can also be used when creating an environment from an <code>environment.yml</code> file:</p>
<pre><code>conda env create -f environment.yml -p /nesi/project/&lt;project_code&gt;/my_conda_env</code></pre>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Reduce prompt prefix</h3>
<p>By default, when activating a conda environment created with <code>-p</code> or <code>--prefix</code>, the entire path of the environment is be added to the prompt. To remove this long prefix in your shell prompt, use the following configuration:</p>
<pre><code>conda config --set env_prompt '({name})'</code></pre>
</blockquote>
<h1 id="faster-solver-experimental-feature">Faster solver <code>mamba</code> (experimental feature)</h1>
<p>If you are using the module <code>Miniconda3/<em data-renderer-mark="true">22.11.1-1</em></code>, you can accelerate conda environments creation and package installation using the new <code>libmamba</code> solver. To use it, append the option <code>--solver=libmamba</code> to your command.</p>
<p>For example, to create an environment from an <code>environment.yml</code> file, use:</p>
<pre><code>conda env create --solver=libmamba -f environment.yml -p venv</code></pre>
<p>or to install a package in an activate environment, use:</p>
<pre><code>conda install --solver=libmamba CONDA_PACKAGE</code></pre>
<p>where <code>CONDA_PACKAGE</code> is the package of interest.</p>