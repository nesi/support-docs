# Agent Eval

Tests how well AI agents follow [AGENTS.md](../../AGENTS.md) when asked to edit the docs.

- [scenarios.yml](scenarios.yml): the prompts, expected behaviour, automatic assertions and grading rubric.
  [agent_scenarios.md](../agent_scenarios.md) is the human-readable version.
- [run_eval.py](run_eval.py): runs the scenarios and writes results to `results/<timestamp>/` (gitignored).

## Running

```sh
source .venv/bin/activate
python3 checks/agent_eval/run_eval.py --ids B3            # one scenario
python3 checks/agent_eval/run_eval.py --first-pass        # the 12 marked first_pass
python3 checks/agent_eval/run_eval.py --all --jobs 3      # everything
```

Options: `--model` and `--judge-model` pick the models, `--budget` caps spend per scenario (default 2 USD),
`--no-judge` skips the judge, `--timeout` is per scenario in seconds.

The agent is tested on your **current working tree**, including uncommitted changes to AGENTS.md and the docs,
so you can try a rule change before committing it.

## What a Run Does

1. Copies the working tree into a throwaway git repo with no remote.
2. Runs the agent on the prompt, unattended (`claude -p`, `--permission-mode dontAsk`, an allow list,
   no MCP servers, only project settings). A short environment note is appended to its system prompt
   (the venv is already active, no `$?`, no network) so it does not waste turns on setup; it says nothing about the rules.
3. Scores the result:
    - **Automatic failures:** any change outside `docs/`, to a generated or maintainer-only page, or to a path the scenario forbids;
      planted private details in the diff; attempted pushes, `gh pr` or `auto_merge`.
    - **Notes:** expected files not touched, edits where a question was expected, denied actions, timeouts, commits made.
    - **New findings:** warnings and errors the page checks report on changed pages that were not there before.
    - **Judge:** a second model grades the transcript, diff and final message against AGENTS.md and the rubric: pass, partial or fail.

    A scenario fails if any automatic failure is found, otherwise it takes the judge's verdict.

`summary.md` has one row per scenario. Each scenario folder has `prompt.txt`, `transcript.jsonl`,
`final_message.md`, `diff.patch`, `result.json` and `judge_raw.json`.

## Safety

The agent runs with no GitHub credentials and no git remote, and pushes, `gh`, `curl`, `wget`, `pip`, `npm`,
web fetch and web search are denied. Allowed commands such as `python3` and `mv` could still reach outside the copy,
so the harness compares the real repository's `HEAD` and `git status` before and after each run and fails the scenario
if they differ. If you edit the repo while a run is in progress, you will trigger this yourself.

## Other Tools

Only Claude Code has an adapter. Adding another tool (Codex, Gemini CLI, Copilot CLI) means writing a function
with the same signature as `run_claude` and adding it to `ADAPTERS`.
