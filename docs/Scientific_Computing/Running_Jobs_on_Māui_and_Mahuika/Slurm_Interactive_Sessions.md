---
created_at: '2020-01-05T21:43:18Z'
hidden: false
label_names: []
position: 5
title: Slurm Interactive Sessions
vote_count: 6
vote_sum: 2
zendesk_article_id: 360001316356
zendesk_section_id: 360000030876
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>A SLURM interactive session reserves resources on compute nodes allowing you to use them interactively as you would the login node.</p>
<p>There are two main commands that can be used to make a session, <code>srun</code> and <code>salloc</code>, both of which use most of the same options available to <code>sbatch</code> (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000691716" target="_self">our Slurm Reference Sheet</a>). </p>
<blockquote class="blockquote-warning">
<h3 id="salloc-time">Warning</h3>
<p>An interactive session will, once it starts, use the entire requested block of CPU time and other resources unless earlier exited from, even if unused. To avoid unnecessary charges to your project, don't forget to exit an interactive session once finished.</p>
</blockquote>
<h2>Using 'srun --pty bash'</h2>
<p><code>srun</code> will add your resource request to the queue. When the allocation starts, a new bash session will start up on <strong>one of the granted nodes.</strong></p>
<p>For example;</p>
<pre><code>srun --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 8 --mem-per-cpu 1500 --time 24:00:00 --pty bash</code></pre>
<p> You will receive a message.</p>
<pre><samp>srun: job 10256812 queued and waiting for resources</samp></pre>
<p>And when the job starts:</p>
<pre><samp>srun: job 10256812 has been allocated resources
[wbn079 ~ SUCCESS ]$</samp></pre>
<p>Note the host name in the prompt has changed to the compute node <code>wbn079</code>.</p>
<p>For a full description of <code>srun</code> and its options, see <a href="https://slurm.schedmd.com/srun.html" target="_self">here</a>.</p>
<h2>Using 'salloc'</h2>
<p><code>salloc</code> functions similarly <code>srun --pty bash</code> in that it will add your resource request to the queue. However the allocation starts, a new bash session will start up on <strong>the login node. </strong>This is useful for running a GUI on the login node, but your processes on the compute nodes.</p>
<p>For example:</p>
<pre><code>salloc --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 8 --mem-per-cpu 1500 --time 24:00:00</code></pre>
<p> You will receive a message.</p>
<pre>salloc: Pending job allocation 10256925<br>salloc: job 10256925 queued and waiting for resources</pre>
<p>And when the job starts;</p>
<pre><samp>salloc: job 10256925 has been allocated resources<br>salloc: Granted job allocation 10256925 
[mahuika01~ SUCCESS ]$</samp></pre>
<p>Note the that you are still on the login node <code>mahuika01</code>, however you will now have permission to <code>ssh</code> to any node you have a session on .</p>
<p>For a full description of <code>srun</code> and its options, see <a href="https://slurm.schedmd.com/salloc.html" target="_self">here</a>.</p>
<h3>Requesting a postponed start</h3>
<p><code>salloc</code> lets you specify that a job is not to start before a specified time, however the job may still be delayed if requested resources are not available. You can request a start time using the <code>--begin</code> flag.</p>
<p>The <code>--begin</code> flag takes either absolute or relative times as values.</p>
<blockquote class="blockquote-warning">
<h3 id="timezone">Warning</h3>
<p>If you specify absolute dates and/or times, Slurm will interpret those according to your environment's current time zone. Ensure that you know what time zone your environment is using, for example by running <code>date</code> in the same terminal session.</p>
</blockquote>
<ul>
<li>
<code>--begin=16:00</code> means start the job no earlier than 4 p.m. today. (Seconds are optional, but the time must be given in 24-hour format.)</li>
<li>
<code>--begin=11/05/20</code> means start the job on (or after) 5 November 2020. Note that Slurm uses American date formats. <code>--begin=2020-11-05</code> is another Slurm-acceptable way of saying the same thing, and possibly easier for a New Zealander.</li>
<li>
<code>--begin=2020-11-05T16:00:00</code> means start the job on (or after) 4 p.m. on 5 November 2020.</li>
<li>
<code>--begin=now+1hour</code> means wait at least one hour before starting the job.</li>
<li>
<code>--begin=now+60</code> means wait at least one minute before starting the job.</li>
</ul>
<p>If no <code>--begin</code> argument is given, the default behaviour is to start as soon as possible.</p>
<h3>While you wait</h3>
<p>It's quite common to have to wait for some time before your interactive session starts, even if you specified, expressly or by implication, that the job is to start as soon as possible.</p>
<p>While you're waiting, you will not have use of that shell prompt. <strong>Do not use <code>Ctrl</code>-<code>C</code> to get the prompt back, as doing so will cancel the job.</strong> If you need a shell prompt, detach your <code>tmux</code> or <code>screen</code> session, or switch to (or open) another terminal session to the same cluster's login node.</p>
<p>In the same way, before logging out (for example, if you choose to shut down your workstation at the end of the working day), be sure to detach the <code>tmux</code> or <code>screen</code> session. In fact, we recommend detaching whenever you leave your workstation unattended for a while, in case your computer turns off or goes to sleep or its connection to the internet is disrupted while you're away.</p>
<p> </p>
<h2>Setting up a detachable terminal</h2>
<blockquote class="blockquote-warning">
<h3 id="detach-warning">Warning</h3>
<p>If you don't request your interactive session from within a detachable terminal, any interruption to the controlling terminal, for example by your computer going to sleep or losing its connection to the internet, will permanently cancel that interactive session and remove it from the queue, whether it has started or not.</p>
</blockquote>
<ol>
<li>Log in to a Mahuika, Māui or Māui-ancil login node.</li>
<li>Start up <code>tmux</code> or <code>screen</code>.</li>
</ol>
<h2>Modifying an existing interactive session</h2>
<p>Whether your interactive session is already running or is still waiting in the queue, you can make a range of changes to it using the <code>scontrol</code> command. Some changes are off limits for ordinary users, such as increasing the maximum permitted wall time, or unsafe, like decreasing the memory request. But many other changes are allowed.</p>
<h3>Postponing the start of an interactive job</h3>
<p>Suppose you submitted an interactive job just after lunch, and it's already 4 p.m. and you're leaving in an hour. You decide that even if the job starts now, you won't have time to do everything you need to do before the office shuts and you have to leave. Even worse, the job might start at 11 p.m. after you've gone to bed, and you'll get to work at 9:00 the next morning and find that it has wasted ten wall-hours of time.</p>
<p>Slurm offers an easy solution: Identify the job, and use <code>scontrol</code> to postpone its start time.</p>
<blockquote class="blockquote-tip">
<h3 id="multicluster-scontrol">Note</h3>
<p>Job IDs are unique to each cluster but not across the whole of NeSI. Therefore, <code>scontrol</code> must be run on a node belonging to the cluster where the job is queued.</p>
</blockquote>
<p>The following command will delay the start of the job with numeric ID 12345678 until (at the earliest) 9:30 a.m. the next day:</p>
<pre><code>scontrol update jobid=12345678 StartTime=tomorrowT09:30:00</code></pre>
<p>This variation, if run on a Friday, will delay the start of the same job until (at the earliest) 9:30 a.m. on Monday:</p>
<pre><code>scontrol update jobid=12345678 StartTime=now+3daysT09:30:00</code></pre>
<blockquote class="blockquote-warning">
<h3 id="tomorrow">Warning</h3>
<p>Don't just set <code>StartTime=tomorrow</code> with no time specification unless you like the idea of your interactive session starting at midnight or in the wee small hours of the morning.</p>
</blockquote>
<h3>Bringing forward the start of an interactive job</h3>
<p>In the same way, you can use scontrol to set a job's start time to earlier than its current value. A likely application is to allow a job to start immediately even though it stood postponed to a later time:</p>
<pre><code>scontrol update jobid=12345678 StartTime=now</code></pre>
<h3>Other changes using <code>scontrol</code>
</h3>
<p>There are many other changes you can make by means of <code>scontrol</code>. For further information, please see <a href="https://slurm.schedmd.com/scontrol.html" target="_self">the <code>scontrol</code> documentation</a> (off site).</p>
<h2>Modifying multiple interactive sessions at once</h2>
<p>In the same way, if you have several interactive sessions waiting to start on the same cluster, you might want to postpone them all using a single command. To do so, you will first need to identify them, hence the earlier suggestion to something specific to interactive jobs in the job name.</p>
<p>For example, if all your interactive job names start with the text "IJ", you could do this:</p>
<pre><code># -u $(whoami) restricts the search to my jobs only.
# The --states=PD option restricts the search to pending jobs only.
#
# Each &lt;tab&gt; string should be replaced with a literal tab character. If you
# can't insert one by pressing the tab key on your keyboard, you should be
# able to insert one by pressing Ctrl-V followed immediately by Ctrl-I.
#
squeue -u $(whoami) --states=PD -o "%A&lt;tab&gt;%j" | grep "&lt;tab&gt;IJ"</code></pre>
<p>The above command will return a list of your jobs whose names <em>start</em> with the text "IJ". In this respect, it's more flexible than the <code>-n</code> option to <code>squeue</code>, which requires the entire job name string in order to identify a match.</p>
<p>In order to use <code>scontrol</code>, we need to throw away all of the line except for the job ID, so let's use <code>awk</code> to do this, and send the output to <code>scontrol</code> via <code>xargs</code>:</p>
<pre><code>squeue -u $(whoami) --states=PD -o "%A&lt;tab&gt;%j" | grep "&lt;tab&gt;IJ" | \
awk '{print $1}' | \
xargs -I {} scontrol update jobid={} StartTime=tomorrowT09:30:00</code></pre>
<p>If you want to do this automatically every working day and you have a consistent element that you use in the name of all your interactive jobs, you can set up cron jobs on Māui, Mahuika and/or Māui-ancil login nodes. This is left as an exercise for the reader, having regard to the following:</p>
<ul>
<li>
<strong>Time zone:</strong> Even if your environment is set up to use a different time zone (commonly New Zealand time, which adjusts for daylight saving as needed), time schedules in the crontab itself are interpreted in UTC. So if you want something to run at 4:30 p.m. New Zealand time regardless of the time of year, the cron job will need to run at 4:30 a.m. UTC (during winter) or 3:30 a.m. UTC (during summer), and you will need to edit the crontab every six months or so.</li>
<li>
<strong>Weekends:</strong> If you just have a single cron job that postpones pending interactive jobs until the next day, interactive jobs pending on a Friday afternoon will be postponed until Saturday morning, which is probably not what you want. Either your cron job detects the fact of a Friday and postpones jobs until Monday, or you have two cron jobs, one that runs on Mondays to Thursdays, and a different cron job running on Fridays.</li>
</ul>
<h2>Cancelling an interactive session</h2>
<p>You can cancel a pending interactive session by attaching the relevant session, putting the job in the foreground (if necessary) and pressing <code>Ctrl</code>-<code>C</code> on your keyboard.</p>
<p>To cancel all your queued interactive sessions on a cluster in one fell swoop, a command like the following should do the trick:</p>
<pre><code>squeue -u $(whoami) --states=PD -o "%A&lt;tab&gt;%j" | grep "&lt;tab&gt;IJ" | \
awk '{print $1}' | \
xargs -I {} scancel {}</code></pre>
<p>If you frequently use interactive jobs, we recommend doing this before you go away on leave or fieldwork or other lengthy absence.</p>