---
created_at: '2015-07-29T23:31:02Z'
hidden: false
label_names:
- mahuika
- chemistry
position: 29
title: Gaussian
vote_count: 4
vote_sum: 0
zendesk_article_id: 207127857
zendesk_section_id: 360000040076
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->
<div class="toc">
<ul>
<li><a href="#description">Description</a></li>
<li><a href="#licensing-requirements">Licensing requirements</a></li>
<li>
<a href="#example-jobs">Example jobs</a><br>
<ul>
<li><a href="#example-job-submission-script">Example job submission script</a></li>
<li><a href="#example-input-file">Example input file</a></li>
</ul>
</li>
<li>
<a href="#further-notes">Further notes</a>
<ul>
<li><a href="#setting-the-memory-and-number-of-cores">Setting the memory and number of cores</a></li>
<li><a href="#saving-temporary-working-files-for-advanced-users">Saving temporary working files (for advanced users)</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="description">Description</h2>
<p>The Gaussian series of programs provides state-of-the-art capabilities for electronic structure modelling. It is used by chemists, chemical engineers, biochemists, physicists and other scientists worldwide. Starting from the fundamental laws of quantum mechanics, Gaussian predicts the energies, molecular structures, vibrational frequencies and molecular properties of molecules and reactions in a wide variety of chemical environments. Gaussian's models can be applied to both stable species and compounds which are difficult or impossible to observe experimentally (e.g., short-lived intermediates and transition structures).</p>
<p>The Gaussian home page is at <a href="http://www.gaussian.com">http://www.gaussian.com</a>.</p>
<h2 id="available-versions">Availablity</h2>
<p>Gaussian is installed on the Mahuika cluster.</p>
<h2 id="licensing-requirements">Licensing requirements</h2>
<p>Gaussian is made available to researchers under closed-source, commercial licence agreements with individuals, research groups or institutions. Whether you have access to Gaussian, which versions you have access to, and under what conditions, will vary depending on where you work or study.</p>
<p>For the sake of compliance with Gaussian licence agreements, we maintain a special Gaussian UNIX group. Only members of this group may access and use Gaussian. You can ask to join the Gaussian group by emailing our support team at <a href="mailto:support@nesi.org.nz?subject=Request%20to%20join%20the%20Gaussian%20group">support@nesi.org.nz</a>.</p>
<p>All University of Auckland staff and students are in the Gaussian group automatically. If you are not a staff member or student at the University of Auckland, we will add you to the Gaussian group if we are satisfied that you require access to Gaussian to carry out your research and that your institution's Gaussian licence agreement permits you to use Gaussian on a computer that is not owned by or housed at your institution. We may at any time remove you from the Gaussian group if we believe these conditions are no longer met.</p>
<p>If you have any questions regarding your eligibility to access Gaussian or any particular version or installation of it, please contact <a href="mailto:support@nesi.org.nz">our support desk</a>.</p>
<h2 id="example-jobs">Example jobs</h2>
<h3 id="example-script-and-input-for-the-pan-cluster">Example job submission script</h3>
<p>The following job submission script is intended for use on Mahuika. Please note that it has a memory requirement built in: at least 2 GB for Gaussian itself, plus a further 2 GB as a buffer zone, for a minimum request of 4 GB (4,096 MB).</p>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name=H2O
#SBATCH --account=nesi99999
#SBATCH --time=00:01:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --hint=nomultithread
#SBATCH --mem=4096MB
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
<br>echo "============ JOB SUBMISSION SCRIPT ============"<br>cat $0<br>echo "==============================================="<br>echo ""<br>echo ""<br>
module load Gaussian/09-D.01

# System name
system="H2O"

# Get the current directory
start_dir=$(pwd)
gjf_template="${system}.gjf.template"

