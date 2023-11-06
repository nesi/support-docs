---
created_at: '2019-09-23T11:11:16Z'
hidden: false
label_names: []
position: 32
title: Julia
vote_count: 3
vote_sum: 3
zendesk_article_id: 360001175895
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>Julia is a flexible dynamic language, appropriate for scientific and numerical computing, with performance comparable to traditional statically-typed languages. The Julia home page is at <a href="https://julialang.org/">https://julialang.org/</a>.</p>
<h1 id="licensing">Licensing requirements</h1>
<p>The Julia language is (mostly) licensed under the MIT licence. For more details, including the full text of the licence and a list of exceptions, see <a href="https://github.com/JuliaLang/julia/blob/master/LICENSE.md">https://github.com/JuliaLang/julia/blob/master/LICENSE.md</a>.</p>
<h1 id="julia-packages">Julia packages</h1>
<p>Besides the core Julia language and interpreter, a great deal of functionality is provided by Julia packages contributed by the Julia developers and by third parties, or you can write your own packages. These packages are licensed separately from the main Julia software, so different terms and conditions may apply.</p>
<h2 id="installing-julia-packages">Installing Julia packages</h2>
<p>Julia extensions, i.e. pieces of code that add functionality, are called <em>modules</em>, and for installation and management purposes modules are grouped into <em>packages</em>. Each package thus consists of one or more modules.</p>
<p>NeSI provides a range of packages with our centrally managed Julia installations, however you may wish to install additional packages, either in your home directory or, more likely, in a project directory so your research team members can be sure of using the same version of relevant software.</p>
<p>Julia provides its own package management system, which is itself a module, the Pkg module, that is included with the base Julia installation. You can use the Pkg module within a Julia script, or on the Julia command line. In this documentation, we will assume you are using the command line, but the commands are the same within a script.</p>
<ol>
<li>Load the environment module (not the same as a Julia module) corresponding to the version of Julia you want to use, e.g. Julia 1.1.0:
<pre><code>$ module load Julia/1.1.0</code></pre>
</li>
<li>Launch the Julia executable:
<pre><code># Use Julia interactively
$ julia
# Alternatively, use a Julia script
$ julia script.jl</code></pre>
</li>
<li>If you have opened Julia interactively, you should now see a Julia welcome message and prompt, like the following.
<pre><code>               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.1.0 (2019-01-21)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |

julia&gt;</code></pre>
</li>
<li>Load the Julia package manager:
<pre><code>julia&gt; using Pkg</code></pre>
</li>
<li>The most important variable for installing packages is called <code>DEPOT_PATH</code>. The depot path is a series of directories that will be searched, in order, for the package that you wish to install and its dependencies. Clear the depot path.
<blockquote class="blockquote-warning">
<h3>Warning</h3>
<p>It is possible for a package to be installed somewhere on <code>DEPOT_PATH</code>, but not compiled. If this happens, and the package is a dependency of what you're trying to install, Julia will try to compile it in situ. This is a bad thing most of the time, because you're unlikely to have write access to the install location, so the compilation will fail. Hence why clearing the depot path is important.</p>
</blockquote>
<pre><code>julia&gt; empty!(DEPOT_PATH)</code></pre>
</li>
<li>Add your preferred Julia package directory to the newly empty depot path.
<pre><code>julia&gt; push!(DEPOT_PATH, "/nesi/project/nesi12345/julia")</code></pre>
<blockquote class="blockquote-tip">
<h3>Tip</h3>
<p>While a conventional personal Julia package directory is <code>/home/joe.bloggs/.julia</code> or similar, there is no reason for the directory to be within any particular user's home directory, or for it to be a hidden directory with a name starting with a dot. For shared Julia package directories, a visible directory within a project directory will probably be more useful to you and your colleagues.</p>
<p>In any case, for obvious reasons, you should choose a directory to which you have write access.</p>
</blockquote>
</li>
<li>Install the desired Julia package. In this case, we are showing the machine-learning package Flux as an example.
<pre><code>julia&gt; Pkg.add("Flux")</code></pre>
Julia should chug away for a while, downloading and compiling various packages into the chosen directory.</li>
</ol>
<h2 id="loading-julia-packages">Making Julia packages available at runtime</h2>
<p>For some reason, Julia uses the <code>DEPOT_PATH</code> variable only to control where newly obtained packages are to be installed. The directories where existing packages are searched for are stored in a different variable, <code>LOAD_PATH</code>.</p>
<p>On NeSI, the default contents of <code>LOAD_PATH</code> are as follows:</p>
<pre><code>julia&gt; LOAD_PATH
5-element Array{String,1}:
 "@"
 "@v#.#"
 "@stdlib"
 "/opt/nesi/mahuika/Julia/1.1.0/local/share/julia/environment/v1.1"
 "."
