---
created_at: 2026-03-23
description: Introduction to basic terminology and principles of High Performance Computing
status: tutorial
tags:
- tutorial
---

!!! time "15 Minutes"

!!! objectives
    - Understand key terminology.
    - Distinguish between remote and local hardware.
    - Describe key components of cluster architecture.
    - Run your first commands on the cluster.

!!! prerequisite
    - A Mahuika account, see [Creating an Account](../../Getting_Started/Creating_an_Account.md).
    - Membership of an active project. If you are attending a workshop, you will be added to a training project.
      Otherwise, [join an existing project](../../Getting_Started/Projects/Applying_to_Join_a_Project.md)
      or [apply for a new one](../../Getting_Started/Projects/Applying_for_a_New_Project.md).
    - A way to log in, see [Connecting to the Cluster](../../Getting_Started/Accessing_the_HPCs/Connecting_to_the_Cluster.md).

## What is an HPC system?

The words "cloud", "cluster", and the phrase "high-performance computing" or
"HPC" are used a lot in different contexts and with various related meanings.
So what do they mean? And more importantly, how do we use them in our work?

A *remote* computer is one you have no physical access to, and must connect to over a network (as opposed to a *local* computer).

*Cloud* refers to remote computing resources
that are provisioned to users on demand or as needed.

*HPC*, *High Performance Computer*, *High Performance Computing* or *Supercomputer* are all general terms for a large or powerful computing resource.

*Cluster* is a more specific term describing a type of supercomputer comprised of multiple smaller computers (nodes) working together.
Almost all supercomputers are clusters.

We will generally use 'cluster'.

![An image of the REANNZ HPCs](../../assets/images/NeSI-HPC-Facility.jpg)
*The REANNZ High Performance Cluster*

## Access

You will connect to a cluster over the internet either with a web client ([OnDemand](../../Interactive_Computing/OnDemand/OnDemand_Overview.md)) or with [SSH (Secure Shell)](../../Getting_Started/Accessing_the_HPCs/Connecting_to_the_Cluster.md).
Your main interface with the cluster will be using command line.
Log in now, so you can run the commands in this lesson. If you use OnDemand, open a terminal from it.

## Nodes

Individual computers that compose a cluster are typically called *nodes*.
On a cluster, there are different types of nodes for different
types of tasks. The node where you are now will be different depending on
how you accessed the cluster.

If you connected with SSH, you are on a *login node*. (If you connect with Mahuika OnDemand, you will not technically be on a login node, but can be treated as such)
Login nodes are the access point to the cluster.

The real work on a cluster gets done by the *compute nodes*.
Compute nodes come in many shapes and sizes, but generally are dedicated to long
or hard tasks that require a lot of computational resources.

## What's in a node?

A node is similar in makeup to a regular desktop or laptop, composed of *CPUs* (sometimes also called *processors* or *cores*), *memory*
(or *RAM*), and *disk* space. Where your laptop might have 8 CPUs and 16 GB of memory, most Mahuika compute nodes have 128 or 168 cores, and 384 GB or more of memory
(see [Hardware](../../Batch_Computing/Hardware.md)).

- **CPUs** are a computer's tool for running programs and calculations.

- **Memory** is for short-term storage, containing the information currently being operated on by the CPUs.

- **Disk** is for long-term storage, data stored here is permanent, i.e. still there even if the computer has been restarted.
It is common for nodes to connect to a shared, remote disk.

![A diagram representing the cluster. There are four identical sections connected to one another. Each section is split into two parts. The first part is the memory. The second part is further subdivided into four CPUs.](../../assets/images/clusterDiagram.png)

!!! info "Differences Between Nodes"
    Many HPC clusters have a variety of nodes optimised for particular workloads.
    Some nodes may have larger amounts of memory, or specialised resources such as
    Graphical Processing Units (GPUs).

!!! info "Dedicated Transfer Nodes"
    If you want to transfer larger amounts of data to or from the cluster, REANNZ
    offers dedicated transfer nodes using the Globus service.  
    More information on using Globus for large data transfer to and from the cluster can be found on the
    [Globus Transfer Service](../../Data_Transfer/Globus/Globus_Overview.md) page.

??? question "What is Mahuika?"
    <quiz>
    Mahuika is...

    - [x] A 'High Performance Computer'.
    - [x] A 'Cluster'
    - [] A 'Cloud'
    > Mahuika is not a cloud resource, however [RDC](../../Service_Subscriptions/Research_Developer_Cloud/User_Guides.md) is.
    - [x] A 'Remote Server'
    > Technically Mahuika is a server, but not the most useful description.
    - [] A 'Node'
    > Mahuika is composed of many nodes.
    - [x] A 'Supercomputer'

    </quiz>

## Have a look around

Let's run a few commands to see where we are.
Type each command and press <kbd>Enter</kbd>.
Your numbers will be different from the examples below, especially if you connected with OnDemand,
as they change while people use the cluster.

`hostname` prints the name of the computer you are on:

```sh
hostname
```

```out
login03.hpc.nesi.org.nz
```

