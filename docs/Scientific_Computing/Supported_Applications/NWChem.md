---
created_at: '2015-12-13T20:47:26Z'
tags:
- mahuika
- tier1
- chemistry
title: NWChem
vote_count: 0
vote_sum: 0
zendesk_article_id: 215680177
zendesk_section_id: 360000040076
---

{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

NWChem aims to provide its users with computational chemistry tools that
are scalable both in their ability to treat large scientific
computational chemistry problems efficiently, and in their use of
available parallel computing resources from high-performance parallel
supercomputers to conventional workstation clusters. NWChem software can
handle: biomolecules, nanostructures, and solid-state; from quantum to
classical, and all combinations; Gaussian basis functions or
plane-waves; scaling from one to thousands of processors; properties and
relativity.

The NWChem home page is at <https://nwchemgit.github.io/>.

NWChem is available to anyone as open source software at no cost under
the terms of the [Educational Community Licence, version
2.0](http://opensource.org/licenses/ecl2.php).

## Example Slurm script

```sh
#!/bin/bash -e

#SBATCH --job-name       NWChem_job
#SBATCH --account        nesi99999
#SBATCH --time           01:00:00
#SBATCH --tasks          64
#SBATCH --cpus-per-task  1
#SBATCH --tasks-per-node 16
#SBATCH --mem-per-cpu    4G
#SBATCH --output         NWChem_job.%j.out    # Include the job ID in the names
#SBATCH --error          NWChem_job.%j.err    # of the output and error files

module load NWChem/6.8.1.revision133-gimkl-2018b-2018-06-14-Python-2.7.16

# Since --output is set, there is no need to redirect output to a file
# on the NWChem command line.
srun nwchem NWChem_job.nw
```

## Shared memory limits

NWChem relies on an environment variable, `ARMCI_DEFAULT_SHMMAX`, to set
the amount of shared memory used per node. `ARMCI_DEFAULT_SHMMAX` must
be set to an appropriate value given the global memory set in the NWChem
input file.

For example, if the global memory (set via the `global` keyword in the
input file) is set to 1,024 MB, `ARMCI_DEFAULT_SHMMAX` should be set to
1,024 multiplied by the number of cores requested per node.

It follows that a NWChem job must request the same number of cores on
each node. This is accomplished by setting the number of cores per task
(`--cpus-per-task`) and tasks per node (`--tasks-per-node`) in the job
submission script. These values should be appropriately set. Setting
`--cpus-per-task` to greater than 1 will force shared-memory
parallelisation; if this option is supplemented by `--tasks` greater
than 1, hybrid parallelisation will be used.
