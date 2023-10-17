---
created_at: '2023-05-03T21:14:18Z'
hidden: true
label_names: []
position: 0
title: R parallel
vote_count: 0
vote_sum: 0
zendesk_article_id: 6906005813519
zendesk_section_id: 360000040056
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
R is a programming language often applied to statistical problems, which
supports parallel execution on a high performance cluster. See
[here](https://support.nesi.org.nz/hc/en-gb/articles/209338087-R) for
more information on how to run R code on NeSI platforms. 

This page presents two approaches to parallel computing with R. The
focus will be on a map-reduce approach where tasks are assigned to
"workers". A final step assembles the results produced by each worker.

## Shared memory parallelism

This is suitable for tasks that can be executed within a node. 

### Pros

-   Simple to implement
-   The same code can run on a desktop and HPC
-   Can be more efficient than distributed parallelism, see section
    below

### Cons

The number of workers is limited by the number of cores available on a
node

## Distributed memory parallelism

### Pros

Scales to the size of the platform

### Cons

Sometimes less efficient than shared memory parallelism as data will
need to be messaged between nodes

 
