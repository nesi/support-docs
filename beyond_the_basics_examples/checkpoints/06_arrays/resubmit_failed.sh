#!/bin/bash -e

# Checkpoint: end of lesson 6 (Job Arrays). Same script as on the Job Dependencies page.
# Resubmits the tasks of job array $1 that failed, ran out of memory or timed out, with more memory.

failed=$(sacct --jobs "$1" --array --allocations --noheader \
    --parsable2 --format JobID,State |
    grep -E 'FAILED|OUT_OF_MEMORY|TIMEOUT' |
    cut -d '|' -f 1 | cut -d '_' -f 2 | paste -sd ,)

if [ -n "${failed}" ]; then
    sbatch --array "${failed}" --mem 4G \
        --output log/%x_%A_%a.out --error log/%x_%A_%a.err sample.sl
fi
