---
created_at: '2022-08-10T21:31:45Z'
hidden: false
position: 3
tags: []
title: 'Clair3 '
vote_count: 0
vote_sum: 0
zendesk_article_id: 5292628239375
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

## Description

[Clair3 homepage](https://github.com/HKU-BAL/Clair3)

Clair3 is a germline small variant caller for long-reads. Clair3 makes
the best of two major method categories: pileup calling handles most
variant candidates with speed, and full-alignment tackles complicated
candidates to maximize precision and recall. Clair3 runs fast and has
superior performance, especially at lower coverage. Clair3 is simple and
modular for easy deployment and integration.

Clair3 is the 3<sup>rd</sup> generation of
[Clair](https://github.com/HKU-BAL/Clair) (the 2<sup>nd</sup>) and
[Clairvoyante](https://github.com/aquaskyline/Clairvoyante) (the
1<sup>st</sup>).

A short pre-print describing Clair3's algorithms and results is at
[bioRxiv](https://www.biorxiv.org/content/10.1101/2021.12.29.474431v1).

 

## License and Disclaimer

Copyright 2021 The University of Hong Kong, Department of Computer
Science

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1.  Re-distributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

2.  Re-distributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

3.  Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

``` sl
 
```

### Example Slurm script

**Caution**: Absolute path is needed for both `INPUT_DIR` and
`OUTPUT_DIR`  
  
  

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      cliar3_job
#SBATCH --mem           6G #12G is just a place holder. Adjust accordingly
#SBATCH --cpus-per-task 4 #4 just a place holder. Adjust accordingly
#SBATCH --time          01:00:00
#SBATCH --output        slurmout.%j.out


#Caution: Absolute path is needed for both INPUT_DIR and OUTPUT_DIR

INPUT_DIR=/path/to/input/data         # e.g. /nesi/nobackup/nesi12345/input (absolute path needed)
OUTPUT_DIR=/path/to/save/outputs      # /nesi/nobackup/nesi12345/output (absolute path needed)
REF=/path/to/reference/genomes        # use the suggested Slurm variable which will read the value from `--cpus-per-task`
MODEL_NAME=/model/name                # e.g. r941_prom_hac_g360+g422


module purge
module load Clair3/0.1.12-Miniconda3

run_clair3.sh \
--bam_fn=${INPUT_DIR} \
--ref_fn=${REF} \
--threads=$SLURM_CPUS_PER_TASK \
--platform=ont \
--model_path=${CONDA_PREFIX}/bin/models/${MODEL_NAME} \
--output=${OUTPUT_DIR} --enable_phasing
```

  
  
  
  