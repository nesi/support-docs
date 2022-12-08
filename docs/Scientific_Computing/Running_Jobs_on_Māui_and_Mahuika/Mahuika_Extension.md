 

# Differences from other Mahuika compute nodes[]{.wysiwyg-font-size-x-large} {#01GAG6XAK1FF5ZNPMT8RF6MCWZ}

## **Hardware**

Each node has two AMD Milan CPU chips, each with 8 chiplets, each of
which have 8 cores and one level 3 cache, so each node has a total of
**128 cores** or 256 hyperthreaded CPUs.  This represents a significant
increase of the number CPUs per node compared to the Broadwell nodes (36
cores). 

It therefore makes sense to use a power of two for the number of cores
requested by a job.\
\
AMD Milan CPU overview, each node has two of these:

![milan.png](https://support.nesi.org.nz/hc/article_attachments/5300908636815/milan.png){width="377"
height="395"}

[**AMD-EPYC-Milan-architecture** from
[HPCwire](https://www.hpcwire.com/2021/03/15/amd-launches-epyc-milan-with-19-skus-for-hpc-enterprise-and-hyperscale/#foobox-4/0/AMD-Epyc-Milan-architecture.png)]{.wysiwyg-font-size-small}[]{.wysiwyg-font-size-small}

\
An overview of the AMD Milan CPUs can be found on the [AMD
website](https://www.amd.com/en/processors/epyc-7003-series).

 

[The memory available to Slurm jobs on these nodes is 460 GB, so
approximately 1800 MB per
CPU.  ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}

Only 30 nodes are available so far, but that number will eventually
increase to 64, eight of which will have double the memory.

## **[Operating System]{.wysiwyg-font-size-large}** {#01GAG6XAK2WZMMAHZX0WJ98RF6}

The existing Mahuika compute nodes use Linux Centos 7.4 while Mahuika
Extension use Rocky 8.5.  These are closely related Linux distributions.
The move from 7 to 8 is more significant than the move from Centos to
Rocky.

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

## **[Older Intel and Cray software]{.wysiwyg-font-size-large}** {#01GAG6XAK2NPSX27CEWEPHD0NJ}

The directories `/cm` and `/opt/cray` contain software which was
installed on Mahuika when we purchased it rather than installed by the
NeSI Application Support team. They are not present on the new nodes. As
with the system libraries, you could take a copy of these libraries and
carry on, but it is best to migrate away from using them if possible.

This affects our pre-2020 toolchains such as *intel/2018b*, but we
should have newer versions of such software already installed in most
cases.

## [**Intel MKL performance**]{.wysiwyg-font-size-large} {#01GAG6XAK23RF9SHH94QH011RK}

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

## [**Do I need to recompile my code?**]{.wysiwyg-font-size-large} {#01GAG6XAK2CBFM66VDVDG2BSDK}

Except for possible missing shared libraries (see above), you should not
need to recompile your code. Please let us know if you encounter any
issues not listed above.

## [**AOCC (AMD Optimizing C/C++ and Fortran Compilers)**]{.wysiwyg-font-size-large} {#01GAG6XAK2DXD7EH0CWHCYRG22}

AMD provides a compiler based on clang (C/C++) and flang (Fortran) which
might perform better on their hardware.  We have installed it but not
integrated it into a high-level toolchain with MPI and BLAS.  If you
wish to try it:

    module load AOCC

For more information on AOCC compiler suite please, visit [AMD
Optimizing C/C++ and Fortran Compilers
(AOCC)](https://developer.amd.com/amd-aocc/)

## [**Network**]{.wysiwyg-font-size-large} {#01GAG6XAK2M6MMYE9057FTW7A4}

Access to the new nodes is currently only possible via the Slurm
`sbatch` and `srun` commands. There is no ssh access, not even to the
nodes where you have a job running.  Programs that launch their remote
tasks via ssh (eg: ORCA) are not expected to work.  Other arbitrary
connections to the new compute nodes such as might be used by debuggers,
HTTP based progress monitoring, and non-MPI distributed programs such as
Dask or PEST, will generally only work if you use the InfiniBand address
of the compute node, eg: *wmc012.ib.hpcf.nesi.org.nz*. Networking
configuration is expected to be addressed in the future.\
\
[]{.wysiwyg-font-size-large}

[]{.wysiwyg-font-size-large}**[Job\
]{.wysiwyg-font-size-x-large}[]{.wysiwyg-font-size-x-large}**[]{.wysiwyg-font-size-x-large}

In order to use the Mahuika Extension nodes, jobs are submitted in the
same way as currently from the Mahuika login node with the following
options.

Either:

-   Add `#SBATCH --partition=milan` to the Slurm script
-   or with `sbatch -p milan MY_JOB_SCRIPT.sl`

Example of Slurm script:

    #!/bin/bash -e
    #SBATCH --job-name=MilanJob       #Name of the job
    #SBATCH --time=00:00:01           #Set a limit of 1 seconde on the total run time of the job allocation
    #SBATCH --partition=milan         #Request the Milan partition for the resource allocation

    srun pwd                          #Prints the working directory with the srun command

Resource allocation limits:   

-   7 days maximum walltime per job.
-   10 nodes per user at one time. eg 1x 10 nodes, or 2x 5 nodes 
-   Please contact [NeSI
    support](https://support.nesi.org.nz/hc/en-gb/articles/360000748496-User-support)
    if you require additional resources for jobs that are best suited to
    the Mahuika Extension.

# **[Notes]{.wysiwyg-font-size-x-large}[ ]{.wysiwyg-font-size-large}** {#01GAG6XAK3WY7N03E9SGCXN90B}

-   **More node**s will be added in the future.
-   Mahuika Extension is not a Cray system and the CPE differs from that
    on Mahuika and Māui
