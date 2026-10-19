---
created_at: 2026-10-15
title: New Rules for AI Agents
description: REANNZ is introducing rules that AI agents must follow on Mahuika. What the rules are, how to install them, when they take effect, and how to ask for a service account.
status: new
tags: [announcement, ai_tools]
search:
  boost: 2
---

AI agents and coding assistants, such as Claude Code, Codex, Gemini CLI and Copilot, are now widely used on Mahuika.

We want to support these new tools. However, some agent behaviour puts a disproportionate load on our shared resources,
and we have seen agents misuse the platform and get around its safeguards, both with and without their user's knowledge.

To protect the shared system, REANNZ is introducing guidelines for agent use, including rules that agents must follow on Mahuika.

## What are the new rules?

- Agents must be supervised. Start the agent yourself, stay at the session, and approve what it does as it happens.
  Loops that keep running after you stop watching, scheduled tasks (such as `cron` or `scrontab`),
  and sessions left running after you log out are not supervised.
- Agents must not have access to the cluster independent of you.
  They must not log in on their own, or be given your passwords, SSH keys or tokens.
- Agents must not open tunnels that let connections from outside reach the cluster,
  such as reverse SSH tunnels, `ngrok`, VS Code tunnels or the remote-control features of AI tools.
- Agents must scope commands to your own jobs and files, poll the scheduler slowly, and keep heavy work off the login node.
- Agents must follow the REANNZ agent rules file, `AGENTS.md`.

The full rules and recommendations are in the [AI Agent Guidelines](../Software/AI_Agents/AI_Agent_Guidelines.md).

## What do I need to do?

If you already use agents on the cluster, run this install script on a login node:

```sh
/opt/nesi/share/mahuika-agents/install.sh
```

It creates links in your home directory so that Claude Code, Codex, Gemini CLI and Copilot CLI read the REANNZ rules at the start of every session.
It never overwrites a file you already have.
For other tools, point your agent at `/opt/nesi/share/mahuika-agents/dist/AGENTS.md` yourself.

Please test your usual workflows with the rules in place, and tell us if they get in the way.

If you use an agent on your own computer to run commands on Mahuika, it needs the rules too.
See [Install the agent rules](../Software/AI_Agents/AI_Agent_Guidelines.md#install-the-agent-rules) for this,
and for skills that help agents with tasks such as writing Slurm jobs.

## Enforcement

On Friday 23 October, we will install the rules system-wide and add the install script's links to every home directory.
If you run the install script now, this won't change anything for you.

From 1 November, we will contact anyone found not following the new rules.

## Service accounts

An agent that can log in to Mahuika on its own, or that keeps running when you are not supervising it, needs a service account.
We are developing service accounts now.
If you need one, {% include "partials/support_request.html" %} with your use case and requirements.
Until then, only run agents while you are supervising them.

## Feedback

We want to support these new technologies, and are open to discussing your requirements.
If you have questions or suggestions, {% include "partials/support_request.html" %},
or come to one of our regular [office hours](../Getting_Started/Getting_Help/Weekly_Online_Office_Hours.md).

!!! note "Further Reading"
    - [Towards Efficient HPC Systems for Agents](https://arxiv.org/html/2609.38723)
