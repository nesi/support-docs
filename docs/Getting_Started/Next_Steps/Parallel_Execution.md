---
created_at: '2019-01-10T03:02:11Z'
hidden: false
label_names: []
position: 4
title: Parallel Execution
vote_count: 7
vote_sum: 5
zendesk_article_id: 360000690275
zendesk_section_id: 360000189716
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p><span style="font-weight: 400;">Many scientific software applications are written<dfn class="dictionary-of-numbers"> to take advantage </dfn>of multiple CPUs in some way. But often<dfn class="dictionary-of-numbers"> this must be </dfn>specifically requested by the user at the time they run the program, rather than happening automatically.</span><span style="font-weight: 400;"><br></span></p>
<p>The are <dfn class="dictionary-of-numbers">three types of parallel </dfn>execution we will cover are <a style="background-color: #ffffff;" href="#t_multi">Multi-Threading(oMP)</a>, <a style="background-color: #ffffff;" href="#t_mpi">Distributed(MPI)</a> and <a style="background-color: #ffffff;" href="#t_array">Job Arrays</a>.</p>
<blockquote class="blockquote-tip">
<h3 id="01H8NBXT8RQWES3GQWMGD6XYBB">Note</h3>
Whenever Slurm mentions CPUs it is referring to <em>logical</em> CPU's (<strong>2</strong> <em>logical</em> CPU's = <strong>1</strong> <em>physical</em> core).<br>
<ul>
<li>
<code>--cpus-per-task=4</code> will give you 4 <em>logical </em>cores.</li>
<li>
<code>--mem-per-cpu=512MB</code> will give <dfn class="dictionary-of-numbers">512 MB of RAM</dfn> per <em>logical</em> core.</li>
<li>If <code>--hint=nomultithread</code> is used then <code>--cpus-per-task</code> will now refer to physical cores, but <code>--mem-per-cpu=512MB</code> still refers to logical cores.</li>
</ul>
</blockquote>
<p>See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000568236" target="_self">our article on hyperthreading</a> for more information.</p>
<h1 id="t_multi">Multi-threading</h1>
<p><span style="font-weight: 400;">Multi-threading is a method of parallelisation whereby the initial single thread of a process forks into a number of parallel threads, generally <em>via</em> a library such as OpenMP (Open MultiProcessing), TBB (Threading Building Blocks), or pthread (PO<dfn class="dictionary-of-numbers">SIX threads)</dfn>.</span></p>
<div class="panel">
<img class="figure-img" src="https://support.nesi.org.nz/hc/article_attachments/360001532455" alt="Diagram showing serial operations."><br><em>Fig. 1: In a serial operation, tasks complete <dfn class="dictionary-of-numbers">one after another</dfn>.</em>
</div>
<h4 id="01H8NBXT8SX7JFY9B1P3YGWX9H"> </h4>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001532435" alt="par.png" width="714" height="160"><em><br>Fig. 2: Multi-threading involves dividing the process into multiple 'threads' which can be run across multiple cores.</em></p>
<p>Multi-threading is limited in that it requires shared memory, so all CPU cores used must be on the same node. However, because all the CPUs share the same memory environment things only need to be loaded into memory once, meaning that memory requirements will usually not increase proportionally to the number of CPUs.</p>
<p>Example script;</p>
<pre><code>#!/bin/bash -e<br>#SBATCH --job-name=MultithreadingTest    # job name (shows up in the queue)<br>#SBATCH --time=00:01:00                  # Walltime (HH:MM:SS)<br>#SBATCH --mem=2048MB                     # memory in MB <br>#SBATCH --cpus-per-task=4                # 2 physical cores per task.<br><br><span style="font-weight: 400;">taskset -c -p $$</span>                         <span style="font-weight: 400;">#Prints which CPUs it can use</span>
</code></pre>
<p>The expected output being</p>
<pre><code>pid 13538's current affinity list: 7,9,43,45</code></pre>
<h1 id="t_mpi">MPI</h1>
<p>MPI stands for <em>Message Passing Interface</em>, and <span style="font-weight: 400;">is a communication protocol used to achieve distributed parallel computation.</span></p>
<p><span style="font-weight: 400;">Similar in some ways to multi-threading, MPI does not have the limitation of requiring shared memory and thus can be used across multiple nodes, but has higher communication and memory overheads.</span></p>
<p>For MPI jobs you need to set <code class="highlighter-rouge">--ntasks</code> to a value larger than 1, or if you want all nodes to run the same number of tasks, set <code class="highlighter-rouge">--ntasks-per-node</code> and <code class="highlighter-rouge">--nodes</code> instead.</p>
<p>MPI programs require a launcher to start the <em>ntasks</em> processes on multiple CPUs, which may belong to different nodes. On Slurm systems like ours, the preferred launcher is <code>srun</code> rather than <code>mpi-run</code>.</p>
<p>Since the distribution of tasks across different nodes may be unpredictable, <code>--mem-per-cpu</code> should be used instead of <code>--mem</code>.<code class="nohighlight"></code></p>
<pre><code>#!/bin/bash -e
#SBATCH --job-name=MPIJob    	# job name (shows up in the queue)
#SBATCH --time=00:01:00     	# Walltime (HH:MM:SS)
#SBATCH --mem-per-cpu=512MB  	# memory/cpu in MB (half the actual required memory)<br>#SBATCH --cpus-per-task=4       # 2 Physical cores per task.
#SBATCH --ntasks=2          	# number of tasks (e.g. MPI)

