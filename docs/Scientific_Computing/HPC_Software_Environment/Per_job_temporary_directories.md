---
created_at: '2023-07-21T04:10:04Z'
hidden: false
label_names: []
position: 0
title: Per job temporary directories
vote_count: 0
vote_sum: 0
zendesk_article_id: 7463891150863
zendesk_section_id: 360000040056
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>Most programs which create temporary files will put those files in the directory specified by the environment variable <code>TMPDIR</code> if that is set, or <code>/tmp</code> otherwise. This is also true in Slurm, such that whenever a job starts, a temporary directory is created for that job and <code>TMPDIR</code> set. When the job ends our Slurm epilog ensures that the directory is deleted.</p>
<p>By default, this job-specific temporary directory is placed in <code>/dev/shm</code>, which is a “tmpfs” filesystem and so actually sits in ordinary RAM.  As a consequence, your job’s memory request should include enough to cover the size of any temporary files.</p>
<p>On the <code>milan</code> and <code>hgx</code> partitions, however, you have the option of specifying <code>#SBATCH --gres=ssd</code> in your job script which will place <code>TMPDIR</code> on a 1.5 TB NVMe SSD attached to the node rather than in RAM. When <code>--gres=ssd</code> is set your job’s memory request <em>does not</em> need to include enough to cover the size of any temporary files (as this is a separate resource). These SSDs give the job a slower but very much larger temporary directory. They are allocated exclusively to jobs, so there can only be one such job per node at a time. This gives the job all the available bandwidth of the SSD device but does limit the number of such jobs.</p>
<p>Alternatively you can ignore the provided directory and set <code>TMPDIR</code> yourself, typically to a location in <code>/nesi/nobackup</code>.  This will be the slowest option with the largest capacity. Also if set to <code>nobackup</code> the files will remain after the job finishes, so be weary of how much space your jobs temporary files use. An example of how <code>TMPDIR</code> may be set yourself is shown below,</p>
<p><code>export TMPDIR=/nesi/nobackup/$SLURM_ACCOUNT/tmp/$SLURM_JOB_ID</code></p>
<p> </p>
<h2 id="01H7HAJK7GE0YQH4BHKQKWHR07">Example of copying data into the p<span>er job temporary directories for use mid-job</span>
</h2>
<p>The per job temporary directory can also be used to store data that needs to be accessed as the job runs. For example you may wish to read the standard database of Kraken2 (located in <code>/opt/nesi/db/Kraken2/standard-2018-09</code>) from the <code>milan</code> SSDs instead of <code>/opt</code>. To do this, request the NVMe SSD on <code>milan</code> as described above. Then, after loading the Kraken2 module in your Slurm script, copy the database onto the SSD,</p>
<pre><span>cp -r /opt/nesi/db/Kraken2/standard-2018-09/* $TMPDIR</span></pre>
<p>To get Kraken2 to read the DB from the SSDs (and not from <code>/opt</code>), change the <code class="bash hljs">KRAKEN2_DEFAULT_DB</code> variable,</p>
<pre><code class="bash hljs"><span class="hljs-built_in">export</span> KRAKEN2_DEFAULT_DB=<span class="hljs-variable">$TMPDIR</span></code></pre>
<p>The variable <code class="bash hljs">KRAKEN2_DEFAULT_DB</code> simply points to the database and is found by <code>module show Kraken2</code>.</p>
