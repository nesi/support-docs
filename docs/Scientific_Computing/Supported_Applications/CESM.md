---
created_at: '2020-11-02T03:07:06Z'
tags: 
    - climate
    - modelling
status: deprecated
description: Supported applications page on CESM
---

The Community Earth System Model (CESM) is a coupled climate model for
simulating Earth’s climate system. Composed of separate models
simultaneously simulating the Earth’s atmosphere, ocean, land, river
run-off, land-ice, and sea-ice, plus one central coupler/moderator
component, CESM allows researchers to conduct fundamental research into
the Earth’s past, present, and future climate states.

Here we provide a guide for downloading, building and running a CESM
test case yourself on NeSI. This guide is based on CESM 2.1 and should work on
both Māui and Mahuika.

## Prerequisites

### Mahuika only

On Mahuika only, load a module with a more recent version of git than the default one:

```bash
module load git
```

You should ensure the *git* module is still loaded when running `git` commands
later on in this guide.

!!! note

    It should be safe to load the git module in your *~/.bashrc* (or other shell init file),
    since it shouldn't conflict with other modules, but if you use Māui too you should wrap
    it in a block such as:

    ```sh
    if [[ "${SYSTEM_STRING}" == "CS400" ]]; then
        module load git
    fi
    ```

    This will ensure the `module load git` command only runs on Mahuika.

### Māui only

On Māui only, you may need to install the Perl *XML::LibXML* module,
especially if you encounter errors like:

```bash
err=Can't locate XML/LibXML.pm in @INC (you may need to install the XML::LibXML module)
```

You can install the module with the following:

```sh
curl -L https://cpanmin.us/ | perl - App::cpanminus
~/perl5/bin/cpanm XML::LibXML
```

Then export the path the module was installed to so that it is picked up by Perl:

```sh
export PERL5LIB=~/perl5/lib/perl5/x86_64-linux-thread-multi
```

The export command above could be added to your *~/.bashrc* file to make it persistent but make sure
you wrap it in a block that ensures the environment variable is only set on Māui (if you are likely
to use Mahuika too), for example:

```sh
if [[ "${SYSTEM_STRING}" == "XC50" ]]; then
    export PERL5LIB=~/perl5/lib/perl5/x86_64-linux-thread-multi
fi
```

### Mahuika and Māui

