---
created_at: '2015-08-18T02:30:33Z'
hidden: false
label_names:
- mahuika
- general
position: 31
title: Java
vote_count: 0
vote_sum: 0
zendesk_article_id: 207765367
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->
<div class="toc"> </div>
<h1 id="description">Description</h1>
<p>Java is a computer programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible. It is intended to let application developers "write once, run anywhere" (WORA), meaning that code that runs on one platform does not need to be recompiled to run on another. Java applications are typically compiled to bytecode (class file) that can run on any Java virtual machine (JVM) regardless of computer architecture. The language derives much of its syntax from C and C++, but it has fewer low-level facilities.</p>
<p>The Java home page is at <a href="http://www.java.com">http://www.java.com</a>.</p>
<h1 id="licensing-requirements">Licensing requirements</h1>
<p>All versions of Java on NeSI clusters have been made available by their respective owners at no cost under a limited, closed-source licence. The full licence terms and conditions for any given version of Java can be found by following the directions in <code>${JAVA_HOME}/LICENSE</code>.</p>
<h1 id="example-scripts">Example scripts</h1>
<h2 id="example-script-for-the-pan-cluster">Example script for Mahuika</h2>
<pre><code class="bash">#!/bin/bash -e
#SBATCH --job-name      MyMultithreadedJavaJob<br>#SBATCH --time          1:00:00          # 1 hour walltime limit
#SBATCH --cpus-per-task 8                # 8 CPU cores for 8 Java threads
#SBATCH --mem           4096MB           # 4 GB of memory

module load Java/1.8.0_144<br># The following line is needed in case your Java application<br># is called indirectly<br>export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR}<br>java -Xmx3g -Djava.io.tmpdir=${TMPDIR} -jar /path/to/foo.jar<br></code></pre>
<h1 id="further-notes">Further notes</h1>
<h2>Java Versions</h2>
<p>The default version of Java that is packaged with the operating system may not be appropriate for your work.  To use a different version of Java us the `module` command to find and load for example:</p>
<pre>$ module spider Java<br>-----------------------------------------------------------------------<br>-----------------------------------------------------------------------<br>Java Platform, Standard Edition (Java SE) lets you develop and deploy <br>Java applications on desktops and servers.<br><br>Versions:<br>Java/1.7.0_51<br>Java/1.8.0_144<br>Java/11.0.4<br>Java/15.0.2<br><br>$ module load Java/15.0.2</pre>
<h2 id="memory-management-and-the-xmx-option">Memory management and the -Xmx option</h2>
<p>It is important to let the Java virtual machine know how much memory it is allowed to use.   The main way this is done is via the <code>-Xmx</code> option, which sets the maximum amount of heap space that it can use.</p>
<p>As a first approximation, we recommend setting the <code>-Xmx</code> option to 75% of the requested memory. For example, if your job asks the scheduler for 32 GB of memory, you should provide the Java executable with <code>-Xmx24g</code>, which will cap its heap usage to 24 GB, leaving at least 6 GB for its stack and any other overheads.</p>
<h2>Temporary Files</h2>
<p>Java programs which use temporary files can (and should) generally be persuaded to use $TMPDIR rather than just the default of <code>/tmp </code>by being given the option <code>-Djava.io.tmpdir=$TMPDIR.</code>  TMPDIR is automatically removed at the end of the job.</p>
<ul>
<li>If you run your Java program by using the <code>java</code> command, that is in a form like <code>java &lt;java_options&gt; java.program &lt;specific_program_options&gt;</code>, you can specify the tmpdir as follows: <code>java -Djava.io.tmpdir=$TMPDIR &lt;other_java_options&gt; java.program &lt;specific_program_options&gt;</code>.</li>
<li>If your Java program is called indirectly, or is pre-wrapped, you will need to put the following line in your job submission script before calling the Java program: <code>export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR}</code>.</li>
</ul>
<p> </p>