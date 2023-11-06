---
created_at: '2019-11-11T21:40:21Z'
hidden: false
label_names: []
position: 0
title: "Mahuika - M\u0101ui Differences"
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001244876
zendesk_section_id: 360000039036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>Aside from differences in software stack there are a few other differences between the platforms to be aware of.</p>
<h1>Logging in</h1>
<p>Both Mahuika and Māui require logging in to the Lander node first.</p>
<pre><code>ssh user123@lander.nesi.org.nz</code></pre>
<p>As you log in to the Lander node, you can expect to receive the following prompts:</p>
<pre><code>Login Password (First Factor):</code></pre>
<pre><code>Authenticator Code (Second Factor):</code></pre>
<p>Note that being prompted for <code>Authenticator Code (Second Factor)</code> does not prove that the system has accepted your <code>Login Password (First Factor)</code> as correct. If you enter either incorrectly, you will be prompted again for both.</p>
<h2>Mahuika</h2>
<p>Mahuika follows the same procedure as the lander node, except that it doesn't ask for a second factor.</p>
<pre><code>ssh login.mahuika.nesi.org.nz</code></pre>
<p>You will be prompted:</p>
<pre><code>Login Password:</code></pre>
<p>At this prompt, enter only your password (a.k.a. first factor).</p>
<h2>Māui</h2>
<p>Maui differs slightly in how you are authenticated the first time.</p>
<pre><code>ssh login.maui.nesi.org.nz</code></pre>
<p>You will be prompted.</p>
<pre><code>Password:</code></pre>
<p>At this prompt, enter only your password (a.k.a. first factor).</p>
<h1>Job Limits</h1>
<p>Both Maui and Mahuika have limits on the size and types of jobs you can run, but the limits on each machine is different.</p>
<h2>Mahuika</h2>
<p>Mahuika is made up of several <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000204076" target="_self">partitions which have different resources and different limits</a>. A job can request up to 20,000 CPU core hours, running up to 3 weeks with up to 576 CPU cores (equivalent to eight full nodes). Furthermore, there are special nodes available with high memory (up to 6 TB) or GPUs. Depending on what resources you are requesting and for how long, your jobs will be automatically assigned to the most suitable partition. Mahuika allows the submission of jobs with variable numbers of CPUs and amounts of RAM (memory). The nodes your job is running on will probably be shared with other jobs.</p>
<h2>Māui</h2>
<p>Māui only has a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000204116" target="_self">single partition to which NeSI users are permitted to submit work</a>. For your job, you can request a maximum of 24 hours or a maximum of 240 nodes, however no job may request more than 1,200 Māui node-hours in total. (This means that if you request more than 50 nodes, your maximum allowed time will start decreasing.) Māui only allows submission of jobs in units of nodes, so the smallest possible job takes a whole node, and there can never be more than one job on a node at a time.</p>
<p>Additionally, projects with valid allocations on Māui will also have access to <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000203776" target="_self">Maui's ancilliary nodes,</a> where jobs requiring up to 768 GB of memory or jobs that require GPUs can be run. When submitting a job to the Māui ancillary nodes you may also request parts of nodes, rather than needing to use the entire node. Because there are relatively few Māui ancillary nodes, if you require substantial amounts of time on nodes like the Māui ancillary nodes, we may grant your project an additional allocation on Mahuika. If we do so, we will not forbid you from using the Māui ancillary nodes while your Māui allocation remains valid and you are permitted to access NeSI clusters.</p>