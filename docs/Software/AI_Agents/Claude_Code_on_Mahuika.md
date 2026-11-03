---
created_at: 2026-09-24
description: How to install Claude Code on Mahuika, give it the REANNZ agent rules, and use it to build software and run Slurm jobs.
tags:
    - ai_tools
    - software
    - slurm
---

[Claude Code](https://code.claude.com/docs/en/overview) is an AI coding agent from Anthropic.
It can read and edit files and run commands, so on Mahuika it can compile your code, submit Slurm jobs and check the results, with you approving each step.
You need your own Claude subscription or Anthropic API key. REANNZ does not provide Claude licences.

!!! warning "Agent policy"
    Read the [AI Agent Guidelines](./AI_Agent_Guidelines.md) before using Claude Code on Mahuika.
    Claude Code sends everything it reads to Anthropic, so only use it on code and data you are allowed to share.

## On Mahuika

Running Claude Code on a login node is recommended for most work.
It works directly on your files, with the same modules, compilers and Slurm commands that you use.

### Install Claude Code

Log in to Mahuika and follow the [Claude Code installation instructions](https://code.claude.com/docs/en/quickstart).
The `claude` command is installed in `~/.local/bin`. If that directory is not on your `PATH`, add it:

```sh
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
claude --version
```

Claude Code keeps its program in `~/.local/share/claude`, and its settings, login and session history in `~/.claude`.
These take a few hundred MB, and the history grows as you use it.
If your 20 GB [home quota](../../Storage/Filesystems_and_Quotas.md) is tight, move them to your project directory:

```sh
CLAUDE_STORE=/nesi/project/nesi99991/$USER/claude
mkdir -p $CLAUDE_STORE
chmod 700 $CLAUDE_STORE
mv ~/.local/share/claude $CLAUDE_STORE/share
mv ~/.claude $CLAUDE_STORE/config
ln -s $CLAUDE_STORE/share ~/.local/share/claude
ln -s $CLAUDE_STORE/config ~/.claude
```

Replace `nesi99991`, here and below, with your project code.
Do not skip the `chmod 700`: other members of your project can read the project directory.
Do not use `/nesi/nobackup`, which is [automatically cleaned](../../Storage/Automatic_Cleaning_of_Nobackup.md).

### Install the agent rules

Run the REANNZ install script, so that Claude Code reads the [agent rules](./AI_Agent_Guidelines.md#install-the-agent-rules) at the start of every session:

```sh
/opt/nesi/share/mahuika-agents/install.sh --skills
```

This links `~/.claude/CLAUDE.md` to the rules, or adds an import line if you already have one.
`--skills` also adds the REANNZ skills, such as `/mahuika-slurm`.

### Log in

Start Claude Code in the directory you want it to work in:

```sh
cd /nesi/project/nesi99991/my_code
claude
```

When it asks whether you trust the folder, select **"Yes, I trust this folder"**. The default, **"No, exit"**, quits Claude Code.

The first time, you are asked how to authenticate:

- **Claude subscription:** Claude Code prints a URL.
  Open it in a browser on your own computer, log in, then copy the code it shows back into the terminal.
  The URL is long, and copying it from a wrapped line (especially in `tmux`) often adds a line break or space.
  Paste it into a text editor and remove them before opening it.
  Alternatively, run `claude setup-token` in Claude Code on your own computer, then add `export CLAUDE_CODE_OAUTH_TOKEN=TOKEN`
  to your `~/.bashrc` on Mahuika, replacing `TOKEN` with the token it prints. Treat this token like a password.
- **API key:** set `ANTHROPIC_API_KEY` in your `~/.bashrc` before starting `claude`.
  Variables in `~/.bashrc` are also set inside your Slurm jobs, so do not print the environment (for example with `env`) in job scripts.

To check that the agent rules are loaded, run `/context`: `~/.claude/CLAUDE.md` should be listed under **Memory files**.

### Connect to Claude Code

- **Terminal:** `ssh mahuika`, then run `claude` inside [`tmux`](../../Getting_Started/Cheat_Sheets/tmux-Reference_sheet.md),
  so a dropped connection does not end the session.
- **VS Code:** connect with [VS Code Remote-SSH](../../Getting_Started/Accessing_the_HPCs/VSCode.md)
  and install the Claude Code extension in the remote window.
- **Claude desktop app:** the Code tab can open sessions on a remote machine over SSH.

Run one session at a time, and quit Claude Code before you log out.
A session left running after you log out, for example in `tmux`, is unsupervised, and [needs a service account](./AI_Agent_Guidelines.md#support).

!!! warning "Do not use Remote Control on Mahuika"
    Claude Code's `/remote-control` command keeps a connection open from Mahuika to Anthropic,
    which the [AI Agent Guidelines](./AI_Agent_Guidelines.md#working-on-the-cluster) do not allow.

### Project CLAUDE.md file

A `CLAUDE.md` file in your project directory tells Claude Code how your code is built and run.
Without it, the agent has to guess, and may run large tests on the login node. For example:

```md
# Building and running this project

- Use the Slurm account nesi99991 and the milan partition.
- Load the build environment with:
      module purge
      module load foss/2023a netCDF-Fortran/4.6.1-gompi-2023a
- Build with `make -j4`. Run the tests with `sbatch tests/run_tests.sl`.
- Source code:   /nesi/project/nesi99991/my_code
- Run directory: /nesi/nobackup/nesi99991/runs  (not backed up, auto-cleaned)
```

### Configure permissions

Claude Code asks before running a command or editing a file.
To reduce prompts, approve routine commands in advance in `.claude/settings.json` in your project directory:

```json
{
  "permissions": {
    "allow": [
      "Bash(squeue --me *)",
      "Bash(sacct -j *)",
      "Bash(module *)"
    ],
    "ask": [
      "Bash(make *)",
      "Bash(sbatch *)",
      "Bash(scancel *)",
      "Bash(rm *)",
      "Bash(find *)",
      "Bash(du *)"
    ],
    "deny": [
      "Read(~/.ssh/**)",
      "Read(~/.bashrc)"
    ]
  }
}
```

Only approve status checks scoped to your own jobs.
`find` and `du` are in `ask` because Claude Code otherwise runs them without asking, and they can scan shared filesystems.
The `deny` rules stop Claude Code reading your SSH keys and tokens.

Do not use `--dangerously-skip-permissions`, auto mode, or other modes that approve commands for you
(see [Working on the cluster](./AI_Agent_Guidelines.md#working-on-the-cluster)).

### Test your setup

This test uses a few seconds of compute time. Start Claude Code in an empty directory:

```sh
mkdir -p /nesi/nobackup/nesi99991/$USER/claude_test
cd /nesi/nobackup/nesi99991/$USER/claude_test
claude
```

Give it this prompt, and approve each step:

```txt
Write a small MPI "hello world" program in C that prints the rank,
the number of ranks and the hostname. Load the foss/2023a module and
compile it here. Then write a Slurm script hello.sl that runs it with
4 tasks, 1 GB of memory and a 5 minute time limit, using the Slurm
account nesi99991. Submit it with sbatch, wait for it to finish, then
show me the output file and the sacct summary.
```

It should compile `hello.c`, submit `hello.sl`, and show a `slurm-<jobid>.out` file containing four lines like
`Hello from rank 2 of 4 on c0123`. The hostname should be a compute node, not a login node.
When you are finished, delete the test directory.

| Problem | Likely cause |
| - | - |
| `claude` exits straight back to the shell | You accepted the default **"No, exit"** when asked to trust the folder. Run `claude` again and select **"Yes, I trust this folder"**. |
| The browser shows `Invalid OAuth Request` | The login URL was broken when it was copied. See [Log in](#log-in). |
| `~/.claude/CLAUDE.md` is not listed by `/context` | The agent rules are not installed. See [Install the agent rules](#install-the-agent-rules). |
| `module: command not found` | Ask Claude Code to run `source /etc/profile` first, or add this to your `CLAUDE.md`. |
| The job stays pending for a long time | This is normal when the cluster is busy. See [Why is my job taking a long time to start?](../../Getting_Started/FAQs/Why_Is_My_Job_Taking_a_Long_Time_to_Start.md). |

## On your own computer

Claude Code can also run on your own computer, usually on a local copy of your code, and run commands on Mahuika through a login session you opened:

```sh
ssh mahuika 'squeue --me'
rsync -av --exclude .git ./ mahuika:/nesi/project/nesi99991/my_code/
ssh mahuika 'cd /nesi/project/nesi99991/my_code && sbatch run.sl'
```

This suits occasional tasks, and code that also builds and runs on your computer.
It is less suitable when the build depends on Mahuika's modules, compilers or MPI libraries, because the agent cannot test those locally.

Log in with `ssh mahuika` in your own terminal first.
With the [standard SSH configuration](../../Getting_Started/Accessing_the_HPCs/Standard_Terminal_Setup.md),
the agent's `ssh mahuika` commands reuse that connection, and stop working once you log out.
Do not give the agent your SSH key or password.

Claude Code on your computer does not see the rules on Mahuika, so [install them on your computer](./AI_Agent_Guidelines.md#install-the-agent-rules) too.

## Getting help

For questions about Claude Code itself, see the [Claude Code documentation](https://code.claude.com/docs/en/overview).
For questions about using it on Mahuika, {% include "partials/support_request.html" %}.
  