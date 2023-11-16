---
created_at: '2016-03-22T01:33:34Z'
hidden: true
position: 22
tags:
- mahuika
- tier1
- biology
title: ABySS
vote_count: 0
vote_sum: 0
zendesk_article_id: 217751818
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

ABySS ("**A**ssembly **By** **S**hort **S**equences") is a *de novo*,
parallel, paired-end sequence assembler.

The ABySS home page is at
<http://www.bcgsc.ca/platform/bioinfo/software/abyss>.

ABySS is made available at no cost for non-commercial use under the
terms of [version 3 of the GNU General Public
Licence](http://www.gnu.org/licenses/gpl-3.0.html) or, at the option of
the user, any later version of the same licence. Researchers intending
to use ABySS for commercial purposes should contact [Patrick
Rebstein](mailto:prebstein@bccancer.bc.ca). For more details, including
the full text of the licence, please consult the `LICENSE` file located
in the `share/doc/abyss` subdirectory of the ABySS installation
directory.

# Example scripts

## Example script for the Pan cluster

``` bash
#!/bin/bash -e

#SBATCH --job-name        ABySS_job
#SBATCH --account         nesi99999
#SBATCH --time            01:00:00
#SBATCH --mem-per-cpu     4G
#SBATCH --nodes           1 
#SBATCH --ntasks-per-node 12
#SBATCH --output          ABySS_job.%j.out # Include the job ID in the names
#SBATCH --error           ABySS_job.%j.err # of the output and error files

module load ABySS/2.0.1-foss-2015a

# This example specifies --ntasks-per-node and --nodes rather than the usual 
# --ntasks because, when given multiple CPUs, ABySS runs both MPI and non-MPI 
# parallel sub-programs.  It does its own MPI launching and so should not be 
# started via srun.
# See https://github.com/bcgsc/abyss#parallel-processing for details.

abyss-pe name=ecoli k=64 in='reads1.fa reads2.fa'
```
