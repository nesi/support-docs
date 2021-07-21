Our systems have returned to normal service and availability after a
scheduled maintenance outage. We appreciate your patience and
understanding during these activities. As always, if you have any
related questions, please don't hesitate to contact [NeSI
Support](https://support.nesi.org.nz/hc/en-gb/articles/360000748496-User-support).

The following is a (non-exhaustive) list of changes/updates made during
and between the System Maintenance outages on 6/11/2019 and
[24/02/2020](https://status.nesi.org.nz/incidents/5yvnqfvrn87n).

**Job submission (Slurm) changes on Mahuika and Māui Ancil.**

-   There is no longer any need to specify `--partition` yourself on
    Mahuika and in general we recommend that you don\'t. A job
    submit-time plugin has been added which selects a sensible default
    partition depending on the job\'s resource requests. It also issues
    a warning if you override it with an unsuitable partition
    (see [Mahuika Slurm
    Partitions](https://support.nesi.org.nz/hc/en-gb/articles/360000204076))
-   Fairshare settings have been changed so that the impact of a job on
    your fairshare score is the same regardless of which partition it
    runs on (see [Fair
    Share](https://support.nesi.org.nz/hc/en-gb/articles/360000743536)).
-   It is now possible to run an interactive X11 job via
    `srun --x11 ...` (see [X11 on
    NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001075975)).
-   It is possible to submit jobs with \> 36 threads (i.e. more than
    half a node) in one task.
-   The \"\--workdir\" option is now \"\--chdir\".
-   You can now ssh into compute nodes on which you have a job running.
    Any resulting resource usage will be tracked by Slurm, and thus
    visible via s*acct* in the special *extern* task.

**Software**

-   Singularity is now available on Māui Ancil (see
    [Singularity](https://support.nesi.org.nz/hc/en-gb/articles/360001107916)).
-   Default version bumps for Mahuika environment modules including:
    [ABAQUS](https://support.nesi.org.nz/hc/en-gb/articles/212457807),
    [BLASTDB](https://support.nesi.org.nz/hc/en-gb/articles/208619807),
    gimkl (i.e. GCC and Intel\'s MPI & MKL),
    [OpenFOAM](https://support.nesi.org.nz/hc/en-gb/articles/360000810556),
    [Python](https://support.nesi.org.nz/hc/en-gb/articles/207782537),
    and [R](https://support.nesi.org.nz/hc/en-gb/articles/209338087).

**Systems/Datacentre**

-   Critical cooling plant updates were completed.
-   Various firmware and OS level security updates have been applied.

 

***Additional Background***\
NeSI regularly performs scheduled maintenance on various components of
its high performance computers (HPCs) to ensure robust and performant
operations. Whenever possible, such works are carried out during regular
operations in order to minimise user impact, however some more intrusive
maintenance activities simply cannot be done without taking critical
shared services offline (e.g., high performance filesystems) or must be
done consistently across all systems as quickly as possible. Therefore,
we must have occasional planned outages were no user activity is
possible on the HPCs.

Whenever scheduled maintenance is required, particularly if it requires
critical shared services to be taken offline, we will endeavour to
notify users in advance and post a status update
to [status.nesi.org.nz.](https://status.nesi.org.nz/) From that status
page, users can subscribe to receive system-specific or all status
updates.

If you have questions about these maintenance and outage processes,
please contact [NeSI Support](mailto:support@nesi.org.nz).