srun pwd                        # Prints  working directory
</code></pre>
<p>The expected output being</p>
<pre><samp>/home/user001/demo
/home/user001/demo
</samp></pre>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>For non-MPI programs, either set <code>--ntasks=1</code> or do not use <code>srun</code> at all. Using <code>srun</code> in conjunction with <code>--cpus-per-task=1</code> will cause <code>--ntasks</code> to default to 2.</p>
</blockquote>
<h1 id="t_array">Job Arrays</h1>
<p>Job arrays are best used for tasks that are completely independent, such as parameter sweeps, permutation analysis or simulation, that could be executed in any order and don't have to run at the same time. This kind of work is often described as<dfn class="dictionary-of-numbers"> </dfn><em>embarrassingly parallel</em>.<br>An embarrassingly parallel problem is one that requires no communication or dependency between the tasks (unlike distributed computing problems that need communication between tasks).</p>
<p>A job array will submit the same script repeatedly over a designated index using the SBATCH command <code class="nohighlight">#SBATCH --array</code></p>
<p>For example, the following code:</p>
<pre><code>#!/bin/bash -e
#SBATCH --job-name=ArrayJob             # job name (shows up in the queue)
#SBATCH --time=00:01:00                 # Walltime (HH:MM:SS)
#SBATCH --mem=512MB                     # Memory
#SBATCH --array=1-2                     # Array jobs
<br>
pwd
echo "This is result ${SLURM_ARRAY_TASK_ID}"
</code></pre>
<p>will submit,  <code class='"nohighlight'>ArrayJob_1</code> and <code class="nohighlight">ArrayJob_2</code>, which will return the results <samp class="nohighlight">This is result 1</samp> and <samp class="nohighlight">This is result 2</samp> respectively.</p>
<h2 id="01H8NBXT8SYDPVVFRY14HWKMC2">Using SLURM_ARRAY_TASK_ID</h2>
<p>Use of the environment variable <code class="nohighlight">${SLURM_ARRAY_TASK_ID}</code> is the recommended method of variation between the jobs. For example:</p>
<ul>
<ul>
<ul>
<li>As a direct input to a function.<br>
<pre><code class="code-matlab">matlab -nodisplay -r "myFunction(${SLURM_ARRAY_TASK_ID})"</code></pre>
</li>
<li>As an index to an array.<br>
<pre><code class="code-bash">inArray=(1 2 4 8 16 32 64 128)<br>input=${inArray[$SLURM_ARRAY_TASK_ID]}</code></pre>
</li>
<li>For selecting input files.<br>
<pre><code class="code-bash">input=inputs/mesh_${SLURM_ARRAY_TASK_ID}.stl</code></pre>
</li>
<li>As a seed for a pseudo-random number.<br>
<ul>
<li>
<p>In R</p>
<pre dir="ltr"><code class="code-r">task_id = as.numeric(Sys.getenv("SLURM_ARRAY_TASK_ID"))
set.seed(task_id)</code></pre>
</li>
<li>
<p>In MATLAB</p>
<pre dir="ltr"><code class="code-r">task_id = str2num(getenv('SLURM_ARRAY_TASK_ID'))
rng(task_id)</code></pre>
</li>
</ul>
<em><br>Using a seed is important, otherwise multiple jobs may receive the same pseudo-random numbers.</em>
</li>
<li>As an index to an array of filenames. 
<pre><code>files=( inputs/*.dat )
input=${files[SLURM_ARRAY_TASK_ID]}
# If there are 5 '.dat' files in 'inputs/' you will want to use '#SBATCH --array=0-4' </code></pre>
This example will submit a job array with each job using a .dat file in 'inputs' as the variable input (in alphabetcial order).</li>
</ul>
</ul>
</ul>
<p>Environment variables <em>will not work</em> in the Slurm header. In place of <code class="nohighlight">${SLURM_ARRAY_TASK_ID}</code>, you can use the token <code>%a</code>. This can be useful for sorting your output files e.g.</p>
<pre><code class="nohighlight">#SBATCH --output=outputs/run_%a/slurm_output.out
#SBATCH --output=outputs/run_%a/slurm_error.err
</code></pre>
<h4 id="01H8NBXT8TSRR7X493NXKR6VXT">Multidimensional array example</h4>
<pre><code>#!/bin/bash -e

#SBATCH --open-mode append
#SBATCH --output week_times.out
#SBATCH --array 0-167 #This needs to be equal to combinations (in this case 7*24), and zero based.

# Define your dimensions in bash arrays.
arr_time=({00..23})
arr_day=("Mon" "Tue" "Wed" "Thur" "Fri" "Sat" "Sun") 

# Index the bash arrays based on the SLURM_ARRAY_TASK)
n_time=${arr_time[$(($SLURM_ARRAY_TASK_ID%${#arr_time[@]}))]} # '%' for finding remainder.
n_day=${arr_day[$(($SLURM_ARRAY_TASK_ID/${#arr_time[@]}))]}

echo "$n_day $n_time:00"</code></pre>
<h2 id="01H8NBXT8TM8N6K7PA8K9VSCYX">Avoiding Conflicts</h2>
<p>As all the array jobs could theoretically run at the same time, it is important that all file references are unique and independent.</p>
<p>If your program makes use of a working directory make sure you set it e.g.</p>
<pre><code class="nohighlight">mkdir .tmp/run_${SLURM_ARRAY_TASK_ID}          #Create new directory<br>export TMPDIR=.tmp/run_${SLURM_ARRAY_TASK_ID}  #Set TMPDIR to point there</code></pre>
<p>If you have no control over the name/path of an output used by a program, this can be resolved in a similar manner.</p>
<pre><code class="nohighlight">mkdir run_${SLURM_ARRAY_TASK_ID}                             #Create new directory<br>cd run_${SLURM_ARRAY_TASK_ID}                                #CD to new directory<br>#<br>bash job.sh<br>#<br>mv output.log ../outputs/output_${SLURM_ARRAY_TASK_ID}.log   #Move and rename output<br>rm -r ../run_${SLURM_ARRAY_TASK_ID}                          #Clear directory</code></pre>
<p>The Slurm documentation on job arrays can be found <a href="https://slurm.schedmd.com/job_array.html">here</a>.</p>
<p> </p>