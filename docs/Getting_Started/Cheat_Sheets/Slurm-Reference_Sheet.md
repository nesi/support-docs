---
created_at: '2019-01-10T02:22:09Z'
tags: []
title: 'Slurm: Reference Sheet'
vote_count: 10
vote_sum: 10
zendesk_article_id: 360000691716
zendesk_section_id: 360000278975
---

If you are unsure about using our job scheduler Slurm, more details can
be found
[here](../../Getting_Started/Next_Steps/Submitting_your_first_job.md).

## Slurm Commands

A complete list of Slurm commands can be found
[here](https://slurm.schedmd.com/man_index.html), or by entering man
slurm into a terminal

|         |                       |                                                                           |
|---------|-----------------------|---------------------------------------------------------------------------|
| sbatch  | `sbatch submit.sl`    | Submits the Slurm script *submit.sl*                                      |
| squeue  | `squeue`              | Displays entire queue.                                                    |
|         | `squeue --me`         | Displays your queued jobs.                                                |
|         | `squeue -p long`      | Displays queued jobs on the *long* partition.                             |
| sacct   | `sacct`               | Displays all the jobs run by you that day.                                |
|         | `sacct -S 2019-01-01` | Displays all the jobs run by you since the *1st Jan 2019*                 |
|         | `sacct -j 123456789`  | Displays job *123456789*                                                  |
| scancel | `scancel 123456789`   | Cancels job *123456789*                                                   |
|         | `scancel --me`        | Cancels all your jobs.                                                    |
| sshare  | `sshare -U`           | Shows the Fair Share scores for all projects of which *you* are a member. |
| sinfo   | `sinfo`               | Shows the current state of our Slurm partitions.                          |
|         |                       |                                                                           |

## `sbatch`` options

A complete list of *sbatch* options can be found
[here](https://slurm.schedmd.com/sbatch.html), or by running man sbatch

Options can be provided on the command line or in the batch file as an
`#SBATCH` directive.  The option name and value can be separated using
an '=' sign e.g. `#SBATCH --account=nesi99999` or a space e.g.
`#SBATCH --account nesi99999`. *But not both!*

### General options

  ----------------------- ---------------------------------------- -------------------------------------------------------------------------------------------------------
  --job-name              `#SBATCH --job-name=MyJob`               The name that will appear when using squeue or sacct

  --account               `#SBATCH --account=nesi99999`            The account your core hours will be 'charged' to.

  --time                  `#SBATCH --time=DD-HH:MM:SS`             Job max walltime  

  --mem                   `#SBATCH --mem=512MB`                    Memory required per node.

  --partition             `#SBATCH --partition=long`               Specified job
                                                                   [partition](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Mahuika_Slurm_Partitions.md).

  --output                `#SBATCH --output=%j_output.out`         Path and name of standard output file.

  --mail-user             `#SBATCH --mail-user=bob123@gmail.com`   Address to send mail notifications.

  --mail-type             `#SBATCH --mail-type=ALL`                Will send a mail notification at `BEGIN END FAIL`

                          `#SBATCH --mail-type=TIME_LIMIT_80`      Will send message at *80%* walltime

  --no-requeue            `#SBATCH --no-requeue`                   Will stop job being requeued in the case of node failure.
  ----------------------- ---------------------------------------- -------------------------------------------------------------------------------------------------------

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
<td style="width: 303px; height: 23px"><code
class="sl">#SBATCH --nodes=2</code></td>
<td style="width: 446px; height: 23px">Will request tasks be run across
2 nodes.</td>
</tr>
<tr class="even" style="height: 23px;">
<td style="width: 148px; height: 23px">--ntasks</td>
<td style="width: 303px; height: 23px"><code
class="sl">#SBATCH --ntasks=2</code></td>
<td style="width: 446px; height: 23px">Will start 2 <a
href="https://support.nesi.org.nz/knowledge/articles/360000690275/">MPI</a>
tasks.</td>
</tr>
<tr class="odd" style="height: 23px;">
<td style="width: 148px; height: 23px">--ntasks-per-node</td>
<td style="width: 303px; height: 23px"><code
class="sl">#SBATCH --ntasks-per-node=1</code></td>
<td style="width: 446px; height: 23px">Will start 1 task per requested
node</td>
</tr>
<tr class="even" style="height: 23px;">
<td style="width: 148px; height: 23px">--cpus-per-task</td>
<td style="width: 303px; height: 23px"><code
class="sl">#SBATCH --cpus-per-task=10</code></td>
<td style="width: 446px; height: 23px"><p>Will request 10
<em>logical</em> CPUs per task.</p>
<p>See <a
href="../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Hyperthreading.md">Hyperthreading</a>.</p></td>
</tr>
<tr class="odd" style="height: 23px;">
<td style="width: 148px; height: 23px">--mem-per-cpu</td>
<td style="width: 303px; height: 23px"><code
class="sl">#SBATCH --mem-per-cpu=512MB</code></td>
<td style="width: 446px; height: 23px"><p>Memory Per <em>logical</em>
CPU.</p>
<p><code class="sl">--mem</code> Should be used if shared memory
job.</p>
<p>See <a href="../../General/FAQs/How_do_I_request_memory.md">How do I
request memory?</a>.</p></td>
</tr>
<tr class="even" style="height: 46px;">
<td style="width: 148px; height: 46px">--array</td>
<td style="width: 303px; height: 46px"><code
class="sl">#SBATCH --array=1-5</code></td>
<td style="width: 446px; height: 46px">Will submit job 5 times each with
a different <code class="sl">$SLURM_ARRAY_TASK_ID</code>
(1,2,3,4,5)</td>
</tr>
<tr class="odd" style="height: 44px;">
<td style="width: 148px; height: 44px"> </td>
<td style="width: 303px; height: 44px"><code
class="sl">#SBATCH --array=0-20:5</code></td>
<td style="width: 446px; height: 44px">Will submit job 5 times each with
a different <code class="sl">$SLURM_ARRAY_TASK_ID</code>
(0,5,10,15,20)</td>
</tr>
<tr class="even">
<td style="width: 148px"> </td>
<td style="width: 303px"><code
class="sl">#SBATCH --array=1-100%10</code></td>
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
<td style="width: 320px"><code
class="sl">#SBATCH --qos=debug</code></td>
<td style="width: 461.567px">Adding this line gives your job a very high
priority. <em>Limited to one job at a time, max 15 minutes</em>.</td>
</tr>
<tr class="even">
<td style="width: 150.433px">--profile</td>
<td style="width: 320px"><code
class="sl">#SBATCH --profile=ALL</code></td>
<td style="width: 461.567px"><p>Allows generation of a .h5 file
containing job profile information.</p>
<p>See <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000810616-How-can-I-profile-a-SLURM-job-">Slurm
Native Profiling</a>.</p></td>
</tr>
<tr class="odd">
<td style="width: 150.433px">--dependency</td>
<td style="width: 320px"><code
class="sl">#SBATCH --dependency=afterok:123456789</code></td>
<td style="width: 461.567px">Will only start after the job 123456789 has
completed.</td>
</tr>
<tr class="even">
<td style="width: 150.433px">--hint</td>
<td style="width: 320px"><code
class="sl">#SBATCH --hint=nomultithread</code></td>
<td style="width: 461.567px">Disables <a
href="../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Hyperthreading.md">hyperthreading</a>,
be aware that this will significantly change how your job is
defined.</td>
</tr>
</tbody>
</table>
!!! tip
     Many options have a short and long form e.g.
     `#SBATCH --job-name=MyJob` & `#SBATCH -J=MyJob`.

     ``` sh
     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"
     ```

## Tokens

These are predefined variables that can be used in sbatch directives
such as the log file name.

## Environment variables

Common examples.

|                        |                                                  |
|------------------------|--------------------------------------------------|
| `$SLURM_JOB_ID`        | Useful for naming output files that won't clash. |
| `$SLURM_JOB_NAME`      | Name of the job.                                 |
| `$SLURM_ARRAY_TASK_ID` | The current index of your array job.             |
| `$SLURM_CPUS_PER_TASK` | Useful as an input for multi-threaded functions. |
| `$SLURM_NTASKS`        | Useful as an input for MPI functions.            |
| `$SLURM_SUBMIT_DIR`    | Directory where `sbatch` was called.             |

!!! tip
     In order to decrease the chance of a variable being misinterpreted you
     should use the syntax `${NAME_OF_VARIABLE}` and define in strings if
     possible. e.g.

     ``` sh
     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"
     ```
