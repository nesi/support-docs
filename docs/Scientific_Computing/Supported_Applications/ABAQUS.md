---
created_at: '2015-10-12T00:28:38Z'
hidden: false
position: 21
tags:
- mahuika
- engineering
- gpu
- mpi
- omp
- fea
title: ABAQUS
vote_count: 2
vote_sum: 0
zendesk_article_id: 212457807
zendesk_section_id: 360000040076
---

A list of ABAQUS commands can be found with:

``` sh
abaqus help
```

[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236)
can provide significant speedup to your computations, however
hyperthreaded CPUs will use twice the number of licence tokens. It may
be worth adding  `#SBATCH --hint nomultithread` to your slurm script if
licence tokens are your main limiting factor.

!!! note
     Required ABAQUS licences can be determined by this simple and
     intuitive formula `⌊ 5 x N`<sup>`0.422`</sup>` ⌋` where `N` is number
     of CPUs.

You can force ABAQUS to use a specific licence type by setting the
parameter `academic=TEACHING` or `academic=RESEARCH` in a relevant
[environment file](#env_file).

## Solver Compatibility

Not all solvers are compatible with all types of parallelisation.

|                   |                    |           |        |         |
|-------------------|--------------------|-----------|--------|---------|
|                   | Element operations | Iterative | Direct | Lanczos |
| `mp_mode=threads` | ✖                  | ✔        | ✔     | ✔       |
| `mp_mode=mpi`     | ✔                  | ✔        | ✖     | ✖       |

!!! warning
     If your input files were created using an older version of ABAQUS you
     will need to update them using the command,
     ``` sh
     abaqus -upgrade -job new_job_name -odb old.odb
     ```
     or
     ``` sh
     abaqus -upgrade -job new_job_name -inp old.inp
     ```
     
## Examples

=== Serial
    For when only one CPU is required, generally as part of
a [job array](https://support.nesi.org.nz/hc/en-gb/articles/360000690275-Parallel-Execution#t_array)
    ```
    #!/bin/bash -e
    #SBATCH --job-name      ABAQUS-serial
    #SBATCH --time          00:05:00 # Walltime
    #SBATCH --cpus-per-task 1 
    #SBATCH --mem           1500          # total mem
    module load ABAQUS/{{applications.ABAQUS.machines.mahuika.versions | last}}
abaqus job="propeller_s4rs_c3d8r" verbose=2 interactive
=== "Shared Memory"
    `mp_mode=threads`
    Uses a nodes shared memory for communication.
    May have a small speedup compared to MPI when using a low number of
    CPUs, scales poorly. Needs significantly less memory than MPI.
    Hyperthreading may be enabled if using shared memory but it is not
    recommended.
    
    ```sl
    #!/bin/bash -e
    #SBATCH --job-name      ABAQUS-Shared
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           2G        # total mem
    module load ABAQUS/{{applications.ABAQUS.machines.mahuika.versions}}
    abaqus job="propeller_s4rs_c3d8r verbose=2 interactive \
        cpus=${SLURM_CPUS_PER_TASK} mp_mode=threads 

=== "UDF"
    Shared memory run with user defined function (fortran or C).
    Function will be compiled at start of run.
    You may need to chance the function suffix if you usually compile
on windows.


    ```
    #!/bin/bash -e
    
    #SBATCH --job-name      ABAQUS-SharedUDF
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           2G         # total mem

    module load imkl</span>
    module</span> load ABAQUS/{{{{applications.ABAQUS.machines.mahuika.versions | last}}
    abaqus job="propeller_s4rs_c3d8r" user=my_udf.f90 \
        verbose=2 interactive cpus=${SLURM_CPUS_PER_TASK} mp_mode=threads
=== "Distributed Memory"
`mp_mode=mpi`
Multiple processes each with a single *thread*. Not limited to one node.
Model will be segmented into `-np` pieces which
should be equal to `--ntasks`
Each task could be running on a different node leading to increased
communication overhead. Jobs can be limited to a single node by adding --nodes=1` however this will increase your time in the
queue as contiguous cpu's are harder to schedule.
This is the default method if `mp_mode` is left
unspecified.
    ```
    #!/bin/bash -e
    #SBATCH --job-name      ABAQUS-Distributed 
    #SBATCH --time          00:05:00       # Walltime</span></span>
    #SBATCH --ntasks        8
    #SBATCH --mem-per-cpu   1500          # Each CPU needs it&#39;s own.
    #SBATCH --nodes         1
    
    module load ABAQUS/{{applications.ABAQUS.machines.mahuika.versions | last}}
   abaqus job "propeller_s4rs_c3d8r" verbose=2 interactive cpus=${SLURM_NTASKS} mp_mode=mpi

=== "GPUs"
    The GPU nodes are limited to 16 CPUs
    In order for the GPUs to be worthwhile, you should see a speedup
    equivalent to 56 CPU's per GPU used. GPU modes will
    generally have less memory/cpus.

    ```
    #!/bin/bash -e
    
    #SBATCH --job-name      ABAQUS-gpu
    #SBATCH --time          00:05:00       # Walltime</span></span>
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           4G         # total mem</span></span>
    #SBATCH --gpus-per-node
module</span> load ABAQUS/2019 </span>
<span id="cb5-10"><a href="#cb5-10" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load CUDA</span>
<span id="cb5-11"><a href="#cb5-11" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb5-12"><a href="#cb5-12" aria-hidden="true" tabindex="-1"></a><span class="ex">abaqus</span> job=<span class="st">&quot;propeller_s4rs_c3d8r&quot;</span> verbose=2 interactive <span class="dt">\</span></span>
<span id="cb5-13"><a href="#cb5-13" aria-hidden="true" tabindex="-1"></a>    cpus=<span class="va">${SLURM_CPUS_PER_TASK}</span> gpus=<span class="va">${SLURM_GPUS_PER_NODE}</span> mp_mode=threads</span></code></pre></div></td>
</tr>
</tbody>
</table>

## User Defined Functions 

User defined functions (UDFs) can be included on the command line with
the argument `user=<filename>` where `<filename>` is the C or fortran
source code.

Extra compiler options can be set in your local `abaqus_v6.env` file.

The default compile commands are for `imkl`, other compilers can be
loaded with `module load`, you may have to change the [compile
commands](https://support.nesi.org.nz/hc/en-gb/articles/360000329015) in
your local `.env` file.

## Environment file

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

``` sl
# Before starting abaqus
echo "parameter=value
parameter=value
parameter=value" > "abaqus_v6.env"

# After job is finished.
rm "abaqus_v6.env"
```
!!! prerequisite Useful Links
     -   [Command line options for standard
         submission.](https://www.sharcnet.ca/Software/Abaqus610/Documentation/docs/v6.10/books/usb/default.htm?startat=pt01ch03s02abx02.html)

 

![ABAQUS\_speedup\_SharedVMPI.png](../../assets/images/ABAQUS.png)

 

*Note: Hyperthreading off, testing done on small mechanical FEA model.
Results highly model dependant. Do your own tests.*
