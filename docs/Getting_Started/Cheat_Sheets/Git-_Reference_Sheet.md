---
created_at: '2020-05-07T02:51:35Z'
hidden: false
label_names:
- git
- github
- version control
- repository
position: 2
title: 'Git: Reference Sheet'
vote_count: 11
vote_sum: 11
zendesk_article_id: 360001508515
zendesk_section_id: 360000278975
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Git is the most universally adopted version control software and is
often used alongside remote repositories like GitHub and GitLab for
developing, managing and distributing code.

Full Git documentation can be
found [here](https://git-scm.com/docs/git), or using `man git`.

![Git\_Diagram.svg](../../assets/images/Git_Diagram.svg)

## Authentication

In order to pull from a private repo, or push changes to a remote, you
need to authenticate yourself on the cluster.
!!! info Password authentication
>
> GitHub removed support for password authentication on August 13, 2021.
> Using a SSH key is now the easiest way to set up authentication.

### SSH Authentication (GitHub)

More information can be found in the [GitHub
documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

-   On the NeSI cluster, run the command 

        ssh-keygen -t ed25519 -C "your_github_account@example.com"

-   When prompted for a file name, press `enter`. When prompted for a
    passcode, press enter twice more.

-   Open up the newly created .pub key with the command 

        cat ~/.ssh/id_ed25519.pub

    (or whatever you named the key). It should look something like: 

        ssh-ed25519 ABCDEFGKSAfjksjafkjsaLJfakjJF your_github_account@example.com

    Copy the whole key.

-   Now log in to your github account. In the upper-right corner of any
    page, click your profile photo click **Settings**.

    ![Settings icon in the user
    bar](../../assets/images/userbar-account-settings.png)

-   In the "Access" section of the sidebar, click **SSH and GPG keys**.

-   Click **New SSH key** or **Add SSH key**.

    There should be an image here but it couldn't be loaded.

-   In the "Title" field, put "Mahuika" or "NeSI".

-   Paste your key into the "Key" field.

    There should be an image here but it couldn't be loaded.

-   Click **Add SSH key**.

-   Switching back to your terminal on the cluster, you can test your
    connection with the command 

        ssh -T git@github.com

    You may be promted to authenticate, if so type 'yes'  
    If everything is working, you should see the message 

        Hi User! You've successfully authenticated, but GitHub does not provide shell access.

## Basics

You can create a repository with either of the following commands.

|       |                                                       |                                                         |
|-------|-------------------------------------------------------|---------------------------------------------------------|
| clone | `git clone https://github.com/nesi/perf-training.git` | Copies a remote repository into your current directory. |
| init  | `git init`                                            | Creates a new empty repo in your current directory.     |

 

|         |                                  |                                                                                                                          |
|---------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| add     | `git add <file1> <file2>`        | Adds `<file1>` and `<file2>` to the staging area.                                                                        |
|         | `git add *.py`                   |  Adds all python files in the current directory to the staging area.                                                     |
| status  | `git status`                     | Lists changes in working directory, and staged files.                                                                    |
| commit  | `git commit`                     | Records everything in the staging area to your repository. The default text editor will prompt you for a commit message. |
|         | `git commit -m "Commit message"` | Records everything in the staging area to your repository with the commit message "Commit message"                       |
|         | `git commit --amend`             | Modify last commit instead of creating a new one. Useful for fixing small mistakes.                                      |
| log     | `git log`                        | Prints commit history of repo.                                                                                           |
|         | `git log <filename>`             | Prints commit history of `<filename>`.                                                                                   |
| reset   | `git reset`                      | Removes all files from staging area. (Opposite of `git add`)                                                             |
|         | `git reset <filename>`           | Removes `<filename>` from staging area.                                                                                  |

## Remote

By default, fetch, pull and push will operate on the origin repo. This
will be the repo you cloned from, or set manually using
` git branch --set-upstream-to <origin>`.

|        |                             |                                                                                                                      |
|--------|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
| fetch  | `git fetch`                 | Gets status of 'origin'. git fetch **does not **change your working directory or local repository (see `git pull`).  |
|        | `git fetch <repo> <branch>` | Get status of `<repo>` `<branch>`.                                                                                   |
| pull   | `git pull`                  | Incorporates changes from 'origin' into local repo.                                                                  |
|        | `git pull <repo> <branch>`  | Incorporates changes from `<repo>` `<branch>` into local repo.                                                       |
| push   | `git push`                  | Incorporates changes from local repo into 'origin'.                                                                  |
|        | `git push <repo> <branch>`  | Incorporates changes from local repo into `<repo>` `<branch>`                                                        |
!!! info Tip
>
> If you are working without collaborators, there should be no reason to
> have a conflict between your local and your remote repo. Make sure you
> always git pull when starting work on your local and git push when
> finished, this will save you wasting time resolving unnecessary
> merges.

## Branches

At an introductory level, it is best to avoid workflows that lead to
multiple branches, or requires merging.

|          |                              |                                            |
|----------|------------------------------|--------------------------------------------|
| branch   | `git branch`                 | List branches.                             |
|          | `git branch <branch-name>`   | Create new branch `<branch-name`           |
| checkout | `git checkout <branch-name>` | Switch to editing branch `<branch-name>`   |
| merge    | `git merge <branch-name>`    | Merge `<branch-name>` into current branch. |
!!! info Other Resources
>
> -   <https://ohshitgit.com/>
