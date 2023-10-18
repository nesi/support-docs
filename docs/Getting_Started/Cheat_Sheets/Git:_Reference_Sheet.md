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

![Git\_Diagram.svg](../../../assets/images/Git_Diagram_0.svg)

## Authentication

In order to pull from a private repo, or push changes to a remote, you
need to authenticate yourself on the cluster.
!!! info
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
    bar](../../../assets/images/userbar-account-settings_0.png)

-   In the "Access" section of the sidebar, click **SSH and GPG keys**.

-   Click **New SSH key** or **Add SSH key**.

    ![SSH Key
    button](../../../assets/images/ssh-add-ssh-key-with-auth_0.png)

-   In the "Title" field, put "Mahuika" or "NeSI".

-   Paste your key into the "Key" field.

    ![The key
    field](../../../assets/images/ssh-key-paste-with-type_0.png)

-   Click **Add SSH key**.

-   Switching back to your terminal on the cluster, you can test your
    connection with the command 

        ssh -T git@github.com

    You may be promted to authenticate, if so type 'yes'  
    If everything is working, you should see the message 

        Hi User! You've successfully authenticated, but GitHub does not provide shell access.

## Basics

You can create a repository with either of the following commands.

<table style="height: 153px; width: 972px;">
<tbody>
<tr class="odd" style="height: 22px;">
<td style="width: 184.031px; height: 63px">clone</td>
<td
style="width: 442.969px; height: 63px"><code>git clone https://github.com/nesi/perf-training.git</code></td>
<td style="width: 310px; height: 63px">Copies a remote repository into
your current directory.</td>
</tr>
<tr class="even" style="height: 22px;">
<td style="width: 184.031px; height: 61.1719px">init</td>
<td style="width: 442.969px; height: 21px"><code>git init</code></td>
<td style="width: 310px; height: 21px">Creates a new empty repo in your
current directory.</td>
</tr>
</tbody>
</table>

 

<table style="height: 678px; width: 974px;">
<tbody>
<tr class="odd" style="height: 89px;">
<td rowspan="2" style="width: 142px; height: 89px">add</td>
<td
style="width: 310px; height: 89px"><span><code>git add &lt;file1&gt; &lt;file2&gt;</code></span></td>
<td style="width: 513px; height: 89px">Adds <code>&lt;file1&gt;</code>
and <code>&lt;file2&gt;</code> to the staging area.</td>
</tr>
<tr class="even" style="height: 89px;">
<td
style="width: 310px; height: 89px"><span><code>git add *.py</code></span></td>
<td style="width: 513px; height: 89px"> Adds all python files in the
current directory to the staging area.</td>
</tr>
<tr class="odd" style="height: 41px;">
<td style="width: 142px; height: 41px">status</td>
<td
style="width: 310px; height: 41px"><span><code>git status</code></span></td>
<td style="width: 513px; height: 41px">Lists changes in working
directory, and staged files.</td>
</tr>
<tr class="even" style="height: 39px;">
<td rowspan="3" style="width: 142px; height: 39px">commit </td>
<td
style="width: 310px; height: 39px"><span><code>git commit</code></span></td>
<td style="width: 513px; height: 39px">Records everything in the staging
area to your repository. The default text editor will prompt you for a
commit message.</td>
</tr>
<tr class="odd" style="height: 39px;">
<td
style="width: 310px; height: 39px"><span><code>git commit -m "Commit message"</code></span></td>
<td style="width: 513px; height: 39px">Records everything in the staging
area to your repository with the commit message "Commit message"</td>
</tr>
<tr class="even" style="height: 39px;">
<td
style="width: 310px; height: 39px"><span><code>git commit --amend</code></span></td>
<td style="width: 513px; height: 39px">Modify last commit instead of
creating a new one. Useful for fixing small mistakes.</td>
</tr>
<tr class="odd" style="height: 41px;">
<td rowspan="2" style="width: 142px; height: 41px">log </td>
<td style="width: 310px; height: 41px"><code>git log</code></td>
<td style="width: 513px; height: 41px">Prints commit history of
repo.</td>
</tr>
<tr class="even" style="height: 41px;">
<td
style="width: 310px; height: 41px"><code>git log &lt;filename&gt;</code></td>
<td style="width: 513px; height: 41px">Prints commit history of
<code>&lt;filename&gt;</code>.</td>
</tr>
<tr class="odd" style="height: 41px;">
<td rowspan="2" style="width: 142px; height: 41px">reset </td>
<td style="width: 310px; height: 41px"><code>git reset</code></td>
<td style="width: 513px; height: 41px">Removes all files from staging
area. (Opposite of <code>git add</code>)</td>
</tr>
<tr class="even" style="height: 41px;">
<td
style="width: 310px; height: 41px"><code>git reset &lt;filename&gt;</code></td>
<td style="width: 513px; height: 41px">Removes
<code>&lt;filename&gt;</code> from staging area.</td>
</tr>
</tbody>
</table>

