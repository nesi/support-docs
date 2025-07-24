---
created_at: '2015-07-29T23:31:02Z'
tags:
- mahuika
- chemistry
description: How to run Gaussian on the NeSI HPC
---

{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

## Description

The Gaussian series of programs provides state-of-the-art capabilities
for electronic structure modelling. It is used by chemists, chemical
engineers, biochemists, physicists and other scientists worldwide.
Starting from the fundamental laws of quantum mechanics, Gaussian
predicts the energies, molecular structures, vibrational frequencies and
molecular properties of molecules and reactions in a wide variety of
chemical environments. Gaussian's models can be applied to both stable
species and compounds which are difficult or impossible to observe
experimentally (e.g., short-lived intermediates and transition
structures).

## Licences

Gaussian is made available to researchers under closed-source,
commercial licence agreements with individuals, research groups or
institutions. Whether you have access to Gaussian, which versions you
have access to, and under what conditions, will vary depending on where
you work or study.

For the sake of compliance with Gaussian licence agreements, we maintain
a special Gaussian UNIX group. Only members of this group may access and
use Gaussian. {% include "partials/support_request.html" %} to join the Gaussian group.

All University of Auckland staff and students are in the Gaussian group
automatically. If you are not a staff member or student at the
University of Auckland, we will add you to the Gaussian group if we are
satisfied that you require access to Gaussian to carry out your research
and that your institution's Gaussian licence agreement permits you to
use Gaussian on a computer that is not owned by or housed at your
institution. We may at any time remove you from the Gaussian group if we
believe these conditions are no longer met.

If you have any questions regarding your eligibility to access Gaussian
or any particular version or installation of it, please {% include "partials/support_request.html" %}.

## Example jobs

The following job submission script is intended for use on Mahuika.
Please note that it has a memory requirement built in: at least 2 GB for
Gaussian itself, plus a further 2 GB as a buffer zone, for a minimum
request of 4 GB (4,096 MB).

Any Gaussian input file must end with a blank line. We also recommend
specifying a checkpoint file using the `%Chk` directive, as a saved
checkpoint file facilitates recovery and restart if your Gaussian job
fails or is killed by the scheduler. In this case, the value of the
checkpoint file is a placeholder (as are the number of cores and the
memory) and is replaced with a real value when the Slurm job starts.

### Shared Memory

``` sl
#!/bin/bash -e

#SBATCH --job-name=H2O_shared_memory
#SBATCH --account=nesi99999
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=8       # Note, Gaussian will use twice the number of CPUs specified by --cpus-per-task.
#SBATCH --hint=nomultithread
#SBATCH --mem=8G

module load Gaussian/09-D.01

INPUT_FILE="H2O.gjf"

GAUSSIAN_MEM="$((${SLURM_MEM_PER_NODE} - 2048))"

# It is reconmended to prepare a job-specific scratch directory
export GAUSS_SCRDIR="/nesi/nobackup/${SLURM_JOB_ACCOUNT}/gaussian_job_${SLURM_JOB_ID}"
mkdir -p "${GAUSS_SCRDIR}"

cat << EOF > $INPUT_FILE

%CPU=$(taskset -cp $$ | awk -F':' '{print $2}')
%Mem=${GAUSSIAN_MEM}MB
%Chk=${INPUT_FILE}.chk

# HF/6-31G(d) Opt=ModRedun Test

water geo optimisation HF/6-31G(d)

0 1
H
O 1 0.95
H 2 0.95 1 109.0


EOF

srun g09 < "${INPUT_FILE}"

```

### Distributed Memory

``` sl
#!/bin/bash -e

#SBATCH --job-name=H2O_distributed_memory
#SBATCH --account=nesi99999
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --hint=nomultithread
#SBATCH --mem=4G

module load Gaussian/09-D.01

INPUT_FILE="H2O.gjf"

GAUSSIAN_MEM="$((${SLURM_MEM_PER_NODE} - 2048))"

# It is reconmended to prepare a job-specific scratch directory
export GAUSS_SCRDIR="/nesi/nobackup/${SLURM_JOB_ACCOUNT}/gaussian_job_${SLURM_JOB_ID}"
mkdir -p "${GAUSS_SCRDIR}"

cat << EOF > $INPUT_FILE

%LindaWorkers=$(for n in $(srun hostname | sort -u);do printf "${n}:${SLURM_NPROCS},"; done)
%Mem=${GAUSSIAN_MEM}MB
%Chk=${INPUT_FILE}.chk

# HF/6-31G(d) Opt=ModRedun Test

water geo optimisation HF/6-31G(d)

0 1
H
O 1 0.95
H 2 0.95 1 109.0


EOF

srun g09 < "${INPUT_FILE}"

```

## Further notes

### Setting the memory and number of cores

It is important to ensure that the memory and number of cores in the
Gaussian input file itself are consistent with what you set in your job
submission script.

The key properties are `%CPU` and `%Mem`:

- `%CPU` should be set to the number of CPU cores you intend
    to use, matching the value of the `-c` or `--cpus-per-task`
    directive in the Slurm job file. Because Slurm assigns which CPUs of the compute node your jobs lands on, the 'taskset' command is needed to identify what CPUs are available to your job.
- `%Mem` should be set to the amount of memory you intend to use. It
    should be about 2 GB (2,048 MB) less than the value of `--mem` in
    the Slurm job submission script. Note that `--mem` is interpreted as
    being in MB rather than GB unless otherwise specified (i.e., with a
    "G" on the end).

If you use the example Slurm script and template `.gjf` file provided above
(with appropriate modifications for your chemical system and desired calculation), this should happen automatically.

### Saving temporary working files (for advanced users)

If you want Gaussian's temporary files (`*.inp`, `*.d2e`, `*.int`,
`*.rwf` and `*.scr`) to be written to a particular directory, you can
achieve this by setting the `GAUSS_SCRDIR` environment variable in your
job submission script, for instance:

```bash
export GAUSS_SCRDIR=/nesi/nobackup/nesi99999/mahuika_job_123456
```

This should happen automatically if you use an appropriately modified
script based on the example job submission script given above.
