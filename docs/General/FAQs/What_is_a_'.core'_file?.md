.core files are created when a program fails in a way that can't be
handled by the program's regular error handling. Normally these failures
are memory-related, such as the program asking for too much memory or
for memory it can't legally access. The creation of a core file is
called a 'core dump'.

.core files are a record of the working memory at time of failure, and
can be used for
[debugging](https://support.nesi.org.nz/hc/en-gb/articles/360001008136).
MPI jobs will usually create a .core file for each task.

As .core files are usually very large, you should delete the ones you
don't plan on using them to avoid filling up your storage quota.
