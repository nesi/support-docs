---
created_at: 2026-10-15
description: Use bash loops and variables in a job script, with braces and quotes so values expand as expected, and set -u to stop on unset variables.
status: tutorial
tags:
- tutorial
- slurm
---

!!! time "45 Minutes"

!!! objectives
    - Read and write a `for` loop that runs a command on each file.
    - Use variables, braces and quotes so values expand the way you expect.
    - Make a script stop on errors and on unset variables.

!!! prerequisite
    - You can write and submit a batch script. See [Submitting Your First Job](../Introduction_To_HPC/Submitting_Your_First_Job.md).
    - Following on from [Measuring Job Efficiency](Measuring_Job_Efficiency.md) is useful, but not needed.

??? info "Skipped ahead? Set up here"
    <!-- Write: copy the example directory and checkpoints/01_measuring/pipeline.sl. -->

<!-- Write: hook. Show the dense alignment loop from pipeline.sl and ask what is hard to read or change. -->

## Loops over files

<!-- Write: for loops over a glob, with the loop in pipeline.sl as the example. Learners can try these on the login node.
Source: new. The intro tutorials do not teach loops. -->

## Command substitution

<!-- Write: $( ), with basename from pipeline.sl as the example. -->

## Variables for file paths

<!-- Write: learners rewrite the alignment loop with a variable for each file before seeing the solution.
Source: "Variables in file paths" section of Using_Variables.md. Note its fq1/fq2 paths should be trimmed/, not trimmed_reads/. -->

!!! question "Rewrite the loop"
    <!-- Write: give each file a variable, then use the variables in the commands. -->

??? question "Solution"
    <!-- Write: the loop from checkpoints/02_loops_variables/pipeline.sl. -->

## Braces and quotes

<!-- Write: introduce braces through the script's own ${base}_1.trim.fastq ($base_1 would be empty),
then quotes with a path containing a space.
Source: "Formatting variables" section of Using_Variables.md. -->

<quiz>
<p class=admonition-title>Braces</p>

What does this print?

```sh
number=01
echo $numbersample.txt
```

- [x] `.txt`
> Bash reads `$numbersample`, a variable that is not set, so it expands to nothing.
- [] `01sample.txt`
> That needs braces: `${number}sample.txt`.
- [] An error saying `numbersample` is not set.
> Only with `set -u`. Without it, bash carries on silently.
</quiz>

## Stopping on errors

<!-- Write: what the -e in #!/bin/bash -e does, then set -u, with a misspelt variable name as the example.
End state: checkpoints/02_loops_variables/pipeline.sl. -->

<quiz>
<p class=admonition-title>Unset variables</p>

A script starts with `set -u` and then runs `mkdir "${resluts}/vcf"`, misspelling `results`. What happens?

- [x] The script stops with an error that `resluts` is unbound.
- [] It creates a directory called `/vcf`.
> That is what happens without `set -u`, as the variable expands to nothing.
- [] It creates `results/vcf`.
</quiz>

!!! keypoints
    - A `for` loop runs the same commands on each file.
    - Variables make a script easier to read and to change in one place.
    - Use braces and quotes so variables expand the way you expect.
    - `#!/bin/bash -e` and `set -u` stop a script at the first error or unset variable.

!!! postrequisite "What next"
    - Next lesson: [Reusable Job Scripts](Reusable_Job_Scripts.md).
    - For more shell practice: the Software Carpentry [Unix Shell](https://swcarpentry.github.io/shell-novice/) lessons on loops and shell scripts.
