Git is the most universally adopted version control software and is
often used alongside remote repositories like GitHub and GitLab for
developing, managing and distributing code.

Full Git documentation can be
found [here](https://git-scm.com/docs/git), or using `man git`.

![Git\_Diagram.svg](https://support.nesi.org.nz/hc/article_attachments/360004194235/Git_Diagram.svg)

### Getting Started

You can create a repository with either of the following commands.

  ------- ------------------------------------------------------- ---------------------------------------------------------
  clone   `git clone https://github.com/nesi/perf-training.git`   Copies a remote repository into your current directory.
  init    `git init`                                              Creates a new empty repo in your current directory.
  ------- ------------------------------------------------------- ---------------------------------------------------------

### Basics

add

`git add <file1> <file2>`

Adds `<file1>` and `<file2>` to the staging area.

[`git add *.py`]{.c}

 Adds all python files in the current directory to the staging area.

status

[`git status`]{.c}

Lists changes in working directory, and staged files.

commit 

`git commit`

Records everything in the staging area to your repository. The default
text editor will prompt you for a commit message.

[`git commit -m "Commit message"`]{.c}

Records everything in the staging area to your repository with the
commit message \"Commit message\"

[`git commit --amend`]{.c}

Modify last commit instead of creating a new one. Useful for fixing
small mistakes.

log 

`git log`

Prints commit history of repo.

`git log <filename>`

Prints commit history of `<filename>`.

reset 

`git reset`

Removes all files from staging area. (Opposite of `git add`)

`git reset <filename>`

Removes `<filename>` from staging area.

### Remote

By default, fetch, pull and push will operate on the origin repo. This
will be the repo you cloned from, or set manually using
` git branch --set-upstream-to   <origin>`.

> ### Tip {#prerequisites}
>
> Running the command `git config --global credential.helper store` will
> store your login details next time they are entered, saving you from
> having to enter them again.

fetch 

`git fetch`

Gets status of \'origin\'. git fetch **does not **change your working
directory or local repository (see `git pull`). 

`git fetch <repo> <branch>`

Get status of `<repo>` `<branch>`.

pull 

`git pull`

Incorporates changes from \'origin\' into local repo. 

`git pull <repo> <branch>`

Incorporates changes from `<repo>` `<branch>` into local repo.

push 

`git push`

Incorporates changes from local repo into \'origin\'. 

`git push <repo> <branch>`

Incorporates changes from local repo into `<repo>` `<branch>`

> ### Tip {#prerequisites}
>
> If you are working without collaborators, there should be no reason to
> have a conflict between your local and your remote repo. Make sure you
> always git pull when starting work on your local and git push when
> finished, this will save you wasting time resolving unnecessary
> merges.

### Branches

At an introductory level, it is best to avoid workflows that lead to
multiple branches, or requires merging.

branch 

`git branch`

List branches.

`git branch <branch-name>`

Create new branch `<branch-name`

checkout

`git checkout <branch-name>`

Switch to editing branch `<branch-name>`

merge

`git merge <branch-name>`

Merge `<branch-name>` into current branch.

> ### Other Resources {#prerequisites}
>
> -   <https://ohshitgit.com/>
