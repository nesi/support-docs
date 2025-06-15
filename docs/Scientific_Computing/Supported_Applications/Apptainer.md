# Apptainer

!!! circle-info "The latest version of Apptainer is installed directly on the host operating system of both the login and compute nodes. We recommend using this system-wide version and advise against attempting to load Apptainer via environment modules. Loading the Apptainer module will trigger a message stating: "*The Apptainer environment module has been removed since the system Apptainer is now just as recent*"

!!! quote  ""
    ## Description 

    Apptainer (formerly Singularity) simplifies the creation and execution of containers, ensuring software components are encapsulated for portability and reproducibility

    <small>Home page  : https://apptainer.org</small>
    <br>
    <small>Github     : https://github.com/apptainer/apptainer</small>

    ## License

    Apptainer is open source software, distributed under the [BSD License](https://github.com/apptainer/apptainer/blob/main/LICENSE.md).

## **How to `pull` /  `build` / `inspect` / execute a container with `shell`, `exec`, `run`** 

!!! code "Set up APPTAINER_TMPDIR and APPTAINER_CACHEDIR before using Apptainer to avoid using your home directory for temporary and cache operations"

    By default, Apptainer will attempt to use your home directory for all operations, creating a hidden directory ~/.apptainer for this purpose. Since home directories are limited to 20GB, we recommend redirecting these operations to the nobackup filesystem. This can be achieved by setting the following environment variables before running Apptainer ( we are using the hypothetical path `/nesi/nobackup/nesi12345/apptainer-cache` to demonstrate this. Please make sure to replace `nesi12345` with your project code and then `apptainer-cache` with a valid directory)

    ```bash
    export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"
    export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}
    ```
    ??? quote "Add those environmant variables to your `~/.bashrc` for future use"

        We recommend adding those environment variables to your `~/.bashrc` to make the future use cases of Apptainer. Please make sure to replace `/nesi/nobackup/nesi12345/apptainer-cache` with your nobackup directory. 

        ```bash
        echo 'export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"' >> ~/.bashrc
        echo 'export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}' >> ~/.bashrc
        ```

