---
created_at: '2024-01-16T22:06:12Z'
hidden: false
position: 0
status: new
tags: []
title: Preparing your code for use on NeSI's new HPC platform
vote_count: 0
vote_sum: 0
zendesk_article_id: 8817840423439
zendesk_section_id: 200732737
---

## Background

Since 2018 NeSI and its Collaborators (University of Auckland, NIWA,
University of Otago, Manaaki Whenua) have operated the current national
HPC platform and underlying infrastructure, best known as Mahuika and
Māui. These Collaborators are now refreshing the underlying HPC
infrastructure through two procurements, led by NeSI for Mahuika and
NIWA for Māui.

NeSI has [completed its
procurement](https://www.nesi.org.nz/news/2024/02/partnering-deliver-next-generation-cloud-data-and-ai-solutions-empower-aotearoas),
selected the underlying infrastructure platform, and is commissioning
the replacement for Mahuika. We anticipate migrating users in a
staggered manner during the coming 6+ months. We will take all care to
manage any changes for you in your work in using NeSI’s HPC.

We anticipate teams might require assistance with getting ready, so
we’re providing wrap-around support. Our goal is to reduce the risk or
pain of the transition for you and your team(s) by working with you to
prepare. This page provides an overview of how to familiarise yourself
with the new infrastructure environment in advance, the ways it will
differ from Māui, and actions you may need to take to prepare your
project for migration.

## Test your code on Mahuika

The platform NeSI has selected to replace Mahuika is similar to the
recently commissioned [Mahuika AMD Milan compute
nodes](../../General/Announcements/Mahuika's_new_Milan_CPU_nodes_open_to_all_NeSI_users.md).
So, we'll be using these current nodes to validate any issues,
mitigating risks of your subsequent migration to the new platform.

Some projects on Māui will move to the new NeSI hardware, so each Māui
project has been given a small allocation on Mahuika which can be used
by Māui users to validate the software they need is available (or can be
built) on the AMD Milan nodes and works as expected. All members of the
project can use this Mahuika allocation.

To access Mahuika's AMD Milan nodes and submit jobs from any NeSI lander
node or Māui login node, use: `ssh login.mahuika.nesi.org.nz`.

At any point, if you don't see what you need or something isn’t working,
{% include "partials/support_request.html" %}. We’re keen to ensure this
early stage validation process is as quick and painless as possible.

## Porting your batch scripts

### Environment Modules

The module command works much the same way on Mahuika, though it happens
to be a different implementation ("Lmod") with a few extra features.
 You will probably find its extra search command `module spider` to be
faster and more useful than the familiar `module avail`.  

If you currently use software on Māui that we have provided via
environment modules, then please check to see if we have it installed on
Mahuika (note that it is unlikely to be the same version) and let us
know about anything that you can't find.  If you compile your own
software, then see below.

### Slurm options

#### Partitions

There are several partitions available to NeSI jobs on Mahuika, however
for the purposes of migrating from Māui and future-proofing, we
recommend the "milan" partition. As its name suggests, that partition
has AMD Milan (Zen3) CPUs, while the rest of Mahuika has Intel Broadwell
CPUs.

If for any reason you want to use any of the other Mahuika partitions,
see [Mahuika Slurm
Partitions](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Mahuika_Slurm_Partitions.md) for
an overview and [Milan Compute
Nodes](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Milan_Compute_Nodes.md) for
the differences between them and *milan*.

#### Shared nodes

Māui is scheduled by node while Mahuika is scheduled by core, so small
jobs can share Mahuika nodes, while on Māui nodes are exclusively
occupied by a single job at a time. 

When submitting an MPI job you have (at least) three options:

- Request a number of tasks without worrying what nodes they land on.
     That is OK for quick tests, but probably not optimal for real work
    as it both increases dependence on the interconnect and fragments
    node resources, as such job submissions end up much more scattered
    than they would on Māui.
- Request a number of tasks and a number (or range) of nodes.
- Request a number of nodes and a number of tasks per node.  This is
    appropriate for most Māui-sized jobs, and by requesting all of the
    CPUs on a node better isolates the job from contention with other
    jobs over socket-level or node-level resources such as memory
    bandwidth or the GPFS client.

#### Node sizes

Since most ex-Māui jobs will want to take whole nodes, it is important
to be aware of the size of those nodes:

|       |              |                           |
|-------|--------------|---------------------------|
|       | Māui         | Mahuika (milan partition) |
| cores | 40           | 128                       |
| CPUs  | 80           | 256                       |
| RAM   | 90 or 180 GB | 460 or 960 GB             |

 

### Temporary files

In Mahuika batch scripts, please replace any mention of `/tmp` with
`$TMPDIR`. 

## Porting your software

### Compiling without the Cray compiler wrappers

If you have been compiling software on Māui you will be familiar with
the CPE, the "Cray Programming Environment" compiler wrappers (*ftn*,
*cc* and their underlying infrastructure) which allow you to switch
between the GCC, Intel, and Cray compilers while using the same command
lines.  CPE is not supported on Mahuika, and so it will be necessary to
use a compiler directly, for example *gfortran* or *gcc*.

We have GCC and Intel compilers (but not the Cray compiler) available on
Mahuika via environment modules, recent examples being:

- *GCC/12.3.0*  - *gfortran*, *gcc*, and *g++*
- *intel-compilers/2022.0.2*  - *ifort*, *icc*, and *icpc*

If you also require MPI or any of the libraries BLAS, LAPACK, ScaLAPACK,
or FFTW then you will be best off loading one of our EasyBuild
"toolchain" environment modules such as:

- *foss/2023a*  - GCC, FFTW,
    [FlexiBLAS](../../Scientific_Computing/Supported_Applications/FlexiBLAS.md),
    OpenBLAS, OpenMPI
- *intel/2022a*  - Intel compilers, Intel MKL with its FFTW wrappers,
    Intel MPI.

For more on this topic, please see [Compiling software on
Mahuika](../../Scientific_Computing/HPC_Software_Environment/Compiling_software_on_Mahuika.md).

Since an increasing proportion of NeSI CPUs are AMD ones, good
performance of Intel's MKL library should not be assumed - other
BLAS/LAPACK implementations will sometimes perform much better on AMD
CPUs.  So far we provide the vendor-neutral OpenBLAS and BLIS, and may
also add AMD's own AOCL libraries.

### Microarchitecture

All of the current Mahuika CPUs have AVX2 instructions, but lack the
AVX512 instructions found on Māui's Skylake CPUs.  The next tranche of
NeSI hardware will have AMD Zen4 CPUs, which will have AVX512.

## Questions?

If you have any questions or need any help, {% include "partials/support_request.html" %}
or pop in to one of our [weekly Online Office
Hours](../../Getting_Started/Getting_Help/Weekly_Online_Office_Hours.md)
to chat with Support staff one-to-one.

No question is too small - don't hesitate to reach out.

