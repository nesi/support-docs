Git is the most universally adopted version control software and is
often used alongside remote repositories like GitHub and GitLab for
developing, managing and distributing code.

Full Git documentation can be
found [here](https://git-scm.com/docs/git), or using `man git`.

![Git\_Diagram.svg](https://support.nesi.org.nz/hc/article_attachments/360004194235/Git_Diagram.svg)

## Authentication

In order to pull from a private repo, or push changes to a remote, you
need to authenticate yourself on the cluster.

> ### Password authentication {#prerequisites}
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

    [![Settings icon in the user
    bar](https://docs.github.com/assets/cb-34573/images/help/settings/userbar-account-settings.png)]{.procedural-image-wrapper}

-   In the \"Access\" section of the sidebar, click **SSH and GPG
    keys**.

-   Click **New SSH key** or **Add SSH key**.

    [![SSH Key
    button](https://docs.github.com/assets/cb-28257/images/help/settings/ssh-add-ssh-key-with-auth.png)]{.procedural-image-wrapper}

-   In the \"Title\" field, put \"Mahuika\" or \"NeSI\".

-   Paste your key into the \"Key\" field.

    [![The key
    field](https://docs.github.com/assets/cb-47495/images/help/settings/ssh-key-paste-with-type.png)]{.procedural-image-wrapper}

-   Click **Add SSH key**.

-   Switching back to your terminal on the cluster, you can test your
    connection with the command 

        ssh -T git@github.com

    You may be promted to authenticate, if so type \'yes\'\
    If everything is working, you should see the message 

        Hi User! You've successfully authenticated, but GitHub does not provide shell access.

## Basics

You can create a repository with either of the following commands.

  ------- ------------------------------------------------------- ---------------------------------------------------------
  clone   `git clone https://github.com/nesi/perf-training.git`   Copies a remote repository into your current directory.
  init    `git init`                                              Creates a new empty repo in your current directory.
  ------- ------------------------------------------------------- ---------------------------------------------------------

 

<table style="height: 678px; width: 974px;">
<tbody>
<tr style="height: 89px;">
<td style="width: 142px; height: 89px;" rowspan="2">
add

</td>
<td style="width: 310px; height: 89px;">
`git add <file1> <file2>`

</td>
<td style="width: 513px; height: 89px;">
Adds `<file1>` and `<file2>` to the staging area.

</td>
</tr>
<tr style="height: 89px;">
<td style="width: 310px; height: 89px;">
[`git add *.py`]{.c}

</td>
<td style="width: 513px; height: 89px;">
 Adds all python files in the current directory to the staging area.

</td>
</tr>
<tr style="height: 41px;">
<td style="width: 142px; height: 41px;">
status

</td>
<td style="width: 310px; height: 41px;">
[`git status`]{.c}

</td>
<td style="width: 513px; height: 41px;">
Lists changes in working directory, and staged files.

</td>
</tr>
<tr style="height: 39px;">
<td style="width: 142px; height: 39px;" rowspan="3">
commit 

</td>
<td style="width: 310px; height: 39px;">
`git commit`

</td>
<td style="width: 513px; height: 39px;">
Records everything in the staging area to your repository. The default
text editor will prompt you for a commit message.

</td>
</tr>
<tr style="height: 39px;">
<td style="width: 310px; height: 39px;">
[`git commit -m "Commit message"`]{.c}

</td>
<td style="width: 513px; height: 39px;">
Records everything in the staging area to your repository with the
commit message \"Commit message\"

</td>
</tr>
<tr style="height: 39px;">
<td style="width: 310px; height: 39px;">
[`git commit --amend`]{.c}

</td>
<td style="width: 513px; height: 39px;">
Modify last commit instead of creating a new one. Useful for fixing
small mistakes.

</td>
</tr>
<tr style="height: 41px;">
<td style="width: 142px; height: 41px;" rowspan="2">
log 

</td>
<td style="width: 310px; height: 41px;">
`git log`

</td>
<td style="width: 513px; height: 41px;">
Prints commit history of repo.

</td>
</tr>
<tr style="height: 41px;">
<td style="width: 310px; height: 41px;">
`git log <filename>`

</td>
<td style="width: 513px; height: 41px;">
Prints commit history of `<filename>`.

</td>
</tr>
<tr style="height: 41px;">
<td style="width: 142px; height: 41px;" rowspan="2">
reset 

</td>
<td style="width: 310px; height: 41px;">
`git reset`

</td>
<td style="width: 513px; height: 41px;">
Removes all files from staging area. (Opposite of `git add`)

</td>
</tr>
<tr style="height: 41px;">
<td style="width: 310px; height: 41px;">
`git reset <filename>`

</td>
<td style="width: 513px; height: 41px;">
Removes `<filename>` from staging area.

</td>
</tr>
</tbody>
</table>
## Remote

By default, fetch, pull and push will operate on the origin repo. This
will be the repo you cloned from, or set manually using
` git branch --set-upstream-to   <origin>`.

<table style="height: 76px; width: 1050px;">
<tbody>
<tr>
<td style="width: 136px;" rowspan="2">
fetch 

</td>
<td style="width: 565.701px;">
`git fetch`

</td>
<td style="width: 310.299px;">
Gets status of \'origin\'. git fetch **does not **change your working
directory or local repository (see `git pull`). 

</td>
</tr>
<tr>
<td style="width: 565.701px;">
`git fetch <repo> <branch>`

</td>
<td style="width: 310.299px;">
Get status of `<repo>` `<branch>`.

</td>
</tr>
<tr>
<td style="width: 136px;" rowspan="2">
pull 

</td>
<td style="width: 565.701px;">
`git pull`

</td>
<td style="width: 310.299px;">
Incorporates changes from \'origin\' into local repo. 

</td>
</tr>
<tr>
<td style="width: 565.701px;">
`git pull <repo> <branch>`

</td>
<td style="width: 310.299px;">
Incorporates changes from `<repo>` `<branch>` into local repo.

</td>
</tr>
<tr>
<td style="width: 136px;" rowspan="2">
push 

</td>
<td style="width: 565.701px;">
`git push`

</td>
<td style="width: 310.299px;">
Incorporates changes from local repo into \'origin\'. 

</td>
</tr>
<tr>
<td style="width: 565.701px;">
`git push <repo> <branch>`

</td>
<td style="width: 310.299px;">
Incorporates changes from local repo into `<repo>` `<branch>`

</td>
</tr>
</tbody>
</table>
> ### Tip {#prerequisites}
>
> If you are working without collaborators, there should be no reason to
> have a conflict between your local and your remote repo. Make sure you
> always git pull when starting work on your local and git push when
> finished, this will save you wasting time resolving unnecessary
> merges.

## Branches

At an introductory level, it is best to avoid workflows that lead to
multiple branches, or requires merging.

<table style="height: 76px; width: 966px;">
<tbody>
<tr>
<td style="width: 136px;" rowspan="2">
branch 

</td>
<td style="width: 303px;">
`git branch`

</td>
<td style="width: 489px;">
List branches.

</td>
</tr>
<tr>
<td style="width: 303px;">
`git branch <branch-name>`

</td>
<td style="width: 489px;">
Create new branch `<branch-name`

</td>
</tr>
<tr>
<td style="width: 136px;">
checkout

</td>
<td style="width: 303px;">
`git checkout <branch-name>`

</td>
<td style="width: 489px;">
Switch to editing branch `<branch-name>`

</td>
</tr>
<tr>
<td style="width: 136px;">
merge

</td>
<td style="width: 303px;">
`git merge <branch-name>`

</td>
<td style="width: 489px;">
Merge `<branch-name>` into current branch.

</td>
</tr>
</tbody>
</table>
> ### Other Resources {#prerequisites}
>
> -   <https://ohshitgit.com/>
