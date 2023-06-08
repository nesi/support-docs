---
created_at: '2015-10-12T00:28:38Z'
hidden: false
label_names:
- mahuika
- engineering
- gpu
- mpi
- omp
position: 21
title: ABAQUS
vote_count: 2
vote_sum: 0
zendesk_article_id: 212457807
zendesk_section_id: 360000040076
---

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

A list of commands can be found with:

    abaqus help

[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236)
can provide significant speedup to your computations, however
hyperthreaded CPUs will use twice the number of licence tokens. It may
be worth adding  `#SBATCH --hint nomultithread` to your slurm script if
licence tokens are your main limiting factor.

> ### Tips
>
> Required ABAQUS licences can be determined by this simple and
> intuitive formula `⌊ 5 x N0.422 ⌋` where `N` is number of CPUs.

You can force ABAQUS to use a specific licence type by setting the
parameter `academic=TEACHING` or `academic=RESEARCH` in a relevant
[environment file](#env_file).

# Solver Compatibility

Not all solvers are compatible with all types of parallelisation.

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>

> ### Note
>
> If your input files were created using an older version of ABAQUS you
> will need to update them using the command,
>
>     abaqus -upgrade -job new_job_name -odb old.odb
>
> or
>
>     abaqus -upgrade -job new_job_name -inp old.inp

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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
</tbody>
</table>

# User Defined Functions 

User defined functions (UDFs) can be included on the command line with
the argument `user=<filename>` where `<filename>` is the C or fortran
source code.

Extra compiler options can be set in your local `abaqus_v6.env` file.

The default compile commands are for `imkl`, other compilers can be
loaded with `module load`, you may have to change the[compile
commands](https://support.nesi.org.nz/hc/en-gb/articles/360000329015) in
your local `.env` file.

# Environment file

The [ABAQUS environment
file](http://media.3ds.com/support/simulia/public/v613/installation-and-licensing-guides/books/sgb/default.htm?startat=ch04s01.html) contains
a number of parameters that define how the your job will run, some of
these you may with to change.

These parameters are read, 

`../ABAQUS/SMA/site/abaqus_v6.env` Set by NeSI and cannot be changed.

`~/abaqus_v6.env` (your home directory) If exists, will be used in all
jobs submitted by you.

`<working directory>/abaqus_v6.env` If exists, will used in this job
only.

You may want to include this short snippet when making changes specific
to a job.

    # Before starting abaqus
    echo "parameter=value
    parameter=value
    parameter=value" > "abaqus_v6.env"

    # After job is finished.
    rm "abaqus_v6.env"

 

> ### Useful Links
>
> -   [Command line options for standard
>     submission.](https://www.sharcnet.ca/Software/Abaqus610/Documentation/docs/v6.10/books/usb/default.htm?startat=pt01ch03s02abx02.html)

 

![ABAQUS\_speedup\_SharedVMPI.png](../includes/ABAQUS_speedup_SharedVMPI.png)

 

*Note: Hyperthreading off, testing
d<dfn class="dictionary-of-numbers">one on small mechanical </dfn>FEA
model. Results highly model dependant. Do your own tests.*
