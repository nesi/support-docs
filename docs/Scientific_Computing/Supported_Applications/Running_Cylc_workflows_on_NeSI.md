What is Cylc {#01G9X8TM54HGX95GWY5CR3E4CS}
------------

[Cylc](https://cylc.github.io/) is a **general purpose workflow engine**
that can also orchestrate **cycling systems** very efficiently. It is
used in production weather, climate, and environmental forecasting on
HPC, but is not specialised to those domains.

Using a workflow engine may enable you to run large parametric or
sensitivity studies while ensuring scalability, reproducibility and
flexibility. If you have embarrassingly parallel jobs then Cylc might be
a good solution for you. The workflow engine will allow for the
concurrent execution of parallel jobs, depending on the task graph and
available resources on the platform. One advantage of this approach over
running a monolithic, parallel executable is that each task will require
less resources that the complete problem, it is thus easier for each
task to slip into the queue and start running.

See the NeSI  [Snakemake](https://snakemake-on-nesi.sschmeier.com/) page
for another, possible choice.

In this article, we show how you can create a simple workflow and run it
on NeSI\'s platform. Consult the [Cylc
documentation](https://cylc.github.io/documentation/) for more elaborate
examples, including some with a cycling (repeated) graph pattern. One of
the strengths of Cylc is that simple workflows can be executed simply
while allowing for very complex workflows, with thousands of tasks,
which may be repeated ad infinitum. 

 

How to select the Cylc version {#01G9X8TM55D8QFZK1483S2X5HX}
------------------------------

Cylc has been installed on Māui and Mahuika, there is no need to load
any module,

    $ which cylc
    /opt/nesi/share/bin/cylc

(Access if via the NeSI module, which is loaded by default.)

Be aware that the default version

    $ cylc version
    7.9.1

is not the latest, and that configuration file and Cylc commands have
changed significantly at version 8.

**New Cylc users should use version 8 or later**,

    $ cylc list-versions

    7.9.1 
    ...
    8.0.1 
    cylc -> 7.9.1

You can select your Cylc version by setting the environment variable
CYLC\_VERSION, for instance,

    $ export CYLC_VERSION=8.0.1
    $ cylc version
    8.0.1

At the time of writing, the latest version is 8.0.1.

A simple example of a Cylc workflow {#01G9X8TM552SXXBMFG41TGRKBP}
-----------------------------------

To demonstrate Cylc, let\'s start with a workflow, which we call
\"simple\",

    $ mkdir -p ~/cylc-src/simple
    $ cd ~/cylc-src/simple

Create/edit the following **flow.cylc** file containing

    [scheduling] # Define the tasks and when they should run
      [[graph]]
        R1 = """ # R1 means run this graph once
          taskA & taskB => taskC # Defines the task graph
        """
    [runtime] # Define what each task should run
      [[root]] # Default settings inherited by all tasks
        platform = mahuika-slurm # Run "cylc conf" to see platforms. 
        [[[directives]]] # Default SLURM options for the tasks below
           --account = nesi99999 # CHANGE
      [[taskA]]
        script = echo "running task A"
          [[[directives]]] # specific SLURM option for this task
            --ntasks = 2
      [[taskB]]
        script = echo "running task B"
      [[taskC]]
        script = echo "running task C"

In the above example, we have three tasks (taskA, taskB and taskC),
which run under SLURM (hence platform = mahuika-slurm). Type

    cylc config --platform-names

[to see a list of platforms. The SLURM settings for taskA are in the
\[\[\[directives\]\]\] section.]{.s1}

How to interact with Cylc {#01GFPTSN3XAE8EXPK03B6W99N7}
-------------------------

Cylc takes command lines. Type 

    $ cylc help all

to see the available commands. Type 

    $ cylc help install # or cylc install --help

to find out how to use a specific command (in this case \"install\").

Installing a workflow {#01G9X8TM55ZW1DWYMSEYTRQBYZ}
---------------------

Prior to running a workflow, **it must be installed** to a run
directory. Due to limited disk space in home directories on NeSI, Cylc
has been configured to symlink the standard run directories to project
directories, if \$PROJECT is defined. Hence, you need to set

    $ export PROJECT=nesi99999 # CHANGE

Then install the workflow with

    cylc install simple

Validating the workflow {#01G9X8TM55X80D5CPV6ATFYJHM}
-----------------------

It\'s a good idea to check that there are no syntax errors in flow.cylc,

    $ cylc validate simple
    Valid for cylc-8.0.1

Looking at the workflow graph {#01G9X8TM55X4AHY2WEE1ENZF34}
-----------------------------

A useful command is 

    $ cylc graph simple

which will generate a png file, generally in the /tmp directory with a
name like [/tmp/tmpzq3bjktw.PNG. Take note of the name of the png file.
To visualise the file you can type ]{.s1}

    $ display  /tmp/tmpzq3bjktw.PNG # ADJUST the file name

Here, we see that our workflow \"simple\" has a \"taskC\", which waits
for \"taskA\" and \"taskB\" to complete,

![simple.png](https://support.nesi.org.nz/hc/article_attachments/5255042984079/simple.png)

The \"1\" indicates that this workflow graph is executed only once.

Different ways to interact with Cylc {#01G9X8TM56VMG4J8KRW0NNZWSZ}
------------------------------------

Every Cylc action can be executed via the command line. Alternatively,
you can invoke each action through a **terminal user interface** (tui), 

    $ cylc tui simple

Another alternative, is to use the **graphical user interface**

    $ cylc gui

This will start a web server, which will display a URL like

<http://wbn003:8888/cylc?token=30d9e2b3dfe097318539cff02f69a24217f2967e8809f0a9>

(the token value will be different). 

If you\'re connecting through <https://jupyter.nesi.org.nz> you\'ll need
to replace anything before the \":\" with
<https://jupyter.nesi.org.nz/user/USERNAME/proxy/> to get access to the
web graphical user interface (where USERNAME is your NeSI user name).
Hence the URL becomes
<https://jupyter.nesi.org.nz/user/USERNAME/proxy/>[8888/cylc?token=TOKEN](http://wbn003:8888/cylc?token=30d9e2b3dfe097318539cff02f69a24217f2967e8809f0a9)

How to execute a workflow {#01G9X8TM56RRFMK8Y0H56RKEMQ}
-------------------------

To execute the workflow type

    $ cylc play --no-detach simple

The \"\--no-detach\" option makes scheduler run in the foreground so you
can see its output in your terminal. Without this option it will
\"daemonize\" so it can keep running even if you log out.

Command

    $ cylc scan

will list all running and installed workflows.[]{.s1}

Checking the output {#01G9X8TM5665B7RHWWTQEZBG2E}
-------------------

    $ cylc cat-log simple//1/taskA  # note // between workflow and task ID

of the first cycle of taskA. The \"1\" refers to the task iteration, or
cycle point. Our simple workflow only has one iteration (as dictated by
the R1 graph above). 

How to clean or remove a workflow {#01G9X8TM56H3QSGFM28FRGAD83}
---------------------------------

    $ cylc clean simple

will remove the file structure associated with workflow \"simple\".

Where jobs, results and log files are stored {#01G9X8TM560YEF30SXD3V2BFBG}
--------------------------------------------

Cylc will create a directory under \$HOME/cylc-run. On NeSI, the output
of the runs will be stored in the project directory, with a symbolic
link pointing from the user home directory to the project directory

    $ ls -l $HOME/cylc-run/simple/run1
    lrwxrwxrwx 1 pletzera pletzera 54 Aug  5 03:19 /home/pletzera/cylc-run/simple/run1 -> /nesi/nobackup/nesi99999/pletzera/cylc-run/simple/run1

About Cylc {#01G9X8TM56RGGS0RY0F1VJFD1C}
----------

More can be found about Cylc
[here](https://cylc.github.io/cylc-doc/nightly/html/tutorial/index.html),
including what Cylc is and how you can leverage Cylc to submit parallel
jobs.
