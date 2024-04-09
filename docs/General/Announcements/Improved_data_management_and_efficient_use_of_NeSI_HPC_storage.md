---
created_at: '2021-09-30T22:51:02Z'
tags: []
title: Improved data management & efficient use of NeSI HPC storage
vote_count: 0
vote_sum: 0
zendesk_article_id: 4407274387599
zendesk_section_id: 200732737
---
A growing number of research projects are storing large amounts of data
on NeSI systems. To better support this growth, as well as optimise the
performance and availability of our filesystems, we are introducing new
data management policies and best practices for our HPC facilities.

By adopting these measures to regularly audit, clean and manage the
amount of data on our filesystems, we’ll ensure they remain
high-performing and responsive to your research computing workloads and
data science workflows.  

## Upcoming changes to data management processes for project directories

### 4-15 October 2021

The NeSI project filesystem is becoming critically full, however it is
currently storing a large amount of dormant data that has not been
accessed for more than 12 months. We need your help to free up space on
the project filesystem as soon as possible. Please review the data you
are currently storing in any  `/nesi/project/` directories and **delete
or relocate** any files that are no longer required for ongoing
computational and/or analytics work on NeSI.

We have started regular audits of data stored in project folders, using
the same format as our nobackup auto cleaning ([described
here](../../Storage/File_Systems_and_Quotas/Automatic_cleaning_of_nobackup_file_system.md)).
See the file
`/nesi/project/<project_code>/.policy.test/scan485/latest.summary.txt`
for a summary of the number and size of files within each project that
have not been accessed for more than 485 days (this is ~15 months, and
is the draft auto cleaning timeframe under consideration for the project
filesystem).

If you need assistance with this, {% include "partials/support_request.html" %} and
we’d be happy to help or answer questions.

If you have data that may be used again on NeSI later, {% include "partials/support_request.html" %}
and we will consider whether a
[Nearline](https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service)
storage allocation would be appropriate to manage this.

### 18 October 2021

We will begin a limited roll-out of a new feature to automatically
identify inactive files in  `/nesi/project/` directories and schedule
them for deletion. Generally, we will be looking to identify files that
are inactive / untouched for more than 12 months.

A selection of active projects will be invited to participate in this
first phase of the programme. If you would like to volunteer to be an
early tester / participant, please {% include "partials/support_request.html" %}.
Otherwise, we will be in touch with projects directly to onboard them.

Insights from this initial phase will inform the criteria and processes
of the programme prior to it being released to the broader user
community.

Alongside this work, we will also adopt a new policy on how long
inactive data may be stored on NeSI systems, particularly once a
research project itself becomes inactive.

### January 2022

Starting in January 2022, we will expand the `/nesi/project/` directory
data management programme to include all active projects on NeSI.
Additional Support documentation and user information sessions will be
hosted prior to wider implementation, to provide advance notice of the
change and to answer any questions you may have around data lifecycle
management.

## Frequently asked questions

### Why are you introducing these new data management processes?

We want to avoid our online filesystems reaching critically full
levels, as that impacts their performance and availability for users. We
also want to ensure our active storage filesystems aren't being used to
store inactive data. This new data management feature
for `/nesi/project/` directories will complement our existing programme
of [automatic cleaning of the /nobackup file system](../../Storage/File_Systems_and_Quotas/Automatic_cleaning_of_nobackup_file_system.md).

### Can I check how much storage I’m currently using on NeSI systems?

You can query your actual usage and disk allocations at any time using
the following command:

`nn_storage_quota`

The values for `nn_storage_quota` are updated approximately every hour
and cached between updates.

### Can I recover data that I accidentally delete from my `/project` directory?

Perhaps. We regularly make read-only copies of the file system and save
them for up to seven days. For more information, 
[refer to our File Recovery page](../../Storage/Data_Recovery/File_Recovery.md "https://support.nesi.org.nz/hc/en-gb/articles/360000207315-File-Recovery").

### Where should I store my data on NeSI systems?

| Access Frequency |  Modifying Frequency | Recommended option |
| -- | -- | -- |
| Often  | Often | `nobackup` |
| Often | Seldom | `project` |
| Seldom | Seldom | `nearline` |

In general, the **project directory** should be used for reference data,
tools, and job submission and management scripts. The **nobackup
directory** should be used for holding large reference working datasets
(e.g., an extraction of compressed input data) and as a destination for
writing and modifying temporary data. The nobackup directory can also be
used to build and edit code, provided that the code is under version
control and changes are regularly checked into upstream revision control
systems. The **long-term storage service** should be used for larger
datasets that you only access occasionally and do not need to change in
situ.

### What should I do if I run out of storage space?

There are two tracked resources in the NeSI filesystem, *disk
space* and *inodes (number of files)*. If you run into problems with
either of these, [refer to this Support page for more
information](../../General/FAQs/Ive_run_out_of_storage_space.md "https://support.nesi.org.nz/hc/en-gb/articles/360001125996-I-ve-run-out-of-storage-space").

### I have questions that aren’t covered here. Who can I talk to?

{% include "partials/support_request.html" %}.
No question is too big or small and our intention is always to work with
you to find the best way to manage your research data.

## More information

This page will continue to be updated in the coming months with more
information. If you have questions at any time, don’t hesitate to
contact Support {% include "partials/support_request.html" %}.
