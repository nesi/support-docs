---
created_at: 2026-09-16
description: Guidelines for using AI agents and coding assistants responsibly on REANNZ HPC systems
tags:
- ai_tools
- access
---

These guidelines describe how to use AI agents, coding assistants and other autonomous tools responsibly on REANNZ HPC systems.
The [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-agree) applies to everything an agent does under your account.
These guidelines _do not_ cover AI or machine learning as the research workload itself.

## Principles

1. You are responsible for anything an agent does under your account, in the same way you are responsible for any other process you run.
2. Understand the basics of operating an autonomous agent safely, such as the risks of supply chain attacks and prompt injection.
3. Agents should follow the same shared-system etiquette expected of any other user process.
4. Take reasonable precautions to protect the platform, other users and REANNZ when operating an agent.

## Install the agent rules

REANNZ publishes the rules on this page in a form agents read: an `AGENTS.md` file, and skills that give agents more detail for particular tasks, such as writing Slurm jobs.
An agent reads `AGENTS.md` at the start of every session, and loads a skill only when a task needs it.
Both are kept in the [mahuika-agents repository](https://github.com/nesi/mahuika-agents), and REANNZ keeps a copy on Mahuika up to date.

On a login node, run the install script:

```sh
/opt/nesi/share/mahuika-agents/install.sh
```

This links `AGENTS.md` into the home directory configuration of Claude Code, Codex, Gemini CLI and Copilot CLI.
The links point at the copy on Mahuika, so you get updates to the rules without running the script again.

| Option | What it does |
| - | - |
| `--skills` | Also links the skills into `~/.agents/skills` and `~/.claude/skills`, so agents can load them directly. Run the script again after an update to pick up new skills. |
| `--project DIRECTORY` | Also links `AGENTS.md` into `DIRECTORY`, for tools that only read it from the project directory, such as Cursor CLI. |

An agent on your own computer doesn't see the copy on Mahuika.
Clone the repository there and run its install script with `--skills`:

```sh
git clone https://github.com/nesi/mahuika-agents.git
mahuika-agents/install.sh --skills
```

To get updates, run `git pull` in the `mahuika-agents` directory.

REANNZ is also installing the rules system-wide and in every home directory, see [New Rules for AI Agents](../../Announcements/AI_Agent_Rules.md).

## What agents should do

Agents should follow these guidelines themselves.
The [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md) is binding: an agent should refuse to break it even when asked.
The guidelines that protect other users (delays between polling, scoping queries to your own work,
keeping heavy work off the login node, and running one session at a time) should not be relaxed at your request.
If you need more than they allow, {% include "partials/support_request.html" %}.
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
  This applies wherever the polling runs, including loops inside job scripts.
  To start a job when another one finishes, use a [job dependency](../../Batch_Computing/Job_Checkpointing.md) instead of polling.
- Run only one agent session at a time, unless support has agreed to more.
- Use `squeue --me` and `ps -u $USER` to keep the agent's view limited to your own work.
- An agent on your own computer may run commands on the cluster through a login session you opened yourself, while you supervise it.
  It is acting as you, so everything on this page applies to it.
  It will not see guidance installed on the cluster, so give it these guidelines yourself.
  Do not give it your passwords, SSH keys, tokens or other sensitive information, and do not let it log in on its own.
- An agent that can access the cluster on its own, or that keeps running on the cluster when you are not supervising it, needs a [service account](#support).
  You are supervising an agent when you are at the session and approving what it does as it happens.
  These are not supervised:
    - loops or monitors that keep running after you stop watching them,
    - scheduled or cloud-hosted routines, such as `cron`, `scrontab` or an AI tool's scheduled tasks,
    - sessions left running after you log out, for example in `tmux` or with `nohup`.
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

Service accounts for agents and other tools that need their own access are still being developed.
If you need one, {% include "partials/support_request.html" %} with your use case and requirements.

## Research Integrity

We recommend that use of AI in research conducted on REANNZ HPC systems follows the [Royal Society guidelines](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf).

!!! note "See Also"
    - [Claude Code on Mahuika](./Claude_Code_on_Mahuika.md)
    - [Access Policy](../../Policy/Access_Policy.md)
    - [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md)
    - [Privacy Policy](../../Policy/Privacy_Policy.md)
    - [Royal Society Te Apārangi GenAI guidelines (2025)](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf)
    - [Public Service AI Framework](https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence)
    - [Towards Efficient HPC Systems for Agents](https://arxiv.org/html/2609.38723), a study of agent use on a Harvard research computing cluster.
