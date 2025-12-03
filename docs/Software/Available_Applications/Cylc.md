---
created_at: '2022-08-03T21:35:50Z'
tags: []
---

## What is Cylc

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
on NeSI's platform. Consult the [Cylc
documentation](https://cylc.github.io/documentation/) for more elaborate
examples, including some with a cycling (repeated) graph pattern. One of
the strengths of Cylc is that simple workflows can be executed simply
while allowing for very complex workflows, with thousands of tasks,
which may be repeated ad infinitum.

## SSH configuration

Cylc uses ssh  to automatically start schedulers on configured "run
hosts" and to submit jobs to remote platforms, so if you haven't already
done so you need to allow ssh to connect to other hosts on the HPC
cluster without prompting for a passphrase (all HPC nodes see the same
filesystem, so this is easy):

- run **`ssh-keygen`** to generate a public/private key pair with **no
    passphrase** (when it asks for a passphrase, just hit enter)
- add your own public key to your authorized keys
    file: **`cat .ssh/id_rsa.pub >> .ssh/authorized_keys`** 
- check that your **keys, authorized\_keys file, ssh
    directory, **and** home directory** all have sufficiently secure
    file permissions. If not, `ssh` will silently revert to requiring
    password entry. See for
    example <https://www.frankindev.com/2020/11/26/permissions-for-.ssh-folder-and-key-files/>
- make sure your **home directory** has a maximum
    of **750** permissions

Now you should be able to run **`ssh login02`**(for example) without
being asked for a passphrase.

## How to install Cylc

Create a new conda environment and install Cylc with the commands:
``` sh
module purge
module load Miniforge3
export CYLC_HOME=/nesi/project/nesi99999/$USER/environment/cylc-env
conda create --prefix $CYLC_HOME python=3.12
```
where `CYLC_HOME` points to the installation path of your choice. Adjust `nesi99999` to fit your project number. It is not recommended to install in your home directory. 

Then type
``` sh
conda init
```
Close and start a new shell.

Now activate the new environment
``` sh
module purge && module load Miniforge3
conda activate /nesi/project/nesi99999/$USER/environment/cylc-env # or whereever you installed cylc-env
conda install -c conda-forge cylc-flow
```
Check that `cylc` was successfully installed
``` sh
cylc --version
```
should return 
``` output
8.6.0
```
or a later version.

## Create a cylc wrapper script

In order to allow `cylc` to be invoked through `SLURM` the following steps are required
``` sh
mkdir $CYLC_HOME/wrapper
cylc get-resources cylc $CYLC_HOME/wrapper
chmod +x $CYLC_HOME/wrapper/cylc
cp $CYLC_HOME/wrapper/cylc $CYLC_HOME/wrapper/cylc.bak
sed -i "s|CYLC_HOME_ROOT=\"\${CYLC_HOME_ROOT:-/opt}\"|CYLC_HOME_ROOT=\"\${CYLC_HOME_ROOT:-${CYLC_HOME}}\"|" $CYLC_HOME/wrapper/cylc
```

Make sure the wrapper script is found when opening a new shell
``` sh
export CYLC_HOME=/nesi/project/nesi99999/$USER/environment/cylc-env # adapt
export PATH=$CYLC_HOME/wrapper:$PATH
```


## Setting up Cylc on Mahuika

In order to allow Cylc to submit tasks to the SLURM scheduler, we need to configure platforms. Edit (or create) your global configuration file:
``` sh
mkdir -p ~/.cylc/flow/
vim ~/.cylc/flow/global.cylc
```
or use the editor of your choice, and add the following lines
``` sh
[platforms]
    [[mahuika-slurm]]
        hosts = login01, login02, login03
        install target = localhost
        job runner = slurm
```

## Test cylc

``` sh
git clone https://github.com/pletzer/cylc_patterns
cd cylc_patterns/cylc-src/slurm/
cylc clean slurm
cylc vip .
```

This will submit a job to SLURM
``` sh
squeue --me
```
should return 
``` output
JOBID         USER     ACCOUNT   NAME        CPUS MIN_MEM PARTITI START_TIME     TIME_LEFT STATE    NODELIST(REASON)    
2974409       pletzera nesi99999 a.1.slurm/ru   1    512M milan,g N/A                 1:00 PENDING  (Priority)
```
You casn also monitor the tasks with the command
``` sh
cylc tui slurm
```
