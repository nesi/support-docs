---
created_at: 2026-09-16
description: Principles and rules for using AI agents on REANNZ HPC systems
tags:
- machine_learning
- access
---

## Purpose

This policy sets out the principles and rules governing the use of AI agents, coding assistants and other autonomous tools on REANNZ platforms.
These are additional requirements and do not replace the [Acceptable Use Policy](./Acceptable_Use_Policy.md).

This _does not_ cover AI or machine learning as the research workload itself.

## Principles

1. You are responsible for anything an agent does under your account, in the same way you are responsible for any other process you run.
2. You must be familiar with basic principles of operating an autonomous agent safely (e.g. Identifying supply chain and prompt injection).
3. Agents must follow the same shared-system etiquette expected of any other user process.
4. Agents must be operated with reasonable precautions to protect the platform, other users and REANNZ.

## Conduct

- If polling commands that utilise shared resources (filesystem op, `sacct`), conservative delays must be used (e.g. `sleep 60` between `squeue --me` calls).
- Only one agent session may run per user at a time (unless otherwise approved by support).
- REANNZ may kill disruptive agent processes without notice (consistent with the Acceptable Use Policy).
- Use `squeue --me` and `ps -u $USER` to keep agent context limited to your own work.
- Do not give an agent your passwords, SSH keys, tokens or other sensitive information if they are running off cluster.
- Do not expose a MCP server or open a reverse tunnel from a REANNZ HPC system outward.
- A workstation agent connecting inward to a cluster MCP endpoint is acceptable, the reverse is not.
- Agents that require cluster access must use a service account. Service accounts are only issued by REANNZ support: {% include "partials/support_request.html" %} to request one.

## Best Practice

### Do

- Scope status checks to your own work: `squeue --me`, `sacct -j <jobid>`, `ps -u $USER`.
- Poll on the order of tens of seconds apart rather than in a tight loop.
- Submit jobs in small, bounded batches, job-arrays or dependency chains (`sbatch --dependency=afterok:...`) instead of many independent submissions.
- Point file operations (`find`, `grep`, `du`) at specific known paths rather than whole shared parent directories.
- Run IO, CPU or memory heavy work as a job, not on the login node.
- Give an agent a narrow working directory rather than broad filesystem access.
- Review the packages or dependencies an agent proposes to install before it installs them, and pre-install where practical.

### Don't

- `watch -n 1 squeue` or `while true; do squeue; sleep 1; done`,  sub-second polling of the scheduler.
- `sacct --allusers -S <date>` full-cluster accounting queries.
- Unscoped recursive `find`/`grep -r` over `/nesi/project`, `/home` or similar shared filesystems.
- `for i in {1..N}; do sbatch job.sh; done` speculative bursts of job submissions while iterating.
- `top`/`ps aux` refreshed continuously and unfiltered across all users.

## Support

REANNZ is not responsible for supporting third-party AI tools.
Before raising a support ticket, verify any commands an agent has generated against the relevant documentation, and that nothing has been hallucinated.

An unofficial AI skill for responsible operation of the REANNZ HPC can be found at [nesi-support-skill](https://github.com/chrisdjscott/nesi-support-skill).

## Research Integrity

Use of AI in research conducted on REANNZ HPC systems should follow the [Royal Society guidelines](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf).

!!! note "See Also"
    - [Access Policy](./Access_Policy.md)
    - [Acceptable Use Policy](./Acceptable_Use_Policy.md)
    - [Privacy Policy](./Privacy_Policy.md)
    - [Royal Society Te Apārangi GenAI guidelines (2025)](https://www.royalsociety.org.nz/assets/Guidelines-for-the-best-practice-use-of-GenAI-in-research_Royal-Society-Te-Aparangi_June-2025_English-.pdf)
    - [Public Service AI Framework](https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/artificial-intelligence)
