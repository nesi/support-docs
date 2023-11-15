---
created_at: '2018-12-17T04:31:59Z'
hidden: true
position: 20
tags: []
title: 'MATLAB: Parallel Operations'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000666055
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

# Passive Parallelisation

# Explicit Parallelisation

## Parfor

# GPUs

#  

# Arrays - Sparse, Dense and GPU 

# Performance

export TMPDIR=tmp

``` sl
#!/bin/bash -e

#SBATCH --job-name MaryTest_C2_N5_M20
#SBATCH --time 06:00:00
#SBATCH --mem-per-cpu 1500
#SBATCH --mail-type=ALL # Optional: Send email notifications
#SBATCH --cpus-per-task=2
#SBATCH --mail-user=callum.walley@nesi.org.nz # Use with --mail-type option
#SBATCH --ntasks=1
#SBATCH --output=%x_out.log
#SBATCH --error=%x_error.err

module load MATLAB

mkdir -p outputs/${SLURM_JOB_NAME}
cd outputs/${SLURM_JOB_NAME}

#Job run
srun matlab -nodisplay -r "addpath(genpath('../../../DL1014'));run_exp(5,20)"

#MOVE FILES INTO NEW DIRECTORY
mv ../../${SLURM_JOB_NAME}_out.log ${SLURM_JOB_NAME}_out.log
mv ../../${SLURM_JOB_NAME}_error.err ${SLURM_JOB_NAME}_error.err
```

 Validation

``` sl
#!/bin/bash
#
# Validation Script
# Checks all your jobs completed successfully 
#
#
#
# Just fill in the sections below each comment.
#  
#
#
# Callum Walley 
# 2019/01/11


#Location of files to be validated.
outputDir="/nesi/project/nesi99999/" 

echo "Validating Files...."

#Range of expected file size.In bytes.
minSize=0
maxSize=65000000

#Number range of jobs to check
firstIndex=10
lastIndex=20

#What to do if missing file is found.
onMissing(){


    echo "Doing the thing"


} 

for (( n=${firstIndex}; n<=${lastIndex}; n++ ))
do

#Specify naming scheme of files. Where ${n} will iterate across all indices.
filename="Job_${n}.cas" 

if [ ! -e ${outputDir}${filename} ]; then

    echo "${filename} does not exist!"
    onMissing ${n}

elif [ $(wc -c <"${outputDir}${filename}") -le $minSize ]; then

    echo "${filename} is too small! ($(wc -c < ${outputDir}${filename}) bytes)"
    onMissing ${n}

elif [ $(wc -c <"${outputDir}${filename}") -ge $maxSize ]; then

    echo "${filename} is too big! ($(wc -c < ${outputDir}${filename}) bytes)" 
    onMissing ${n}

fi

done
echo "Done!"
```
