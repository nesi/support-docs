---
created_at: '2015-10-15T02:15:46Z'
hidden: false
position: 24
tags:
- mahuika
- application
- engineering
title: ANSYS
vote_count: 3
vote_sum: 3
zendesk_article_id: 212642617
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

## License Types

The three main ANSYS licenses are;

-   **ANSYS Teaching License **(aa\_t)

    This is the default license type, it can be used on up to 6 CPUs on
    models with less than 512k nodes

-   **ANSYS Research license** (aa\_r)

    No node restrictions. Can be used on up to 16 CPUs, for every
    additional CPU over 16 you must request additional 'aa\_r\_hpc'
    licenses.

-   **ANSYS HPC License** (aa\_r\_hpc)**  
    **One of these is required for each CPU over 16 when using
    a research license.

## License Order

Whether to use a teaching or research license **must be set manually**.
If your job is greater than the node limit, not switching to the
research license before submitting a job will **cause the job to fail**.

The license order can be changed in workbench under tools &gt; license
preferences (provided you have X11 forwarding set up), or by running
either of the following (ANSYS module must be loaded first using
`module load ANSYS`).

``` sl
prefer_research_license
```

``` sl
prefer_teaching_license
```
!!! info Note
     License preferences are individually tracked by *each version of
     ANSYS.* Make sure you set preferences using the same version as in
     your script.

# Journal files

Some ANSYS applications take a 'journal' text file as input. It is often
useful to create this journal file in your SLURM script (tidiness,
submitting jobs programmatically, etc). This can be done by using `cat`
to make a file from a
'[heredoc](http://tldp.org/LDP/abs/html/here-docs.html)'.

Below is an example of this from a fluent script.

``` bash
#!/bin/bash -e

#SBATCH --job-name      Fluent_Array
#SBATCH --time          01:00:00          # Wall time
#SBATCH --mem           512MB             # Memory per node
#SBATCH --licenses      aa_r:1       # One license token per CPU, less 16
#SBATCH --array         1-100 
#SBATCH --hint          nomultithread     # No hyperthreading

module load ANSYS/19.2

JOURNAL_FILE=fluent_${SLURM_JOB_ID}.in
cat <<EOF > ${JOURNAL_FILE}
/file/read-case-data testCase${SLURM_ARRAY_TASK_ID}.cas
/solve/dual-time-iterate 10
/file/write-case-data testOut${SLURM_ARRAY_TASK_ID}.cas
/exit yes
EOF

# Use one of the -v options 2d, 2ddp, 3d, or 3ddp
fluent -v3ddp -g -i ${JOURNAL_FILE}
rm ${JOURNAL_FILE}
```

`JOURNAL_FILE` is a variable holding the name of a file, the next line
`cat` creates the file then writes a block of text into it. The block of
text written is everything between an arbitrary string (in this case
`EOF`) and its next occurrence.

In this case (assuming it is the first run of the array and the
jobid=1234567), the file  `fluent_1234567.in` will be created:

``` bash
/file/read-case-data testCase1
; This will read testCase1.cas and testCase1.dat
; Inputs can be read separately with 'read-case' and 'read-data'

/solve/dual-time-iterate 10
; Solve 10 time steps

/file/write-case-data testCase1 ok
; Since our output name is the same as our input, we have to provide conformation to overwrite, 'ok' 

exit yes
; Not including 'exit yes' will cause fluent to exit with an error. (Everything will be fine, but SLURM will read it as FAILED).)
```

then called as an input `fluent -v3ddp -g -i fluent_1234567.in`,  
then deleted `rm fluent_1234567.in`

This can be used with variable substitution to great effect as it allows
the use of variables in what might otherwise be a fixed input.
!!! info Note
     Comments can be added to journal files using a `;`. For example:
     ``` sl
     ; This is a comment
     ```

# Fluent

