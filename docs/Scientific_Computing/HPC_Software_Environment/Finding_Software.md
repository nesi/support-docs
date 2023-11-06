---
created_at: '2018-07-31T10:13:22Z'
hidden: false
label_names: []
position: 15
title: Finding Software
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000360576
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h2 id="environment-modules">Environment Modules</h2>
<p>NeSI uses environment modules to manage <a href="https://support.nesi.org.nz/hc/articles/360000170355">installed software</a>.</p>
<p>Using the <code class="highlighter-rouge">module</code> command you can:</p>
<ul>
<li>View loaded modules:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module list
</code></pre>
</div>
</div>
</li>
<li>List all available modules
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module avail
</code></pre>
</div>
</div>
</li>
<li>Load a module:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module load Python/2.7.14-gimkl-2017a
</code></pre>
</div>
</div>
</li>
<li>Switch out a loaded module for a different version:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module switch Python/2.7.14-gimkl-2017a Python/3.6.3-gimkl-2017a
</code></pre>
</div>
</div>
</li>
</ul>
<h2 id="lmod-on-mahuika">Lmod on Mahuika</h2>
<p>As on Pan, Mahuika uses an enhanced version of modules called <a href="https://lmod.readthedocs.io/en/latest/010_user.html">Lmod</a> .</p>
<p>Lmod extends the basic environment modules by adding simple shortcuts and a more powerful search capability. The <code class="highlighter-rouge">ml</code> shortcut can be used in place of <code class="highlighter-rouge">module</code>. With Lmod you can:</p>
<ul>
<li>View loaded modules:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>ml
</code></pre>
</div>
</div>
</li>
<li>List all available modules:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>ml spider
</code></pre>
</div>
</div>
</li>
<li>Use “spider” to search for modules, e.g. “Python” modules:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>ml spider Python
</code></pre>
</div>
</div>
</li>
<li>Load a module:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>ml Python/2.7.14-gimkl-2017a
</code></pre>
</div>
</div>
</li>
<li>Prefix a module with “-“ to unload it, e.g. switch from Python 2 to Python 3:
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>ml -Python/2.7.14-gimkl-2017a Python/3.6.3-gimkl-2017a
</code></pre>
</div>
</div>
</li>
<li>To get a fresh environment, we recommend that you log out and log in again. By logging out and logging in again you will revert to not only the default set of modules, but also the default set of environment variables.</li>
</ul>
<p>Further information can be found in the online <a href="https://lmod.readthedocs.io/en/latest/010_user.html">User Guide for Lmod</a>.</p>
<h2>Modules on Māui</h2>
<p>On Māui and Māui_Ancil we use top level modules to provide the different software stacks. Per default the "NeSI" module is loaded, which provides access to the different NeSI software stacks.</p>
<p>On Māui XC nodes an improved version of the modules framework is provided. Therewith you can also search for modules using a sub-string using the "-S" option, e.g.</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module avail -S netcdf</code></pre>
</div>
</div>
<p>as a result you will also find modules having the substring "netcdf" in name, e.g. cray-netcdf.</p>
<p>NOTE: The substring search will be soon implemented by default, then you do not need to specify the -S anymore. Furthermore, this improvement should be also ported to the Māui_Ancil part.</p>
<p> </p>
<p>NOTE: you can create your own modules. This is described <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000474535-Installing-Third-Party-applications">here</a>.</p>