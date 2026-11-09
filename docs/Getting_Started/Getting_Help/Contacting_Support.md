---
created_at: 2026-03-18
description: How to contact our support team, and what to include in your request so we can help you sooner.
tags:
- troubleshooting
---

You are always welcome to {% include "partials/support_request.html" %}, with any question, big or small.

## What to include

We can help sooner if your request includes:

- the commands you ran, and the error message.
    It may be in the Slurm output file, which unless you named it is in the directory you submitted from, called something like `slurm-12345678.out`,
- your environment: the modules you have loaded (`module list`), and any conda or Python virtual environment,
- what you have tried so far.

If the problem is with a Slurm job, also include:

- the job ID (`sacct` lists your recent jobs),
- the Slurm script. Adding `cat $0` to a script prints it into the job's output, so you always have the version you submitted,
- the path to your files,
- when a job last worked, and its job ID.

Before you write, check [System Status](System_Status.md) for known problems,
and [Login Troubleshooting](../Accessing_the_HPCs/Login_Troubleshooting.md) if you can't log in.

## Other ways to get help

- [Training](Training.md): introductory sessions, workshops and recordings.
- [Weekly Online Office Hours](Weekly_Online_Office_Hours.md): drop-in sessions where you can ask us anything.
- [Consultancy](Consultancy.md): ongoing help with a research project.