[Some great documentation on journal
files](https://docs.hpc.shef.ac.uk/en/latest/referenceinfo/ANSYS/fluent/writing-fluent-journal-files.html)

`fluent -help` for a list of commands.

Must have one of these flags. 

|        |                                    |
|--------|------------------------------------|
| `2d`   | 2D solver, single point precision. |
| `3d`   | 3D solver, single point precision. |
| `2ddp` | 2D solver, double point precision. |
| `3ddp` | 3D solver, double point precision. |

 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="serial-example">Serial Example</h2>
<hr />
<p>Single <em>process</em> with a single <em>thread</em> <span>(2
threads if hyperthreading </span>enabled).</p>
<p>Usually submitted as part of an array, as in the case of parameter
sweeps.</p></td>
<td><div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      Fluent-Serial</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses      aa_r@uoa_foe:1 #One research license.</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00          # Walltime</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task 1                 # Double if hyperthreading enabled</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           512MB             # total memory (per node)</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread     # Hyperthreading disabled</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load ANSYS/19.2</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="va">JOURNAL_FILE</span><span class="op">=</span>/share/test/ansys/fluent/wing.in</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="ex">fluent</span> 3ddp <span class="at">-g</span> <span class="at">-i</span> <span class="va">${JOURNAL_FILE}</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td class="wysiwyg-text-align-left"><h2
id="distributed-memory-example">Distributed Memory Example</h2>
<hr />
<p>Multiple <em>processes</em> each with a single <em>thread</em>.</p>
<p>Not limited to <span>one node</span>.<br />
Model will be segmented into <code class="sl">-t</code> pieces which
should be equal to <code class="sl">--ntasks</code>.</p>
<p>Each task could be running on a different node leading to increased
communication overhead. Jobs can be limited to a single node by
adding  <code class="sl">--nodes=1</code> however this will increase
your time in the queue as contiguous cpu's are harder to
schedule.</p></td>
<td><div class="sourceCode" id="cb2"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name          Fluent-Dis</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time              00:05:00          # Walltime</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses          aa_r@uoa_foe:1,aa_r_hpc@uoa_foe:20</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="co">##One research license, (ntasks-16) hpc licenses</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --nodes             1                 # Limit to n nodes (Optional)</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --ntasks            8                 # Number processes</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task     1                 # Double if hyperthreading enabled</span></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem-per-cpu       1500              # Fine for small jobs; increase if needed</span></span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint              nomultithread     # Hyperthreading disabled</span></span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load ANSYS/19.2</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a><span class="va">JOURNAL_FILE</span><span class="op">=</span>/share/test/ansys/fluent/wing.in</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a><span class="ex">fluent</span> 3ddp <span class="at">-g</span> <span class="at">-t</span> <span class="va">${SLURM_NTASKS}</span> <span class="at">-i</span> <span class="va">${JOURNAL_FILE}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
!!! info Useful Links
     -   [All command line
         options.](https://www.sharcnet.ca/Software/Ansys/16.2.3/en-us/help/flu_gs/flu_ug_sec_startup_option.html)

## Interactive

While it will always be more time and resource efficient using a slurm
script as shown above, there are occasions where the GUI is required. If
you only require a few CPUs for a short while you may run the fluent on
the login node, otherwise use of an [slurm interactive
session](https://support.nesi.org.nz/hc/en-gb/articles/360001316356) is
recommended. 

For example.

``` sl
salloc --job-name flUI --nodes 4 --ntasks-per-node 8 --mem-per-cpu 1500 --time 04:00:00
```

Will return;

``` sl
  salloc: Pending job allocation 10270935
  salloc: job 10270935 queued and waiting for resources
  salloc: job 10270935 has been allocated resources
  salloc: Granted job allocation 10270935
  salloc: Waiting for resource configuration
  salloc: Nodes wbn[053-056] are ready for job
```
!!! info Note
     Include all the commands you would usually use in your slurm header
     here.

Once you have your allocation, run the command

``` sl
fluent
```

You will then be presented with the launcher, make any necessary changes
then click launch.

If everything has set up correctly you should see a printout of the
hostnames with the resources requested. Note: 'host' should be
mahuika0\[1-2\].

``` sl
n24-31 wbn056 8/72 Linux-64 71521-71528 Intel(R) Xeon(R) E5-2695 v4
 n16-23 wbn055 8/72 Linux-64 52264-52271 Intel(R) Xeon(R) E5-2695 v4
 n8-15 wbn054 8/72 Linux-64 177090-177097 Intel(R) Xeon(R) E5-2695 v4
 n0-7 wbn053 8/72 Linux-64 48376-48384 Intel(R) Xeon(R) E5-2695 v4
 host mahuika01 Linux-64 185962 Intel(R) Xeon(R) E5-2695 v4
```
!!! info Important
     Closing the fluent GUI will not end the SLURM interactive session. Use
     `exit` or `scancel `*`jobid`* when finished, else you will continue to
     'use' the requested CPUs.

## Checkpointing

It is best practice when running long jobs to enable autosaves.

``` sl
/file/autosave/data-frequency <n>
```

Where `<n>` is the number of iterations to run before creating a save.

In order to save disk space you may also want to include the line 

## Interrupting

Including the following code at the top of your journal file will allow
you to interrupt the job.

``` sl
(set! checkpoint/exit-filename "./exit-fluent")
```

Creating a file named `exit-fluent` in the run directory will cause the
job to save the current state and exit (`touch exit-fluent`). This will
also write a new journal file called `restart.inp` that restarts the
simulation at that point.

## User Defined Functions

When compiling code, make sure to `module load gimkl` in addition to the
ANSYS module.

### Case Definition

When setting up the case file on your local machine, make sure you
select 'Compiled UDF', and select the \`.c\` source file. You can also
specify the name of the library, the default being 'libudf', if possible
you should stick with the default name.

Make sure all names follows unix naming conventions (no spaces or
special characters) and are the same on the cluster as when you defined
it.

It will also save you time if the that the path to your UDF source is
*relative*. The easiest way to do this is to have the source file in the
same directory as your `.cas` file, then specify *only the name as your
UDF source*.

When calling a function, make sure you select the compiled NOT the
interpreted version.

\`udf funcName\` is funcName as being interpreted directly from your
\`.c\` source file.

\`udf funcName::libudf\` is funcName as compiled in library \`libudf\`

### Compilation

When running in a new environment for the first time (local machine,
Mahuika, Māui), the C code will have to first be compiled. The compiled
code will be placed in a directory with the name of the library (by
default this will be `libudf/`.

*If you copied the compiled library from a different environment, you
will have to delete this directory first.*

If the compiled library with the name specified in the case file (e.g.
`libudf/`) is not found, fluent will try to compile it from the
specified source file.

If for some reason the UDF does not compile automatically, you can
manually build it with the following command in your fluent journal file
(should go before loading model).

``` sl
define/user-defined/compiled-functions compile "<libname>" yes "<source_file_1>" "<source_file_n>" "<header_file_1>" "<header_file_n>" "" ""
```

Note, the command must end with two `""` to indicate there are no more
files to add. 

As an example 

``` sl
define/user-defined/compiled-functions compile "libudf" yes "myUDF.c" "" ""
```

Will compile the code `myUDF.c` into a library named `libudf`

### Loading File

``` sl
define/user-defined/compiled-functions load libudf
```

Will load the library `libudf` to be accessible by ANSYS.

### UDF errors

``` sl
Error: chip-exec: function
```

might be using interpreted func

solution specify as relative path, or unload compiled lib before saving
.cas file.

# CFX

`cfx5solve -help` for a list of commands.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="serial-example-1">Serial Example</h2>
<hr />
<p>Single <em>process</em> with a single <em>thread</em> <span>(2
threads if hyperthreading </span>enabled).</p>
<p>Usually submitted as part of an array, as in the case of parameter
sweeps.</p></td>
<td><div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      CFX-serial</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses      aa_r@uoa_foe:1 #One research license.</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00          # Walltime</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task 1                 # Double if hyperthreading enabled</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           512MB             # total mem</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread     # Hyperthreading disabled</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load ANSYS/19.2</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="va">input</span><span class="op">=</span>/share/test/ansys/cfx/pump.def</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="ex">cfx5solve</span> <span class="at">-batch</span> <span class="at">-def</span> <span class="st">&quot;</span><span class="va">$input</span><span class="st">&quot;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td class="wysiwyg-text-align-left"><h2
id="distributed-memory-example-1">Distributed Memory Example</h2>
<hr />
<p>Multiple <em>processes</em> each with a single <em>thread</em>.</p>
<p>Not limited to <span>one node</span>.<br />
Model will be segmented into <code class="sl">-np</code> pieces which
should be equal to <code class="sl">--ntasks</code>.</p>
<p>Each task could be running on a different node leading to increased
communication overhead<br />
.Jobs can be limited to a single node by adding  <code
class="sl">--nodes=1</code> however this will increase your time in the
queue as contiguous cpu's are harder to schedule.</p></td>
<td><div class="sourceCode" id="cb2"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name          ANSYS-Dis</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time              00:05:00          # Walltime</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses          aa_r@uoa_foe:1,aa_r_hpc@uoa_foe:20</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="co">##One research license, (ntasks-16) hpc licenses</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --nodes             1                 # Limit to n nodes (Optional)</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --ntasks            36                # Number processes</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task     1                 # Double if hyperthreading enabled</span></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem-per-cpu       512MB             # Standard for large partition</span></span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint              nomultithread     # Hyperthreading disabled</span></span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load ANSYS/19.2</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a><span class="va">input</span><span class="op">=</span>/share/test/ansys/mechanical/structural.dat</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a><span class="ex">cfx5solve</span> <span class="at">-batch</span> <span class="at">-def</span> <span class="st">&quot;</span><span class="va">$input</span><span class="st">&quot;</span> <span class="at">-part</span> <span class="va">$SLURM_NTASKS</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
!!! info Tip
     Initial values path specified in '.def' file can be overridden using
     the `-ini <initial-file-path>` flag.

## CFX-Post

Even when running headless (without a GUI) CFX-Post requires connection
to a graphical output. For some cases it may be suitable running
CFX-Post on the login node and using your X-11 display, but for larger
batch compute jobs you will need to make use of a dummy X-11 server.

This is as simple as prepending your command with the X Virtual Frame
Buffer command.

``` sl
xvfb-run cfx5post input.cse
```

# Mechanical APDL

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="serial-example-2">Serial Example</h2>
<hr />
<p>Single <em>process</em> with a single <em>thread</em> <span>(2
threads if hyperthreading </span>enabled).</p>
<p>Usually submitted as part of an array, as in the case of parameter
sweeps.</p></td>
<td><div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      ANSYS-serial</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses aa_r@uoa_foe:1</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00          # Walltime</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           1500M             # total mem</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread     # Hyperthreading disabled</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load ANSYS/2021R2</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="va">input</span><span class="op">=</span><span class="va">${ANSYS_ROOT}</span>/ansys/data/verif/vm263.dat</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="ex">mapdl</span> <span class="at">-b</span> <span class="at">-i</span> <span class="st">&quot;</span><span class="va">$input</span><span class="st">&quot;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><h2 id="shared-memory-example">Shared Memory Example</h2>
<hr />
<p>Single <em>process</em> multiple <em>threads.</em></p>
<p>All threads must be on the same node, limiting scalability.<br />
Number of threads is set by <code class="sl">-np</code> and should be
equal to <code class="sl">--cpus-per-task</code>.</p>
<p><br />
Not recommended if using more than 8 cores (16 CPUs if hyperthreading
enabled).</p></td>
<td><div class="sourceCode" id="cb2"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      ANSYS-Shared</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses aa_r@uoa_foe:1</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00          # Walltime</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task 8                 # Double if hyperthreading enabled</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           12G               # 8 threads at 1500 MB per thread</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread     # Hyperthreading disabled</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load ANSYS/2021R2</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a><span class="va">input</span><span class="op">=</span><span class="va">${ANSYS_ROOT}</span>/ansys/data/verif/vm263.dat</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a><span class="ex">mapdl</span> <span class="at">-b</span> <span class="at">-np</span> <span class="va">${SLURM_CPUS_PER_TASK}</span> <span class="at">-i</span> <span class="st">&quot;</span><span class="va">$input</span><span class="st">&quot;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td class="wysiwyg-text-align-left"><h2
id="distributed-memory-example-2">Distributed Memory Example</h2>
<hr />
<p>Multiple <em>processes</em> each with a single <em>thread</em>.</p>
<p>Not limited to <span>one node</span>.<br />
Model will be segmented into <code class="sl">-np</code> pieces which
should be equal to <code class="sl">--ntasks</code>.</p>
<p>Each task could be running on a different node leading to increased
communication overhead<br />
.Jobs can be limited to a single node by adding  <code
class="sl">--nodes=1</code> however this will increase your time in the
queue as contiguous cpu's are harder to schedule.</p>
<p><strong>Distributed Memory Parallel is currently not supported on
Māui.</strong></p></td>
<td><div class="sourceCode" id="cb3"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name          ANSYS-Dis</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses aa_r@uoa_foe:1,aa_r_hpc@uoa_foe:4</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time              00:05:00          # Walltime</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --nodes             1                 # (OPTIONAL) Limit to n nodes</span></span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --ntasks            16                # Number processes</span></span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem-per-cpu       1500</span></span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint              nomultithread     # Hyperthreading disabled</span></span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load ANSYS/2021R2</span>
<span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a><span class="va">input</span><span class="op">=</span><span class="va">${ANSYS_ROOT}</span>/ansys/data/verif/vm263.dat</span>
<span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a><span class="ex">mapdl</span> <span class="at">-b</span> <span class="at">-dis</span> <span class="at">-np</span> <span class="va">${SLURM_NTASKS}</span> <span class="at">-i</span> <span class="st">&quot;</span><span class="va">$input</span><span class="st">&quot;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><h2 id="distributed-memory-example-3">Distributed Memory
Example</h2>
<hr />
<p>Multiple <em>processes</em> each with a
single <em>thread</em></p></td>
<td> </td>
</tr>
</tbody>
</table>

Not all MAPDL solvers work using distributed memory. 

|                           |     |
|---------------------------|-----|
| Sparse                    | ✔   |
| PCG                       | ✔   |
| ICCG                      | ✖   |
| JCG                       | ✖   |
| QMR                       | ✖   |
| Block Lanczos eigensolver | ✖   |
| PCG Lanczos eigensolver   | ✔   |
| Supernode eigensolver     | ✖   |
| Subspace eigensolver      | ✔   |
| Unsymmetric eigensolver   | ✔   |
| Damped eigensolver        | ✔   |
| QRDAMP eigensolver        | ✖   |
| Element formulation       | ✔   |
| Results calculation       | ✔   |
| Pre/Postprocessing        | ✖   |
!!! info Useful Links
     -   [All command line
         options.](https://www.sharcnet.ca/Software/Ansys/17.0/en-us/help/ans_ope/Hlp_G_OPE3_1.html)
     -   [All MAPDL
         commands.](https://www.sharcnet.ca/Software/Fluent14/help/ans_cmd/Hlp_C_CmdTOC.html)
     -   [Debug
         options.](https://www.sharcnet.ca/Software/Ansys/16.2.3/en-us/help/ans_prog/S7K4r190lcd.html)
     -   [MAPDL Parallel Processing
         Guide](https://www.sharcnet.ca/Software/Ansys/16.2.3/en-us/help/ans_dan/dantoc.html)

# LS-DYNA

## Fluid-Structure Example

``` bash
#!/bin/bash -e
#SBATCH --job-name      LS-DYNA
#SBATCH --account       nesi99999         # Project Account
#SBATCH --time          01:00:00          # Walltime
#SBATCH --ntasks        16                # Number of CPUs to use
#SBATCH --mem-per-cpu   512MB             # Memory per cpu
#SBATCH --hint          nomultithread     # No hyperthreading

module load ANSYS/18.1
input=3cars_shell2_150ms.k
lsdyna -dis -np $SLURM_NTASKS i="$input" memory=$(($SLURM_MEM_PER_CPU/8))M
```

# Multiphysics

### Example - MAPDL Fluent Interaction

``` bash
#!/bin/bash -e
#SBATCH --job-name      ANSYS_FSI
#SBATCH --account       nesi99999         # Project Account
#SBATCH --time          01:00:00          # Walltime
#SBATCH --ntasks        16                # Number of CPUs to use
#SBATCH --mem-per-cpu   2GB               # Memory per CPU
#SBATCH --hint          nomultithread     # No hyperthreading

module load ANSYS/18.1

COMP_CPUS=$((SLURM_NTASKS-1))
MECHANICAL_CPUS=1
FLUID_CPUS=$((COMP_CPUS-MECHANICAL_CPUS))
export SLURM_EXCLUSIVE="" # don't share CPUs
echo "CPUs: Coupler:1 Struct:$MECHANICAL_CPUS Fluid:$FLUID_CPUS"

echo "STARTING SYSTEM COUPLER"

cd Coupling

# Run the system coupler in the background.
srun -N1 -n1 $WORKBENCH_CMD \
    ansys.services.systemcoupling.exe \
    -inputFile coupling.sci || scancel $SLURM_JOBID &
cd ..
serverfile="$PWD/Coupling/scServer.scs"

while [[ ! -f "$serverfile" ]] ; do
    sleep 1 # waiting for SC to start
done
sleep 1

echo "PARSING SYSTEM COUPLER CONFIG"

{
    read hostport
    port=${hostport%@*}
    node=${hostport#*@}
    read count
    for solver in $(seq $count)
    do
        read solname
        read soltype
        case $soltype in 
            Fluid) fluentsolname=$solname;;
            Structural) mechsolname=$solname;;
        esac
    done
} < "$serverfile"

echo " Port number: $port"
echo " Node name: $node"
echo " Fluent name: $fluentsolname"
echo " Mechanical name: $mechsolname"

echo "STARTING ANSYS"

cd Structural

# Run ANSYS in the background, alongside the system coupler and Fluent.
mapdl -b -dis -mpi intel -np $MECHANICAL_CPUS \
    -scport $port -schost $node -scname "$mechsolname" \
    -i "structural.dat" > struct.out || scancel $SLURM_JOBID &
cd ..

sleep 2
echo "STARTING FLUENT"

cd FluidFlow

# Run Fluent in the background, alongside the system coupler and ANSYS.
fluent 3ddp -g -t$FLUID_CPUS \
    -scport=$port -schost=$node -scname="$fluentsolname" \
    -i "fluidFlow.jou" > fluent.out || scancel $SLURM_JOBID &
cd ..

# Before exiting, wait for all background tasks (the system coupler, ANSYS and
# Fluent) to complete.
wait
```

# FENSAP-ICE

FENSAP-ICE is a fully integrated ice-accretion and aerodynamics
simulator.

Currently FENSAP-ICE is only available on Mahuika and in ANSYS 19.2.

The following FENSAP solvers are compatible with MPI

-   FENSAP
-   DROP3D
-   ICE3D
-   C3D
-   OptiGrid

## Case setup 

## With GUI

If you have set up X-11 forwarding, you may launch the FENSAP ice using
the command `fensapiceGUI` from within your FENSAP project directory. 

<table style="height: 44px;" width="590">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="width: 291px"><p>1. Launch the run and select the desired
number of (physical) CPUs.</p>
<p>2. Open the 'configure' panel.</p></td>
<td style="width: 292px"><img src="../../assets/images/ANSYS.png"
alt="FENSAP_GUI1.png" /></td>
</tr>
<tr class="even">
<td style="width: 291px"><p>3. Under 'Additional mpirun parameters' add
your inline SLURM options. You should include at least.</p>
<pre class="sl"><code>--job-name my_job
--mem-per-cpu memory
--time time
--licenses required licences
--hint nomultithread </code></pre>
<p>Note: All these parameters will be applied to <em>each individual
step</em>.</p>
<p>4. Start the job. You can track progress under the 'log'
tab.</p></td>
<td style="width: 292px"><img src="../../assets/images/ANSYS_0.png"
alt="FENSAP_GUI2.png" /></td>
</tr>
</tbody>
</table>

You may close your session and the job will continue to run on the
compute nodes. You will be able to view the running job at any time by
opening the GUI within the project folder.
!!! info Note
     Submitting your job through the use of the GUI has disadvantages and
     may not be suitable in all cases.
     -   Closing the session or losing connection will prevent the next
         stage of the job starting (currently executing step will continue
         to run).  It is a good idea to launch the GUI inside a tmux/screen
         session then send the process to background to avoid this.
     -   Each individual step will be launched with the same parameters
         given in the GUI.
     -   By default 'restart' is set to disabled. If you wish to continue a
         job from a given step/shot you must select so in the dropdown
         menu.

## Using fensap2slurm

Set up your model as you would normally, except rather than starting the
run just click 'save'. You *do not* need to set number of CPUs or MPI
configuration.  
Then in your terminal type `fensap2slurm path/to/project` or run
`fensap2slurm` from inside the run directory.

This will generate a template file for each stage of the job, edit these
as you would a normal SLURM script and set the resources requirements.

For your first shot, it is a good idea to set `CONTINUE=FALSE` for the
last stage of the shot, that way you can set more accurate resource
requirements for the remainder.

The workflow can then by running `.solvercmd` e.g `bash .solvercmd`.
Progress can be tracked through the GUI as usual. 

# ANSYS-Electromagnetic

ANSYS-EM jobs can be submitted through a slurm script or by [interactive
session](https://support.nesi.org.nz/hc/en-gb/articles/360001316356).

## RSM

Unlike other ANSYS applications ANSYS-EM requires RSM (remote solver
manager) running on all nodes. The command `startRSM` has been written
to facilitate this and needs to be run *after* starting the slurm job
but *before* running edt. Please contact NeSI support if the command is
not working for you.

## Example Slurm Script

``` sl
#!/bin/bash -e

#SBATCH --time                04:00:00
#SBATCH --nodes               2
#SBATCH --ntasks-per-node     36
#SBATCH --mem-per-cpu         1500

module load ANSYS/19.1
INPUTNAME="Sim1.aedt"
startRSM

ansysedt -ng -batchsolve -distributed -machinelistfile=".machinefile" -batchoptions "HFSS/HPCLicenseType=Pool" $INPUTNAME
```

All batch options can be listed using

``` sl
ansysedt -batchoptionhelp
```

(Note, this requires a working X-server) 
!!! info Note
     Each batch option must have it's own flag, e.g.
     ``` sl
     -batchoptions "HFSS/HPCLicenseType=Pool" -batchoptions "Desktop/ProjectDirectory=$PWD" -batchoptions "HFSS/MPIVendor=Intel"
     ```

## Interactive

First start an interactive slurm session.

``` sl
salloc --job-name edt_interactive --nodes 2 --ntasks-per-node 36 --mem-per-cpu 1500
```

Then load your desired version of ANSYS

``` sl
module load ANSYS/19.2
```

Run the script to start startRSM, this will start ANSYS remote solver on
your requested nodes, and set the environment variable `MACHINELIST`.

``` sl
startRSM
```

Then launch ansys edt with the following flags

``` sl
ansysedt -machinelist file=".machinefile" -batchoptions "HFSS/HPCLicenseType=Pool HFSS/MPIVendor=Intel HFSS/UseLegacyElectronicsHPC=1"
```

# Best Practices

## GPU acceleration support

GPUs can be slow for smaller jobs because it takes time to transfer data
from the main memory to the GPU memory. We therefore suggest that you
only use them for larger jobs, unless benchmarking reveals otherwise.

## Interactive use

It is best to use journal files *etc* to automate ANSYS so that you can
submit batch jobs, but when interactivity is really needed alongside
more CPU power and/or memory than is reasonable to take from a login
node (maybe postprocessing a large output file) then an alternative
which may work is to run the GUI frontend on a login node while the MPI
tasks it launches run on a compute node. This requires using *salloc*
instead of *sbatch*, for example:

``` bash
salloc -A nesi99999 -t 30 -n 16 -C avx --mem-per-cpu=512MB bash -c 'module load ANSYS; fluent -v3ddp -t$SLURM_NTASKS' 
```

As with any job, you may have to wait a while before the resource is
granted and you can begin, so you might want to use the
--mail-type=BEGIN and --mail-user= options.

## Hyperthreading

Utilising hyperthreading (ie: removing the "--hint=nomultithread" sbatch
directive and doubling the number of tasks) will give a small speedup on
most jobs with less than 8 cores, but also doubles the number of
`aa_r_hpc` license tokens required.
