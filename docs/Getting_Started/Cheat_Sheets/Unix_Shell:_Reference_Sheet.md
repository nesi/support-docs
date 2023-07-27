---
created_at: '2020-02-25T02:45:24Z'
hidden: false
label_names: []
position: 0
title: 'Unix Shell: Reference Sheet'
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001393596
zendesk_section_id: 360000278975
---

Regardless of the operating system of your personal computer you will
need to know some basic Unix Shell commands since the HPC are Linux
machines. If you do not have any experiencing using Unix Shell we would
advise going at least the first (3 parts) of the [Software Carpentry
Unix Shell lessons](http://swcarpentry.github.io/shell-novice/).

 

<table style="height: 410px; width: 746px;">
<tbody>
<tr>
<td style="width: 66px;">

**Command**

</td>
<td style="width: 400.317px;">

**Examples of use**

</td>
<td style="width: 416.683px;">

**Description**

</td>
</tr>
<tr>
<td style="width: 66px;" rowspan="3">

ls

</td>
<td style="width: 400.317px;">

ls

</td>
<td style="width: 416.683px;">

Lists the files in your current directory.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

ls /path/to/directory/

</td>
<td style="width: 416.683px;">

Lists the files in the specified directory.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

ls -ltra

</td>
<td style="width: 416.683px;">

Lists all files, including hidden ones (-a), in long format (-l), in
reverse order (-r) of time since edited (t) (meaning that the newest
file is at the bottom of the page.

</td>
</tr>
<tr>
<td style="width: 66px;">

pwd

</td>
<td style="width: 400.317px;">

pwd

</td>
<td style="width: 416.683px;">

Prints the path of your current working directory.

</td>
</tr>
<tr>
<td style="width: 66px;">

cd

</td>
<td style="width: 400.317px;">

cd /path/to/directory/

</td>
<td style="width: 416.683px;">

Changes your current directory to the specified directory.

</td>
</tr>
<tr>
<td style="width: 66px;">

touch

</td>
<td style="width: 400.317px;">

touch file.txt

</td>
<td style="width: 416.683px;">

Created an empty file of specified name.

</td>
</tr>
<tr>
<td style="width: 66px;" rowspan="2">

nano

</td>
<td style="width: 400.317px;">

nano

</td>
<td style="width: 416.683px;">

Opens the nano text editor.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

nano file.txt

</td>
<td style="width: 416.683px;">

Opens the specified file in the nano text editor.

</td>
</tr>
<tr>
<td style="width: 66px;" rowspan="2">

head

</td>
<td style="width: 400.317px;">

head file.txt

</td>
<td style="width: 416.683px;">

Prints the top 10 lines of the specified file.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

head -n 2 file.txt

</td>
<td style="width: 416.683px;">

Prints the top n lines of the specified file (in this case 2).

</td>
</tr>
<tr>
<td style="width: 66px;" rowspan="2">

tail

</td>
<td style="width: 400.317px;">

tail file.txt

</td>
<td style="width: 416.683px;">

Prints the bottom 10 lines of the specified file.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

tail -n 2 file.txt

</td>
<td style="width: 416.683px;">

Prints the bottom n lines of the specified file (in this case 2).

</td>
</tr>
<tr>
<td style="width: 66px;" rowspan="3">

mv

</td>
<td style="width: 400.317px;">

mv file.txt newname.txt

</td>
<td style="width: 416.683px;">

rename the file.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

mv file.txt /path/to/destination/

</td>
<td style="width: 416.683px;">

Move the file to the specified directory.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

mv -r directory/ /path/to/destination/

</td>
<td style="width: 416.683px;">

Recursively move the directory and all contained files and directories
to the specified path.

</td>
</tr>
<tr>
<td style="width: 66px;" rowspan="3">

cp

</td>
<td style="width: 400.317px;">

cp file.txt /path/to/destination/

</td>
<td style="width: 416.683px;">

Make a copy of the file in the specified directory.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

cp file.txt /path/to/destination/newname.txt

</td>
<td style="width: 416.683px;">

Make a copy of the file in the specified directory with the specified
name.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

cp -r directory/ /path/to/destination/

</td>
<td style="width: 416.683px;">

Recursively copy all files and directories of a directory to the
specified location.

</td>
</tr>
<tr>
<td style="width: 66px;" rowspan="2">

rm

</td>
<td style="width: 400.317px;">

rm file.txt

</td>
<td style="width: 416.683px;">

Delete the specified file.

</td>
</tr>
<tr>
<td style="width: 400.317px;">

rm -r directory/

</td>
<td style="width: 416.683px;">

Recursively delete the files and directories of the specified directory.

</td>
</tr>
<tr>
<td style="width: 66px;">

mkdir

</td>
<td style="width: 400.317px;">

mkdir directory

</td>
<td style="width: 416.683px;">

Create a directory of the specified name.

</td>
</tr>
<tr>
<td style="width: 66px;">

man

</td>
<td style="width: 400.317px;">

man ls

</td>
<td style="width: 416.683px;">

Bring up the manual of a command (in this case ls).

</td>
</tr>
</tbody>
</table>

> ### Tip
>
> Pressing the 'tab' key once will automatically complete the line if it
> is the only option. e.g. 
>
> ![complete1.gif](../includes/complete1.gif)
>
> If there are more than one possible completions, pressing tab again
> will show all those options.
>
> ![complete2.gif](../includes/complete2.gif)
>
> Use of the tab key can help navigate the filesystem, spellcheck your
> commands and save you time typing.