If you connected with SSH, the name starts with `login`, so you are on a login node.

!!! tip "Local and remote"
    If you have a terminal open on your own computer, run `hostname` there too.
    You will get a different name: one is your local computer, the other is the remote cluster.

Before running the next two commands, guess how many CPUs and how much memory your laptop has.
Then guess the same for the login node.

`nproc` prints the number of CPUs you can use:

```sh
nproc
```

```out
248
```

`free -h` prints the amount of memory, in human readable units (`-h`).
The `total` column is the memory in the node, here `503Gi`:

```sh
free -h
```

```out
               total        used        free      shared  buff/cache   available
Mem:           503Gi       161Gi       3.5Gi       5.8Gi       352Gi       341Gi
Swap:             0B          0B          0B
```

That is a lot more than a laptop, but you are not the only one using it.
`who` lists the login sessions on this node, and `wc -l` counts them.
The `|` passes the output of `who` to `wc` (more on this in [Environment & Modules](Environment_And_Modules.md)):

```sh
who | wc -l
```

```out
148
```

The login node is shared by everyone logged in to it.
That is why login nodes are for light work, such as editing files and submitting jobs,
and anything that needs a lot of CPU or memory should run on the compute nodes.

`sinfo` shows the compute nodes, grouped into *partitions*.
The `genoa` and `milan` partitions are named after the type of CPU in their nodes:

```sh
sinfo
```

```out
PARTITION     AVAIL   TIMELIMIT    S:C:T MEMORY   NODES(A/I) NODELIST
genoa         up    21-00:00:00   2:84:2 366694+  30/28      c[001-044],g[01-12],l[01-08]
milan         up    21-00:00:00  4+:6+:2 491520+  64/2       mc[046-100],mg[13-19],ml[09-12]
hugemem       up    21-00:00:00 2+:20+:2 1469012+ 1/1        cl[17-19]
maintenance   up    21-00:00:00  2+:6+:2 366694+  95/31      c[001-044],cl[17-19],g[01-12],l[01-08],mc[046-100],mg[13-19],ml[09-12]
```

The `NODES(A/I)` column counts the nodes that are allocated (in use) and idle.
In this example, 94 of the 124 nodes in `genoa` and `milan` are in use.
When the cluster is busy, a new job waits in a queue until there is room for it.
You will see this in [Submitting Your First Job](Submitting_Your_First_Job.md).

## Which tool?

A cluster is not always the right tool.
For each problem, which would you use?

### Analysing data

<!-- ??? question "Some biology thing"
    <quiz>
    Your script stops with this error:

    ```out
    Error: cannot allocate vector of size 40.0 Gb
    ```

    - [x] HPC cluster
    > R needs 40 GB of memory for one object, more than most laptops have. Most Mahuika compute nodes have 384 GB or more.
    - [ ] Cloud resource
    > You could rent a large enough machine, but you would be setting it up and paying for it for one script.
    - [x] Virtual machine
    > A virtual machine big enough for this would sit idle once the script has finished.
    - [ ] Local laptop
    > Most laptops do not have 40 GB of memory to give to one object.
    </quiz> -->

??? question "Many samples"
    <quiz>
    You have 500 samples, and processing each one takes an hour on one CPU.

    - [x] HPC cluster
    > One after another, they would take about three weeks. Run at the same time on many CPUs, they can finish in hours. You will see how in [Parallel](Parallel.md).
    - [ ] Cloud resource
    > You could start many machines, but you would have to set them up and share out the work yourself. A cluster's scheduler does this for you.
    - [ ] Virtual machine
    > One virtual machine has a limited number of CPUs, so the samples would still mostly run one after another.
    - [ ] Local laptop
    > One after another, they would take about three weeks.
    </quiz>

??? question "A big plot"
    <quiz>
    You have a large dataset you need to plot.

    - [ ] HPC cluster
    > You could, but logging in and moving the data there is more work than the plot.
    - [ ] Cloud resource
    > Nothing here needs more than your own computer.
    - [ ] Virtual machine
    > Nothing here needs more than your own computer.
    - [x] Local laptop
    > Small, quick and interactive work is easiest on your own computer.
    </quiz>

??? question "Web tool"
    <quiz>
    You are building a web service for collecting and proccessing research data.

    - [ ] HPC cluster
    > A cluster runs batch jobs, not web services.
    - [x] Cloud resource
    > Cloud resources can have networks set up as required. Resources can be added as required.
    - [ ] Virtual machine
    > Could do, would be wasteful though.
    - [ ] Local laptop
    > Your laptop probably doesn't have a static IP and would need to be on always.
    </quiz>

!!! keypoints
    - A 'cluster' describes a particular architecture of HPC.
    - Remote hardware must be accessed via SSH, or a dedicated web client.
    - Clusters have specialised nodes for different tasks.
    - Login nodes are shared, so heavy work belongs on the compute nodes.
    - A cluster suits large batch work. Small interactive work is easier on a laptop, and long-running services belong in the cloud.

!!! postrequisite "What Next"
    - [Bash Shell](Bash_Shell.md)
