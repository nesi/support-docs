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
    - Read the [AI Agent Guidelines](./AI_Agent_Guidelines.md) and the [Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md).

!!! warning "Your code and data leave the cluster"
    Claude Code sends the prompts, file contents and command output it works with to Anthropic's servers for processing.
    Only let it read code and data you are allowed to share with a third party,
    and see [Data and privacy](./AI_Agent_Guidelines.md#data-and-privacy) in the AI Agent Guidelines before you start.

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

!!! warning "Set your project code"
    The instructions on this page use the shell variable `PROJECT` for your project code.
    Set it first, **replacing `nesi12345` with your own project code**:

    ```sh
    export PROJECT=nesi12345
    ```

    To have it set in every new shell, including the shells Claude Code uses to run commands, add it to your `~/.bashrc` on Mahuika:

    ```sh
    echo 'export PROJECT=nesi12345' >> ~/.bashrc
    ```

    For Options 2 and 3, also set it on your own computer.

## Option 1: On Mahuika

In this setup Claude Code is installed in the home directory of your agent service account and runs on a Mahuika login node.
Log in with the service account, not your own account, for all the steps below.
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

### Installing outside home

Claude Code keeps its program files (a few hundred MB) in `~/.local/share/claude`,
and its settings, login credentials and session history in `~/.claude`.
The session history grows as you use it.
If your home directory is short of space, you can store both in your project directory and leave symbolic links in your home directory.

Ideally, do this **before** running the installer.
Make sure `PROJECT` is [set to your project code](#where-to-run-claude-code) first:

```sh
CLAUDE_STORE=/nesi/project/$PROJECT/$USER/claude
mkdir -p $CLAUDE_STORE/share $CLAUDE_STORE/config ~/.local/share
chmod 700 $CLAUDE_STORE
ln -s $CLAUDE_STORE/share ~/.local/share/claude
ln -s $CLAUDE_STORE/config ~/.claude
```

If Claude Code is already installed, move the existing directories first:

```sh
CLAUDE_STORE=/nesi/project/$PROJECT/$USER/claude
mkdir -p $CLAUDE_STORE
chmod 700 $CLAUDE_STORE
mv ~/.local/share/claude $CLAUDE_STORE/share
mv ~/.claude $CLAUDE_STORE/config
ln -s $CLAUDE_STORE/share ~/.local/share/claude
ln -s $CLAUDE_STORE/config ~/.claude
```

!!! warning
    - Use `/nesi/project`, not `/nesi/nobackup`.
      Files in nobackup are [automatically deleted](../../Storage/Automatic_Cleaning_of_Nobackup.md), which would remove your installation and settings.
    - Project directories can be read by other members of your project.
      The `chmod 700` above keeps your credentials and session history private. Do not skip it.

### Log in

Start Claude Code in your project directory:

```sh
cd /nesi/project/$PROJECT/my_code
claude
```

The first time, you will be asked how to authenticate:

- **Claude subscription:** Claude Code prints a URL.
  Open it in a browser on your own computer, sign in, then copy the code it shows back into the terminal.
- **API key:** set `ANTHROPIC_API_KEY` in your environment before starting `claude`.
  Keep the key out of shared project directories and job scripts.
  Your home directory is not readable by other users, but it can be accessed by Mahuika administrators.
  Variables set in `~/.bashrc` are also set inside your Slurm jobs, so do not print the environment (for example with `env`) in job scripts.

!!! warning "The login URL breaks if it wraps"
    The login URL is longer than a normal terminal line.
    When you copy it from a wrapped terminal, especially inside `tmux`, a line break or space is often copied along with it.
    The browser then shows an error such as `Invalid OAuth Request` or `Invalid code_challenge_method: S25 6. Expected: 'S256'`.

    To avoid this, do one of the following:

    - Paste the URL into a text editor, remove any spaces and line breaks, then open it in your browser.
    - Make the terminal wide enough (or zoom out) that the URL fits on one line, and log in outside `tmux`.
      You only need to log in once.
    - Log in without a browser on Mahuika: run `claude setup-token` in Claude Code on your own computer, then add
      `export CLAUDE_CODE_OAUTH_TOKEN=<token>` to your `~/.bashrc` on Mahuika.
      Treat this token like a password.

!!! warning "Choose 'Yes' when asked to trust the folder"
    The first time you start `claude` in a directory, it asks
    **"Is this a project you created or one you trust?"**.
    The highlighted default is **"No, exit"**, so pressing <kbd>Enter</kbd> straight away quits Claude Code and returns you to the shell.
    Press <kbd>↓</kbd> to select **"Yes, I trust this folder"**, then press <kbd>Enter</kbd>.
    You are asked once per directory.

    If the arrow keys do nothing, check that `echo $TERM` shows a value such as `xterm-256color`, or try again outside `tmux`.

### Keep sessions running

Claude Code sessions can run for a long time, for example while waiting for a job to finish.
Start Claude Code inside [`tmux`](../../Getting_Started/Cheat_Sheets/tmux-Reference_sheet.md)
so that the session continues if your SSH connection drops:

```sh
tmux new -s agent
claude
```

Detach with <kbd>ctrl</kbd> + <kbd>b</kbd> then <kbd>d</kbd>, and reattach later with `tmux attach -t agent`.

[Run only one agent session at a time](./AI_Agent_Guidelines.md#working-on-the-cluster).
Before starting a new session, check for an old one with `tmux ls` and reattach to it or close it.

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
- **Claude desktop app SSH session:** the Code tab of the Claude desktop app can open sessions on a remote machine over SSH.
  It must connect with your agent service account, not by reusing your own `ssh mahuika` login.

!!! warning "Do not use Remote Control on Mahuika"
    Claude Code's `/remote-control` command lets a session be controlled from the Claude website or apps.
    It keeps a connection open from Mahuika to Anthropic's servers, which is a
    [reverse tunnel out of the cluster](./AI_Agent_Guidelines.md#credentials-and-access).

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
- Slurm account: the value of the `PROJECT` environment variable. `#SBATCH`
  lines do not expand variables, so write the value itself in job scripts or
  pass `--account=$PROJECT` to sbatch. Use `--partition=milan` unless told otherwise.
- Load the build environment with:
      module purge
      module load foss/2023a netCDF-Fortran/4.6.1-gompi-2023a
- Source code:   /nesi/project/$PROJECT/my_code
- Run directory: /nesi/nobackup/$PROJECT/runs  (not backed up, auto-cleaned)
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
      "Bash(module:*)"
    ],
    "ask": [
      "Bash(make:*)",
      "Bash(sbatch:*)",
      "Bash(scancel:*)",
      "Bash(rm:*)"
    ],
    "deny": [
      "Read(~/.ssh/**)",
      "Read(~/.bashrc)"
    ]
  }
}
```

`make` is in the `ask` list because targets such as `make test` or `make -j` can run heavy work on the login node.
The `deny` rules stop the agent from reading your SSH keys and any tokens in `~/.bashrc`,
so that they are not sent to Anthropic (see [Credentials and access](./AI_Agent_Guidelines.md#credentials-and-access)).
They apply to Claude Code's file tools, not every shell command.

!!! warning
    Claude Code runs with the permissions of the account it runs under, including write access to your shared project directories.
    Do not use `--dangerously-skip-permissions` or similar modes that bypass approval on Mahuika.
    Keep approval on for anything that deletes files, cancels jobs, or uses a significant part of your allocation.

### Test your setup

This short test checks that Claude Code can log in, use the module system, compile code, and submit and monitor a Slurm job.
It uses a few seconds of compute time.

1. Create an empty test directory and start Claude Code in it:

    ```sh
    mkdir -p /nesi/nobackup/$PROJECT/$USER/claude_test
    cd /nesi/nobackup/$PROJECT/$USER/claude_test
    claude
    ```

    Because this is a new directory, Claude Code first asks whether you trust the folder.
    Press <kbd>↓</kbd> to select **"Yes, I trust this folder"** before pressing <kbd>Enter</kbd>.
    The default, **"No, exit"**, quits Claude Code.

2. Give Claude Code this prompt:

    ```txt
    Write a small MPI "hello world" program in C that prints the rank,
    the number of ranks and the hostname. Load the foss/2023a module and
    compile it here. Then write a Slurm script hello.sl that runs it with
    4 tasks, 1 GB of memory and a 5 minute time limit, using the Slurm
    account in the PROJECT environment variable. Submit it with sbatch,
    check with squeue until it has finished, then show me the output
    file and the sacct summary.
    ```

3. Approve each step as Claude Code asks for permission.
   You should see it:

    - create `hello.c` and `hello.sl`,
    - run `module load foss/2023a` and `mpicc` on the login node,
    - run `sbatch hello.sl` and report the job ID,
    - check the job with `squeue` or `sacct` until it finishes,
    - show the `slurm-<jobid>.out` file, containing four lines like
      `Hello from rank 2 of 4 on c0123`, and an `sacct` summary with the state `COMPLETED`.

Check that the program ran on a compute node, not on the login node.
The hostname in the output should not be a login node name such as `login01`.

| Problem | Likely cause |
| - | - |
| `claude` exits straight back to the shell | You accepted the default **"No, exit"** when asked to trust the folder. Run `claude` again and [select "Yes, I trust this folder"](#log-in). |
| The browser shows `Invalid OAuth Request` or `Invalid code_challenge_method` | The login URL was broken when it was copied from a wrapped terminal line. See [the login URL warning](#log-in). |
| Login or network errors when starting `claude` | Claude Code cannot reach Anthropic's servers, or the login has expired. Run `claude` again and follow the login prompt. |
| `module: command not found` or no compilers | The agent's shell has not loaded the module system. Ask it to run `source /etc/profile` first, or add this to your `CLAUDE.md`. |
| The agent runs `mpirun` or `srun` on the login node instead of submitting a job | Add the "run everything through Slurm" rule from the [example `CLAUDE.md`](#project-claudemd-file) to your project. |
| The job stays pending for a long time | This is normal when the cluster is busy. See [Why is my job taking a long time to start?](../../Getting_Started/FAQs/Why_Is_My_Job_Taking_a_Long_Time_to_Start.md). |

When you are finished, delete the test directory.

### Good practice on Mahuika

Follow the [AI Agent Guidelines best practice](./AI_Agent_Guidelines.md#best-practice),
such as reviewing job scripts before they are submitted and keeping heavy work off the login node.
The [example `CLAUDE.md`](#project-claudemd-file) passes the most important of these on to the agent.

Also watch your home quota. Claude Code stores its settings and session history under `~/.claude` and its program under `~/.local`.
These are small, but home directories have a 20 GB quota (see [Filesystems and Quotas](../../Storage/Filesystems_and_Quotas.md)).
If space is tight, [install outside your home directory](#installing-outside-home).
Keep large outputs out of your source directory so the agent does not read through them.

## Option 2: Local, over SSH

In this setup Claude Code runs on your own computer and runs commands on Mahuika through SSH with your agent service account,
for example `ssh mahuika-agent 'squeue --me'` or `ssh mahuika-agent "cd /nesi/project/$PROJECT/my_code && sbatch run.sl"`,
where `mahuika-agent` is the SSH host name for your service account.
The double quotes make your computer's shell fill in `$PROJECT` before the command is sent.

This needs no installation on Mahuika, and your Claude credentials stay on your own computer.
It works well for occasional tasks such as submitting a job or summarising output files.
It is awkward for development, because the agent cannot easily edit files on the cluster.

!!! warning "Use a service account, not your own login"
    Do not let the agent reuse your own SSH connection to Mahuika, for example one kept open with `ControlPersist`.
    This gets around two-factor authentication, which
    [clause 12 of the Acceptable Use Policy](../../Policy/Acceptable_Use_Policy.md#you-agree) does not allow.
    See [Credentials and access](./AI_Agent_Guidelines.md#credentials-and-access) in the AI Agent Guidelines.

You must apply to support for a service account: {% include "partials/support_request.html" %}.

## Option 3: Local, then sync

In this setup you and Claude Code work on a copy of your code on your own computer.
When it is ready, copy it to Mahuika (for example with `rsync`) and submit jobs there yourself.
If you want the agent to run these commands, it must use a service account as in [Option 2](#option-2-local-over-ssh).

```sh
rsync -av --exclude .git ./ mahuika:/nesi/project/$PROJECT/my_code/
ssh mahuika "cd /nesi/project/$PROJECT/my_code && sbatch run.sl"
```

This is a good fit if your code also builds and runs on your computer, so most development and testing can happen locally.
It is less suitable when the build depends on Mahuika's modules, compilers or MPI libraries, because the agent cannot test those locally.
See [Data Transfer](../../Data_Transfer/Data_Transfer_Overview.md) for other ways to move files.

## Getting help

For questions about Claude Code itself, see the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview).
For questions about using it on Mahuika, {% include "partials/support_request.html" %}.
