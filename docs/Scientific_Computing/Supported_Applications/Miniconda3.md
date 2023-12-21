---
created_at: '2020-06-23T23:10:13Z'
hidden: false
weight: 12
tags: []
title: Miniconda3
vote_count: 4
vote_sum: 4
zendesk_article_id: 360001580415
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

The `Miniconda3` environment module provides the
[Conda](https://docs.conda.io/projects/conda/en/latest/) package and
environment manager. Conda lets you install packages and their
dependencies in dedicated environment, giving you more freedom to
install software yourself at the expense of possibly less optimized
packages and no curation by the NeSI team.

!!! note "Alternatives"
     - If you want a more reproducible and isolated environment, we
         recommend using the [Singularity
         containers](../../Scientific_Computing/Supported_Applications/Singularity.md).
     - If you only need access to Python and standard numerical libraries
         (numpy, scipy, matplotlib, etc.), you can use the [Python
         environment
         module](../../Scientific_Computing/Supported_Applications/Python.md).

!!! tip "Māui Ancillary Nodes"
     On Māui Ancillary Nodes, you can also use the `Anaconda3` module,
     which provides a default environment pre-installed with a set of
     numerical libraries (numpy, scipy, matplotlib, etc.).

## Module loading and conda environments isolation

When using the Miniconda3 module, we recommend using the following
snippet to ensure that your conda environments can be activated and are
isolated as possible from the rest of the system:

``` sh
module purge && module load Miniconda3
source $(conda info --base)/etc/profile.d/conda.sh
export PYTHONNOUSERSITE=1
```

Here are the explanations for each line of this snippet:

- `module purge && module load Miniconda3` ensures that no other
    environment module can affect your conda environments. In
    particular, the Python environment module change the `PYTHONPATH`
    variable, breaking the isolation of the conda environments. If you
    need other environment modules, make sure to load them after this
    line.
- `source $(conda info --base)/etc/profile.d/conda.sh` ensures that
    you can use the `conda activate` command.
- `export PYTHONNOUSERSITE=1` makes sure that local packages installed
    in your home folder `~/.local/lib/pythonX.Y/site-packages/` (where
    `X.Y` is the Python version, e.g. 3.8) by `pip install --user` are
    excluded from your conda environments.

!!! warning
     We **strongly** recommend against using `conda init`. It inserts a
     snippet in your `~/.bashrc` file that will freeze the version of conda
     used, bypassing the environment module system.

!!! note "Māui Ancillary Nodes"
     On Māui Ancillary Nodes, you need to (re)load the `NeSI` module after
     using `module purge`:
     ``` sl
     module purge && module load NeSI Miniconda3
     source $(conda info --base)/etc/profile.d/conda.sh
     export PYTHONNOUSERSITE=1
     ```

## Prevent conda from using /home storage

Conda environments and the conda packages cache can take a lot of
storage space. By default, Conda use [/home
storage](../../Storage/File_Systems_and_Quotas/NeSI_File_Systems_and_Quotas.md),
which is restricted to 20GB on NeSI. Here are some techniques to avoid
running out of space when using Conda.

First, we recommend that you move the cache folder used for downloaded
packages on the `nobackup` folder of your project:

``` sh
conda config --add pkgs_dirs /nesi/nobackup/<project_code>/$USER/conda_pkgs
```

where `<project_code>` should be replace with your project code. This
setting is saved in your `~/.condarc` configuration file.
!!! prerequisite Note
     Your package cache will be subject to the nobackup autodelete process
     (details available in the [Nobackup
     autodelete](../../Storage/File_Systems_and_Quotas/Automatic_cleaning_of_nobackup_file_system.md)
     support page). The package cache folder is for temporary storage so it
     is safe if files within the cache folder are removed.

Next, we recommend using the `-p` or `--prefix` options when creating
new conda environments, instead of `-n` or `--name` options. Using `-p`
or `--prefix`, you can specify the conda environment folder location,
ideally in your project folder. For example:

``` sh
conda create --prefix /nesi/project/<project_code>/my_conda_env python=3.8
```

Then use the path of the conda environment to activate it:

``` sh
conda activate /nesi/project/<project_code>/my_conda_env
```

Note that `-p` and `--prefix` options can also be used when creating an
environment from an `environment.yml` file:

``` sl
conda env create -f environment.yml -p /nesi/project/<project_code>/my_conda_env
```

!!! tip "Reduce prompt prefix"
     By default, when activating a conda environment created with `-p` or
     `--prefix`, the entire path of the environment is be added to the
     prompt. To remove this long prefix in your shell prompt, use the
     following configuration:
     ``` sl
     conda config --set env_prompt '({name})'
     ```

## Faster solver `mamba` (experimental feature)

If you are using the module `Miniconda3/`*`22.11.1-1`*, you can
accelerate conda environments creation and package installation using
the new `libmamba` solver. To use it, append the option
`--solver=libmamba` to your command.

For example, to create an environment from an `environment.yml` file,
use:

``` sh
conda env create --solver=libmamba -f environment.yml -p venv
```

or to install a package in an activate environment, use:

``` sh
conda install --solver=libmamba CONDA_PACKAGE
```

where `CONDA_PACKAGE` is the package of interest.
