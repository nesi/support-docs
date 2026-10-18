#!/bin/bash -e

# Checkpoint: end of lesson 7 (Putting it Together).
# Queues the whole pipeline: prepare.sl, a job array with a task per sample, then summarise.sl.
# Run it on the login node: bash submit.sh

mkdir -p log

n_samples=$(wc -l < samples.txt)

prepare=$(sbatch --parsable prepare.sl)

# %A is the array's job ID and %a the task index, so each task gets its own log.
# %2 runs at most 2 tasks at a time.
samples=$(sbatch --parsable --dependency afterok:${prepare} \
    --array 1-${n_samples}%2 \
    --output log/%x_%A_%a.out --error log/%x_%A_%a.err \
    sample.sl)

# If any task fails, resubmit only the failed tasks, with more memory.
sbatch --dependency afternotok:${samples} --job-name resubmit \
    --time 00:05:00 --mem 512M --output log/%x_%j.out \
    --wrap "bash resubmit_failed.sh ${samples}"

# Once every task has succeeded, summarise the results.
# If tasks are resubmitted, run summarise.sl yourself once they finish.
summary=$(sbatch --parsable --dependency afterok:${samples} summarise.sl)

echo "prepare: ${prepare}  samples: ${samples}  summarise: ${summary}"