Git Large File Storage seems to be required to download some of the CESM
components. Download the [Git-LFS archive](https://git-lfs.github.com/) and install it into your home directory.
Finally, add that directory to *PATH* in your ~/.bashrc file.
The following commands will achieve this:

```sh
wget https://github.com/git-lfs/git-lfs/releases/download/v3.5.1/git-lfs-linux-amd64-v3.5.1.tar.gz
tar xf git-lfs-linux-amd64-v3.5.1.tar.gz
cd git-lfs-3.5.1
./install.sh --local
export PATH=~/.local/bin:$PATH
echo export PATH=\$HOME/.local/bin:\$PATH >> ~/.bashrc
```

Confirm Git-LFS is installed by running:

```sh
git lfs version
```

which should print something like:

```out
git-lfs/3.5.1 (GitHub; linux amd64; go 1.21.7; git e237bb3a)
```

## Download CESM

First, set an environment with your NeSI project code to make replacing our default one easier
in the commands below (replacing *&lt;your\_project\_code&gt;* with your project code):

```sh
export PROJECT_CODE=<your_project_code>
```

These instructions are based on the [upstream documentation](https://escomp.github.io/CESM/release-cesm2/downloading_cesm.html).
First switch to your project directory (or wherever else you would like
the CESM source to live) and then run the commands to download CESM:

``` sh
cd /nesi/project/${PROJECT_CODE}
git clone -b release-cesm2.1.5 https://github.com/ESCOMP/CESM.git my_cesm_sandbox
cd my_cesm_sandbox
./manage_externals/checkout_externals
```

Make sure the above command is successful (see the upstream
documentation linked above for how to check). You may need to rerun the
command until it is successful, especially if it asks you to accept a
certificate.

## NeSI specific CIME configuration

Make sure you still have the environment variable set with your project code:

```sh
export PROJECT_CODE=<your_project_code>
```

Clone the repo containing NeSI specific CIME configuration
([CIME](http://esmci.github.io/cime/versions/master/html/what_cime/index.html)
provides a case control system for configuring, building and executing
Earth system models) and copy the config files to *~/.cime* (this will overwrite
any current configuration your have in *~/.cime*):

``` sh
cd /nesi/project/${PROJECT_CODE}
git clone https://github.com/nesi/nesi-cesm-config.git
cd nesi-cesm-config
mkdir -p ~/.cime
sed "s/nesi99999/${PROJECT_CODE}/g" config_machines.xml > ~/.cime/config_machines.xml
cp config_batch.xml ~/.cime/config_batch.xml
cp config_compilers.xml ~/.cime/config_compilers.xml
```

Check that you are happy with the paths specified in
*~/.cime/config\_machines.xml*, in particular, it is recommended that
CESM users share the same input data locations as the input data can be
large.

Make sure that the directory pointed to by `DIN_LOC_ROOT` in *~/.cime/config_machines.xml* exists, e.g.

```sh
mkdir -p /nesi/nobackup/${PROJECT_CODE}/cesm/inputdata
```

## Setting up and running a test case

Make sure you still have the environment variable set with your project code:

```sh
export PROJECT_CODE=<your_project_code>
```

Here we will run the test described in the CESM [quick start
guide](https://escomp.github.io/CESM/release-cesm2/quickstart.html). The
following are basic instructions to create and run the case, see the
above link for more information.

Change to the *cime/scripts* directory:

``` sh
cd /nesi/project/${PROJECT_CODE}/my_cesm_sandbox/cime/scripts
```

Create the case directory:

```sh
./create_newcase \
    --case /nesi/nobackup/${PROJECT_CODE}/$USER/cesm/output/b.e20.B1850.f19_g17.test \
    --compset B1850 --res f19_g17 --machine mahuika --compiler gnu
```

In the above command:

- `--machine mahuika` could be changed to `--machine maui` if you are running on Māui
- `--compiler gnu` could be changed to `--compiler intel` if you want to build with the Intel compilers instead of GNU (it can be useful to compare different compilers in case one performs much better)
- the name of the directory for `--case` (i.e. *b.e20.B1850.f19\_g17.test* in this example) is arbitrary

Change to the new case directory that you just created:

```sh
cd /nesi/nobackup/${PROJECT_CODE}/$USER/cesm/output/b.e20.B1850.f19_g17.test
```

**On Mahuika only**: we will now adjust the number of processors (tasks) the simulation will run on. This case is configured to run on 6 full nodes by default but we're just running a short test, so let's reduce the maximum number of tasks per node, keeping the layout between different components the same:

```sh
./xmlchange MAX_TASKS_PER_NODE=32
./xmlchange MAX_MPITASKS_PER_NODE=32
```

Changes to the number of processors/tasks and layout must be made before calling `case.setup`.
More details about modifying a case can be found in the CESM documentation and also in [ARCHER2's CESM documentation](https://docs.archer2.ac.uk/research-software/cesm213_run/#making-changes-to-a-case).

Let's also reduce the wall time (which will default to the maximum value otherwise):

```sh
./xmlchange --subgroup case.run JOB_WALLCLOCK_TIME="00:20:00"
```

Next, set up the case and preview the run:

``` sh
./case.setup
./preview_run
```

Check that everything looks correct in the preview. On Mahuika you should see that the case is setup to run on 192 total tasks:

```sh
CASE INFO:
  nodes: 6
  total tasks: 192
  tasks per node: 32
  thread count: 1
```

On Māui this should show 240 total tasks and 40 tasks per node, unless you changed those above.

Now build the case (this could take a while if it needs to download input data):

``` sh
./case.build
```

Update any other settings as necessary, for example here we turn off short
term archiving:

``` sh
./xmlchange DOUT_S=FALSE
```

Finally, run the job (this could take a while if it needs to download input data):

``` sh
./case.submit
```

A job will be submitted to the Slurm queue, you can view the queue using
*squeue --me*. Check the job succeeded as described on the upstream
[quick start guide](https://escomp.github.io/CESM/release-cesm2/quickstart.html#run-the-case).

## Performance tuning - optimising processor layout

With CESM it can be important to tune the processor layout for best
performance with respect to the different components (atmosphere, land,
sea ice, etc.). Many different configurations are possible, although
there are some hard coded constraints, and this is well documented in
CIME (the case control system used by CESM):

[https://esmci.github.io/cime/versions/maint-5.6/html/users\_guide/pes-threads.html](https://esmci.github.io/cime/versions/maint-5.6/html/users_guide/pes-threads.html)

The above link lists some of the common configurations, such as fully
sequential or fully sequential except the ocean running concurrently.

One approach to load balancing (i.e. optimising processor layout) is
documented on the above ESMCI page in the section "One approach to load
balancing".
It involves performing a number of short model runs to determine which
components are most expensive and how the individual components scale.
That information can then be used to determine an optimal load balance.
