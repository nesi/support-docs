---
created_at: '2019-06-03T23:23:13Z'
hidden: false
weight: 55
tags: []
title: Trinity
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000980375
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

Trinity, developed at the [Broad
Institute](http://www.broadinstitute.org/) and the [Hebrew University of
Jerusalem](http://www.cs.huji.ac.il/), performs de novo reconstruction
of transcriptomes from RNA-seq data. It combines three independent
software modules: Inchworm, Chrysalis, and Butterfly, applied
sequentially to process large volumes of RNA-seq reads. Trinity
partitions the sequence data into many individual de Bruijn graphs, each
representing the transcriptional complexity at a given gene or locus,
and then processes each graph independently to extract full-length
splicing isoforms and to tease apart transcripts derived from paralogous
genes.

General documentation for running Trinity can be found on their GitHub
page
[here](https://github.com/trinityrnaseq/trinityrnaseq/wiki/Running-Trinity).

## Running Trinity on NeSI

The recommended approach for running Trinity on NeSI is to split the run
into two separate job submissions. The first submission will run Trinity
Phase 1 (read clustering) and the second submission will run Trinity
Phase 2 (assembling read clusters). We have observed faster run times
and reduced core hour usage when applying this approach to benchmark
data, compared to running both phases in one multithreaded job (see the
[Benchmarks](#benchmarks) section below).

### File system considerations

You should run Trinity within your [nobackup project
directory](../../Storage/File_Systems_and_Quotas/NeSI_File_Systems_and_Quotas.md),
which has no limit on disk space usage but does have a file count quota.
Trinity creates a large number of files, particularly in the
"read\_partitions" directory, thus it is important that you [contact
us](mailto:support@nesi.org.nz) before running Trinity on NeSI, as we
may need to increase your default file count quota.

### Quality Control

We must stress the importance of read QC prior to running the assembly
otherwise it is likely to fail or take a very long time to complete.

### Running Trinity Phase 1

Trinity Phase 1 can be broken into three main components:

- Initial in silico normalisation step and kmer counting
- Inchworm
- Chrysalis

So far we have found no reason to run each component individually since
they have been observed to require similar resources. This phase
typically has high memory requirements and supports multithreading in
places.

The following Slurm script is a template for running Trinity Phase 1

**Note**  :

-   `--cpus-per-task` and `--mem` defined in the following example are
    just place holders. 
-   Use a subset of your sample, run a test first to find the
    suitable/required amount of CPUs and memory for your dataset

``` sl
#!/bin/bash -e
#SBATCH --job-name=trinity-phase1
#SBATCH --account=nesi12345   # your NeSI project code
#SBATCH --time=30:00:00       # maximum run time
#SBATCH --ntasks=1            # always 1
#SBATCH --cpus-per-task=16    # number of threads to use for Trinity
#SBATCH --mem=220G            # maximum memory available to Trinity
#SBATCH --hint=nomultithread  # disable hyper-threading

# load a Trinity module
module load Trinity/2.14.0-gimkl-2022a

# run trinity, stop before phase 2
srun Trinity --no_distributed_trinity_exec \
  --CPU ${SLURM_CPUS_PER_TASK} --max_memory 200G \
  [your_other_trinity_options]
```

The extra Trinity arguments are:

-   `--no_distributed_trinity_exec` tells Trinity to stop before running
    Phase 2
-   `--CPU ${SLURM_CPUS_PER_TASK}` tells Trinity to use the number of
    CPUs specified by the sbatch option `--cpus-per-task` (i.e. you only
    need to update it in one place if you change it)
-   `--max_memory` should be the same (or maybe slightly lower, so you
    have a small buffer) than the value specified with the sbatch option
    `--mem`
-   `[your_other_trinity_options]` should be replaced with the other
    trinity options you would usually use, e.g. `--seqType fq`, etc.

### Running Trinity Phase 2

Upstream documentation for running Trinity Phase 2 in parallel can be
found
[here](https://github.com/trinityrnaseq/trinityrnaseq/wiki/Running-Trinity#optional-adapting-trinity-to-a-computing-grid-for-massively-parallel-processing-of-embarrassingly-parallel-steps).

Trinity Phase 2 performs all the mini-assemblies in parallel. This phase
consists of a large number (e.g. tens or hundreds of thousands) of
commands that can be executed in parallel, each having independent
inputs and outputs (embarrassingly parallel).

By default, Phase 2 will be run in the same way as Phase 1, i.e. using
multiple threads on a single compute node to work through the list of
Phase 2 commands that need to be run. However, these commands are very
I/O intensive and can easily saturate the I/O bandwidth of a single
node. By utilising Trinity's "grid mode" we can distribute these
commands across many compute nodes, accessing a higher total I/O
bandwidth than is possible from a single node, which appears to improve
performance considerably. We have installed HPC GridRunner (recommended
in the Trinity documentation) to achieve this.

HPC GridRunner runs a master process, submitted as its own Slurm job,
that works by splitting the Phase 2 commands into batches of a certain
size (specified by the user) and submits these batches of commands to
the Slurm queue as separate jobs (referred to here as sub-jobs). The
user can configure how many sub-jobs are allowed to be in the Slurm
queue at any given time (so as not to overload the queue). Thus when a
sub-job finishes, HPC GridRunner will submit another, maintaining the
requested number of sub-jobs in the queue at any given time, until all
commands have been run.

An example configuration script for HPC GridRunner follows. This script
was tested and worked with our benchmark case but some parameters may
need to be adjusted, such as memory and time requirements. Note the
Trinity documentation suggested each command will need a maximum of 1 GB
memory, however we observed some commands spiking above 4 GB. This could
vary depending on your inputs.

``` sh
[GRID]
# grid type:
gridtype=SLURM

# template for a grid submission
# make sure:
#     --partition is chosen appropriately for the resource requirements 
#       (here we choose either large or bigmem, whichever is available first)
#     --ntasks and --cpus-per-task should always be 1
#     --mem may need to be adjusted
#     --time may need to adjusted
#       (must be enough time for a batch of commands to finish)
#     --account should be your NeSI project code
#     add other sbatch options as required
cmd=sbatch --partition=large,bigmem --mem=5G --ntasks=1 --cpus-per-task=1 --time=01:00:00 --account=nesi12345

# note -e error.file -o out.file are set internally, so dont set them in the above cmd.

#############################################################################
# settings below configure the Trinity job submission system, not tied to the grid itself.
#############################################################################

# number of grid submissions to be maintained at steady state by the Trinity submission system
max_nodes=100

# number of commands that are batched into a single grid submission job.
cmds_per_node=100
```

 The important details are:

-   `cmds_per_node` is the size of each batch of commands, i.e. here
    each Slurm sub-job runs 100 commands and then exits
-   `max_nodes` is the number of sub-jobs that can be in the queue at
    any given time (each sub-job is single threaded, i.e. it uses just
    one core)
-   name this file SLURM.conf in the directory you will submit the job
    from
-   memory usage may be low enough that the sub-jobs can be run on
    either the large or bigmem partitions, which should improve
    throughput compared to bigmem alone

A template Slurm submission script for Trinity Phase 2 is shown below:

``` sl
#!/bin/bash -e
#SBATCH --job-name=trinity-phase2grid
#SBATCH --account=nesi12345  # your NeSI project code
#SBATCH --time=30:00:00      # enough time for all sub-jobs to complete
#SBATCH --ntasks=1           # always 1 - this is the master process
#SBATCH --cpus-per-task=1    # always 1
#SBATCH --mem=20G            # memory requirements for master process
#SBATCH --partition=bigmem   # submit to an appropriate partition
#SBATCH --hint=nomultithread

# load Trinity and HPC GridRunner
module load Trinity/2.14.0-gimkl-2022a
module load HpcGridRunner/20210803

# run Trinity - this will be the master HPC GridRunner process that handles
#   submitting sub-jobs (batches of commands) to the Slurm queue
srun Trinity --CPU ${SLURM_CPUS_PER_TASK} --max_memory 20G \
  --grid_exec "hpc_cmds_GridRunner.pl --grid_conf ${SLURM_SUBMIT_DIR}/SLURM.conf -c" \
  [your_other_trinity_options]
```

-   This assumes that you named the HPC GridRunner configuration script
    SLURM.conf and placed it in the same directory that you submit this
    job from
-   The options `--CPU` and `--max_memory` aren't used by Trinity in
    "grid mode" but are still required to be set (i.e. it shouldn't
    matter what you set them to)

## Benchmarks

Here we provide details of a number of Trinity assemblies that have been
carried out on NeSI, in order to give a rough idea of how Trinity can
perform on NeSI and an indication of its resource requirements.

Timings mentioned here should be taken as indicative only and, even if
assembling the same sample again, would be expected to vary
significantly depending on various factors, such as the load on the
system and project fair share scores and priorities.

### Test sample

We ran a small test job of 8 million paired reads. Although much smaller
than usual this allowed us to quickly see the effect of making changes
to the workflow and ran quickly enough that we could compare the default
way of running Trinity to splitting the Trinity run into two phases and
using "grid mode".

Phase 1 took less than 1 hour to complete, using 8 cores and 10 GB
memory. For Phase 2 we requested 8 GB memory for the master process and
4 GB memory and 1 hour wall time for the sub-jobs. There were 195,741
mini-assemblies to run in Phase 2.

The table below summarises the timings for Phase 2, comparing the
default, single node way to run Phase 2, to using Trinity's "grid mode".

|                       |                                          |                              |                                |
|-----------------------|------------------------------------------|------------------------------|--------------------------------|
| **Type of run**       | **Number of cores / grid specification** | **Run time (hrs:mins:secs)** | **Approximate core hour cost** |
| Single node (default) | 16 cores                                 | 24:09:36                     | 387                            |
| Grid                  | max\_nodes=20; cmds\_per\_node=500       | 07:59:58                     | 168                            |
| Grid                  | max\_nodes=40; cmds\_per\_node=500       | 04:10:45                     | 171                            |
| Grid                  | max\_nodes=60; cmds\_per\_node=500       | 02:36:58                     | 160                            |
| Grid                  | max\_nodes=80; cmds\_per\_node=500       | 02:14:46                     | 182                            |

This shows that performance is much better with Trinity's "grid mode".
Not only are the run times significantly lower but the total number of
core hours used is also much lower.

### Marine sediment sample 1

This benchmark concerns the assembly of a marine sediment sample,
containing two distinct microbial populations, from two distinct
geographical locations, of approximately 286 million paired reads. The
assembly was performed using the two-phase Trinity workflow discussed
above, using those submission scripts as templates.

Phase 1 ran on 18 threads with 220 GB memory on the bigmem partition and
took approximately 15 hours to complete.

For Phase 2, the master process ran on a single core with 20 GB memory
on the bigmem partition. HPC GridRunner was configured with both
`cmds_per_node` and `max_nodes` set to 100, with the sub-jobs running on
either large or bigmem partitions and requesting 5 GB memory and 1 hour
wall time each. The number of commands (mini-assemblies) that needed to
be run during this phase was 2,020,460. Phase 2 took approximately 19
hours to complete (elapsed time) and cost around 1,800 core hours.

### Marine sediment sample 2

This sediment sample, containing 303 million reads, was all from the
same location and was taken from a treatment experiment. The assembly
was performed using the two-phase Trinity workflow discussed above,
using those submission scripts as templates.

There were 4,136,295 mini-assemblies to run in Phase 2. The master
process requested 30 GB memory on the bigmem partition and HPC
GridRunner was configured with both `cmds_per_node` and `max_nodes` set
to 100. The sub-jobs ran on either the large or bigmem partitions and
required 1 hour wall time and 5 GB memory each. Phase 2 took
approximately 32 hours to complete (elapsed time) and cost around 3,100
core hours.
