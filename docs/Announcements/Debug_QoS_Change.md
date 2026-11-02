---
created_at: 2026-11-02
description: Starting 9 November 2026, the maximum walltime for debug QoS jobs on Mahuika goes to 15 minutes.
status: new
tags: [announcement, slurm, ai_tools]
search:
  boost: 2
---

From 9 November 2026, the maximum walltime for jobs using the [--qos debug](../Batch_Computing/Debug_QoS.md) on Mahuika
goes back from 2 hours to 15 minutes.

## Why is it changing?

QoS debug jobs get a large priority boost and are intended for one-off tests and debugging.
Since the timing limit was changed we have recorded misuse of the debug QoS (much by AI agents), this _negatively affects everyone_.

## What do I need to do?

- Any jobs using `--qos=debug` will have to set `--time` to 15 minutes or less, for example `--time 00:15:00`.
- Use the normal QoS for anything longer, and for regular work. See [When Not to Use Debug QoS](../Batch_Computing/Debug_QoS.md#when-not-to-use-debug-qos).
- If you use an AI agent on Mahuika, make sure it follows the [AI Agent Guidelines](../Software/AI_Agents/AI_Agent_Guidelines.md),
  and update any scripts or agent instructions that ask for the debug QoS with a longer time.

If you have questions, {% include "partials/support_request.html" %}.
