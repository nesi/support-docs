Regardless of the operating system of your personal computer you will
need to know some basic Unix Shell commands since the HPC are Linux
machines. If you do not have any experiencing using Unix Shell we would
advise going at least the first (3 parts) of the [Software Carpentry
Unix Shell lessons](http://swcarpentry.github.io/shell-novice/).

 

**Command**

**Examples of use**

**Description**

ls

ls

Lists the files in your current directory.

ls /path/to/directory/

Lists the files in the specified directory.

ls -ltra

Lists all files, including hidden ones (-a), in long format (-l), in
reverse order (-r) of time since edited (t) (meaning that the newest
file is at the bottom of the page.

pwd

pwd

Prints the path of your current working directory.

cd

cd /path/to/directory/

Changes your current directory to the specified directory.

touch

touch file.txt

Created an empty file of specified name.

nano

nano

Opens the nano text editor.

nano file.txt

Opens the specified file in the nano text editor.

head

head file.txt

Prints the top 10 lines of the specified file.

head -n 2 file.txt

Prints the top n lines of the specified file (in this case 2).

tail

tail file.txt

Prints the bottom 10 lines of the specified file.

tail -n 2 file.txt

Prints the bottom n lines of the specified file (in this case 2).

mv

mv file.txt newname.txt

rename the file.

mv file.txt /path/to/destination/

Move the file to the specified directory.

mv -r directory/ /path/to/destination/

Recursively move the directory and all contained files and directories
to the specified path.

cp

cp file.txt /path/to/destination/

Make a copy of the file in the specified directory.

cp file.txt /path/to/destination/newname.txt

Make a copy of the file in the specified directory with the specified
name.

cp -r directory/ /path/to/destination/

Recursively copy all files and directories of a directory to the
specified location.

rm

rm file.txt

Delete the specified file.

rm -r directory/

Recursively delete the files and directories of the specified directory.

mkdir

mkdir directory

Create a directory of the specified name.

man

man ls

Bring up the manual of a command (in this case ls).

> ### Tip {#prerequisites}
>
> Pressing the \'tab\' key once will automatically complete the line if
> it is the only option. e.g. 
>
> ![complete1.gif](https://support.nesi.org.nz/hc/article_attachments/360004748996/complete1.gif)
>
> If there are more than one possible completions, pressing tab again
> will show all those options.
>
> ![complete2.gif](https://support.nesi.org.nz/hc/article_attachments/360004621875/complete2.gif)
>
> Use of the tab key can help navigate the filesystem, spellcheck your
> commands and save you time typing.
