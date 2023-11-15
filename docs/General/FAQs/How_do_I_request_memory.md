---
created_at: '2019-08-14T05:49:00Z'
hidden: false
position: 6
tags: []
title: How do I request memory?
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001108756
zendesk_section_id: 360000039036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

In Slurm, there are two ways to request memory for your job:

-   `--mem`: Memory per node
-   `--mem-per-cpu`: Memory per [logical
    CPU](https://support.nesi.org.nz/hc/en-gb/articles/360000568236)

In most circumstances, you should request memory using `--mem`. The
exception is if you are running an MPI job that could be placed on more
than one node, with tasks divided up randomly, in which case
`--mem-per-cpu` is more appropriate. More detail is in the following
table, including how you can tell what sort of job you're submitting.

  --------------- ------------------------- --------------------- ------------------------ ------------------------ ------------------ --------------------
  Job type        Requested tasks           Requested logical     Requested nodes (`-N`,   Requested tasks per      Preferred memory   Ideal value
                  (`-n`, `--ntasks`)        CPUs per task         `--nodes`)               node                     format             
                                            (`--cpus-per-task`)                            (`--ntasks-per-node`)                       

  Serial          1 (or unspecified)        1 (or unspecified)    (Irrelevant, but should  (Irrelevant, but should  `--mem=`           Peak
                                                                  not be                   not be                                      memory<sup>3</sup>
                                                                  specified)<sup>1</sup>   specified)<sup>2</sup>                      needed by the
                                                                                                                                       program

  Multithreaded   1 (or unspecified)        &gt; 1                (Irrelevant, but should  (Irrelevant, but should  `--mem=`           Peak
  (e.g. OpenMP),                                                  not be                   not be                                      memory<sup>3</sup>
  but not MPI                                                     specified)<sup>1</sup>   specified)<sup>2</sup>                      needed by the
                                                                                                                                       program

  MPI, evenly     Unspecified<sup>4</sup>   ≥ 1 (or unspecified)  ≥ 1<sup>5</sup>          ≥ 1<sup>5</sup>          `--mem=`           (Peak
  split between                                                                                                                        memory<sup>3</sup>
  nodes                                                                                                                                needed per MPI
  (recommended                                                                                                                         task) × (number of
  method)                                                                                                                              tasks per node)

  MPI, evenly     &gt; 1                    ≥ 1 (or unspecified)  Either 1 or the number   (Irrelevant, but should  `--mem=`           (Peak
  split between                                                   of tasks<sup>6</sup>     not be                                      memory<sup>3</sup>
  nodes                                                                                    specified)<sup>4</sup>                      needed per MPI
  (discouraged                                                                                                                         task) × (number of
  method)                                                                                                                              tasks per node) 

  MPI, randomly   &gt; 1                    ≥ 1 (or unspecified)  &gt; 1; &lt; number of   (Irrelevant, but should  `--mem-per-cpu=`   (Peak
  placed                                                          tasks<sup>6</sup> (or    not be                                      memory<sup>3</sup>
                                                                  unspecified)             specified)<sup>4</sup>                      needed per MPI
                                                                                                                                       task) ÷ (number of
                                                                                                                                       logical CPUs per MPI
                                                                                                                                       task)
  --------------- ------------------------- --------------------- ------------------------ ------------------------ ------------------ --------------------

<sup>1</sup> If your job consists of only one task there's no reason to
request a specific number of nodes, and requesting more than one node
will cause you to be charged too much for your job. A one-task job will
be assigned one node by default.

<sup>2</sup> If you don't request a specific number of nodes, it makes
no sense to request a specific number of tasks per node.

<sup>3</sup> It's usually a good idea to request a little more memory
from Slurm than your program absolutely needs, to give your job a buffer
in case its behaviour varies slightly from run to run.

<sup>4</sup> If either `-n` or `--ntasks` is used along with
`--ntasks-per-node`, `--ntasks-per-node` will be silently ignored.

<sup>5</sup> An MPI job that is evenly split between two or more nodes
and that doesn't specify a total number of tasks will need either `-N`
(or `--nodes`) or `--ntasks-per-node`, or both, to be greater than 1;
and both must be positive integers.

<sup>6</sup> If you set `-N` (or `--nodes`) to 1, that is effectively
the same as setting`--ntasks-per-node` the same as`-n` (or `--ntasks`),
and the job is guaranteed to run on a single node. On the other hand, if
you request `-N` (or `--nodes`) to be the same as `-n` (or `--ntasks`),
that is effectively the same as setting `--ntasks-per-node=1`, and the
job will be evenly split between nodes. In either of these cases,
`--mem` is better than`--mem-per-cpu`. Meanwhile, requesting more nodes
than tasks never makes sense.
