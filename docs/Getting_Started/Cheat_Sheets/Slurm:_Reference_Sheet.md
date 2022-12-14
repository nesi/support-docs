---
created_at: '2019-01-10T02:22:09Z'
hidden: false
label_names: []
position: 1
title: 'Slurm: Reference Sheet'
vote_count: 8
vote_sum: 8
zendesk_article_id: 360000691716
zendesk_section_id: 360000278975
---

If you are unsure about using our job scheduler Slurm, more details can
be found
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000684396).

## Slurm Commands

A complete list of Slurm commands can be found
[here](https://slurm.schedmd.com/man_index.html), or by entering <span
class="kbd">man slurm</span> into a terminal

<table style="height: 246px; width: 966px;">
<tbody>
<tr style="height: 22px;">
<td style="width: 157.141px; height: 21px;">

sbatch

</td>
<td style="width: 301.297px; height: 21px;">

`sbatch submit.sl`

</td>
<td style="width: 473.562px; height: 21px;">

Submits the SLURM script *submit.sl*

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 157.141px; height: 61px;" rowspan="3">

squeue

</td>
<td style="width: 301.297px; height: 21px;">

`squeue`

</td>
<td style="width: 473.562px; height: 21px;">

Displays entire queue.

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 301.297px; height: 18px;">

`squeue -u usr9999`

</td>
<td style="width: 473.562px; height: 18px;">

Displays queued jobs submitted by *usr9999*.

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 301.297px; height: 22px;">

`squeue -p long`

</td>
<td style="width: 473.562px; height: 22px;">

Displays queued jobs on the *long* partition.

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 157.141px; height: 66px;" rowspan="3">

sacct

</td>
<td style="width: 301.297px; height: 22px;">

`sacct`

</td>
<td style="width: 473.562px; height: 22px;">

Displays all the jobs run by you that day.

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 301.297px; height: 22px;">

`sacct -S 2019-01-01`

</td>
<td style="width: 473.562px; height: 22px;">

Displays all the jobs run by you since the *1st Jan 2019*

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 301.297px; height: 22px;">

`sacct -j 123456789`

</td>
<td style="width: 473.562px; height: 22px;">

Displays job *123456789*

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 157.141px; height: 44px;" rowspan="2">

scancel

</td>
<td style="width: 301.297px; height: 22px;">

`scancel 123456789`

</td>
<td style="width: 473.562px; height: 22px;">

Cancels job *123456789*

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 301.297px; height: 22px;">

`scancel -u usr9999`

</td>
<td style="width: 473.562px; height: 22px;">

Cancels all your jobs (assuming you are *usr9999*). If you are not
*usr9999*, you will get an error message.

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 157.141px; height: 22px;">

sshare

</td>
<td style="width: 301.297px; height: 22px;">

`sshare -U usr9999`

</td>
<td style="width: 473.562px; height: 22px;">

Shows the Fair Share scores for all projects of which *usr9999* is a
member.

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 157.141px; height: 22px;">

sinfo

</td>
<td style="width: 301.297px; height: 22px;">

`sinfo`

</td>
<td style="width: 473.562px; height: 22px;">

Shows the current state of our SLURM partitions.

</td>
</tr>
<tr style="height: 22px;">
<td style="width: 157.141px; height: 10px;">

 

</td>
<td style="width: 301.297px; height: 10px;">

 

</td>
<td style="width: 473.562px; height: 10px;">

 

</td>
</tr>
</tbody>
</table>

 

------------------------------------------------------------------------

 

## *sbatch* options

A complete list of *sbatch* options can be found
[here](https://slurm.schedmd.com/sbatch.html), or by running <span
class="kbd">man sbatch</span>

Options can be provided on the command line or in the batch file as an
`#SBATCH` directive.  The option name and value can be separated using
an '=' sign e.g. `#SBATCH --account=nesi99999` or a space e.g.
`#SBATCH --account nesi99999`. *But not both!*

### General options

<table style="width: 966px; height: 40px;">
<tbody>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;">

--job-name

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --job-name=MyJob`

</td>
<td style="width: 461.5px; height: 40px;">

<span class="c">The name that will appear when using squeue or
sacct</span>

</td>
</tr>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;">

--account

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --account=nesi99999`

</td>
<td style="width: 461.5px; height: 40px;">

<span class="c">The account your core hours will be 'charged' to.</span>

</td>
</tr>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;">

--time

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --time=DD-HH:MM:SS`

</td>
<td style="width: 461.5px; height: 40px;">

<span class="c">Job max walltime  
</span>

</td>
</tr>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;">

--mem

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --mem=512MB`

</td>
<td style="width: 461.5px; height: 40px;">

Memory required per node.

</td>
</tr>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;">

--partition

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --partition=long`

</td>
<td style="width: 461.5px; height: 40px;">

Specified job
[partition](https://support.nesi.org.nz/hc/en-gb/articles/360000204076-Mahuika-Slurm-Partitions).

</td>
</tr>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;">

--output

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --output=%j_output.out`

</td>
<td style="width: 461.5px; height: 41px;">

Path and name of standard output file.

</td>
</tr>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;">

--mail-user

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --mail-user=bob123@gmail.com`

</td>
<td style="width: 461.5px; height: 40px;">

Address to send mail notifications.

</td>
</tr>
<tr style="height: 40px;">
<td style="width: 156.167px; height: 40px;" rowspan="2">

--mail-type

</td>
<td style="width: 314.333px; height: 40px;">

`#SBATCH --mail-type=ALL`

</td>
<td style="width: 461.5px; height: 40px;">

Will send a mail notification at `BEGIN  END  FAIL`

</td>
</tr>
<tr style="height: 41px;">
<td style="width: 314.333px; height: 40px;">

`#SBATCH --mail-type=TIME_LIMIT_80`

</td>
<td style="width: 461.5px; height: 40px;">

Will send message at *80%* walltime

</td>
</tr>
<tr>
<td style="width: 156.167px;">

--no-requeue

</td>
<td style="width: 314.333px;">

`#SBATCH --no-requeue`

</td>
<td style="width: 461.5px;">

Will stop job being requeued in the case of node failure.

</td>
</tr>
</tbody>
</table>

### Parallel options

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

### Other

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

> ### Tip
>
> Many options have a short and long form e.g.
> `#SBATCH --job-name=MyJob` & `#SBATCH -J=MyJob`.
>
>     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"

## Tokens

These are predefined variables that can be used in sbatch directives
such as the log file name.

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

## Environment variables

Common examples.

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

> ### Tip
>
> In order to decrease the chance of a variable being misinterpreted you
> should use the syntax `${NAME_OF_VARIABLE}` and define in strings if
> possible. e.g.
>
>     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"
