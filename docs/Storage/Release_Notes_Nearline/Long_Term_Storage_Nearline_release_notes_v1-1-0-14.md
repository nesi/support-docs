---
created_at: '2020-11-04T04:39:50Z'
hidden: false
position: 0
tags:
- releasenote
title: Long-Term Storage - Nearline release notes  v1.1.0.14
vote_count: 0
vote_sum: 0
zendesk_article_id: 360002113295
zendesk_section_id: 360000502675
---

## Version 1.1.0.14

*Released 5 November 2020.*

This release includes the following changes:

-   `nlls`, `nlget`, `nlpurge`, `nlput` and `nljobstatus` now come with
    a debug mode, accessible via the `--debug` command line switch.
-   Help documentation, as well as the usage message when a nearline
    command is run with incorrect arguments, has been improved.
-   `nljobstatus` now includes more comprehensive job status
    information. In particular, the job status message now includes a
    brief description of the stage the job is up to, and whether the job
    is at that moment pending (waiting in a queue to start the next
    operation), running, or complete.
-   The `nlls` command's `-ls` switch has been replaced with `-s`,
    though `-ls` still works, being interpreted as equivalent to
    `-l -s`. `nlls` also now comes with a `-b` switch, for reporting
    individual sizes in bytes instead of in human-readable sizes.
-   `nltraverse` has been improved, and now reports file sizes, and sums
    of file sizes, in bytes, for greater accuracy and ease of comparison
    with the output of `ls`.
-   There have been numerous other bug fixes to improve performance and
    reduce the risk of unexpected failures and errors.