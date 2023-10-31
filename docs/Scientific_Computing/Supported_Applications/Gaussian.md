---
created_at: '2015-07-29T23:31:02Z'
hidden: false
label_names:
- mahuika
- chemistry
position: 29
title: Gaussian
vote_count: 5
vote_sum: 1
zendesk_article_id: 207127857
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

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

The Gaussian home page is at <http://www.gaussian.com>.

## Availablity

Gaussian is installed on the Mahuika cluster.

## Licensing requirements

Gaussian is made available to researchers under closed-source,
commercial licence agreements with individuals, research groups or
institutions. Whether you have access to Gaussian, which versions you
have access to, and under what conditions, will vary depending on where
you work or study.

For the sake of compliance with Gaussian licence agreements, we maintain
a special Gaussian UNIX group. Only members of this group may access and
use Gaussian. You can ask to join the Gaussian group by emailing our
support team at
[support@nesi.org.nz](mailto:support@nesi.org.nz?subject=Request%20to%20join%20the%20Gaussian%20group).

All University of Auckland staff and students are in the Gaussian group
automatically. If you are not a staff member or student at the
University of Auckland, we will add you to the Gaussian group if we are
satisfied that you require access to Gaussian to carry out your research
and that your institution's Gaussian licence agreement permits you to
use Gaussian on a computer that is not owned by or housed at your
institution. We may at any time remove you from the Gaussian group if we
believe these conditions are no longer met.

If you have any questions regarding your eligibility to access Gaussian
or any particular version or installation of it, please contact [our
support desk](mailto:support@nesi.org.nz).

## Example jobs

### Example job submission script

The following job submission script is intended for use on Mahuika.
Please note that it has a memory requirement built in: at least 2 GB for
Gaussian itself, plus a further 2 GB as a buffer zone, for a minimum
request of 4 GB (4,096 MB).

``` bash
#!/bin/bash -e

#SBATCH --job-name=H2O
#SBATCH --account=nesi99999
#SBATCH --time=00:01:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --hint=nomultithread
#SBATCH --mem=4096MB
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err

echo "============ JOB SUBMISSION SCRIPT ============"
cat $0
echo "==============================================="
echo ""
echo ""

module load Gaussian/09-D.01

# System name
system="H2O"

# Get the current directory
start_dir=$(pwd)
gjf_template="${system}.gjf.template"

# Prepare a job-specific nobackup directory and set GAUSS_SCRDIR accordingly
if [[ -n "${SLURM_ARRAY_TASK_COUNT}" && "${SLURM_ARRAY_TASK_COUNT}" -gt 1 ]]
then
        job_code="${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}"
else
        job_code="${SLURM_JOB_ID}"
fi
export GAUSS_SCRDIR="/nesi/nobackup/${SLURM_JOB_ACCOUNT}/mahuika_job_${job_code}"
/usr/bin/mkdir -p "${GAUSS_SCRDIR}"

# Calculate the number of CPUs to use within Gaussian
if [[ -n "${SLURM_CPUS_PER_TASK}" ]]
then
        gaussian_ncpus="${SLURM_CPUS_PER_TASK}"
else
        gaussian_ncpus=1
fi

# Calculate the amount of memory to use within Gaussian
# That is, amount of memory requested of Slurm minus 2 GB
if [[ -n "${SLURM_MEM_PER_NODE}" && "${SLURM_MEM_PER_NODE}" -ge 4096 ]]
then
        gaussian_memory=$((${SLURM_MEM_PER_NODE} - 2048))
else
        /usr/bin/echo "Error: Not enough RAM requested (${SLURM_MEM_PER_NODE})." >&2
        /usr/bin/echo "       Please set \"#SBATCH --mem\" to at least 4096 MB." >&2
        exit 2
fi

gjf_working_copy="${GAUSS_SCRDIR}/${system}.gjf"
gaussian_checkpoint="${GAUSS_SCRDIR}/${system}.chk"
/usr/bin/sed -e "s/<<NUMBER_OF_CORES>>/${gaussian_ncpus}/" "${gjf_template}" | \
        /usr/bin/sed -e "s/<<MEMORY>>/${gaussian_memory}/" | \
        /usr/bin/sed -e "s:<<CHECKPOINT_FILE>>:${gaussian_checkpoint}:" > "${gjf_working_copy}"

srun g09 < "${gjf_working_copy}"
```

### Example template input file

Any Gaussian input file must end with a blank line. We also recommend
specifying a checkpoint file using the %Chk directive, as a saved
checkpoint file facilitates recovery and restart if your Gaussian job
fails or is killed by the scheduler. In this case, the value of the
checkpoint file is a placeholder (as are the number of cores and the
memory) and is replaced with a real value when the Slurm job starts.

    $RunGauss$

    %NProcShared=<<NUMBER_OF_CORES>>
    %Mem=<<MEMORY>>MB
    %Chk=<<CHECKPOINT_FILE>>

    #P HF/STO-3G SP

    Single-point energy calculation on water

    0 1
    H
    O 1 0.95
    H 2 0.95 1 109.0

## Further notes

### Setting the memory and number of cores

It is important to ensure that the memory and number of cores in the
Gaussian input file itself are consistent with what you set in your job
submission script.

The key properties are `%NProcShared` and `%Mem`:

-   `%NProcShared` should be set to the number of CPU cores you intend
    to use, matching the value of the `-c` or `--cpus-per-task`
    directive in the Slurm job file.
-   `%Mem` should be set to the amount of memory you intend to use. It
    should be about 2 GB (2,048 MB) less than the value of `--mem` in
    the Slurm job submission script. Note that `--mem` is interpreted as
    being in MB rather than GB unless otherwise specified (i.e., with a
    "G" on the end).

If you use the example Slurm script and template gjf file provided above
(with appropriate modifications for your chemical system and desired
calculation), this should happen automatically.

### Saving temporary working files (for advanced users)

If you want Gaussian's temporary files (`*.inp`, `*.d2e`, `*.int`,
`*.rwf` and `*.scr`) to be written to a particular directory, you can
achieve this by setting the `GAUSS_SCRDIR` environment variable in your
job submission script, for instance:

``` bash
export GAUSS_SCRDIR=/nesi/nobackup/nesi99999/mahuika_job_123456
```

This should happen automatically if you use an appropriately modified
script based on the example job submission script given above.
