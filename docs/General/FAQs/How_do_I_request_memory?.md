In Slurm, there are two ways to request memory for your job:

-   `--mem`: Memory per node
-   `--mem-per-cpu`: Memory per [logical
    CPU](https://support.nesi.org.nz/hc/en-gb/articles/360000568236)

In most circumstances, you should request memory using `--mem`. The
exception is if you are running an MPI job that could be placed on more
than one node, with tasks divided up randomly, in which case
`--mem-per-cpu` is more appropriate. More detail is in the following
table, including how you can tell what sort of job you\'re submitting.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Job type                                               Requested tasks\     Requested logical CPUs per task\   Requested nodes (`-N`, `--nodes`)              Requested tasks per node\                      Preferred memory format   Ideal value
                                                         (`-n`, `--ntasks`)   (`--cpus-per-task`)                                                               (`--ntasks-per-node`)                                                    
  ------------------------------------------------------ -------------------- ---------------------------------- ---------------------------------------------- ---------------------------------------------- ------------------------- ------------------------------------------------------------------------------
  Serial                                                 1 (or unspecified)   1 (or unspecified)                 (Irrelevant, but should not be specified)^1^   (Irrelevant, but should not be specified)^2^   `--mem=`                  Peak memory^3^ needed by the program

  Multithreaded (e.g. OpenMP), but not MPI               1 (or unspecified)   \> 1                               (Irrelevant, but should not be specified)^1^   (Irrelevant, but should not be specified)^2^   `--mem=`                  Peak memory^3^ needed by the program

  MPI, evenly split between nodes (recommended method)   Unspecified^4^       ≥ 1 (or unspecified)               ≥ 1^5^                                         ≥ 1^5^                                         `--mem=`                  (Peak memory^3^ needed per MPI task) × (number of tasks per node)

  MPI, evenly split between nodes (discouraged method)   \> 1                 ≥ 1 (or unspecified)               Either 1 or the number of tasks^6^             (Irrelevant, but should not be specified)^4^   `--mem=`                  (Peak memory^3^ needed per MPI task) × (number of tasks per node) 

  MPI, randomly placed                                   \> 1                 ≥ 1 (or unspecified)               \> 1; \< number of tasks^6^ (or unspecified)   (Irrelevant, but should not be specified)^4^   `--mem-per-cpu=`          (Peak memory^3^ needed per MPI task) ÷ (number of logical CPUs per MPI task)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