</code></pre>
<p>The first three elements are special entries, while the fourth element is the set of centrally managed Julia packages, and the fifth is the current working directory. As you can see, custom depot directories are not present in <code>LOAD_PATH</code> by default.</p>
<p>There are several ways to add a directory to <code>LOAD_PATH</code>, but almost certainly the easiest is to do the following in your environment:</p>
<pre><code>$ export JULIA_LOAD_PATH="/nesi/project/nesi12345/julia:${JULIA_LOAD_PATH}"
</code></pre>
<blockquote class="blockquote-tip">
<h3>Tip</h3>
<p>By prepending the directory to <code>JULIA_LOAD_PATH</code> instead of appending it, you ensure that your project's versions of Julia packages are used by default, in preference to whatever might be managed centrally. This is probably what you want to do. If you want to use the centrally managed versions of Julia packages first and only use your project's package if there isn't a centrally managed instance, you can append it instead:</p>
<pre><code>$ export JULIA_LOAD_PATH=${JULIA_LOAD_PATH}:/nesi/project/nesi12345/julia"</code></pre>
</blockquote>
<blockquote class="blockquote-tip">
<h3>Tip</h3>
<p>To revert to the default load path, just unset <code>JULIA_LOAD_PATH</code>:</p>
<pre><code>$ unset JULIA_LOAD_PATH
$ export JULIA_LOAD_PATH</code></pre>
</blockquote>
<h1>Profiling Julia code</h1>
<p>In addition to the Julia Profile module (see the <a href="https://docs.julialang.org/en/v1/manual/profile/" target="_blank" rel="noopener">official documentation</a>), it is also possible to profile Julia code with <a href="https://docs.julialang.org/en/v1/manual/profile/#External-Profiling-1" target="_blank" rel="noopener">external profilers</a>. On Mahuika we have installed "-VTune" variants of Julia, which are built from source with support for profiling using Intel VTune. VTune is a nice tool for profiling parallel code (e.g. code making use of threading or MPI.jl).</p>
<p>In order to collect profiling data with VTune you should:</p>
<ul>
<li>load a "-VTune" variant of Julia, for example:
<pre><code>module load Julia/1.2.0-gimkl-2018b-VTune</code></pre>
</li>
<li>load a VTune module:
<pre><code>module load VTune</code></pre>
</li>
<li>enable Julia VTune profiling by setting an environment variable:
<pre><code>export ENABLE_JITPROFILING=1</code></pre>
</li>
<li>prepend the usual command that you use to run your Julia program with the desired VTune command, for example to run a hotspots analysis:
<pre><code>srun amplxe-cl -collect hotspots -- julia your_program.jl</code></pre>
</li>
</ul>
<p>VTune will create a result directory which contains the profiling information. This result can be loaded using the VTune GUI, assuming you have X11 forwarding enabled:</p>
<pre><code>amplxe-gui --path-to-open &lt;vtune-result-directory&gt;</code></pre>
<p> Additional information about VTune can be found in the <a href="https://software.intel.com/en-us/vtune-amplifier-help" target="_blank" rel="noopener">User Guide</a>.</p>