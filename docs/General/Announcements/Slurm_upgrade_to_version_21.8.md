::: {.p-rich_text_section}
Slurm, the scheduler that controls Māui and Mahuika, has been upgraded
to version 21.8 on machines.  Below are the highlights of the changes
expected in the new version. The full list of bugfixes, improvements and
changes is available on Schemd  website: [Slurm
news](https://slurm.schedmd.com/news.html)
:::

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}
:::

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}
:::

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}***squeue***
:::

-   Added `--me` option, equivalent to` --user=$USER`.
-   Added \"pendingtime\" as a option for \--Format.
-   Put sorted start times of \"N/A\" or 0 at the end of the list.

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}***sacct***
:::

-   Add time specification: \"now-\" (i.e. subtract from the present)
-   AllocGres and ReqGres were removed. Alloc/ReqTres should be used
    instead. 

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}***scontrol***
:::

-   MAGNETIC flag on reservations. Reservations the user doesn\'t have
    to even request.
-   The LicensesUsed line has been removed
    from[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}`scontrol show config`[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}[.
    Please use
    updated]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}`scontrol show licenses`[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}[command
    as an
    alternative.]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}***sbatch***\
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}
:::

-    `--threads-per-core` now influences task layout/binding, not just
    allocation.
-   `--gpus-per-node`[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}[can
    be used instead
    of]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}`--gres=GPU`
-   `--hint=nomultithread`[ can now be replaced
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}[with]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}`--threads-per-core=1`
-   The inconsistent terminology and environment variable naming for
    Heterogeneous Job (\"HetJob\") support has been tidied up.
-   The correct term for these jobs are \"HetJobs\", references to
    \"PackJob\"   have been corrected.
-   The correct term for the separate constituent jobs are
    \"components\",   references to \"packs\" have been corrected.

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}**salloc**
:::

-   Added support for an \"Interactive Step\", designed to be used with
    salloc to launch a terminal on an allocated compute node
    automatically. Enable by setting \"use\_interactive\_step\" as part
    of LaunchParameters.

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}***srun***
:::

-    By default, a step started with srun will be granted exclusive (or
    non- overlapping) access to the resources assigned to that step. No
    other parallel step will be allowed to run on the same resources at
    the same time. This replaces one facet of the \'\--exclusive\'
    option\'s behavior, but does not imply the \'\--exact\' option
    described below. To get the previous default behavior - which
    allowed parallel steps to share all resources - use the new srun
    \'\--overlap\' option.
-   In conjunction to this non-overlapping step allocation behavior
    being the new default, there is an additional new option for step
    management \'\--exact\', which will allow a step access to only
    those resources requested by the step. This is the second half of
    the \'\--exclusive\' behavior. Otherwise, by default all non-gres
    resources on each node in the allocation will be used by the step,
    making it so no other parallel step will have access to those
    resources unless both steps have specified \'\--overlap\'.

::: {.p-rich_text_section}
[]{.c-mrkdwn__br data-stringify-type="paragraph-break"}***scrontab***
:::

-   New command which permits crontab-compatible job scripts to be
    defined. These scripts will recur automatically (at most) on the
    intervals described.
