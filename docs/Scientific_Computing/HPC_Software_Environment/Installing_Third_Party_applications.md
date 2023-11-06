---
created_at: '2018-09-24T01:51:32Z'
hidden: false
label_names: []
position: 16
title: Installing (Third Party) applications
vote_count: 3
vote_sum: 3
zendesk_article_id: 360000474535
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>NeSI provides a long list of various applications on its systems. Nevertheless, if you need additional applications or libraries (below called package), we distinguish:</p>
<ul>
<li>you need a <strong>newer version</strong> of an already installed package: <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_blank" rel="noopener">ask NeSI support</a> for an update</li>
<li>you need an <strong>older version</strong> of an installed package: please use the Easybuild installation procedure (below) to install it into your working space</li>
<li>you want to test a <strong>new (not installed)</strong> package: below we collected some hints, how you can install it in your user space.</li>
</ul>
<p>In any case, if you have issues, do not hesitate to <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_blank" rel="noopener">open a ticket</a> and ask NeSI support for help.</p>
<h2>Additional Packages for Python, R, etc.</h2>
<p>See <a href="https://support.nesi.org.nz/hc/en-gb/articles/207782537-Python">Python</a> or <a href="https://support.nesi.org.nz/hc/en-gb/articles/209338087-R">R</a>, or for other languages check if we have additional documentation for it in our <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000040076-Supported-Applications">application documentation</a>.</p>
<h2>Third party applications</h2>
<p>Installation instruction vary from application to application. In any case we suggest to read the provided installing instructions. Nevertheless, the following should give you an impression which steps you usually need to consider:</p>
<ul>
<li>Change into a desired source code directory. We suggest to use <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">/nesi/nobackup/&lt;projectID&gt;</code> or <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">/nesi/project/&lt;projectID&gt;</code>
</li>
<li>download the source code. This could be done via a repository checkout (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">git clone &lt;URL to the application source repository&gt;</code>) or via downloading a tarball (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">wget &lt;URL to the tarball&gt;</code>). Unpack the tarball using <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">tar xf &lt;tar file name&gt;</code>. Change into source directory.</li>
<li>
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;"></code>load compiler module and modules for additional libraries (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load gimkl FFTW</code>)</li>
<li>run the configure with appropriate options <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">./configure --prefix=&lt;desired install directory&gt; --use-fftw=$EBROOTFFTW  </code>(options can be listed using <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">./configure --help</code>)</li>
<li>In other applications you need to adjust the provided <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">Makefile</code> to reflect compiler, and library options (see below)</li>
<li>compile code (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">make</code><code>)</code>
</li>
<li>install the binaries and libraries into the specified directory (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">make install</code>)</li>
</ul>
<h2 id="create-your-own-modules">Create your own modules (Optional)</h2>
<p>You can create personalised module environments, which can load modules and set up environment variables. For example, you could define a modules in a project directory <code class="highlighter-rouge">/nesi/project/&lt;projectID&gt;/modulefiles/ProdXY</code> as the following:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>#%module

conflict ProdABC   # conflicts with other versions of itself
module load CMake  # load other additional modules
module load netCDF/4.4.1-gimkl-2017a<br>module load Python/3.6.3-gimkl-2017a
<br>
# provide a description
whatis "The ProdXY for doing clever things."
proc ModulesHelp { } {
 puts stderr "This module loads the ProdXY tool. It requires CMake and netCDF."
 puts stderr "\t the executable prodXY is provided."
}
<br># set the path to the software product (can be used later in the module)
set PKG_PREFIX /path/to/software/package/ProdXY<br># add the location of binaries to PATH, such they are immediately accessible
prepend-path PATH $PKG_PREFIX/bin
# add to library path for dynamically linked applications
prepend-path LD_LIBRARY_PATH $PKG_PREFIX/lib<br># add a location for Python packages<br>prepend-path PYTHONPATH $PKG_PREFIX/lib/python3.6/site-packages/<br># for example, you can set environment variables for compiling
setenv CFLAGS "-DNDEBUG"

</code></pre>
</div>
</div>
<p>In the first lines, we can set conflicts with other modules (here named ProdABC). Then we load some dependency modules and provide some description. The additional lines depend on your requirements for the module. With <em>set</em> you can define internal variables (within this module file). The command <em>setenv</em> defines a environment variable. And <em>prepend-path</em> and <em>append-path</em> extend an environment variable at the front or end.</p>
<p>There are common environment variables like:</p>
<ul>
<li>
<em>PATH</em> for providing executabl,</li>
<li>
<em>LD_LIBRARY_PATH</em> for self created libraries,</li>
<li>
<em>PYTHONPATH </em>for providing Python modules,</li>
<li>
<em>CONDA_ENVS_PATH</em> for providing Conda environments,</li>
<li>etc.</li>
</ul>
<p>And others which are very application specific.</p>
<p>To use the module (or all in that directory and sub-directories) we need to register that directory to the module environment. This can be done by setting the following environment variable:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module use <code class="highlighter-rouge">/nesi/project/&lt;projectID&gt;/modulefiles/</code> </code></pre>
</div>
</div>
<p>by adding that line to your <code class="highlighter-rouge">$HOME/.bashrc</code> you will have the modules always available.</p>
<p>The module then can be loaded by:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module load ProdXY
</code></pre>
</div>
</div>
<p>These modules can easily be shared with collaborators. They just need to specify the last two steps.</p>
<p> </p>
<p> </p>
<p> </p>