# Prepare a job-specific nobackup directory and set GAUSS_SCRDIR accordingly
if [[ -n "${SLURM_ARRAY_TASK_COUNT}" &amp;&amp; "${SLURM_ARRAY_TASK_COUNT}" -gt 1 ]]
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
if [[ -n "${SLURM_MEM_PER_NODE}" &amp;&amp; "${SLURM_MEM_PER_NODE}" -ge 4096 ]]
then
        gaussian_memory=$((${SLURM_MEM_PER_NODE} - 2048))
else
        /usr/bin/echo "Error: Not enough RAM requested (${SLURM_MEM_PER_NODE})." &gt;&amp;2
        /usr/bin/echo "       Please set \"#SBATCH --mem\" to at least 4096 MB." &gt;&amp;2
        exit 2
fi

gjf_working_copy="${GAUSS_SCRDIR}/${system}.gjf"
gaussian_checkpoint="${GAUSS_SCRDIR}/${system}.chk"
/usr/bin/sed -e "s/&lt;&lt;NUMBER_OF_CORES&gt;&gt;/${gaussian_ncpus}/" "${gjf_template}" | \
        /usr/bin/sed -e "s/&lt;&lt;MEMORY&gt;&gt;/${gaussian_memory}/" | \
        /usr/bin/sed -e "s:&lt;&lt;CHECKPOINT_FILE&gt;&gt;:${gaussian_checkpoint}:" &gt; "${gjf_working_copy}"

srun g09 &lt; "${gjf_working_copy}"
</code></pre>
<h3 id="example-input-file">Example template input file</h3>
<p>Any Gaussian input file must end with a blank line. We also recommend specifying a checkpoint file using the %Chk directive, as a saved checkpoint file facilitates recovery and restart if your Gaussian job fails or is killed by the scheduler. In this case, the value of the checkpoint file is a placeholder (as are the number of cores and the memory) and is replaced with a real value when the Slurm job starts.</p>
<pre><code>$RunGauss$

%NProcShared=&lt;&lt;NUMBER_OF_CORES&gt;&gt;
%Mem=&lt;&lt;MEMORY&gt;&gt;MB
%Chk=&lt;&lt;CHECKPOINT_FILE&gt;&gt;

#P HF/STO-3G SP

Single-point energy calculation on water

0 1
H
O 1 0.95
H 2 0.95 1 109.0

</code></pre>
<h2 id="further-notes">Further notes</h2>
<h3 id="setting-the-memory-and-number-of-cores">Setting the memory and number of cores</h3>
<p>It is important to ensure that the memory and number of cores in the Gaussian input file itself are consistent with what you set in your job submission script.</p>
<p>The key properties are <code>%NProcShared</code> and <code>%Mem</code>:</p>
<ul>
<li>
<code>%NProcShared</code> should be set to the number of CPU cores you intend to use, matching the value of the <code>-c</code> or <code>--cpus-per-task</code> directive in the Slurm job file.</li>
<li>
<code>%Mem</code> should be set to the amount of memory you intend to use. It should be about 2 GB (2,048 MB) less than the value of <code>--mem</code> in the Slurm job submission script. Note that <code>--mem</code> is interpreted as being in MB rather than GB unless otherwise specified (i.e., with a "G" on the end).</li>
</ul>
<p>If you use the example Slurm script and template gjf file provided above (with appropriate modifications for your chemical system and desired calculation), this should happen automatically.</p>
<h3 id="saving-temporary-working-files-for-advanced-users">Saving temporary working files (for advanced users)</h3>
<p>If you want Gaussian's temporary files (<code>*.inp</code>, <code>*.d2e</code>, <code>*.int</code>, <code>*.rwf</code> and <code>*.scr</code>) to be written to a particular directory, you can achieve this by setting the <code>GAUSS_SCRDIR</code> environment variable in your job submission script, for instance:</p>
<pre><code class="bash">export GAUSS_SCRDIR=/nesi/nobackup/nesi99999/mahuika_job_123456</code></pre>
<p>This should happen automatically if you use an appropriately modified script based on the example job submission script given above.</p>