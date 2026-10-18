# Beyond the Basics example files (scaffold)

Draft of the example directory for the Beyond the Basics tutorials, to go in `/opt/nesi/examples` on the cluster.
Not published and not committed. The data (`untrimmed_fastq/`, `ref_genome/`) is not included here.

## Layout

```txt
pipeline.sl          Starting point for lesson 1: one job runs every step for every sample.
samples.txt          One sample name per line.
checkpoints/NN_*/    The scripts as they are at the END of lesson NN.
                     A learner who skips ahead copies the previous lesson's checkpoint.
```

## How the scripts change

| Lesson | Ends with | Change |
| - | - | - |
| 01 Measuring Job Efficiency | `pipeline.sl` | `srun` in front of each command, so each shows as its own step in `sacct` and `profile_plot`. |
| 02 Loops and Variables | `pipeline.sl` | Paths in variables, braces and quotes, `set -u`. Same steps and outputs. |
| 03 Reusable Job Scripts | `pipeline.sl`, `sample.sl` | Per-sample steps move to `sample.sl`, which takes the sample as `$1` and uses `${SLURM_CPUS_PER_TASK}`. `pipeline.sl` only indexes the reference genome. |
| 04 Debugging Failed Jobs | `pipeline.sl`, `sample.sl` | `sample.sl` checks its inputs and gives a clear error for a missing argument. Resources set from `seff`. |
| 05 Splitting and Chaining Jobs | `prepare.sl`, `sample.sl`, `submit.sh` | `pipeline.sl` renamed `prepare.sl`. `submit.sh` queues each sample with `afterok` on `prepare.sl`. Less I/O: trimmed reads stay compressed and the alignment is piped into `samtools sort`. |
| 06 Job Arrays | `prepare.sl`, `sample.sl`, `submit.sh`, `resubmit_failed.sh` | One job array in place of the loop of `sbatch`. `sample.sl` takes an argument or its line of `samples.txt`. `%A_%a` logs, `%2` limit, follow-up job resubmits failed tasks with more memory. |
| 07 Putting it Together | adds `summarise.sl` | Runs after the array (`afterok`) and counts variants per sample. |

For lesson 4, the failures are caused from the command line rather than with broken copies of the script, for example:

```sh
sbatch sample.sl NOT_A_SAMPLE                     # missing input: exit code 1, message in .err
sbatch --mem 100M sample.sl SRR2584863            # OUT_OF_MEMORY
sbatch --time 00:00:30 sample.sl SRR2584863       # TIMEOUT
rm -r log; sbatch sample.sl SRR2584863            # no log directory: no output at all
```

## To check on the cluster before use

None of these scripts have been run.

- `${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa` exists once `Trimmomatic/0.39-Java-1.8.0_144` is loaded
  (replaces the old `/opt/nesi/CS400_centos7_bdw/...` path).
- `vcfutils.pl` is on the path from the BCFtools module.
- `bwa-mem2 mem` reads gzipped FASTQ (lesson 5 onwards), and `samtools sort` reads SAM from stdin with `-`.
- `bwa-mem2 index` writes `ecoli_rel606.fasta.bwt.2bit.64`, which lesson 4's input check looks for.
- `srun bash -c "... | ..."` profiles the pipe as one step.
- `resubmit_failed.sh`: the `sacct --array --parsable2` output and the state names.
- The three sample names, and whether to add more samples so a job array limit like `%2` has something to limit.
- Resources (`--mem`, `--time`, `--cpus-per-task`) in every script, from `seff` of recorded runs.
- `--account nesi99991` is a placeholder. Learners replace it, or leave it out if they are only in one project.

The recorded jobs for each lesson will need new job IDs in `mkdocs.yml` once these are run.
