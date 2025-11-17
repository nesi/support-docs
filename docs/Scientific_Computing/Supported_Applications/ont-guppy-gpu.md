---
created_at: '2022-03-22T07:46:51Z'
tags:
- biology
- gpu
- software
description: Supported applications page for Guppy
title: ont-guppy-gpu
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Description

Guppy, is a data processing toolkit that contains Oxford Nanopore’s
(<https://nanoporetech.com/>) basecalling algorithms, and several
bioinformatic post-processing features, such as
barcoding/demultiplexing, adapter trimming, and alignment. The Guppy
toolkit also performs modified basecalling (5mC, 6mA and CpG) from the
raw signal data, producing an additional FAST5 file of modified base
probabilities.

## License and Disclaimer

“Base Caller Software” shall mean Oxford’s proprietary software,
including all functional specifications associated therewith made
available to the Oxford Group’s customers on the Oxford Group’s
websites, as amended from time to time (the “Base Caller
Documentation”), designed to convert certain Instrument  
Data to Biological Data, as may be made available to Customers by
Oxford, whether free of charge or for a fee.

Guppy is available to ONT customers via their community website
<https://community.nanoporetech.com/>

### Example Slurm script

- Following Slurm script is a template to run Basecalling on NVIDIA
    P100 GPUs.( We do not recommend running Guppy jobs on CPUs )
- `--device auto` will automatically pick up the GPU over CPU
- Also,  NeSI Mahuika cluster can provide A100 GPUs  which can be 5-6
    times faster than P100 GPUs for Guppy Basecalling with  version. 5
    and above. This can be requested with
    `#SBATCH --gpus-per-node A100:1` variable
- Config files are stored in
    ***/opt/nesi/CS400\_centos7\_bdw/ont-guppy-gpu/(version)/data/***
    with read permissions to all researchers (replace ***(version)***
    with the version of the module)

``` sl
#!/bin/bash -e

#SBATCH --account        nesi12345
#SBATCH --job-name       ont-guppy-gpu_job
#SBATCH --gpus-per-node  A100:1
#SBATCH --mem            6G
#SBATCH --cpus-per-task  4
#SBATCH --time           10:00:00
#SBATCH --output         slurmout.%j.out

module purge
module load ont-guppy-gpu/6.4.2

guppy_basecaller -i /path/to/input/data/directory -s /path/to/save/fastq/files \
--config /opt/nesi/CS400_centos7_bdw/ont-guppy-gpu/6.4.2/data/nameof.cfg \
--device auto --recursive --records_per_fastq 4000 \
--calib_detect --calib_reference lambda_3.6kb.fasta --detect_mid_strand_adapter
```
