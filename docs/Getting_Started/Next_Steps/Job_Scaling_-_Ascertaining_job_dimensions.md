---
created_at: '2019-01-31T01:17:22Z'
hidden: false
label_names:
- scaling
position: 6
title: Job Scaling - Ascertaining job dimensions
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000728016
zendesk_section_id: 360000189716
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p><span class="wysiwyg-color-black">When you run software in an interactive environment such as your ordinary workstation (desktop PC or laptop), the software is able to request from the operating system whatever resources it needs from moment to moment. By contrast, on our HPC platforms, you must request your needed resources <em>when you submit the job</em>, so that the scheduler can make sure enough resources are available for your job during the whole time it is running, and also knows what resources will be free for others to use at the same time.</span></p>
<p>The three resources that every single job submitted on the platforms needs to request are:</p>
<ul>
<li>CPUs (i.e. logical CPU cores), and</li>
<li>Memory (RAM), and</li>
<li>Time.</li>
</ul>
<p>Some jobs will also need to request GPUs.</p>
<h1>What happens if I ask for the wrong resources?</h1>
<p>When you are initially trying to set up your jobs it can be difficult to ascertain how much of each of these resources you will need. Asking for too little or too much, however, can both cause problems: your jobs will be at increased risk of taking a long time in the queue or failing, and your project's <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000743536" target="_self">fair share score</a> is likely to suffer.  Y<span class="wysiwyg-color-black">our project's fair share score will be reduced in view of compute time spent regardless of whether you obtain a result or not.</span> </p>
<table style="width: 646px;">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 60px;"><strong>Resource</strong></td>
<td class="wysiwyg-text-align-center" style="width: 287px;"><strong>Asking for too much</strong></td>
<td class="wysiwyg-text-align-center" style="width: 293px;"><strong>Not asking for enough</strong></td>
</tr>
<tr>
<td style="width: 60px;">Number of CPUs</td>
<td style="width: 287px;">
<ul>
<li>The job may wait in the queue for longer.</li>
<li>Your fair share score will <span class="wysiwyg-color-black">fall rapidly (your project will be charged for CPU cores that it reserved but didn't use)</span>
</li>
</ul>
</td>
<td style="width: 293px;">
<ul>
<li>The job will run more slowly than expected, and so may run out of time and get killed for exceeding its time limit.</li>
</ul>
</td>
</tr>
<tr>
<td style="width: 60px;">Memory</td>
<td style="width: 287px;">
<ul>
<li>The job may wait in the queue for longer.</li>
<li>Your fair share score will fall more than necessary.</li>
</ul>
</td>
<td style="width: 293px;">
<ul>
<li>Your job will fail, probably with an 'OUT OF MEMORY' error, segmentation fault or bus error. This may not happen immediately.</li>
</ul>
</td>
</tr>
<tr>
<td style="width: 60px;">Wall time</td>
<td style="width: 287px;">
<ul>
<li>The job may wait in the queue for longer than necessary</li>
</ul>
</td>
<td style="width: 293px;">
<ul>
<li>The job will run out of time and get killed. </li>
</ul>
</td>
</tr>
</tbody>
</table>
<p><strong><em>See our <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001385735" target="_self">"What is an allocation?" support page</a> for more details on how each resource effects your compute usage.</em></strong></p>
<p>It is therefore important to try and make your jobs resource requests reasonably accurate. In this article we <span class="wysiwyg-color-black">will discuss how you can scale your jobs to help you better estimate your jobs resource needs.</span></p>
<h1>Job Scaling</h1>
<p>Before you start submitting the main bulk of your jobs, it is <span class="SDZsVb" tabindex="0" data-term-for-update="advisable" data-ved="2ahUKEwj-0-zoj-fhAhXCfX0KHYH_DJYQ_SowAHoECAwQDA">advisable to first submit a <em>test job</em>. </span></p>
<p><span class="SDZsVb" tabindex="0" data-term-for-update="advisable" data-ved="2ahUKEwj-0-zoj-fhAhXCfX0KHYH_DJYQ_SowAHoECAwQDA">A test job should be representative of the main body of your work, scaled down (e.g. a small subset of your data or a low number of job steps). Aim for your test job to run for around 10 minutes, too much shorter and your job will be spending a high proportion of its time on overhead and therefore be less accurate for the purposes of scaling.</span></p>
<p><span class="SDZsVb" tabindex="0" data-term-for-update="advisable" data-ved="2ahUKEwj-0-zoj-fhAhXCfX0KHYH_DJYQ_SowAHoECAwQDA">Keeping your test job small ensures a short queue time, short run time and that minimal resources are expended.</span></p>
<p><span class="wysiwyg-color-black">When scaling your jobs, one of the most beneficial things you can do is to first scale down your data and calculations to as small as you can. Whether this means only computing on a few rows and columns of your data, or only doing a subset of the calculations you intend to do in the complete jobs, cutting your initial test jobs down in size means that they will both queue faster and run for less time. Also, if one of these jobs fails due to not asking for enough resources, a small scale job will (hopefully) not have waited for hours or days in the queue beforehand.</span></p>
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Examples</h3>
<p><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001173895" target="_blank" rel="noopener">Multithreading Scaling</a></p>
<p><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001173875" target="_blank" rel="noopener">MPI Scaling</a></p>
</blockquote>