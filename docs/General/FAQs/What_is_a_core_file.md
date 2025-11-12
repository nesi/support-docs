---
created_at: '2020-06-25T01:10:40Z'
tags:
- corefile
- troubleshooting
description: Explanation of .core files
---

`.core` files are created when a program fails in a way that can't be
handled by the program's regular error handling.

Your application may crash with an error like, `Segmentation fault (core dumped)`.

These failures are memory-related, such as the program asking for more memory than allocated or
for memory it can't legally access.
Your first step in troubleshooting should be checking if this is the case,
see [Finding Job_Efficiency](../../Getting_Started/Next_Steps/Finding_Job_Efficiency.md)

`.core` files are a record of the working memory at time of failure, and
can be used for
[debugging](../../Scientific_Computing/Profiling_and_Debugging/Debugging.md).
MPI jobs will usually create a `.core` file for each task.

The creation of a `.core` file is called a 'core dump' is files is **disabled by default**,

You can enable the creation of core dumps with `ulimit -c unlimited`.

As `.core` files are large, you should delete the ones you
don't plan on using them to avoid filling up your storage quota.
