---
created_at: '2015-08-18T02:30:33Z'
tags:
- mahuika
- general
description: Supported applications page for Java
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Description

Java is a computer programming language that is concurrent, class-based,
object-oriented, and specifically designed to have as few implementation
dependencies as possible. It is intended to let application developers
"write once, run anywhere" (WORA), meaning that code that runs on one
platform does not need to be recompiled to run on another. Java
applications are typically compiled to bytecode (class file) that can
run on any Java virtual machine (JVM) regardless of computer
architecture. The language derives much of its syntax from C and C++,
but it has fewer low-level facilities.

The Java home page is at <http://www.java.com>.

## Licensing requirements

All versions of Java on NeSI clusters have been made available by their
respective owners at no cost under a limited, closed-source licence. The
full licence terms and conditions for any given version of Java can be
found by following the directions in `${JAVA_HOME}/LICENSE`.

## Example scripts

### Example script for Mahuika

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      MyMultithreadedJavaJob
#SBATCH --time          1:00:00          # 1 hour walltime limit
#SBATCH --cpus-per-task 8                # 8 CPU cores for 8 Java threads
#SBATCH --mem           4096MB           # 4 GB of memory

module load Java/1.8.0_144
# The following line is needed in case your Java application
# is called indirectly
export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR}
java -Xmx3g -Djava.io.tmpdir=${TMPDIR} -jar /path/to/foo.jar
```

## Further notes

### Java Versions

The default version of Java that is packaged with the operating system
may not be appropriate for your work.  To use a different version of
Java us the \`module\` command to find and load for example:

``` sh
$ module spider Java
-----------------------------------------------------------------------
-----------------------------------------------------------------------
Java Platform, Standard Edition (Java SE) lets you develop and deploy 
Java applications on desktops and servers.

Versions:
Java/1.7.0_51
Java/1.8.0_144
Java/11.0.4
Java/15.0.2

$ module load Java/15.0.2
```

### Memory management and the -Xmx option

It is important to let the Java virtual machine know how much memory it
is allowed to use.   The main way this is done is via the `-Xmx`
option, which sets the maximum amount of heap space that it can use.

As a first approximation, we recommend setting the `-Xmx` option to 75%
of the requested memory. For example, if your job asks the scheduler for
32 GB of memory, you should provide the Java executable with `-Xmx24g`,
which will cap its heap usage to 24 GB, leaving at least 6 GB for its
stack and any other overheads.

### Temporary Files

Java programs which use temporary files can (and should) generally be
persuaded to use $TMPDIR rather than just the default of `/tmp `by being
given the option `-Djava.io.tmpdir=$TMPDIR.`  TMPDIR is automatically
removed at the end of the job.

- If you run your Java program by using the `java` command, that is in
    a form like
    `java <java_options> java.program <specific_program_options>`, you
    can specify the tmpdir as follows:
    `java -Djava.io.tmpdir=$TMPDIR <other_java_options> java.program <specific_program_options>`.
- If your Java program is called indirectly, or is pre-wrapped, you
    will need to put the following line in your job submission script
    before calling the Java program:
    `export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR}`.
