---
created_at: '2016-03-14T01:52:06Z'
hidden: false
label_names: []
position: 0
title: Converting from Windows-style to UNIX-style line endings
vote_count: 43
vote_sum: 9
zendesk_article_id: 218032857
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->
<div class="toc">
<h2>The Problem</h2>
</div>
<p>In a plain text file, to tell the computer that a line of text doesn't continue forever, the end of each line is marked by a sequence of one or more invisible characters, called <em>control characters</em>. While there are many control characters for different purposes, the relevant ones for line endings are the carriage return (CR) and line feed (LF) characters.</p>
<p>Unfortunately, the programmers of different operating systems have represented line endings using different sequences:</p>
<ul>
<li>All versions of Microsoft Windows represent line endings as CR followed by LF.</li>
<li>UNIX and UNIX-like operating systems (including Mac OS X) represent line endings as LF alone.</li>
</ul>
<p>Therefore, a text file prepared in a Windows environment will, when copied to a UNIX-like environment such as a NeSI cluster, have an unnecessary carriage return character at the end of each line. To make matters worse, this character will normally be invisible, though in some text editors it will show up as ^M or similar.</p>
<p>Many programs, including the Slurm and LoadLeveler batch queue schedulers, will give errors when given a file containing carriage return characters as input.</p>
<p>Therefore, you will need to convert any such file so it has only UNIX-style line endings before using it on a NeSI cluster.</p>
<h2 id="the-symptoms">The Symptoms</h2>
<h3 id="in-the-slurm-job-scheduler">In the Slurm job scheduler</h3>
<p>If you submit (using <code>sbatch</code>) a Slurm submission script with Windows-style line endings, you will likely receive the following error:</p>
<pre><code class="bash">sbatch: error: Batch script contains DOS line breaks (\r\n) 
sbatch: error: instead of expected UNIX line breaks (\n).
</code></pre>
<h3 id="in-other-programs">In other programs</h3>
<p>Some UNIX or Linux programs are tolerant to Windows-style line endings, while others give errors. The text of the error is almost infinitely variable, but program behaviours might include the following responses:</p>
<ul>
<li>Explicitly stating the problem with line endings</li>
<li>Complaining more vaguely that the input data is incomplete or corrupt or that there are problems reading it</li>
<li>Failing in a more serious way such as a segmentation fault</li>
</ul>
<h2 id="checking-a-files-line-ending-format">Checking a file's line ending format</h2>
<p>If you have what you think is a text file on the cluster but you don't know whether its line endings are in the correct format or not, you can run the following command:</p>
<pre><code class="bash">file foo.txt          # Replace foo.txt with the name of your file
</code></pre>
<p>Depending on the contents of <code>foo.txt</code>, the output of this command may vary, but if the output has "CR" or "CRLF" in it, you will need to convert <code>foo.txt</code> to UNIX format line endings if you want to use it on the cluster.</p>
<h2 id="how-to-convert">How to Convert</h2>
<h3 id="converting-using-notepad">Converting using Notepad++</h3>
<p>In the Windows text editing program Notepad++ (not to be confused with ordinary Notepad), there is a function to prepare text files with UNIX-style line endings.</p>
<p>To write your file in this way, while you have the file open, go to the Edit menu, select the "EOL Conversion" submenu, and from the options that come up select "UNIX/OSX Format". The next time you save the file, its line endings will, all going well, be saved with UNIX-style line endings.</p>
<p>You can check what format line endings you are currently editing in by looking in the status bar at the bottom of the window. Between the range box (a box containing Ln, Col and Sel entries) and the text encoding box (which will contain UTF-8, ANSI, or some other technical string) will be a box containing the current line ending format.</p>
<ul>
<li>In most cases, this box will contain the text "DOS\Windows".</li>
<li>In a few cases, such as the file having been prepared on a UNIX or Linux machine or a Mac, it will contain the text "UNIX".</li>
<li>It is possible, though highly unlikely by now, that the file may have old-style (pre-OSX) Mac line endings, in which case the box will contain the text "Macintosh".</li>
</ul>
<p>Please note that if you change a file's line ending style, you must save your changes before copying the file anywhere, including to a cluster.</p>
<h3 id="converting-using-dos2unix">Converting using dos2unix</h3>
<p>Suppose, though, that you've copied a text file to the cluster already, and you realise you need to convert it to UNIX format. How do you do that?</p>
<p>Simple: Use the program <code>dos2unix</code>.</p>
<p>Just give the name of your file to <code>dos2unix</code> as an argument, and it will convert the file's line endings to UNIX format:</p>
<pre><code class="bash">dos2unix foo.txt      # Replace foo.txt with the name of your file
</code></pre>
<p>There are other options in the rare case that you don't want to just modify your existing file; run <code>man dos2unix</code> for details.</p>