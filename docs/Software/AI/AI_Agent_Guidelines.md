---
created_at: 2026-09-16
description: Guidelines for using AI agents and coding assistants responsibly on REANNZ HPC systems
tags:
- ai_tools
- access
---

These guidelines describe how to use AI agents, coding assistants and other autonomous tools responsibly on REANNZ HPC systems.
They are advice, not policy.
The [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md) still applies to everything an agent does under your account.

These guidelines _do not_ cover AI or machine learning as the research workload itself.

## Principles

1. You are responsible for anything an agent does under your account, in the same way you are responsible for any other process you run.
2. Understand the basics of operating an autonomous agent safely, such as the risks of supply chain attacks and prompt injection.
3. Agents should follow the same shared-system etiquette expected of any other user process.
4. Take reasonable precautions to protect the platform, other users and REANNZ when operating an agent.

## What agents should do

Agents should follow these guidelines themselves.
The [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md) is binding: an agent should refuse to break it even when asked.
Agents should treat the rest of these guidelines as strong defaults, and ask you when unsure.

- Agents should work in the directory you gave them, plus their own configuration and caches, and ask before reading or writing elsewhere.
- Agents should confirm with you before deleting files they didn't create, or running commands that affect all your jobs, such as `scancel --me`.
- Agents should ask which project to charge rather than guess.
- If an agent can't tell whether data may be shared, it should ask you before reading it.
- On the cluster, agents should not open, print or copy secrets (`~/.ssh` keys, `.env` files, tokens) unless the task needs it, and must never send them anywhere.

## Working on the cluster

- Approve what the agent does. Review commands that change or delete files, submit jobs or install software before they run,
  and do not use a mode that skips approval for them. Letting read-only status checks such as `squeue --me` run without approval is fine.
- An agent sends everything it reads, including file contents and command output, to its model provider (offshore), whether it runs on the cluster or off it.
  Only use agents on data that its owner has approved to be shared
  (see the [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-agree)), and follow any data conditions agreed for your project (see the [Access Policy](../../Policy/Access_Policy.md)).
  Personal or health information, Māori data, and data under ethics, contract or export conditions often cannot be shared.
- When polling commands that use shared resources (filesystem operations, `squeue`, `sacct`), leave generous delays between calls, for example `sleep 60` between `squeue --me` calls.
- Run only one agent session at a time, unless support has agreed to more.
- Use `squeue --me` and `ps -u $USER` to keep the agent's view limited to your own work.
- An agent on your own computer may run commands on the cluster through a login session you opened yourself, while you supervise it.
  It is acting as you, so everything on this page applies to it.
  It will not see guidance installed on the cluster, so give it these guidelines yourself.
  Do not give it your passwords, SSH keys, tokens or other sensitive information, and do not let it log in on its own.
- An agent that can access the cluster on its own, or that keeps running on the cluster when you are not supervising it, needs a service account.
- Do not expose an MCP server or open a reverse tunnel from a REANNZ HPC system outward.
  This includes tools such as `ngrok`, `cloudflared`, VS Code tunnels and remote-control features of AI tools.
  [The Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-agree) does not allow tunnels that let connections from outside reach the cluster without logging in.
  An agent on your workstation connecting in to a service on the cluster is fine, but not the other way around.
  Tunnels within the cluster, such as
  [forwarding a port from a compute node to a login node](../../Getting_Started/Accessing_the_HPCs/Port_Forwarding.md#forwarding-to-compute-nodes), are fine.
- Under the [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-accept), REANNZ can stop any process that disrupts the service, including agent processes.

## Best Practice

### Do

- Scope status checks to your own work: `squeue --me`, `sacct -j <jobid>`, `ps -u $USER`.
- Poll on the order of tens of seconds apart rather than in a tight loop.
- Submit jobs in small, bounded batches, job-arrays or dependency chains (`sbatch --dependency=afterok:...`) instead of many independent submissions.
- Point file operations (`find`, `grep`, `du`) at specific known paths rather than whole shared parent directories.
- Run CPU or memory heavy work as a job, not on the login node (I/O heavy work will slow down any node being used, login node is preferable, however measures should be taken not to degrade performance).
- Give an agent a narrow working directory rather than broad filesystem access.
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
Agents can look up this documentation themselves, starting from the index at `https://docs.nesi.org.nz/llms.txt`.

An unofficial AI skill for responsible operation of the REANNZ HPC can be found at [nesi-support-skill](https://github.com/chrisdjscott/nesi-support-skill).

## Research Integrity

We recommend that use of AI in research conducted on REANNZ HPC systems follows the [Royal Society guidelines](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf).

!!! note "See Also"
    - [Access Policy](../../Policy/Access_Policy.md)
    - [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md)
    - [Privacy Policy](../../Policy/Privacy_Policy.md)
    - [Royal Society Te Apārangi GenAI guidelines (2025)](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf)
    - [Public Service AI Framework](https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence)