## Remote

By default, fetch, pull and push will operate on the origin repo. This
will be the repo you cloned from, or set manually using
` git branch --set-upstream-to <origin>`.

<table style="height: 76px; width: 1050px;">
<tbody>
<tr class="odd">
<td rowspan="2" style="width: 136px">fetch </td>
<td style="width: 565.701px"><code>git fetch</code></td>
<td style="width: 310.299px">Gets status of 'origin'. git fetch
<strong>does not </strong>change your working directory or local
repository (see <code>git pull</code>). </td>
</tr>
<tr class="even">
<td
style="width: 565.701px"><code>git fetch &lt;repo&gt; &lt;branch&gt;</code></td>
<td style="width: 310.299px">Get status of <code>&lt;repo&gt;</code>
<code>&lt;branch&gt;</code>.</td>
</tr>
<tr class="odd">
<td rowspan="2" style="width: 136px">pull </td>
<td style="width: 565.701px"><code>git pull</code></td>
<td style="width: 310.299px">Incorporates changes from 'origin' into
local repo. </td>
</tr>
<tr class="even">
<td
style="width: 565.701px"><code>git pull &lt;repo&gt; &lt;branch&gt;</code></td>
<td style="width: 310.299px">Incorporates changes from
<code>&lt;repo&gt;</code> <code>&lt;branch&gt;</code> into local
repo.</td>
</tr>
<tr class="odd">
<td rowspan="2" style="width: 136px">push </td>
<td style="width: 565.701px"><code>git push</code></td>
<td style="width: 310.299px">Incorporates changes from local repo into
'origin'. </td>
</tr>
<tr class="even">
<td
style="width: 565.701px"><code>git push &lt;repo&gt; &lt;branch&gt;</code></td>
<td style="width: 310.299px">Incorporates changes from local repo into
<code>&lt;repo&gt;</code> <code>&lt;branch&gt;</code></td>
</tr>
</tbody>
</table>
!!! info
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
<tr class="odd">
<td rowspan="2" style="width: 136px">branch </td>
<td style="width: 303px"><code>git branch</code></td>
<td style="width: 489px">List branches.</td>
</tr>
<tr class="even">
<td
style="width: 303px"><code>git branch &lt;branch-name&gt;</code></td>
<td style="width: 489px">Create new branch
<code>&lt;branch-name</code></td>
</tr>
<tr class="odd">
<td style="width: 136px">checkout</td>
<td
style="width: 303px"><code>git checkout &lt;branch-name&gt;</code></td>
<td style="width: 489px">Switch to editing branch
<code>&lt;branch-name&gt;</code></td>
</tr>
<tr class="even">
<td style="width: 136px">merge</td>
<td style="width: 303px"><code>git merge &lt;branch-name&gt;</code></td>
<td style="width: 489px">Merge <code>&lt;branch-name&gt;</code> into
current branch.</td>
</tr>
</tbody>
</table>
!!! info
>
> -   <https://ohshitgit.com/>
