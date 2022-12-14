---
created_at: '2019-11-08T01:42:08Z'
hidden: false
label_names:
- storage
- data
position: 17
title: Important changes to storing data on NeSI - expiry of data on 'nobackup' filesystem
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001239435
zendesk_section_id: 200732737
---

<span class="wysiwyg-font-size-small">This announcement is an updated
version of the email we sent to all active users on 8th November
2019.</span>

<span class="wysiwyg-font-size-small">---</span>

From **26 November 2019** we will take next steps to implement <span
class="il">data</span> <span class="il">expiry</span> and automated
deletion to optimise the availability of the highest performance storage
on our HPC platform -- **/<span
class="il">nesi</span>/nobackup/** storage, a.k.a the “nobackup”
filesystem.

**What does this mean?**  
Project directories in **/<span class="il">nesi</span>/nobackup/** (e.g.
/<span class="il">nesi</span>/nobackup/nesi12345/) are intended
for *active* <span class="il">data</span> that needs to be accessed and
stored by your HPC compute and analytics jobs or associated interactive
processing. All NeSI projects also have a persistent project directory
in **/nesi/project/** which is available for the life of the project on
NeSI.

Later this month, we will begin rolling out a new <span
class="il">data</span> <span class="il">expiry</span> feature to
remove *inactive* research <span class="il">data</span> from **/<span
class="il">nesi</span>/nobackup/** - <span class="il">data</span> which
hasn’t been accessed or modified within the last 120 days, stored in a
nobackup project directory that takes up at least 1 TB of disk space.  
<span class="il">NeSI</span> Support has information and instructions
here: [Automatic cleaning of nobackup file
system](https://support.nesi.org.nz/hc/en-gb/articles/360001162856)

**How does this affect me?**  
Starting on 26 November, we will begin to roll out <span
class="il">data</span> <span class="il">expiry</span> and automated
deletion. This process carries through to late January 2020.  
  
We will successively identify and work with a subset of project teams to
implement <span class="il">data</span> <span
class="il">expiry</span> and automated deletion on all
associated **/<span class="il">nesi</span>/nobackup/&lt;project
code&gt;/** directories.  
  
We will contact each project team directly when this is being
implemented on their project directories, and any files about to <span
class="il">expire</span> will be notified 2 weeks prior to actual
deletions taking place. More information is available on <span
class="il">NeSI</span> Support: [Automatic cleaning of nobackup file
system](https://support.nesi.org.nz/hc/en-gb/articles/360001162856)

Look out for further updates as this rollout progresses.  
  
If you have any questions, please [contact our support
team](https://support.nesi.org.nz/hc/requests/new).  
  
Kind regards,  
The <span class="il">NeSI</span> Team
