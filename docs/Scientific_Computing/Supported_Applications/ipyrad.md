---
created_at: '2022-09-26T08:09:35Z'
tags:
- biology
- software
description: Supported applications page for ipyrad
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Description

**ipyrad**, an interactive assembly and analysis toolkit for
restriction-site associated DNA (RAD-seq) and related data types. Please
explore the documentation to find out more about the features of
ipyrad.\\

Home page is at <https://ipyrad.readthedocs.io/en/latest/index.html>

### Cite the Manuscript

Eaton DAR & Overcast I. "ipyrad: Interactive assembly and analysis of
RADseq datasets." Bioinformatics (2020).

### License

GPLv3

## Getting Started

Following **example** uses  rad\_example which can be downloaded as per
instructions on
<https://ipyrad.readthedocs.io/en/latest/tutorial_advanced_cli.html>

``` sh
curl -LkO https://eaton-lab.org/data/ipsimdata.tar.gz
tar -xvzf ipsimdata.tar.gz
```

Start by creating a new Assembly  `data1`  , and then we’ll edit the
params file to tell it how to find the input data files for this data
set.

``` sh
module purge
module load ipyrad/0.9.85-gimkl-2022a-Python-3.10.5
ipyrad -n data1

New file 'params-data1.txt' created in ........
```

`params-data1.txt` will be created on current working directory. Review
and edit the paths in parameter file to match the destinations of input
data, barcode paths,etc.

### Slurm Script for Using Multiple CPUs a Single Compute Node

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      ipyrad
#SBATCH --cpus-per-task 12
#SBATCH --time          00:05:00
#SBATCH --mem           10G
#SBATCH --output        ipyrad_output_%j.txt

## assembly name
assembly_name="data1"

## load environment and module
module purge
module load ipyrad/0.9.85-gimkl-2022a-Python-3.10.5

## create, prepare and change to a job specific dir
jobdir="ipyrad_${SLURM_JOB_ID}"
params="params-${assembly_name}.txt"

mkdir $jobdir
sed "s#$(pwd) #$(pwd)/$jobdir#" $params > $jobdir/$params
cd $jobdir


## call ipyrad on your params file and perform 7 steps from the workflow
srun ipyrad -p $params -s 12 --force 

```
