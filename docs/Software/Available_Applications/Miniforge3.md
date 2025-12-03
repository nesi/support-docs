---
created_at: '2020-06-23T23:10:13Z'
tags: 
  - python
  - environments
---

!!! note "Preferred Alternatives"
     - If you want a more reproducible and isolated environment, we
         recommend using the [Apptainer containers](Apptainer.md).
     - If you only need access to Python and standard numerical libraries
         (numpy, scipy, matplotlib, etc.), you can use the 
         [Python environment module](Python.md).

{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

The `Miniforge3` environment module provides the
[Conda](https://docs.conda.io/projects/conda/en/latest/) package and
environment manager. Conda lets you install packages and their
dependencies in dedicated environment, giving you more freedom to
install software yourself at the expense of possibly less optimized
packages and no curation by the NeSI team.

## Module loading and conda environments isolation

When using the Miniforge3 module, we recommend using the following
snippet to ensure that your conda environments can be activated and are
isolated as possible from the rest of the system:

``` sh
module purge && module load Miniforge3
source $(conda info --base)/etc/profile.d/conda.sh
export PYTHONNOUSERSITE=1
```

Here are the explanations for each line of this snippet:

- `module purge && module load Miniforge3` ensures that no other
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

!!! warning "Defaults Channel"
     If you are using a `environment.yml` file, you will have to remove the
     `defaults` channel, or you will receive an error.
     
     ``` out
     Failed to create Conda environment
     The channel is not accessible or is invalid.
     ``` 
     
     The `defaults` channel is blocked due to Anaconda's licensing requirements.
     
## Prevent conda from using /home storage

Conda environments and the conda packages cache can take a lot of
storage space. By default, Conda use
[/home](../../Storage/File_Systems_and_Quotas/Filesystems_and_Quotas.md),
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
     (details available in the [Nobackup autodelete](../../Storage/File_Systems_and_Quotas/Automatic_cleaning_of_nobackup_file_system.md)
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

``` sh
conda env create -f environment.yml -p /nesi/project/<project_code>/my_conda_env
```

!!! tip "Reduce prompt prefix"
     By default, when activating a conda environment created with `-p` or
     `--prefix`, the entire path of the environment is be added to the
     prompt. To remove this long prefix in your shell prompt, use the
     following configuration:
     ``` sh
     conda config --set env_prompt '({name})'
     ```
