---
created_at: '2021-09-21T00:16:50Z'
hidden: true
label_names: []
position: 2
title: Repeating jobs
vote_count: 0
vote_sum: 0
zendesk_article_id: 4406771973007
zendesk_section_id: 360000030876
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h2>Re-submitting a job script from within itself</h2>
<p>Jobs can submit additional jobs. To avoid any risk of a runaway explosion of jobs, there should be no more than one such self-resubmission.  Doing this reliably can be a bit complicated.  Potentially useful tools include:</p>
<ul>
<li>Various sbatch options:
<ul>
<li>"--depend=afterok:$SLURM_JOB_ID"</li>
<li>"--depend=singleton"</li>
<li>"--begin=now+1days"</li>
<li>"--signal=USR1@120"</li>
</ul>
</li>
<li>Using bash traps to execute something on job exit</li>
</ul>
<h2>Cron</h2>
<p>Cron is the standard Unix way of performing a task at a fixed time every hour, day, or week.  It is possible to use it on most interactive NeSI nodes, however there are some complications and limitations:</p>
<ul>
<li>We don't want too much heavy calculation or memory use happening on the login nodes since they are shared will all other users. So large scheduled tasks should be run indirectly - with the <em>cron</em> script merely submitting a Slurm job, or one of the other mechanisms described here should be used.</li>
<li>The main clusters each have two login nodes and when one has problems we switch to the other being the default, so you need to keep track of which node's cron you are using.</li>
<li>The stored <em>crontab</em> files will be deleted whenever we have to reboot the node in question, so this example crontab file backs itself up every week:</li>
</ul>
<pre><span>CRON_TZ=NZ</span><br><span>PATH=/usr/bin</span><br><br><span># min<span class="Apple-converted-space">    </span>hr<span class="Apple-converted-space">    </span>dom <span class="Apple-converted-space">  </span>month<span class="Apple-converted-space">      </span>dow <span class="Apple-converted-space">        </span>command</span><br>   30    12    *       *        sun         crontab -l &gt; $HOME/.crontab.backup</pre>
<p>Scripts run via cron should generally start like:</p>
<pre>#!/bin/bash<br>source /etc/profile &gt;/dev/null 2&gt;&amp;1</pre>
<p>That sets up the environment as if you had logged in, including the <em>module </em>command. Except that it doesn't use your <em>.bash_profile</em> or <em>.bashrc</em> files, so you need to source those too if you define anything you need in them.</p>
<p>For general instructions see:</p>
<pre>man crontab</pre>
<h2>Scron</h2>
<p dir="auto"><em>scrontab</em> is Slurm's analogue of <em>crontab</em>.  Rather than running directly on the login node it submits Slurm jobs at the scheduled times.  At present is is only available on Mahuika.  In general we think it is superior to cron, particularly if the job requires significant resources.  But it does also have it's own particular drawbacks:</p>
<ul>
<li dir="auto">It does not support the CRON_TZ setting, so all times (and dates) must be UTC ones.</li>
<li dir="auto">The exact start time of jobs is not be guaranteed as the jobs must still queue. However short, serial jobs usually start promptly, and if you need more certainty please ask us as we could arrange higher priority for <em>scron</em> jobs.</li>
</ul>
<p>Job options which would normally be given as #SBATCH directives are instead given as #SCRON directives directly in the <em>scrontab</em> file, eg:</p>
<pre><span>#SCRON -t 10<br>#SCRON -J my_weekly_scron_job<br># min<span class="Apple-converted-space">    </span>hr<span class="Apple-converted-space">    </span>dom <span class="Apple-converted-space">  </span>month<span class="Apple-converted-space">      </span>dow <span class="Apple-converted-space">        </span>command</span><br>   30    12    *       *        sun         bash /home/me/weekly_script.sh</pre>
<p>For general instructions see:</p>
<pre>man scrontab</pre>
<h2 dir="auto">Cylc</h2>
<p>Cylc is NIWA's system for running cylic workflows such as those used in weather forecasting. </p>