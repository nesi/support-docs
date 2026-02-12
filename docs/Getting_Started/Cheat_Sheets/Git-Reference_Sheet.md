---
created_at: '2020-05-07T02:51:35Z'
tags:
- git
- version control
- repository
title: 'Git: Reference Sheet'
vote_count: 13
vote_sum: 13
zendesk_article_id: 360001508515
zendesk_section_id: 360000278975
---

Git is the most universally adopted version control software and is
often used alongside remote repositories like GitHub, GitLab, Bitbucket or Gitea for
developing, managing and distributing code.

Full Git documentation can be found [here](https://git-scm.com/docs/git), or using `man git`.

![Git\_Diagram.svg](../../assets/images/Git-Reference_Sheet.svg)


## Basics

You can create a repository with either of the following commands.

|       |                                                       |                                                         |
|-------|-------------------------------------------------------|---------------------------------------------------------|
| `clone` | `git clone https://github.com/nesi/perf-training.git` | Copies a remote repository into your current directory. |
| `init`  | `git init`                                            | Creates a new empty repo in your current directory.     |

|         |                                  |                                                                                                                          |
|---------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `add`     | `git add <file1> <file2>`        | Adds `<file1>` and `<file2>` to the staging area.                                                                        |
|         | `git add *.py`                   |  Adds all python files in the current directory to the staging area.                                                     |
| `status`  | `git status`                     | Lists changes in working directory, and staged files.                                                                    |
| `commit` | `git commit`                     | Records everything in the staging area to your repository. The default text editor will prompt you for a commit message. |
|         | `git commit -m "Commit message"` | Records everything in the staging area to your repository with the commit message "Commit message"                       |
|         | `git commit --amend`             | Modify last commit instead of creating a new one. Useful for fixing small mistakes.                                      |
| `log`    | `git log`                        | Prints commit history of repo.                                                                                           |
|         | `git log <filename>`             | Prints commit history of `<filename>`.                                                                                   |
| `reset`  | `git reset`                      | Removes all files from staging area. (Opposite of `git add`)                                                             |
|         | `git reset <filename>`           | Removes `<filename>` from staging area.                                                                                  |

## Remote

By default, fetch, pull and push will operate on the origin repo. This
will be the repo you cloned from, or set manually using
`git branch --set-upstream-to <origin>`.

||||
|--------|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
| fetch  | `git fetch`                 | Gets status of `origin`. git fetch **does not** change your working directory or local repository (see `git pull`).  |
|        | `git fetch <repo> <branch>` | Get status of `<repo>` `<branch>`.                                                                                   |
| pull   | `git pull`                  | Incorporates changes from 'origin' into local repo.                                                                  |
|        | `git pull <repo> <branch>`  | Incorporates changes from `<repo>` `<branch>` into local repo.                                                       |
| push   | `git push`                  | Incorporates changes from local repo into `origin`.                                                                  |
|        | `git push <repo> <branch>`  | Incorporates changes from local repo into `<repo>` `<branch>`                                                        |

!!! tip
     If you are working without collaborators, there should be no reason to
     have a conflict between your local and your remote repo. Make sure you
     always git pull when starting work on your local and git push when
     finished, this will save you wasting time resolving unnecessary
     merges.

## Branches

At an introductory level, it is best to avoid workflows that lead to
multiple branches, or requires merging.

|          |                              |                                            |
|----------|------------------------------|--------------------------------------------|
| branch   | `git branch`                 | List branches.                             |
|          | `git branch <branch-name>`   | Create new branch `<branch-name`           |
| checkout | `git checkout <branch-name>` | Switch to editing branch `<branch-name>`   |
| merge    | `git merge <branch-name>`    | Merge `<branch-name>` into current branch. |

!!! prerequisite "Other Resources"
     -  [oshitgit.com](https://ohshitgit.com/)
