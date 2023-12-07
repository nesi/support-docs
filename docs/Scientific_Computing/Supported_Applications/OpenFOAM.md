---
created_at: '2019-02-24T22:16:04Z'
hidden: false
position: 40
tags:
- engineering
- cfd
- cae
- fea
title: OpenFOAM
vote_count: 0
template: app.html
vote_sum: 0
zendesk_article_id: 360000810556
zendesk_section_id: 360000040076
---

OpenFOAM (Open Field Operation And Manipulation) is a open-source C++
toolbox maintained by the OpenFOAM foundation and ESI Group. Although
primarily used for CFD (Computational Fluid Dynamics) OpenFOAM can be
used in a wide range of fields from solid mechanics to chemistry.  
  
The lack of licence limitations and native parallelisation makes
OpenFOAM well suited for a HPC environment. OpenFOAM is an incredibly
powerful tool, but does require a moderate degree of computer literacy
to use effectively.

OpenFOAM can be loaded using;

``` sl
module load OpenFOAM
source $FOAM_BASH
```

## Example Script

```sh
#!/bin/bash -e

#SBATCH --time              04:00:00
#SBATCH --job-name          OF_16CORES
#SBATCH --output            %x.output   #set output to job name
#SBATCH --ntasks            16
#SBATCH --mem-per-cpu               512MB

#Working directory always needs to contain 'system', 'constant', and '0'

module load OpenFOAM/{{app.machines.mahuika.versions | last}}
source ${FOAM_BASH}

decomposePar                   #Break domain into pieces for parallel execution.
srun simpleFoam -parallel       
reconstructPar -latestTime     #Collect 
```

## Filesystem Limitations

OpenFOAM generates a large number of files during run-time. In addition
to the I/O load there is also the danger of using up available
[inodes](https://support.nesi.org.nz/knowledge/articles/360000177256).

**Filesystems in excess of their allocation will cause any job trying to
write there to crash.**

There are a few ways to mitigate this

- **Use** `/nesi/nobackup`
    The nobackup directory has a significantly higher inode count and no
    disk space limits.

- **ControlDict Settings**  
  - `WriteInterval`  
        Using a high write interval reduce number of output files and
        I/O load.
  - `deltaT`  
        Consider carefully an appropriate time-step, use adjustTimeStep
        if suitable.
    - `purgeWrite`  
        Not applicable for many jobs, this keeps only the last n steps,
        e.g. purgeWrite 5 will keep the last 5 time-steps, with the
        directories being constantly overwritten.
    - `runTimeModifiable`  
        When true, dictionaries will be re-read at the start of every
        time step. Setting this to false will decrease I/O load.
    - `writeFormat`  
        Setting this to binary as opposed to ascii will decrease disk
        use and I/O load.

- **Monitor Filesystem**  
    The command `nn_storage_quota` should be used to track filesystem
    usage. There is a delay between making changes to a filesystem and
    seeing it on `nn_storage_quota`.

    ```sh
    Filesystem         Available      Used     Use%     Inodes     IUsed     IUse%
    home_cwal219             20G    1.957G    9.79%      92160     21052    22.84%
    project_nesi99999         2T      798G   38.96%     100000     66951    66.95%
    nobackup_nesi99999              6.833T            10000000    2691383   26.91%
    ```

- **Contact Support**  
    If you are following the recommendations here yet are still
    concerned about indoes, open a support ticket and we can raise the
    limit for you.

## Environment Variables

You may find it useful to use environment variables in your dictionaries
e.g.

```sh
numberOfSubdomains ${SLURM_NTASKS};
```

Or create your variables to be set in your Slurm script.

```sh
startFrom ${START_TIME};
```

 This is essential when running parameter sweeps.

You can also directly edit your dictionaries with `sed`,Concordia.ah

```sh
NSUBDOMAINS=10
sed -i "s/\(numberOfSubdomains \)[[:digit:]]*\(;\)/\1 $NSUBDOMAINS\2/g" system/controlDict
```

## Recommended Resources

Generally, using 16 or less tasks will keep your job reasonably
efficient. However this is *highly* dependant on the type of simulation
and how the model was decomposed.

## Adding custom solvers

Rather than installing custom solvers centrally, we encourage users to
install under their user or project.

### Downloading

Generally your custom solver will be stored in a git repo. Make sure you
have the same version as the OpenFOAM you plan to use, this may require
changing branch.

![git\_releases.png](../../assets/images/OpenFOAM.png)

#### If releases are available

Open the 'releases' tab, right click on the '.tar' or '.zip' of the
version you want and select 'copy link address', then paste that link
into your terminal after `wget`. For example:

```sh
wget https://github.com/vincentcasseau/hyStrath/archive/Concordia.tar.gz
```

`wget` can also be used to fetch files from other sources.

#### If repo only

Use the command `git clone <path to repo>.git` For example:

```sh
git clone https://github.com/vincentcasseau/hyStrath.git
```

### Decompress

If your source is a .zip file use the command `unzip <filename>` if it
is a .tar.gz use the command `tar -xvzf <filename>`

From here steps will vary, it is best to check the README of the package
you are installing.

### wmake

`wmake` is an OpenFOAM tool used to compile code, based on `make`.

A more comprehensive description of the use of wmake can be
found [here](https://cfd.direct/openfoam/user-guide/v6-compiling-applications/).

A library/application named 'newApp' would have the structure.

 To build \`newApp\` one would run:

```sh
module load OpenFOAM
source $FOAM_BASH
wmake
```

However, most applications will involve building multiple libraries and
solvers, and will generally come with a shell script (`.sh`) that saves
the user having to compile each item manually.

Some apps will try to place the new libraries in `$FOAM_LIBBIN` and
objects in `$FOAM_APPBIN`, this will cause the build to fail as you will
not have permission to write there. Make sure the `Make/options` file
specifies variables `$FOAM_USER_LIBBIN` or `$FOAM_USER_APPBIN` instead.

### Location

User compiled libraries are kept in `$FOAM_USER_LIBBIN`, by default this
is set
to `~/$USER/OpenFOAM/$USER-<version>/platforms/linux64GccDPInt32Opt/lib`

User compiled objects are kept in `$FOAM_USER_APPBIN`, by default this
is set
to `~/$USER/OpenFOAM/$USER-<version>/platforms/linux64GccDPInt32Opt/bin`

You will need to change these locations if you want the rest of your
project members to have access.

For example

```sh
module load OpenFOAM
  
source $FOAM_BASH
  
export FOAM_USER_LIBBIN=/nesi/project/nesi99999/custom_OF/lib
export FOAM_USER_APPBIN=/nesi/project/nesi99999/custom_OF/bin
```

These variables need to be set to the same chosen paths before compiling
and before running the solvers.

!!! warning
     Make sure to `export` your custom paths before `source $FOAM_BASH`
     else they will be reset to default.
