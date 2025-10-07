---
title: "NeSI Filesystem"
teaching: 15
exercises: 5
questions:
- "Where is the best place to store my data?"
- "How do I recover deleted files?"
- "How do I find out how much disk space I have?"
objectives:
- "Learn about the NeSI filesystems, and when to use each one."
keypoints:
- ""

---

The NeSI filesystem looks something like this:

![The file system is made up of a root directory that contains sub-directories
titled home, nesi, and system files](../fig/NesiFiletree.svg)

The directories that are relevant to us are.

<table style="width: 100%; height: 90px;">
<tbody>
<tr>
<td style="width: 300px;"></td>
<td style="width: 250px;">Location</td>
<td style="width: 167.562px;">Default Storage</td>
<td style="width: 142.734px;">Default Files</td>
<td style="width: 89.3594px;">Backup</td>
<td style="width: 155.188px;">Access Speed</td>
</tr>
<tr>
<td style="width: 300px;"><strong>Home</strong> is for user-specific files such as configuration files, environment setup, source code, etc.</td>
<td style="width: 250px;"><code>/home/&lt;username&gt;</code></td>
<td style="width: 167.562px;">20GB</td>
<td style="width: 142.734px;">1,000,000</td>
<td style="width: 89.3594px;">Daily</td>
<td style="width: 155.188px;">Normal</td>
</tr>
<tr>
<td style="width: 300px;"><strong>Project</strong> is for persistent project-related data, project-related software, etc.</td>
<td style="width: 250px;"><code>/nesi/project/&lt;projectcode&gt;</code></td>
<td style="width: 167.562px;">100GB</td>
<td style="width: 142.734px;">100,000</td>
<td style="width: 89.3594px;">Daily</td>
<td style="width: 155.188px;">Normal</td>
</tr>
<tr>
<td style="width: 300px;"><strong>Nobackup</strong> is a 'scratch space', for data you don't need to keep long term. Old data is periodically deleted from nobackup</td>
<td style="width: 250px;"><code>/nesi/nobackup/&lt;projectcode&gt;</code></td>
<td style="width: 167.562px;">10TB</td>
<td style="width: 142.734px;">1,000,000</td>
<td style="width: 89.3594px;">None</td>
<td style="width: 155.188px;">Fast</td>
</tr>
</tbody>
</table>

### Managing your data and storage (backups and quotas)

NeSI performs backups of the `/home` and `/nesi/project` (persistent) filesystems.  However, backups are only captured once per day.  So, if you edit or change code or data and then immediately delete it, it likely cannot be recovered.  Note, as the name suggests, NeSI does **not** backup the `/nesi/nobackup` filesystem.

Protecting critical data from corruption or deletion is primarily your
responsibility. Ensure you have a data management plan and stick to the plan to reduce the chance of data loss.  Also important is managing your storage quota.  To check your quotas, use the `nn_storage_quota` command, eg

{% include {{ site.snippets }}/filedir/sinfo.snip %}

As well as disk space, 'inodes' are also tracked, this is the *number* of files.

Notice that the project space for this user is over quota and has been locked, meaning no more data can be added.  When your space is locked you will need to move or remove data.  Also note that none of the nobackup space is being used.  Likely data from project can be moved to nobackup. `nn_storage_quota` uses cached data, and so will no immediately show changes to storage use.

For more details on our persistent and nobackup storage systems, including data retention and the nobackup autodelete schedule,
please see our [Filesystem and Quota](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/NeSI_File_Systems_and_Quotas/) documentation.

### Working Directory

We will be working from the directory `{{ site.working_dir[-1] }}`.

```
{{ site.remote.prompt }} cd {{ site.working_dir | join: '/' }}
```

{: .language-bash}

### Creating directories

<!-- NOTE: This bit uses relative paths even though the convept hasn't been introduced yet. -->

As previously mentioned, it is general useful to organise your work in a hierarchical file structure to make managing and finding files easier. It is also is especially important when working within a shared directory with colleagues, such as a project, to minimise the chance of accidentally affecting your colleagues work. So for this workshop you will each make a directory using the `mkdir` command within the workshops directory for you to personally work from.

