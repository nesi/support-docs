---
created_at: '2018-09-20T23:52:07Z'
hidden: false
label_names: []
position: 0
title: Can I change my time zone to New Zealand time?
vote_count: 6
vote_sum: -4
zendesk_article_id: 360000473256
zendesk_section_id: 360000039036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>The time displayed in your shell is controlled by a system variable called <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">TZ</code>. To change to New Zealand time you need to set the variable as follows:</p>
<pre><code>export TZ="NZ"</code></pre>
<p>This setting will automatically adjust for daylight saving, since the <code>tzdata</code> package is installed at the system level. Our system engineers will keep the <code>tzdata</code> package up to date.</p>
<h2>Making the change persistent</h2>
<p>You can make your time zone setting persistent by adding the above line to your <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">~/.bashrc</code>. If you do this, we recommend adding the following line to your <code>~/.bash_profile</code>, or to your <code>~/.profile</code> if you have the latter but not the former:</p>
<pre><code>test -r ~/.bashrc &amp;&amp; . ~/.bashrc</code></pre>
<p>Please see the article, "<a href="https://support.nesi.org.nz/hc/en-gb/articles/360001194536" target="_self">.bashrc or .bash_profile?</a>" for more information.</p>
<h2>What about cron jobs?</h2>
<p>To have the specifications in your crontab file interpreted as NZ times start it with:</p>
<pre>CRON_TZ=NZ</pre>
<p>Also note that cron does not source either <code>~/.bashrc</code> or <code>~/.bash_profile</code>, so most environment variables will not be set, including TZ.</p>