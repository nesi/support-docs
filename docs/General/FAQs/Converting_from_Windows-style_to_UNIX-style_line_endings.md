In a plain text file, to tell the computer that a line of text doesn\'t
continue forever, the end of each line is marked by a sequence of one or
more invisible characters, called *control characters*. While there are
many control characters for different purposes, the relevant ones for
line endings are the carriage return (CR) and line feed (LF) characters.

Unfortunately, the programmers of different operating systems have
represented line endings using different sequences:

-   All versions of Microsoft Windows represent line endings as CR
    followed by LF.
-   UNIX and UNIX-like operating systems (including Mac OS X) represent
    line endings as LF alone.

Therefore, a text file prepared in a Windows environment will, when
copied to a UNIX-like environment such as a NeSI cluster, have an
unnecessary carriage return character at the end of each line. To make
matters worse, this character will normally be invisible, though in some
text editors it will show up as \^M or similar.

Many programs, including the Slurm and LoadLeveler batch queue
schedulers, will give errors when given a file containing carriage
return characters as input.

Therefore, you will need to convert any such file so it has only
UNIX-style line endings before using it on a NeSI cluster.

The Symptoms
------------

### In the Slurm job scheduler

If you submit (using `sbatch`) a Slurm submission script with
Windows-style line endings, you will likely receive the following error:

    sbatch: error: Batch script contains DOS line breaks (\r\n) 
    sbatch: error: instead of expected UNIX line breaks (\n).

### In other programs

Some UNIX or Linux programs are tolerant to Windows-style line endings,
while others give errors. The text of the error is almost infinitely
variable, but program behaviours might include the following responses:

-   Explicitly stating the problem with line endings
-   Complaining more vaguely that the input data is incomplete or
    corrupt or that there are problems reading it
-   Failing in a more serious way such as a segmentation fault

Checking a file\'s line ending format
-------------------------------------

If you have what you think is a text file on the cluster but you don\'t
know whether its line endings are in the correct format or not, you can
run the following command:

    file foo.txt          # Replace foo.txt with the name of your file

Depending on the contents of `foo.txt`, the output of this command may
vary, but if the output has \"CR\" or \"CRLF\" in it, you will need to
convert `foo.txt` to UNIX format line endings if you want to use it on
the cluster.

How to Convert
--------------

### Converting using Notepad++

In the Windows text editing program Notepad++ (not to be confused with
ordinary Notepad), there is a function to prepare text files with
UNIX-style line endings.

To write your file in this way, while you have the file open, go to the
Edit menu, select the \"EOL Conversion\" submenu, and from the options
that come up select \"UNIX/OSX Format\". The next time you save the
file, its line endings will, all going well, be saved with UNIX-style
line endings.

You can check what format line endings you are currently editing in by
looking in the status bar at the bottom of the window. Between the range
box (a box containing Ln, Col and Sel entries) and the text encoding box
(which will contain UTF-8, ANSI, or some other technical string) will be
a box containing the current line ending format.

-   In most cases, this box will contain the text \"DOS\\Windows\".
-   In a few cases, such as the file having been prepared on a UNIX or
    Linux machine or a Mac, it will contain the text \"UNIX\".
-   It is possible, though highly unlikely by now, that the file may
    have old-style (pre-OSX) Mac line endings, in which case the box
    will contain the text \"Macintosh\".

Please note that if you change a file\'s line ending style, you must
save your changes before copying the file anywhere, including to a
cluster.

### Converting using dos2unix

Suppose, though, that you\'ve copied a text file to the cluster already,
and you realise you need to convert it to UNIX format. How do you do
that?

Simple: Use the program `dos2unix`.

Just give the name of your file to `dos2unix` as an argument, and it
will convert the file\'s line endings to UNIX format:

    dos2unix foo.txt      # Replace foo.txt with the name of your file

There are other options in the rare case that you don\'t want to just
modify your existing file; run `man dos2unix` for details.
