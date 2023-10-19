---
created_at: '2020-03-08T20:06:48Z'
hidden: false
label_names: []
position: 4
title: Job Checkpointing
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001413096
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>Job/<a href="https://en.wikipedia.org/wiki/Application_checkpointing" target="_self">Application Checkpointing</a> is the snapshotting of a programs state, so that it can be restarted from that point in case of failure. This is especially important in long running jobs.</p>
<p>How checkpointing can be implemented depends on the application/code being used, some will have inbuilt methods whereas others might require some scripting.</p>
<h1>Queueing </h1>
<p>Checkpointing code has the added advantage that it allows you to split your work into smaller jobs, allowing them to move through the queue faster. </p>
<p>Below is an example of submitting the same job again, if previous has run successfully.</p>
<pre># Slurm header '#SBATCH etc etc<br><code><br>sbatch --dependency=afterok:${SLURM_JOB_ID} "$0" <br># "$0" is equal to the name of this script.<br><br># Code that implements checkpointing</code></pre>
<p>This job will resubmit itself forever until stopped.</p>
<p>Another example for a job requiring explicit step inputs.</p>
<pre># Slurm header '#SBATCH etc etc<br><br>n_steps=1000<br>starting_step=${1:-0} # Will be equal to first argument, or '0' if unset.<br>ending_step=$(( starting_step + n_steps )) <br><code><br># Submit next step with starting step equal to ending step of this job.<br>sbatch --dependency=afterok:${SLURM_JOB_ID} "$0" ${ending_step}<br></code><br>my-program --nfirst ${starting_step} --nlast ${ending_step}</pre>
<p>The use of <code>--dependency</code> has the advantage of adding the next job to the queue <em>before</em> starting, saving queue time in between jobs.</p>
<h1>Examples</h1>
<h2>Matlab</h2>
<pre><code>% If checkpoint file, load from there.
checkpoint='checkpoint_2020-03-09T0916.mat';
if exist(checkpoint,'file')==2, load(checkpoint);startindex=i;else startindex=1;end

for i = startindex:100
    % Long running process<br><br>    % Save workspace at end of each loop.
    save(['checkpoint_', datestr(now, 'yyyy-mm-ddTHHMM')])
end</code></pre>
<p> </p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p>We <strong><em>strongly</em> </strong>recommend implementing checkpointing on any job running longer than 3 days!</p>
</blockquote>