```
{{ site.remote.prompt }} mkdir <username>
```

{: .language-bash}

You should then be able to see your new directory is there using `ls`.

```
{{ site.remote.prompt }} ls {{ site.working_dir | join: '/' }}
```

{: .language-bash}

{% include {{ site.snippets }}/filedir/dir-contents1.snip %}

## Create a text file

Now let's create a file. To do this we will use a text editor called Nano to create a file called `draft.txt`:

We will want to do this from inside the directory we just created.

```
{{ site.remote.prompt }} cd <username>
{{ site.remote.prompt }} nano draft.txt
```

{: .language-bash}

> ## Which Editor?
>
> When we say, '`nano` is a text editor' we really do mean 'text': it can
> only work with plain character data, not tables, images, or any other
> human-friendly media. We use it in examples because it is one of the
> least complex text editors. However, because of this trait, it may
> not be powerful enough or flexible enough for the work you need to do
> after this workshop. On Unix systems (such as Linux and macOS),
> many programmers use [Emacs](http://www.gnu.org/software/emacs/) or
> [Vim](http://www.vim.org/) (both of which require more time to learn),
> or a graphical editor such as
> [Gedit](http://projects.gnome.org/gedit/). On Windows, you may wish to
> use [Notepad++](http://notepad-plus-plus.org/).  Windows also has a built-in
> editor called `notepad` that can be run from the command line in the same
> way as `nano` for the purposes of this lesson.
>
> No matter what editor you use, you will need to know where it searches
> for and saves files. If you start it from the shell, it will (probably)
> use your current working directory as its default location. If you use
> your computer's start menu, it may want to save files in your desktop or
> documents directory instead. You can change this by navigating to
> another directory the first time you 'Save As...'
{: .callout}

Let's type in a few lines of text.
Once we're happy with our text, we can press <kbd>Ctrl</kbd>+<kbd>O</kbd>
(press the <kbd>Ctrl</kbd> or <kbd>Control</kbd> key and, while
holding it down, press the <kbd>O</kbd> key) to write our data to disk
(we'll be asked what file we want to save this to:
press <kbd>Return</kbd> to accept the suggested default of `draft.txt`).

<div style="width:80%; margin: auto;"><img alt="screenshot of nano text editor in action"
src="../fig/nano-screenshot.png"></div>

Once our file is saved, we can use <kbd>Ctrl</kbd>+<kbd>X</kbd> to quit the editor and
return to the shell.

> ## Control, Ctrl, or ^ Key
>
> The Control key is also called the 'Ctrl' key. There are various ways
> in which using the Control key may be described. For example, you may
> see an instruction to press the <kbd>Control</kbd> key and, while holding it down,
> press the <kbd>X</kbd> key, described as any of:
>
> * `Control-X`
> * `Control+X`
> * `Ctrl-X`
> * `Ctrl+X`
> * `^X`
> * `C-x`
>
> In nano, along the bottom of the screen you'll see `^G Get Help ^O WriteOut`.
> This means that you can use `Control-G` to get help and `Control-O` to save your
> file.
{: .callout}

`nano` doesn't leave any output on the screen after it exits,
but `ls` now shows that we have created a file called `draft.txt`:

```
{{ site.remote.prompt }} ls
```

{: .language-bash}

```
draft.txt
```

{: .output}

## Copying files and directories

In a future lesson, we will be running the R script ```{{ site.working_dir | join: '/' }}/{{ site.example.script }} ```, but as we can't all work on the same file at once you will need to take your own copy. This can be done with the **c**o**p**y command `cp`, at least two arguments are needed the file (or directory) you want to copy, and the directory (or file) where you want the copy to be created. We will be copying the file into the directory we made previously, as this should be your current directory the second argument can be a simple `.`.

```
{{ site.remote.prompt }} cp {{ site.working_dir | join: '/' }}/{{ site.example.script }}  .
```

{: .output}

We can check that it did the right thing using `ls`

```
{{ site.remote.prompt }} ls
```

{: .language-bash}

```
draft.txt   {{ site.example.script }} 
```

{: .output}
