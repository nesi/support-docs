---
created_at: '2020-06-25T01:10:40Z'
hidden: false
label_names:
- corefile
- coredump
position: 0
title: What is a '.core' file?
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001584875
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>.core files are created when a program fails in a way that can't be handled by the program's regular error handling. Normally these failures are memory-related, such as the program asking for too much memory or for memory it can't legally access. The creation of a core file is called a 'core dump'.</p>
<p>.core files are a record of the working memory at time of failure, and can be used for <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001008136" target="_self">debugging</a>. MPI jobs will usually create a .core file for each task.</p>
<p>As .core files are usually very large, you should delete the ones you don't plan on using them to avoid filling up your storage quota.</p>