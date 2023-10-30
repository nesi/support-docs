---
created_at: '2019-01-10T02:22:09Z'
hidden: false
label_names: []
position: 1
title: 'Slurm: Reference Sheet'
vote_count: 9
vote_sum: 9
zendesk_article_id: 360000691716
zendesk_section_id: 360000278975
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

If you are unsure about using our job scheduler Slurm, more details can
be found
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000684396).

## Slurm Commands

A complete list of Slurm commands can be found
[here](https://slurm.schedmd.com/man_index.html), or by entering man
slurm into a terminal

<table style="height: 246px; width: 966px;">
<tbody>
<tr class="odd" style="height: 22px;">
<td style="width: 157.141px; height: 21px">sbatch</td>
<td
style="width: 301.297px; height: 21px"><code>sbatch submit.sl</code></td>
<td style="width: 473.562px; height: 21px">Submits the Slurm script
<em>submit.sl</em></td>
</tr>
<tr class="even" style="height: 22px;">
<td rowspan="3" style="width: 157.141px; height: 61px">squeue</td>
<td style="width: 301.297px; height: 21px"><code>squeue</code></td>
<td style="width: 473.562px; height: 21px">Displays entire queue.</td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="width: 301.297px; height: 18px"><code>squeue --me</code></td>
<td style="width: 473.562px; height: 18px">Displays your queued
jobs.</td>
</tr>
<tr class="even" style="height: 22px;">
<td
style="width: 301.297px; height: 22px"><code>squeue -p long</code></td>
<td style="width: 473.562px; height: 22px">Displays queued jobs on
the <em>long</em> partition.</td>
</tr>
<tr class="odd" style="height: 22px;">
<td rowspan="3" style="width: 157.141px; height: 66px">sacct</td>
<td style="width: 301.297px; height: 22px"><code>sacct</code></td>
<td style="width: 473.562px; height: 22px">Displays all the jobs run by
you that day.</td>
</tr>
<tr class="even" style="height: 22px;">
<td
style="width: 301.297px; height: 22px"><code>sacct -S 2019-01-01</code></td>
<td style="width: 473.562px; height: 22px">Displays all the jobs run by
you since the <em>1st Jan 2019</em></td>
</tr>
<tr class="odd" style="height: 22px;">
<td
style="width: 301.297px; height: 22px"><code>sacct -j 123456789</code></td>
<td style="width: 473.562px; height: 22px">Displays job
<em>123456789</em></td>
</tr>
<tr class="even" style="height: 22px;">
<td rowspan="2" style="width: 157.141px; height: 44px">scancel</td>
<td
style="width: 301.297px; height: 22px"><code>scancel 123456789</code></td>
<td style="width: 473.562px; height: 22px">Cancels job
<em>123456789</em></td>
</tr>
<tr class="odd" style="height: 22px;">
<td
style="width: 301.297px; height: 22px"><code>scancel --me</code></td>
<td style="width: 473.562px; height: 22px">Cancels all your jobs.</td>
</tr>
<tr class="even" style="height: 22px;">
<td style="width: 157.141px; height: 22px">sshare</td>
<td style="width: 301.297px; height: 22px"><code>sshare -U</code></td>
<td style="width: 473.562px; height: 22px">Shows the Fair Share scores
for all projects of which <em>you</em> are a member.</td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="width: 157.141px; height: 22px">sinfo</td>
<td style="width: 301.297px; height: 22px"><code>sinfo</code></td>
<td style="width: 473.562px; height: 22px">Shows the current state of
our Slurm partitions.</td>
</tr>
<tr class="even" style="height: 22px;">
<td style="width: 157.141px; height: 10px"> </td>
<td style="width: 301.297px; height: 10px"> </td>
<td style="width: 473.562px; height: 10px"> </td>
</tr>
</tbody>
</table>

 

------------------------------------------------------------------------

 

## *sbatch* options

A complete list of *sbatch* options can be found
[here](https://slurm.schedmd.com/sbatch.html), or by running man sbatch

Options can be provided on the command line or in the batch file as an
`#SBATCH` directive.  The option name and value can be separated using
an '=' sign e.g. `#SBATCH --account=nesi99999` or a space e.g.
`#SBATCH --account nesi99999`. *But not both!*

### General options

<table style="width: 966px; height: 40px;">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd" style="height: 40px;">
<td style="width: 156.167px; height: 40px">--job-name</td>
<td
style="width: 314.333px; height: 40px"><span><code>#SBATCH --job-name=MyJob</code></span></td>
<td style="width: 461.5px; height: 40px"><span>The name that will appear
when using squeue or sacct</span></td>
</tr>
<tr class="even" style="height: 40px;">
<td style="width: 156.167px; height: 40px">--account</td>
<td
style="width: 314.333px; height: 40px"><span><code>#SBATCH --account=nesi99999</code></span></td>
<td style="width: 461.5px; height: 40px"><span>The account your core
hours will be 'charged' to.</span></td>
</tr>
<tr class="odd" style="height: 40px;">
<td style="width: 156.167px; height: 40px">--time</td>
<td
style="width: 314.333px; height: 40px"><span><code>#SBATCH --time=DD-HH:MM:SS</code></span></td>
<td style="width: 461.5px; height: 40px"><span>Job max walltime<br />
</span></td>
</tr>
<tr class="even" style="height: 40px;">
<td style="width: 156.167px; height: 40px">--mem</td>
<td
style="width: 314.333px; height: 40px"><span><code>#SBATCH --mem=512MB</code></span></td>
<td style="width: 461.5px; height: 40px">Memory required per node.</td>
</tr>
<tr class="odd" style="height: 40px;">
<td style="width: 156.167px; height: 40px">--partition</td>
<td
style="width: 314.333px; height: 40px"><span><code>#SBATCH --partition=long</code></span></td>
<td style="width: 461.5px; height: 40px">Specified job <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000204076-Mahuika-Slurm-Partitions">partition</a>.</td>
</tr>
<tr class="even" style="height: 40px;">
<td style="width: 156.167px; height: 40px">--output</td>
<td
style="width: 314.333px; height: 40px"><code>#SBATCH --output=%j_output.out</code></td>
<td style="width: 461.5px; height: 41px">Path and name of standard
output file.</td>
</tr>
<tr class="odd" style="height: 40px;">
<td style="width: 156.167px; height: 40px">--mail-user</td>
<td style="width: 314.333px; height: 40px"><code
class="nohighlight">#SBATCH --mail-user=bob123@gmail.com</code></td>
<td style="width: 461.5px; height: 40px">Address to send mail
notifications.</td>
</tr>
<tr class="even" style="height: 40px;">
<td rowspan="2" style="width: 156.167px; height: 40px">--mail-type</td>
<td
style="width: 314.333px; height: 40px"><code>#SBATCH --mail-type=ALL</code></td>
<td style="width: 461.5px; height: 40px">Will send a mail notification
at <code>BEGIN END FAIL</code></td>
</tr>
<tr class="odd" style="height: 41px;">
<td
style="width: 314.333px; height: 40px"><code>#SBATCH --mail-type=TIME_LIMIT_80</code></td>
<td style="width: 461.5px; height: 40px">Will send message at
<em>80%</em> walltime</td>
</tr>
<tr class="even">
<td style="width: 156.167px">--no-requeue</td>
<td style="width: 314.333px"><code>#SBATCH --no-requeue</code><br />
</td>
<td style="width: 461.5px">Will stop job being requeued in the case of
node failure.</td>
</tr>
</tbody>
</table>

### Parallel options

<table style="height: 205px; width: 966px;">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd" style="height: 23px;">
<td style="width: 148px; height: 23px">--nodes</td>
<td
style="width: 303px; height: 23px"><code>#SBATCH --nodes=2</code></td>
<td style="width: 446px; height: 23px">Will request tasks be run across
2 nodes.</td>
</tr>
<tr class="even" style="height: 23px;">
<td style="width: 148px; height: 23px">--ntasks</td>
<td
style="width: 303px; height: 23px"><code>#SBATCH --ntasks=2</code></td>
<td style="width: 446px; height: 23px">Will start 2 <a
href="https://support.nesi.org.nz/knowledge/articles/360000690275/">MPI</a>
tasks.</td>
</tr>
<tr class="odd" style="height: 23px;">
<td style="width: 148px; height: 23px">--ntasks-per-node</td>
<td
style="width: 303px; height: 23px"><code>#SBATCH --ntasks-per-node=1</code></td>
<td style="width: 446px; height: 23px">Will start 1 task per requested
node</td>
</tr>
<tr class="even" style="height: 23px;">
<td style="width: 148px; height: 23px">--cpus-per-task</td>
<td
style="width: 303px; height: 23px"><code>#SBATCH --cpus-per-task=10</code></td>
<td style="width: 446px; height: 23px"><p>Will request 10
<em>logical</em> CPUs per task.</p>
<p>See <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000568236-Hyperthreading">Hyperthreading</a>.</p></td>
</tr>
<tr class="odd" style="height: 23px;">
<td style="width: 148px; height: 23px">--mem-per-cpu</td>
<td
style="width: 303px; height: 23px"><code>#SBATCH --mem-per-cpu=512MB</code></td>
<td style="width: 446px; height: 23px"><p>Memory Per <em>logical</em>
CPU.</p>
<p><code>--mem</code> Should be used if shared memory job.</p>
<p>See <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360001108756">How do
I request memory?</a>.</p></td>
</tr>
<tr class="even" style="height: 46px;">
<td style="width: 148px; height: 46px">--array</td>
<td
style="width: 303px; height: 46px"><code>#SBATCH --array=1-5</code></td>
<td style="width: 446px; height: 46px">Will submit job 5 times each with
a different <code>$SLURM_ARRAY_TASK_ID</code> (1,2,3,4,5)</td>
</tr>
<tr class="odd" style="height: 44px;">
<td style="width: 148px; height: 44px"> </td>
<td
style="width: 303px; height: 44px"><code>#SBATCH --array=0-20:5</code></td>
<td style="width: 446px; height: 44px">Will submit job 5 times each with
a different <code>$SLURM_ARRAY_TASK_ID</code> (0,5,10,15,20)</td>
</tr>
<tr class="even">
<td style="width: 148px"> </td>
<td style="width: 303px"><code>#SBATCH --array=1-100%10</code></td>
<td style="width: 446px">Will submit 1 though to 100 jobs but no more
than 10 at once.</td>
</tr>
</tbody>
</table>

### Other

<table style="height: 76px; width: 966px;">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="width: 150.433px">--qos</td>
<td style="width: 320px"><code>#SBATCH --qos=debug</code></td>
<td style="width: 461.567px">Adding this line gives your job a very high
priority. <em>Limited to one job at a time, max 15 minutes</em>.</td>
</tr>
<tr class="even">
<td style="width: 150.433px">--profile</td>
<td style="width: 320px"><code>#SBATCH --profile=ALL</code></td>
<td style="width: 461.567px"><p>Allows generation of a .h5 file
containing job profile information.</p>
<p>See <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000810616-How-can-I-profile-a-SLURM-job-">Slurm
Native Profiling</a>.</p></td>
</tr>
<tr class="odd">
<td style="width: 150.433px">--dependency</td>
<td
style="width: 320px"><code>#SBATCH --dependency=afterok:123456789</code></td>
<td style="width: 461.567px">Will only start after the job 123456789 has
completed.</td>
</tr>
<tr class="even">
<td style="width: 150.433px">--hint</td>
<td style="width: 320px"><code>#SBATCH --hint=nomultithread</code></td>
<td style="width: 461.567px">Disables <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000568236-Hyperthreading">hyperthreading</a>,
be aware that this will significantly change how your job is
defined.</td>
</tr>
</tbody>
</table>
!!! info Tip
>
> Many options have a short and long form e.g.
> `#SBATCH --job-name=MyJob` & `#SBATCH -J=MyJob`.
>
>     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"

## Tokens

These are predefined variables that can be used in sbatch directives
such as the log file name.

<table style="height: 92px; width: 600px;">
<tbody>
<tr class="odd" style="height: 23px;">
<td style="width: 209.367px; height: 23px"><code
class="nohighlight">%x</code></td>
<td style="width: 367.633px; height: 23px">Job name</td>
</tr>
<tr class="even" style="height: 23px;">
<td style="width: 209.367px; height: 23px"><code
class="nohighlight">%u</code></td>
<td style="width: 367.633px; height: 23px">User name.</td>
</tr>
<tr class="odd" style="height: 23px;">
<td style="width: 209.367px; height: 23px"><code
class="nohighlight">%j</code></td>
<td style="width: 367.633px; height: 23px">Job ID </td>
</tr>
<tr class="even" style="height: 23px;">
<td style="width: 209.367px; height: 23px"><code
class="nohighlight">%a</code></td>
<td style="width: 367.633px; height: 23px">Job array Index</td>
</tr>
</tbody>
</table>

## Environment variables

Common examples.

<table style="height: 91px; width: 600px;">
<tbody>
<tr class="odd">
<td style="width: 210.367px"><code
class="highlighter-rouge">$SLURM_JOB_ID</code></td>
<td style="width: 366.633px">Useful for naming output files that won't
clash.</td>
</tr>
<tr class="even">
<td style="width: 210.367px"><code
class="highlighter-rouge">$SLURM_JOB_NAME</code></td>
<td style="width: 366.633px">Name of the job.</td>
</tr>
<tr class="odd">
<td style="width: 210.367px"><code
class="highlighter-rouge">$SLURM_ARRAY_TASK_ID</code></td>
<td style="width: 366.633px">The current index of your array job. </td>
</tr>
<tr class="even">
<td style="width: 210.367px"><code
class="highlighter-rouge">$SLURM_CPUS_PER_TASK</code></td>
<td style="width: 366.633px">Useful as an input for multi-threaded
functions.</td>
</tr>
<tr class="odd">
<td style="width: 210.367px"><code
class="highlighter-rouge">$SLURM_NTASKS</code></td>
<td style="width: 366.633px">Useful as an input for MPI functions.</td>
</tr>
<tr class="even">
<td style="width: 210.367px"><code
class="highlighter-rouge">$SLURM_SUBMIT_DIR</code></td>
<td style="width: 366.633px">Directory where <code
class="nohighlight">sbatch</code> was called.</td>
</tr>
</tbody>
</table>
!!! info Tip
>
> In order to decrease the chance of a variable being misinterpreted you
> should use the syntax `${NAME_OF_VARIABLE}` and define in strings if
> possible. e.g.
>
>     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"
