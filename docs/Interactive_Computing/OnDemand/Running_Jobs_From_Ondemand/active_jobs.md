# Viewing Active Jobs: `Active Jobs`

The `Active Jobs` section allows you to see what jobs are running. This section queries `squeue` and `scontrol` and reports information from these slurm command to this dashboard.

![Main face of Active Jobs](../../../assets/images/Jobs_OnDemand_2.png)

There are two buttons of interest:

1. The Information Button: Show you more information about that specific job.
2. The Status Icon: Tells you what state your job is in (such as `Queued`, `Running`, and `Completed`).
3. The Trash Button: Allow you to cancel a specific job.

## The Information Button

Clicking this button will allow you to see more information about this job:

![Information on this Job](../../../assets/images/Jobs_OnDemand_3.png)

This information tab contains three further buttons at the bottom left hand of the tab:

1. The File Manager: Clicking this button will take you to the directory of your job on Mahuika OnDemand. In here, you will find your output files for your job. You can view text files from here, including `.out` and `.err` files.
2. The Terminal Button: Clicking this button will take you to the terminal, where you will be placed in the directory for this job.
3. The Trash Button: Allow you to cancel a specific job.

## The Status Icon

This can be seen as `Queued`, `Running`, or `Completed`.

!!! note

    This does not auto-refresh, so you may need to refresh your screen for up to date information.

![Queued](../../../assets/images/Jobs_OnDemand_2.png)
![Running](../../../assets/images/Jobs_OnDemand_4.png)
![Completed](../../../assets/images/Jobs_OnDemand_5.png)

## The Trash Button

You will get a pop-up indicating if you want to cancel a job before it is cancelled. Click `OK` to cancel your job.

![Pop-Up about Cancelling Job](../../../assets/images/Jobs_OnDemand_6.png)
