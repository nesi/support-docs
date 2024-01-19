---
created_at: '2020-11-02T03:07:06Z'
hidden: false
tags: []
title: CESM
vote_count: 0
# template: app.html
vote_sum: 0
zendesk_article_id: 360002105076
zendesk_section_id: 360000040076
---

The Community Earth System Model (CESM) is a coupled climate model for
simulating Earth’s climate system. Composed of separate models
simultaneously simulating the Earth’s atmosphere, ocean, land, river
run-off, land-ice, and sea-ice, plus one central coupler/moderator
component, CESM allows researchers to conduct fundamental research into
the Earth’s past, present, and future climate states.

## Building CESM2 on Māui

Here we provide a guide for downloading, building and running a CESM
test case yourself on Māui This guide is based on CESM 2.1.

### Prerequisites

Git Large File Storage seems to be required to download some of the CESM
components. Download the Git-LFS archive from
[here](https://git-lfs.github.com/), copy the *git-lfs* executable to
the *bin* directory in your home, add that directory to *PATH* and run a
git command to finish the Git-LFS installation. The following commands
will achieve this:

```sh
mkdir git-lfs
cd git-lfs
wget https://github.com/git-lfs/git-lfs/releases/download/v2.12.0/git-lfs-linux-amd64-v2.12.0.tar.gz
tar xf git-lfs-linux-amd64-v2.12.0.tar.gz
mkdir -p ~/bin
cp git-lfs ~/bin/
export PATH=$PATH:~/bin
echo export PATH=\$PATH:\$HOME/bin >> ~/.bashrc
git lfs install
```

### Download CESM

These instructions are based on the [upstream
documentation](https://escomp.github.io/CESM/release-cesm2/downloading_cesm.html).
First switch to your project directory (or wherever else you would like
the CESM source to live) and then run the commands to download CESM
(replacing *&lt;your\_project\_code&gt;* with your project code):

``` sh
cd /nesi/project/<your_project_code>
git clone -b release-cesm2.1.3 https://github.com/ESCOMP/CESM.git my_cesm_sandbox
cd my_cesm_sandbox
./manage_externals/checkout_externals
```

Make sure the above command is successful (see the upstream
documentation linked above for how to check). You may need to rerun the
command until it is successful, especially if it asks you to accept a
certificate.

### NeSI specific CIME configuration

Clone the repo containing NeSI specific CIME configuration
([CIME](http://esmci.github.io/cime/versions/master/html/what_cime/index.html)
provides a case control system for configuring, building and executing
Earth system models) and copy the config files to *~/.cime*. In the
following, replace *&lt;your\_project\_code&gt;* with your project code
(this will overwrite any current configuration your have in *~/.cime*):

``` sh
cd /nesi/project/<your_project_code>
git clone https://github.com/nesi/nesi-cesm-config.git
cd nesi-cesm-config
mkdir -p ~/.cime
sed 's/nesi99999/<your_project_code>/g' config_machines.xml > ~/.cime/config_machines.xml
cp config_batch.xml ~/.cime/config_batch.xml
```

Check that you are happy with the paths specified in
*~/.cime/config\_machines.xml*, in particular, it is recommended that
CESM users share the same input data locations as the input data can be
large.

### Setting up and running a test case

Here we will run the test described in the CESM [quick start
guide](https://escomp.github.io/CESM/release-cesm2/quickstart.html). The
following are basic instructions to run create and run the case, see the
above link for more information.

First, create the case:

``` sh
cd /nesi/project/<your_project_code>/my_cesm_sandbox/cime/scripts
./create_newcase --case /nesi/nobackup/<your_project_code>/$USER/cesm/output/b.e20.B1850.f19_g17.test --compset B1850 --res f19_g17 --machine maui --compiler intel
cd /nesi/nobackup/<your_project_code>/$USER/cesm/output/b.e20.B1850.f19_g17.test
```

The *--machine Māui --compiler intel* arguments to *./create\_case* tell
CESM to use the NeSI specific configuration we added to your home
directory in the previous step.

Next, set up the case and preview the run:

``` sh
./case.setup
./preview_run
```

Check that everything looks correct in the preview and then build the
case:

``` sh
./case.build
```

Update any settings if necessary, for example here we turn off short
term archiving:

``` sh
./xmlchange DOUT_S=FALSE
```

Finally, run the job:

``` sh
./case.submit
```

A job will be submitted to the Slurm queue, you can view the queue using
*squeue* or *squeue -u $USER* for just your own jobs. Check the job
succeeded as described on the upstream quick start guide.

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
documented on the above page in the section "One approach to load
balancing"
[here](https://esmci.github.io/cime/versions/maint-5.6/html/users_guide/pes-threads.html).
It involves performing a number of short model runs to determine which
components are most expensive and how the individual components scale.
That information can then be used to determine an optimal load balance.