# Description

[Clair3 homepage](https://github.com/HKU-BAL/Clair3)

Clair3 is a germline small variant caller for long-reads. Clair3 makes
the best of two major method categories: pileup calling handles most
variant candidates with speed, and full-alignment tackles complicated
candidates to maximize precision and recall. Clair3 runs fast and has
superior performance, especially at lower coverage. Clair3 is simple and
modular for easy deployment and integration.

Clair3 is the 3^rd^ generation of
[Clair](https://github.com/HKU-BAL/Clair) (the 2^nd^) and
[Clairvoyante](https://github.com/aquaskyline/Clairvoyante) (the 1^st^).

A short pre-print describing Clair3\'s algorithms and results is at
[bioRxiv](https://www.biorxiv.org/content/10.1101/2021.12.29.474431v1).

 

# License and Disclaimer {#license_and_disclaimer}

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

# Singularity container

Although we do not provide Clair3 as a module, it is available as a
Singularity container which is stored in `/opt/nesi/container/Clair3`   

    /opt/nesi/containers/Clair3/
    └── clair3_Aug2022.simg

### How to use Clair3 with Singularity {#how-to-use-clair3-with-singularity dir="auto"}

**Caution**: Absolute path is needed for both `INPUT_DIR` and
`OUTPUT_DIR`.

    INPUT_DIR="[YOUR_INPUT_FOLDER]"        # e.g. /nesi/nobackup/nesi12345/input (absolute path needed)
    OUTPUT_DIR="[YOUR_OUTPUT_FOLDER]"      # e.g. /nesi/nobackup/nesi12345/output (absolute path needed)
    THREADS="[MAXIMUM_THREADS]"            # e.g. Refer to Slurm script below for more information on this
    MODEL_NAME="[YOUR_MODEL_NAME]"         # e.g. r941_prom_hac_g360+g422

    # run clair3 like this afterward
    singularity exec clair3_latest.sif \
      /opt/bin/run_clair3.sh \
      --bam_fn=${INPUT_DIR}/input.bam \    ## change your bam file name here
      --ref_fn=${INPUT_DIR}/ref.fa \       ## change your reference file name here
      --threads=${THREADS} \               ## maximum threads to be used
      --platform="ont" \                   ## options: {ont,hifi,ilmn}
      --model_path="/opt/models/${MODEL_NAME}" \
      --output=${OUTPUT_DIR}               ## absolute output path prefix

##   {#section .highlight .highlight-source-shell .notranslate .position-relative .overflow-auto}

##   {#section-1 .highlight .highlight-source-shell .notranslate .position-relative .overflow-auto}

## Example Slurm script {#example-slurm-script .highlight .highlight-source-shell .notranslate .position-relative .overflow-auto}

**Caution**: Absolute path is needed for both `INPUT_DIR` and
`OUTPUT_DIR`[\
\
\
]{.pl-c}

    #!/bin/bash -e

    #SBATCH --account       nesi12345
    #SBATCH --job-name      cliar3_job
    #SBATCH --mem           12G #12G is just a place holder. Adjust accordingly
    #SBATCH --cpus-per-task 4 #4 just a place holder. Adjust accordingly
    #SBATCH --time          10:00:00
    #SBATCH --output        slurmout.%j.out


    #Caution: Absolute path is needed for both INPUT_DIR and OUTPUT_DIR

    INPUT_DIR="[YOUR_INPUT_FOLDER]"       # e.g. /nesi/nobackup/nesi12345/input (absolute path needed)
    OUTPUT_DIR="[YOUR_OUTPUT_FOLDER]"     # /nesi/nobackup/nesi12345/output (absolute path needed)
    THREADS=$SLURM_CPUS_PER_TASK          # use the suggested Slurm variable which will read the value from `--cpus-per-task`
    MODEL_NAME="[YOUR_MODEL_NAME]"        # e.g. r941_prom_hac_g360+g422


    #Load Singularity module. Change the Singularity module version as necessary
    module purge
    module load Singularity/3.10.0

    # run clair3 like this afterward
    singularity exec clair3_latest.sif \
    /opt/bin/run_clair3.sh \
    --bam_fn=${INPUT_DIR}/input.bam \ ## change your bam file name here
    --ref_fn=${INPUT_DIR}/ref.fa \ ## change your reference file name here
    --threads=${THREADS} \ ## maximum threads to be used
    --platform="ont" \ ## options: {ont,hifi,ilmn}
    --model_path="/opt/models/${MODEL_NAME}" \
    --output=${OUTPUT_DIR} ## absolute output path prefix

[\
\
\
\
]{.pl-c}

``
