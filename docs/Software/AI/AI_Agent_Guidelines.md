---
created_at: 2026-09-16
description: Guidelines for using AI agents and coding assistants responsibly on REANNZ HPC systems
tags:
- machine_learning
- access
---

These guidelines describe how to use AI agents, coding assistants and other autonomous tools responsibly on REANNZ HPC systems.
They are advice, not policy.
The [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md) still applies to everything an agent does under your account.

These guidelines _do not_ cover AI or machine learning as the research workload itself.

!!! tip "See also: agent setup guides"
    - [Claude Code on Mahuika](./Claude_Code_on_Mahuika.md)

## Principles

1. You are responsible for anything an agent does under your account, in the same way you are responsible for any other process you run.
2. Understand the basics of operating an autonomous agent safely, such as the risks of supply chain attacks and prompt injection.
3. Agents should follow the same shared-system etiquette expected of any other user process.
4. Take reasonable precautions to protect the platform, other users and REANNZ when operating an agent.

## Data and privacy

Most AI agents send your prompts, the files they read and the output of the commands they run to the provider's servers for processing.
This happens whether the agent runs on your own computer or on the cluster.

- Only let the agent read code and data you have permission to share with a third party.
  Do not use it in directories containing sensitive, identifiable or otherwise restricted data.
- Project directories are shared. Start the agent in a directory that holds only your own work,
  so that it does not read other project members' files.
- Some software licences do not allow the source code to be shared with third parties.
  Check the licence conditions of any third-party code before the agent reads it.
- Check your account's privacy settings with the provider to see how long your conversations are kept
  and whether they are used to train models.

## Credentials and access

- Do not let an agent read your passwords, SSH keys or tokens, wherever it runs.
  Anything the agent reads is sent to the provider.
  Use the agent's own settings to block access to files such as `~/.ssh`, and keep credentials out of the directories it works in.
- If an agent reads or prints a password, SSH key or token for REANNZ systems, treat it as exposed and report it,
  as required by the [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-agree).
  {% include "partials/support_request.html" %}.
- Do not let an agent on your own computer reuse your SSH connection to the cluster, for example one kept open with `ControlPersist`.
  Letting an automated tool use your login session gets around two-factor authentication,
  which [clause 12 of the Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-agree) does not allow.
- If an agent needs access to the cluster, apply to support for a service account: {% include "partials/support_request.html" %}.
- Do not expose an MCP server or open a reverse tunnel from a REANNZ HPC system outward.
  This includes tools such as `ngrok`, `cloudflared`, VS Code tunnels and remote-control features of AI tools.
  [The Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-agree) does not allow tunnels that let connections from outside reach the cluster without logging in.
  An agent on your workstation connecting in to a service on the cluster is fine, but not the other way around.
  Tunnels within the cluster, such as
  [forwarding a port from a compute node to a login node](../../Getting_Started/Accessing_the_HPCs/Port_Forwarding.md#forwarding-to-compute-nodes), are fine.

## Working on the cluster

- When polling commands that use shared resources (filesystem operations, `squeue`, `sacct`), leave generous delays between calls, for example `sleep 60` between `squeue --me` calls.
- Run only one agent session at a time, unless support has agreed to more.
- Use `squeue --me` and `ps -u $USER` to keep the agent's view limited to your own work.
- Keep approval turned on for anything that deletes files, cancels jobs or uses a significant part of your allocation.
  Do not use modes that let the agent act without asking.
- Under the [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-accept), REANNZ can stop any process that disrupts the service, including agent processes.

## Best Practice

### Do

- Scope status checks to your own work: `squeue --me`, `sacct -j <jobid>`, `ps -u $USER`.
- Poll on the order of tens of seconds apart rather than in a tight loop.
- Submit jobs in small, bounded batches, job-arrays or dependency chains (`sbatch --dependency=afterok:...`) instead of many independent submissions.
- Review job scripts before they are submitted. Check the resources requested (`--time`, `--mem`, `--ntasks`, GPUs),
  because every job uses your project's allocation and [Fair Share](../../Batch_Computing/Fair_Share.md).
- Point file operations (`find`, `grep`, `du`) at specific known paths rather than whole shared parent directories.
- Run IO, CPU or memory heavy work as a job, not on the login node. Compiling with a few cores on the login node is fine.
- Give an agent a narrow working directory rather than broad filesystem access.
- Commit your work with `git` before asking the agent for large changes, so you can review and undo them.
- Review the packages or dependencies an agent proposes to install before it installs them, and pre-install where practical.

### Don't

- `watch -n 1 squeue` or `while true; do squeue; sleep 1; done`, sub-second polling of the scheduler.
- `sacct --allusers -S <date>` full-cluster accounting queries.
- Unscoped recursive `find`/`grep -r` over `/nesi/project`, `/home` or similar shared filesystems.
- `for i in {1..N}; do sbatch job.sh; done` speculative bursts of job submissions while iterating.
- `top`/`ps aux` refreshed continuously and unfiltered across all users.

## Support

REANNZ does not provide support for third-party AI tools.
Before raising a support ticket, verify any commands an agent has generated against the relevant documentation, and check that nothing has been hallucinated.

An unofficial AI skill for responsible operation of the REANNZ HPC can be found at [nesi-support-skill](https://github.com/chrisdjscott/nesi-support-skill).

## Research Integrity

We recommend that use of AI in research conducted on REANNZ HPC systems follows the [Royal Society guidelines](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf).

!!! note "See Also"
    - [Access Policy](../../Policy/Access_Policy.md)
    - [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md)
    - [Privacy Policy](../../Policy/Privacy_Policy.md)
    - [Royal Society Te Apārangi GenAI guidelines (2025)](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf)
    - [Public Service AI Framework](https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence)
