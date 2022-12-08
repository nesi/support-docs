> ### Service Status {#nearline-service-status}
>
> Mahuika\'s new CPU nodes are in an **Early Access Programme (EAP)
> phase** and not fully in production.

# Early Access Programme

## *Overview*

Prior to launching Mahuika\'s newest CPU nodes for general production,
we are allowing early access to help us identify any issues with:

-   -   accessing the new nodes

    -   codes that don't run or have issues running

    -   documentation

    -   comparing performance to the old nodes

[If you'd like to participate as tester / early access user for the new
Mahuika CPU nodes you are welcome to try them out. If you want access to
our temporary testing project to run jobs or benchmarks free of charge,
refer to the [Temporary Project
section](https://support.nesi.org.nz/hc/en-gb/articles/5002335382543-Mahuika-Extension-Onboarding#temporary_project)
below and ]{#9713733c-843a-4b40-8f2b-a0b5b7095aa1
data-renderer-mark="true" data-mark-type="annotation"
data-mark-annotation-type="inlineComment"
data-id="9713733c-843a-4b40-8f2b-a0b5b7095aa1"}[[reach out to NeSI
Support]{#9713733c-843a-4b40-8f2b-a0b5b7095aa1 data-renderer-mark="true"
data-mark-type="annotation" data-mark-annotation-type="inlineComment"
data-id="9713733c-843a-4b40-8f2b-a0b5b7095aa1"}](https://support.nesi.org.nz/hc/en-gb/requests/new "https://support.nesi.org.nz/hc/en-gb/requests/new"){.css-tgpl01}. 

## *Important notes*

Before accessing the new nodes, please review these important points. If
you have any questions, [contact NeSI
Support](https://support.nesi.org.nz/hc/en-gb/requests/new). 

-   To access the new Milan CPUs for \'free\' through the course of this
    testing phase, you can request to be added to the temporary test
    project account `nesi03638`, with the condition that you only use it
    for testing and benchmarking these new nodes. [See the Benchmarking
    section](https://support.nesi.org.nz/hc/en-gb/articles/5002335382543-Mahuika-Extension-Onboarding#benchmarking)
    below for more details.
-   Jobs are submitted from the same Mahuika login node that you
    currently use, however you will need to explicitly specify the
    `milan` partition in your `sbatch` command line. [See the Slurm
    Configuration
    section](https://support.nesi.org.nz/hc/en-gb/articles/5002335382543-Mahuika-Extension-Onboarding#slurm_configuration)
    below for more details.
-   We\'re currently allowing up to 8 nodes per user, 24 hour maximum
    walltime. To request more than that, [contact NeSI
    Support.](https://support.nesi.org.nz/hc/en-gb/requests/new)
-   We\'re asking early access users to let us know of any issues,
    challenges, or suggestions for improving your experience getting
    onto and using the new nodes. We also welcome any testing that
    compares your job(s) performance on the new nodes against the older
    nodes. All feedback and insights should be sent to [NeSI
    Support.](https://support.nesi.org.nz/hc/en-gb/requests/new)

For more details on the new Mahuika Extension technology and what we\'re
requesting in terms of benchmarking, please read the information below.

------------------------------------------------------------------------

# Differences from original Mahuika compute nodes

## Hardware

Each node has two AMD Milan CPUs, each with 8 \"chiplets\" of 8 cores
and one level 3 cache, so each node has a total of **128 cores** or 256
hyperthreaded CPUs.  This represents a significant increase of the
number CPUs per node compared to the Broadwell nodes (36 cores). 

[The memory available to Slurm jobs is 460 GB per node, so approximately
1800 MB per
CPU.  ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}

Only 30 nodes are available so far, but that number will eventually
increase to 64, 8 of which will have double the memory.

## Software

### Operating System

The existing Mahuika compute nodes use Linux Centos 7.4 while the new
ones use Rocky 8.5.  These are closely related Linux distributions. The
move from 7 to 8 is more significant than the move from Centos to Rocky.

Many system libraries have changed version numbers between versions 7
and 8, so **some software compiled on Centos 7 will not run as-is on
Rocky 8**. This can result in the runtime
error`error while loading shared libraries:... cannot open shared object file`, 
which can be fixed by providing a copy of the old system library.  

We have repaired several of our existing environment modules that way.
 For programs which you have compiled yourself, we have installed a new
environment module that provides many of the Centos 7 libraries:

    module load LegacySystemLibs/7

Please let us know if that isn\'t sufficient to get your existing
compiled code running on the new nodes.

Of course you can also recompile code inside a job run in the milan
partition and so produce an executable linked against the new system
libraries, but then that would be unlikely to work on the old nodes.

In the longer term all Mahuika nodes will be upgraded to Rocky 8.

### Older Intel and Cray software

The directories `/cm` and `/opt/cray` contain software which was
installed on Mahuika when we purchased it rather than installed by the
NeSI Application Support team. They are not present on the new nodes. As
with the system libraries, you could take a copy of these libraries and
carry on, but it is best to migrate away from using them if possible.

This affects our pre-2020 toolchains such as *intel/2018b*, but we
should have newer versions of such software already installed in most
cases.

### Intel MKL performance

In many ways, Intel\'s MKL is the best implementation of the BLAS and
LAPACK libraries to which we have access, which is why we use it in our
\"*intel*\" and \"*gimkl*\" toolchains.  Unfortunately, recent versions
of MKL deliberately choose not to use the accelerated AVX instructions
when not running on an Intel CPU.  

In order to persuade MKL to use the same fast optimised kernels on the
new AMD Milan CPUs, you can do

    module load AlwaysIntelMKL

We have set that as the default for our most recent toolchain
*gimkl/2022a*.

Two alternative implementations have also been installed: OpenBLAS and
BLIS. If you try them then please let us know if they work better than
MKL for your application.  BLIS is expected to perform well as a BLAS
alternative but not match MKL\'s LAPACK performance.  

### Do I need to recompile my code?

Except for possible missing shared libraries (see above), you should not
need to recompile your code. Please let us know if you encounter any
issues not listed above.

### AOCC

AMD provides a compiler based on clang (C/C++) and flang (Fortran) which
might perform better on their hardware.  We have installed it but not
integrated it into a high-level toolchain with MPI and BLAS.  If you
wish to try it:

    module load AOCC

For more information on AOCC compiler suite please, visit [AMD
Optimizing C/C++ and Fortran Compilers
(AOCC)](https://developer.amd.com/amd-aocc/)

## Network

Access to the new nodes is currently only possible via the Slurm
`sbatch` and `srun` commands. There is no ssh access, not even to the
nodes where you have a job running.  Programs that launch their remote
tasks via ssh (eg: ORCA) are not expected to work.  Other arbitrary
connections to the new compute nodes such as might be used by debuggers,
HTTP based progress monitoring, and non-MPI distributed programs such as
Dask or PEST, will generally only work if you use the Infiniband address
of the compute node, eg: *wmc012.ib.hpcf.nesi.org.nz*. Networking
configuration is expected to be addressed in the future.

## Slurm Configuration

### Access

To run on the new Milan nodes, you will need to explicitly specify the
`milan` partition in your `sbatch` command line. Jobs are submitted from
the same Mahuika login node that you currently use and share the same
file system as other cluster nodes. 

    sbatch -p milan ...

Alternatively, the same effect can be achieved by placing a pragma into
the job description file:

    #SBATCH --partition=milan

### Limits

Currently up to 10 nodes per account, 7 days maximum job duration. If
you need more then please contact us to discuss your requirements.

# Benchmarking

We at NeSI would love to know how the new AMD Milan CPUs are performing
for your code.  In order to compare performance against the older nodes,
we expect you to run the same job on both node types and provide us with
performance results of both. Note that in order to submit the same job
to the old nodes, you only need to remove the partition specification
(`-p milan`) in the `sbatch` command.

Timing can be obtained through time command, for example:

    time srun <command>

or via `sacct`.

## Advanced Slurm options for benchmarking

When running benchmarks (and only then!) we recommend using 

    sbatch --exclusive=user ...

(with short jobs please) so that you have node(s) to yourself and will
not be affected by jobs from other users.  

### I/O performance

There are reports about lower I/O performance when running jobs on Milan
nodes. This issue is being investigated and will be addressed once the
partition is fully populated. Please, note that the reduced performance
does not affect all input/output operations. Please, contact us if you
have concerns regarding this issue.

# Any questions?

Don\'t hesitate to contact us at <support@nesi.org.nz>. We are available
for Zoom sessions if you need to talk to us about specific details of
your testing and benchmarking.
