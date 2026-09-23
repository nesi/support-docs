---
created_at: 2026-09-24
description: How to install and configure the Claude Code AI coding agent to build software, submit Slurm jobs and inspect results on Mahuika.
tags:
    - machine_learning
    - software
    - slurm
    - access
---

[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) is an AI coding agent developed by Anthropic.
Unlike a chat assistant, it can read and edit files, run shell commands, and iterate on the results.
On an HPC system this means it can compile your code, submit Slurm jobs, check their output and fix problems, with you approving each step.

This page describes how to set up Claude Code so that it runs tasks on Mahuika.

!!! prerequisite
    - Have an [active account and project](../../Getting_Started/Creating_an_Account.md).
    - Be able to [log in to Mahuika with SSH](../../Getting_Started/Accessing_the_HPCs/Standard_Terminal_Setup.md).
    - Have a Claude subscription (Pro, Max, Team or Enterprise) or an Anthropic API key.
      REANNZ does not provide Claude licences.

!!! warning "Your code and data leave the cluster"
    Claude Code sends the prompts, file contents and command output it works with to Anthropic's servers for processing.
    Before using it, check that this is allowed for your project's data and any third-party code or datasets,
    and that it is consistent with the [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md).
    Do not use it in directories containing sensitive, identifiable or otherwise restricted data.

## Where to run Claude Code

There are three common ways to use Claude Code with Mahuika:

