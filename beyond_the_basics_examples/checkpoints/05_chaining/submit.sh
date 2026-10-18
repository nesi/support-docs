#!/bin/bash -e

# Checkpoint: end of lesson 5 (Splitting and Chaining Jobs).
# Queues the whole pipeline. Run it on the login node: bash submit.sh
# Each sample job waits for prepare.sl to finish successfully.

mkdir -p log

prepare=$(sbatch --parsable prepare.sl)
echo "prepare: ${prepare}"

# One job per sample. Lesson 6 replaces this loop with a job array.
while read -r sample; do
    job=$(sbatch --parsable --dependency afterok:${prepare} sample.sl "${sample}")
    echo "${sample}: ${job}"
done < samples.txt
