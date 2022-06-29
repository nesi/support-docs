> ### Service Status {#nearline-service-status}
>
> Mahuika\'s new nodes are in an **Early Access Programme (EAP) phase**
> and not fully in production for all NeSI users. Selected researchers
> have been given access. If you are interested in participating in the
> EAP phase, please [contact
> support](https://support.nesi.org.nz/hc/en-gb/requests/new). 

 

Differences from original Mahuika compute nodes
===============================================

Hardware
--------

Each node has two AMD Milan CPUs, each with 8 \"chiplets\" of 8 cores
and one level 3 cache, so each node has a total of **128 cores** or 256
hyperthreaded CPUs.  This represents a significant increase of the
number CPUs per node compared to the Broadwell nodes (36 cores). 

[The memory available to Slurm jobs is 460 GB per node, so approximately
1800 MB per
CPU.  ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}

Only 30 nodes are available so far, but that number will eventually
increase to 64, 8 of which will have double the memory.

Software
--------

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

Network
-------

Access to the new nodes is currently only possible via the Slurm
`sbatch` and `srun` commands. There is no ssh access, not even to the
nodes where you have a job running.  Programs that launch their remote
tasks via ssh (eg: ORCA) are not expected to work.  Other arbitrary
connections to the new compute nodes such as might be used by debuggers,
HTTP based progress monitoring, and non-MPI distributed programs such as
Dask or PEST, will generally only work if you use the Infiniband address
of the compute node, eg: *wmc012.ib.hpcf.nesi.org.nz*. Networking
configuration is expected to be addressed in the future.

Slurm Configuration
-------------------

### Access

To run on the new Milan nodes, you will need to explicitly specify the
`milan` partition in your `sbatch` command line. Jobs are submitted from
the same Mahuika login node that you currently use and share the same
file system as other cluster nodes. 

    sbatch -p milan ...

### Limits

Currently up to 8 nodes per user, 4 hour maximum walltime. If you need
more then please contact us to discuss your requirements.

Benchmarking
============

We at NeSI would love to know how the new AMD Milan CPUs are performing
for your code.  In order to compare performance against the older nodes,
we expect you to run the same job on both node types and provide us with
performance results of both. Note that in order to submit the same job
to the old nodes, you only need to remove the partition specification
(`-p milan`) in the `sbatch` command.

Timing can be obtained through time command, for example:

    time srun <command>

or via `sacct`.

Temporary project
-----------------

We have created a dedicated project `nesi03638` that has access to the
new milan partition. You can use this project code when submitting test
or benchmarking jobs:

    #SBATCH --account=nesi03638

You may use the test project directories `/nesi/nobackup/nesi03638`
and `/nesi/project/nesi03638` to store data for testing purposes.
However these are shared directories accessible by all other early
access testers so do not store any sensitive data there.  We recommend
just using your existing project directories instead.

Advanced Slurm options for benchmarking
---------------------------------------

When running benchmarks (and only then!) we recommend using 

    sbatch --exclusive ...

(with short jobs please) so that your job has its node(s) to itself and
will not be affected by any other job running on the same node.  By
default Slurm will then let your job use the the whole node, so also
use `srun --exact` to limit the job step to just the number of cores
that you requested.  And finally for MPI jobs, Slurm will let your tasks
spread out across the whole node, but you can ask it to pack them
tighter together with  `srun -m block`, which might more realistically
match how they will run in the future when the new nodes are busier.

Early access user feedback
==========================

The [purpose of this early access / testing
phase]{#7d72b2c5-4fa2-4f0e-9d27-e81fcc185169 .inline-highlight
data-renderer-mark="true" data-mark-type="annotation"
data-mark-annotation-type="inlineComment"
data-id="7d72b2c5-4fa2-4f0e-9d27-e81fcc185169"} is to help us identify
any issues you may have with using the new infrastructure, including:

-   -   accessing the new nodes

    -   identifying codes that don't run or have issues running

    -   improving documentation

    -   comparing performance to the old nodes

So, as you begin accessing and using the new nodes, please let us know
of any challenges, issues, or suggestions for improvement.

Any questions?
==============

Don\'t hesitate to contact us at <support@nesi.org.nz>. We are available
for Zoom sessions if you need to talk to us about specific details of
your testing and benchmarking.