| Option | Where the agent runs | Best for |
| - | - | - |
| [1. On the Mahuika login node](#option-1-on-mahuika) (recommended) | Mahuika | Developing, building and running code on the cluster |
| [2. On your computer, using SSH](#option-2-local-over-ssh) | Your computer | Occasionally submitting or checking jobs |
| [3. On your computer, syncing files](#option-3-local-then-sync) | Your computer | Code that you develop and test locally before running at scale |

Option 1 is recommended for most HPC work.
The agent runs next to your files, the environment modules, the compilers and Slurm,
so it can complete the edit, build, submit and check cycle itself.

## Option 1: On Mahuika

In this setup Claude Code is installed in your home directory and runs on a Mahuika login node.
You connect to it from your own computer with a terminal, VS Code, or the Claude apps.
The agent works directly on your files in `/nesi/project` and `/nesi/nobackup`, uses the same modules and compilers that you do,
and submits and monitors Slurm jobs with the standard commands.
The steps below cover installation, login, keeping sessions alive, and configuring the agent for Mahuika.

### Install Claude Code

Log in to Mahuika and run the native installer.
It installs into your home directory and does not need administrator rights or a Node.js module.

```sh
curl -fsSL https://claude.ai/install.sh | bash
```

The `claude` command is installed in `~/.local/bin`.
If that directory is not already on your `PATH`, add it to your `~/.bashrc`:

```sh
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
claude --version
```

### Log in

Start Claude Code in your project directory:

```sh
cd /nesi/project/nesi12345/my_code
claude
```

The first time, you will be asked how to authenticate:

- **Claude subscription:** Claude Code prints a URL.
  Open it in a browser on your own computer, sign in, then copy the code it shows back into the terminal.
- **API key:** set `ANTHROPIC_API_KEY` in your environment before starting `claude`.
  Keep the key out of shared project directories and job scripts.
  Your home directory is not readable by other users, but it can be accessed by Mahuika administrators.

### Keep sessions running

Claude Code sessions can run for a long time, for example while waiting for a job to finish.
Start Claude Code inside [`tmux`](../../Getting_Started/Cheat_Sheets/tmux-Reference_sheet.md)
so that the session continues if your SSH connection drops:

```sh
tmux new -s agent
claude
```

Detach with <kbd>ctrl</kbd> + <kbd>b</kbd> then <kbd>d</kbd>, and reattach later with `tmux attach -t agent`.

!!! warning "Remember which login node you are on"
    Mahuika has several login nodes, and `ssh mahuika` can connect you to any of them.
    A `tmux` session only exists on the node where it was started.
    Run `hostname` before you start `tmux`. To get back to the session later, connect to that node
    (for example `ssh login02` from any login node) before running `tmux attach`.

### Connect from your computer

Once Claude Code is running on Mahuika, you can interact with it in any of these ways:

- **Terminal:** `ssh mahuika`, then `tmux attach`. This is the simplest option and works everywhere.
- **VS Code:** connect to Mahuika with [VS Code Remote-SSH](../../Getting_Started/Accessing_the_HPCs/VSCode.md)
  and install the Claude Code extension in the remote window.
  The agent then runs on Mahuika and shows file edits as diffs in the editor.
- **Remote Control:** in a running Claude Code session, type `/remote-control`.
  You can then follow and steer the session from the Claude desktop app, the Claude website or the Claude mobile app.
  This is useful for checking on a long-running task away from your desk.
- **Claude desktop app SSH session:** the Code tab of the Claude desktop app can open sessions on a remote machine over SSH.
  It needs a working `ssh mahuika` connection from your computer.
  Because of the browser-based two-factor login, open a normal `ssh mahuika` connection in a terminal first
  so the app can reuse it (see the `ControlMaster` settings in [Option 2](#option-2-local-over-ssh)).

### Project CLAUDE.md file

Claude Code reads a file called `CLAUDE.md` in your project directory at the start of every session.
Use it to tell the agent how your code is built and run on Mahuika.
Without it, the agent has to guess, and it will often try to run large tests directly on the login node.

An example `CLAUDE.md`:

```md
# Working on Mahuika

- This is a shared HPC login node. Do not run anything that uses more than
  4 cores or runs for more than a few minutes here. Compile with `make -j4`.
- Run all tests and production runs through Slurm with `sbatch` (or `srun`
  for short interactive tests). Never run `mpirun` on the login node.
- Slurm account: `nesi12345`. Use `--partition=milan` unless told otherwise.
- Load the build environment with:
      module purge
      module load foss/2023a netCDF-Fortran/4.6.1-gompi-2023a
- Source code:   /nesi/project/nesi12345/my_code
- Run directory: /nesi/nobackup/nesi12345/runs  (not backed up, auto-cleaned)
- After submitting a job, check its state with `squeue --me` or
  `sacct -j <jobid>`, at most every few minutes, and read the
  `slurm-<jobid>.out` file when it finishes.
```

Adjust the modules, partitions and paths for your project.
See [Hardware](../../Batch_Computing/Hardware.md) and
[Slurm Best Practice](../../Batch_Computing/SLURM-Best_Practice.md) for guidance on choosing resources.

### Configure permissions

By default, Claude Code asks before running a command or editing a file.
You can pre-approve safe, routine commands to reduce prompts by creating `.claude/settings.json` in your project directory:

```json
{
  "permissions": {
    "allow": [
      "Bash(squeue:*)",
      "Bash(sacct:*)",
      "Bash(sinfo:*)",
      "Bash(module:*)",
      "Bash(make:*)"
    ],
    "ask": [
      "Bash(sbatch:*)",
      "Bash(scancel:*)",
      "Bash(rm:*)"
    ]
  }
}
```

!!! warning
    Claude Code runs with your user permissions, including write access to your shared project directories.
    Do not use `--dangerously-skip-permissions` or similar modes that bypass approval on Mahuika.
    Keep approval on for anything that deletes files, cancels jobs, or uses a significant part of your allocation.

### Good practice on Mahuika

- **Keep heavy work off the login node.** Login nodes are shared by all users.
  The agent should compile with a few cores and send everything else to Slurm.
- **Review job scripts before they are submitted.** Check the resources requested (`--time`, `--mem`, `--ntasks`, GPUs),
  because every job uses your project's allocation and [Fair Share](../../Batch_Computing/Fair_Share.md).
- **Watch your home quota.** Claude Code stores its settings and session history under `~/.claude` and its program under `~/.local`.
  These are small, but home directories have a 20 GB quota (see [Filesystems and Quotas](../../Storage/Filesystems_and_Quotas.md)).
  Keep large outputs out of your source directory so the agent does not read through them.
- **Use version control.** Commit your work with `git` before asking the agent for large changes, so you can review and undo them.

## Option 2: Local, over SSH

In this setup Claude Code runs on your own computer and runs commands on Mahuika through SSH,
for example `ssh mahuika 'squeue --me'` or `ssh mahuika 'cd /nesi/project/nesi12345/my_code && sbatch run.sl'`.

This needs no installation on Mahuika, and your Claude credentials stay on your own computer.
It works well for occasional tasks such as submitting a job or summarising output files.
It is awkward for development, because the agent cannot easily edit files on the cluster.

Mahuika requires a browser-based two-factor login, which Claude Code cannot complete.
Instead, you log in once yourself and let the agent reuse that connection.
In `~/.ssh/config` on your computer, add a longer `ControlPersist` to the `mahuika` entry from the
[Standard Terminal Setup](../../Getting_Started/Accessing_the_HPCs/Standard_Terminal_Setup.md):

```sh
Host mahuika
    User username
    Hostname login.hpc.nesi.org.nz
    ProxyCommand ssh -W %h:%p lander
    ControlMaster auto
    ControlPath ~/.ssh/sockets/ssh_mux_%h_%p_%r
    ControlPersist 8h
```

!!! tip
    SSH uses the first value it finds for each setting.
    Put this `Host mahuika` block **above** any `Host *` block, otherwise the `ControlPersist 1` from `Host *` is used instead.

Log in once with `ssh mahuika` in your own terminal and complete the authentication.
For the next 8 hours, `ssh mahuika` commands run by Claude Code will reuse this connection without asking you to log in again.

## Option 3: Local, then sync

In this setup you and Claude Code work on a copy of your code on your own computer.
When it is ready, copy it to Mahuika (for example with `rsync`) and submit jobs there, either yourself or through SSH as in Option 2.

```sh
rsync -av --exclude .git ./ mahuika:/nesi/project/nesi12345/my_code/
ssh mahuika 'cd /nesi/project/nesi12345/my_code && sbatch run.sl'
```

This is a good fit if your code also builds and runs on your computer, so most development and testing can happen locally.
It is less suitable when the build depends on Mahuika's modules, compilers or MPI libraries, because the agent cannot test those locally.
See [Data Transfer](../../Data_Transfer/Data_Transfer_Overview.md) for other ways to move files.

## Getting help

For questions about Claude Code itself, see the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview).
For questions about using it on Mahuika, {% include "partials/support_request.html" %}.
