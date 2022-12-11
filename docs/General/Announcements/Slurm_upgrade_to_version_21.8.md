Slurm, the scheduler that controls Māui and Mahuika, has been upgraded
to version 21.8 on machines.  Below are the highlights of the changes
expected in the new version. The full list of bugfixes, improvements and
changes is available on Schemd  website: [Slurm
news](https://slurm.schedmd.com/news.html)

<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span>

<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span>

<span class="c-mrkdwn__br"
data-stringify-type="paragraph-break"></span>***squeue***

-   Added `--me` option, equivalent to` --user=$USER`.
-   Added "pendingtime" as a option for --Format.
-   Put sorted start times of "N/A" or 0 at the end of the list.

<span class="c-mrkdwn__br"
data-stringify-type="paragraph-break"></span>***sacct***

-   Add time specification: "now-" (i.e. subtract from the present)
-   AllocGres and ReqGres were removed. Alloc/ReqTres should be used
    instead. 

<span class="c-mrkdwn__br"
data-stringify-type="paragraph-break"></span>***scontrol***

-   MAGNETIC flag on reservations. Reservations the user doesn't have to
    even request.
-   The LicensesUsed line has been removed from<span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span>`scontrol show config`<span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">.
    Please use updated</span><span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span>`scontrol show licenses`<span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">command
    as an alternative.</span>

<span class="c-mrkdwn__br"
data-stringify-type="paragraph-break"></span>***sbatch***  
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span>

-    `--threads-per-core` now influences task layout/binding, not just
    allocation.
-   `--gpus-per-node`<span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">can
    be used instead of</span><span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span>`--gres=GPU`
-   `--hint=nomultithread`<span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">
    can now be replaced </span><span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">with</span><span
    style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span>`--threads-per-core=1`
-   The inconsistent terminology and environment variable naming for
    Heterogeneous Job ("HetJob") support has been tidied up.
-   The correct term for these jobs are "HetJobs", references to
    "PackJob"   have been corrected.
-   The correct term for the separate constituent jobs are
    "components",   references to "packs" have been corrected.

<span class="c-mrkdwn__br"
data-stringify-type="paragraph-break"></span>**salloc**

-   Added support for an "Interactive Step", designed to be used with
    salloc to launch a terminal on an allocated compute node
    automatically. Enable by setting "use\_interactive\_step" as part of
    LaunchParameters.

<span class="c-mrkdwn__br"
data-stringify-type="paragraph-break"></span>***srun***

-    By default, a step started with srun will be granted exclusive (or
    non- overlapping) access to the resources assigned to that step. No
    other parallel step will be allowed to run on the same resources at
    the same time. This replaces one facet of the '--exclusive' option's
    behavior, but does not imply the '--exact' option described below.
    To get the previous default behavior - which allowed parallel steps
    to share all resources - use the new srun '--overlap' option.
-   In conjunction to this non-overlapping step allocation behavior
    being the new default, there is an additional new option for step
    management '--exact', which will allow a step access to only those
    resources requested by the step. This is the second half of the
    '--exclusive' behavior. Otherwise, by default all non-gres resources
    on each node in the allocation will be used by the step, making it
    so no other parallel step will have access to those resources unless
    both steps have specified '--overlap'.

<span class="c-mrkdwn__br"
data-stringify-type="paragraph-break"></span>***scrontab***

-   New command which permits crontab-compatible job scripts to be
    defined. These scripts will recur automatically (at most) on the
    intervals described.
