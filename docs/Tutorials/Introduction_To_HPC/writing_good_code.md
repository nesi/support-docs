---
title: "Writing good code"
teaching: 20
exercises: 10
questions:
- "How do we write a good job script."
objectives:
- "Write a script that can be run serial or parallel."
- "Write a script that using SLURM environment variables."
- "Understand the limitations of random number generation."
keypoints:
- "Write your script in a way that is independent of data or environment. (elaborate)"
---

When talking about 'a script' we could be referring to multiple things.

* Slurm/Bash script - Almost everyone will be using one of these to submit their Slurm jobs.
* Work script - If your work involves running another script (usually in a language other than Bash like Python, R or MATLAB) that will have to be invoked in your bash script.

This section will cover best practice for both types of script.

<!-- ```
python python_script.py
```
{: .language-bash}


```
rscript r_script.r
```
{: .language-bash}

```
matlab -r matlab_script
```
{: .language-bash} -->

## Use environment variables

In this lesson we will take a look at a few of the things to watch out for when writing scripts for use on the cluster.
This will be most relevant to people writing their own code, but covers general practices applicable to everyone.

There is a lot of useful information contained within environment variable.

> ## Slurm Environment
>
> For a small demo of the sort of useful info contained within env variables, run the command.
>
> ```
> sbatch --output "slurm_env.out" --wrap "env | grep"
> ```
> {: .language-bash}
>
> once the job has finished check the results with,
>
> ```
> cat slurm_env.out
> ```
> {: .language-bash}
>
> ```
> SLURM_JOB_START_TIME=1695513911
> SLURM_NODELIST=wbn098
> SLURM_JOB_NAME=wrap
> SLURMD_NODENAME=wbn098
> SLURM_TOPOLOGY_ADDR=top.s13.s7.wbn098
> SLURM_PRIO_PROCESS=0
> SLURM_NODE_ALIASES=(null)
> SLURM_JOB_QOS=staff
> SLURM_TOPOLOGY_ADDR_PATTERN=switch.switch.switch.node
> SLURM_JOB_END_TIME=1695514811
> SLURM_MEM_PER_CPU=512
> SLURM_NNODES=1
> SLURM_JOBID=39572365
> SLURM_TASKS_PER_NODE=2
> SLURM_WORKING_CLUSTER=mahuika:hpcwslurmctrl01:6817:9984:109
> SLURM_CONF=/etc/opt/slurm/slurm.conf
> SLURM_JOB_ID=39572365
> SLURM_JOB_USER=cwal219
> __LMOD_STACK_SLURM_I_MPI_PMI_LIBRARY=L29wdC9zbHVybS9saWI2NC9saWJwbWkyLnNv
> SLURM_JOB_UID=201333
> SLURM_NODEID=0
> SLURM_SUBMIT_DIR=/scale_wlg_persistent/filesets/home/cwal219
> SLURM_TASK_PID=8747
> SLURM_CPUS_ON_NODE=2
> SLURM_PROCID=0
> SLURM_JOB_NODELIST=wbn098
> SLURM_LOCALID=0
> SLURM_JOB_GID=201333
> SLURM_JOB_CPUS_PER_NODE=2
> SLURM_CLUSTER_NAME=mahuika
> SLURM_GTIDS=0
> SLURM_SUBMIT_HOST=wbn003
> SLURM_JOB_PARTITION=large
> SLURM_JOB_ACCOUNT=nesi99999
> SLURM_JOB_NUM_NODES=1
> SLURM_SCRIPT_CONTEXT=prolog_task
> ```
> {: .output}
>
> Can you think of some examples as to how these variables could be used in your script?

> > ## Solution
> >
> > * `SLURM_JOB_CPUS_PER_NODE` could be used to pass CPU numbers directly to any programs being used.
> > * Some other things.
> {: .solution}
{: .challenge}

> ## Variables in Slurm Header
>
> Environment variables set by Slurm cannot be referenced in the Slurm header.
{: .callout}

## Default values

It is good practice to set default values when using environment variables when there is a chance they will be run in an environment where they may not be present. 

```
FOO="${VARIABLE:-default}"
```
{: .language-bash}

`FOO` will be to to the value of `VARIABLE` if is set, otherwise it will be set to `default`.

As a slight variation on the above example. (`:=` as opposed to `:-`).

```
FOO="${VARIABLE:=default}"
```
{: .language-bash}

`FOO` will be to to the value of `VARIABLE` if is set, otherwise it will be set to `default`, `VARIABLE` will also be set to `default`.

<!-- Lets have a look at the script we ran before, `{{ site.example.script }} `,

> ## Using {{ site.example.lang }} commands
>
> If you are unfamiliar with {{ site.example.lang }}, don't worry there are equivalent operations in any language you choose to use.
{: .callout}

Starting from the top; -->


```
num_cpus <- 2
```
{: .language-r}

The number of CPU's being used is fixed in the script. We can save time and reduce chances for making mistakes by replacing this static value with an environment variable.
We can use the environment variable `SLURM_CPUS_PER_TASK`.

```
num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK')) 
```
{: .language-r}

Slurm sets many environment variables when starting a job, see [Slurm Documentation for the full list](https://slurm.schedmd.com/sbatch.html).

The problem with this approach however, is our code will throw an error if we run it on the login node, or on our local machine or anywhere else that `SLURM_CPUS_PER_TASK` is not set.

Generally it is best not to diverge your codebase especially if you don't have it under version control, so lets add some compatibility for those use cases.

```
num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK', unset = "1")) 
```
{: .language-r}

Now if `SLURM_CPUS_PER_TASK` variable is not set, 1 CPU will be used. You could also use some other method of detecting CPUs, like `detectCores()`.

## Interoperability

windows + mac + linux
headless + interactive

## Verbose

Having a printout of job progress is fine for an interactive terminal, but when you aren't seeing the updates in real time anyway, it's just bloat for your output files.

Let's add an option to mute the updates.

```
print_progress <- FALSE
```
{: .language-r}


```
if (print_progress && percent_complete%%1==0){

```
{: .language-r}

## Reproduceability

As this script uses [Pseudorandom number generation](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) there are a few additional factors to consider.
It is desirable that our output be reproducible so we can confirm that changes to the code have not affected it. 

We can do this by setting the seed of the PRNG. That way we will get the same progression of 'random' numbers.

We are using the environment variable `SLURM_ARRAY_TASK_ID` for reasons we will get to later. We also need to make sure a default seed is set for the occasions when `SLURM_ARRAY_TASK_ID` is not set.

```
seed <- strtoi(Sys.getenv('SLURM_ARRAY_TASK_ID', unset = "0"))
set.seed(seed)
```
{: .language-r}


Now your script should look something like this;

```
{% include example_scripts/sum_matrix.r %}
```
{: .language-r}

## Readability

Comments!

## Debugging

```
#!/bin/bash -e
```
{: .language-bash}

Exit bash script on error

```
#!/bin/bash -x
```
{: .language-bash}

Print environment.

```
env
```
{: .language-bash}

Print environment, if someone else has problems replicating the problem, it will likely come down to differences in your environment.

```
cat $0
```
{: .language-bash}

Will print your input Slurm script to you output, this can help identify when changes in your submission script leads to errors.

## Version control

Version control is when changes to a document are tracked over time.

In many cases you may be using the same piece of code across multiple environments, in these situations it can be difficult to keep track of changes made and your code can begin to diverge. Setting up version control like Git can save a lot of time.

### Portability



## Testing

More often than not, problems come in the form of typos, or other small errors that become apparent within the first few seconds/minutes of script. 

Running on login node?

Control + c to kill.

{% include links.md %}
