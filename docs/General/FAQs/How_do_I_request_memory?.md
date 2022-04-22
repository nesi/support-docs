In Slurm, there are two ways to request memory for your job:

-   `--mem`: Memory per node
-   `--mem-per-cpu`: Memory per [logical
    CPU](https://support.nesi.org.nz/hc/en-gb/articles/360000568236)

In most circumstances, you should request memory using `--mem`. The
exception is if you are running an MPI job that could be placed on more
than one node, with tasks divided up randomly, in which case
`--mem-per-cpu` is more appropriate. More detail is in the following
table, including how you can tell what sort of job you\'re submitting.

  -----------------------------------------------------------------------------------------------------------------------------
  Job type        Requested tasks\ Requested logical     Requested nodes Requested tasks per     Preferred memory   Ideal value
                  (`-n`,           CPUs per task\        (`-N`,          node\                   format             
                  `--ntasks`)      (`--cpus-per-task`)   `--nodes`)      (`--ntasks-per-node`)                      
  --------------- ---------------- --------------------- --------------- ----------------------- ------------------ -----------
  Serial          1 (or            1 (or unspecified)    (Irrelevant,    (Irrelevant, but should `--mem=`           Peak
                  unspecified)                           but should not  not be specified)^2^                       memory^3^
                                                         be                                                         needed by
                                                         specified)^1^                                              the program

  Multithreaded   1 (or            \> 1                  (Irrelevant,    (Irrelevant, but should `--mem=`           Peak
  (e.g. OpenMP),  unspecified)                           but should not  not be specified)^2^                       memory^3^
  but not MPI                                            be                                                         needed by
                                                         specified)^1^                                              the program

  MPI, evenly     Unspecified^4^   ≥ 1 (or unspecified)  ≥ 1^5^          ≥ 1^5^                  `--mem=`           (Peak
  split between                                                                                                     memory^3^
  nodes                                                                                                             needed per
  (recommended                                                                                                      MPI task) ×
  method)                                                                                                           (number of
                                                                                                                    tasks per
                                                                                                                    node)

  MPI, evenly     \> 1             ≥ 1 (or unspecified)  Either 1 or the (Irrelevant, but should `--mem=`           (Peak
  split between                                          number of       not be specified)^4^                       memory^3^
  nodes                                                  tasks^6^                                                   needed per
  (discouraged                                                                                                      MPI task) ×
  method)                                                                                                           (number of
                                                                                                                    tasks per
                                                                                                                    node) 

  MPI, randomly   \> 1             ≥ 1 (or unspecified)  \> 1; \< number (Irrelevant, but should `--mem-per-cpu=`   (Peak
  placed                                                 of tasks^6^ (or not be specified)^4^                       memory^3^
                                                         unspecified)                                               needed per
                                                                                                                    MPI task) ÷
                                                                                                                    (number of
                                                                                                                    logical
                                                                                                                    CPUs per
                                                                                                                    MPI task)
  -----------------------------------------------------------------------------------------------------------------------------

^1^ If your job consists of only one task there\'s no reason to request
a specific number of nodes, and requesting more than one node will cause
you to be charged too much for your job. A one-task job will be assigned
one node by default.

^2^ If you don\'t request a specific number of nodes, it makes no sense
to request a specific number of tasks per node.

^3^ It\'s usually a good idea to request a little more memory from Slurm
than your program absolutely needs, to give your job a buffer in case
its behaviour varies slightly from run to run.

^4^ If either `-n` or `--ntasks` is used along with `--ntasks-per-node`,
`--ntasks-per-node` will be silently ignored.

^5^ An MPI job that is evenly split between two or more nodes and that
doesn\'t specify a total number of tasks will need either `-N` (or
`--nodes`) or `--ntasks-per-node`, or both, to be greater than 1; and
both must be positive integers.

^6^ If you set `-N` (or `--nodes`) to 1, that is effectively the same as
setting`--ntasks-per-node` the same as`-n` (or `--ntasks`), and the job
is guaranteed to run on a single node. On the other hand, if you request
`-N` (or `--nodes`) to be the same as `-n` (or `--ntasks`), that is
effectively the same as setting `--ntasks-per-node=1`, and the job will
be evenly split between nodes. In either of these cases, `--mem` is
better than`--mem-per-cpu`. Meanwhile, requesting more nodes than tasks
never makes sense.
