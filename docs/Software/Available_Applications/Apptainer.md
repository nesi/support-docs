<center>
    
![apptainer-icon](../../assets/images/apptainer_icon.png)

</center>
!!! circle-info "The latest version of Apptainer is installed directly on the host operating system of both the login and compute nodes. We recommend using this system-wide version and advise against attempting to load Apptainer via environment modules. Loading the Apptainer module will trigger a message stating: "*The Apptainer environment module has been removed since the system Apptainer is now just as recent*"

!!! quote  ""
    ## Description 

    Apptainer (formerly Singularity) simplifies the creation and execution of containers, ensuring software components are encapsulated for portability and reproducibility

    <small>Home page  : https://apptainer.org</small>
    <br>
    <small>Github     : https://github.com/apptainer/apptainer</small>

    ## License

    Apptainer is open source software, distributed under the [BSD License](https://github.com/apptainer/apptainer/blob/main/LICENSE.md).

---

## **How to `pull` /  `build` / `inspect` / execute a container with `shell`, `exec`, `run`** 

!!! code "Set up APPTAINER_TMPDIR and APPTAINER_CACHEDIR before using Apptainer to avoid using your home directory for temporary and cache operations"

    By default, Apptainer will attempt to use your home directory for all operations, creating a hidden directory ~/.apptainer for this purpose. Since home directories are limited to 20GB, we recommend redirecting these operations to the nobackup filesystem. This can be achieved by setting the following environment variables before running Apptainer ( we are using the hypothetical path `/nesi/nobackup/nesi12345/apptainer-cache` to demonstrate this. Please make sure to replace `nesi12345` with your project code and then `apptainer-cache` with a valid directory)

    ```bash
    export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"
    export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}
    ```
    ??? quote "Add those environment variables to your `~/.bashrc` for future use"

        We recommend adding those environment variables to your `~/.bashrc` to make the future use cases of Apptainer. Please make sure to replace `/nesi/nobackup/nesi12345/apptainer-cache` with your nobackup directory. 

        ```bash
        echo 'export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"' >> ~/.bashrc
        echo 'export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}' >> ~/.bashrc
        ```
<br>

??? container "1. How to pull a container image from an upstream registry such as docker hub"
    
    Docker containers ( primarily stored in https://hub.docker.com/) can be pulled as Apptainer container images. For an example, if we want to pull the latest version of Tensorflow (GPU) container provided by the Tensorflow developers 

    * Search and find the container registry for TF in https://hub.docker/com. 
        * image we are after in this instance is https://hub.docker.com/r/tensorflow/tensorflow/tags

    * Copy tthe version you prefer with blue <kbd>Copy</kbd> button next to the corresponding tag. We will use `latest-gpu` as an example
        * It will be in the form of `docker pull tensorflow/tensorflow:latest-gpu`
        * IN order to pull this as an apptainer, remove the word `pull` and create a URL as `docker://tensorflow/tensorflow:latest-gpu`
    * Then pull it with `apptainer pull nameforthelocalimage.aif docker://tensorflow/tensorflow:latest-gpu`
        * `nameforthelocalimage.aif` is the name of the file to be saved once pulled. File extension can be anything but it is ideal to use `.aif` making it easier to idenity the container image 

    ```bash
    apptainer pull tensorflow-latest-gpu.aif docker://tensorflow/tensorflow:latest-gpu
    ```

??? container "2. How to build a container with `apptainer build --force --fakeroot`"

    Although we do not have a dedicated sandbox to build containers at the moment, `fakeroot` is enabled in both the login nodes and compute nodes allowing researchers to build containers as needed 

    * Since some container builds can consume a reasonable amount of CPUS and memory, our recommendation is to do this via a Slurm job ( interactive or batch queue). We will demonstrate this via the latter option
        * You will be required to prepare your container definition file ( It will be difficult for NeSI support to provide extensive support on writing container definition files but there are a number of online resources/tutorials with instructions/templates)
    * To illustrate this functionality, create an example container definition file *my_container.def* from a shell session on NeSI as follows:

    ```bash
    cat << EOF > my_container.def
    BootStrap: docker
    From: ubuntu:20.04
    %post
        apt-get -y update
        apt-get install -y wget
    EOF
    ```

    * Then submit the following Slurm job submission script to build the container:

    ```bash linenums="1"
    #!/bin/bash -e

    #SBATCH --job-name=apptainer_build
    #SBATCH --time=0-00:30:00
    #SBATCH --mem=4GB
    #SBATCH --cpus-per-task=2

    # recent Apptainer modules set APPTAINER_BIND, which typically breaks
    # container builds, so unset it here
    unset APPTAINER_BIND

    # create a build and cache directory on nobackup storage
    export APPTAINER_CACHEDIR="/nesi/nobackup/$SLURM_JOB_ACCOUNT/$USER/apptainer_cache"
    export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}
    mkdir -p ${APPTAINER_CACHEDIR}

    # build the container
    apptainer build --force --fakeroot my_container.aif my_container.def
    ```

    * If you encounter the following error when using a base Docker image in your Apptainer definition file

    ```bash
    While making image from oci registry: error fetching image to cache: while building SIF from layers: conveyor failed to get: unsupported image-specific operation on artifact with type "application/vnd.docker.container.image.v1+json"
    ```
    it is likely due to an upstream issue (e.g. bad image on Dockerhub). In this case, try an older image version or a different base image.

    * **Other limitations**
        - This method, using `fakeroot`, is known to not work for all types of Apptainer/Singularity containers. If you encounter an issue, please Contact our Support Team

??? container "3. Running a container, both interactively ( only the `shell`or `inspect` ) and via Slurm"

    * To have a look at the contents of your container, you can "shell" into it using `apptainer shell containername` . 
        ```bash
        apptainer shell my_container.aif
        ```
        **Note** - Above shell command will enter the shell within the container image. Note the prompt is now prefixed with "Apptainer",
        ```bash
        Apptainer>
        ```
        Exit the container by running the command `exit` which will bring you back to the **host** system 
        ```bash
        Apptainer> exit
        ```

    * To view metadata and configuration details about an Apptainer container image, use `apptainer inspect containername` 
        ```bash
        apptainer inspect my_container.aif
        ```
    * `apptainer exec` command 

        - The `apptainer exec` command allows you to run a specific command inside an Apptainer container, making it ideal for executing scripts, tools, or workflows within the container’s environment. For example, you can run a Python script or query the container’s filesystem without entering an interactive shell. Let't say you have a python script ( let's call it *my_tensorflow.py*) using Tensorflow libraries  with a help menu and assuming you have Tensorflow container with all required libraries 

        ```bash
        apptainer exec tensorflow-latest-gpu.aif my_tensorflow.py --help
        ```
    * The apptainer `run` command, on the other hand, is designed to execute the default process defined in the container (such as its runscript), providing a convenient way to start the container’s main application or service as intended by its creator. This is commonly used when you want to use the container as a standalone executable.

    **Slurm template** 

    ```bash
    #!/bin/bash -e

    #SBATCH --job-name=tensorflow-via-apptainer
    #SBATCH --time=01:00:00
    #SBATCH --mem=4G
    #SBATCH --ntasks=
    #SBATCH --cpus-per-task=4

    # Run container %runscript
    apptainer exec tensorflow-latest-gpu.aif my_tensorflow.py some_argument
    ```

??? container "4.  Accessing a GPU via Appptainer"

    * If your Slurm job has requested access to an NVIDIA GPU (see GPU use on NeSI to learn how to request a GPU), an Apptainer container can transparently access it using the --nv flag:

        ```bash
        apptainer exec --nv my_container.sif
        ```
    * For an example, 

        ```bash
        apptainer exec --nv tensorflow-latest-gpu.aif my_tensorflow.py some_argument
        ```

??? container "5. Network isolation"

    * Apptainer allows you to configure network isolation for containers using the `--net` flag with commands like `apptainer exeec --net`. By default, this isolates the container’s network to a loopback interface, meaning it cannot communicate with the host or external networks unless additional network types are specified. Administrators can enable advanced network types (such as bridge or ptp) for privileged users, but for most users, `--net` alone provides strong network isolation for security and reproducibility

        ```bash
        apptainer exec --nv --net --network=none tensorflow-latest-gpu.aif 
        ```


!!! stethoscope "Tips & Tricks"

    * Try to configure all software to run in user space without requiring privilege escalation via "sudo" or other privileged capabilities such as reserved network ports - although Singularity supports some of these features inside a container on some systems, they may not always be available on the HPC or other platforms, therefore relying on features such as Linux user namespaces could limit the portability of your container
    * If your container runs an MPI application, make sure that the MPI distribution that is installed inside the container is compatible with Intel MPI
    * Write output data and log files to the HPC filesystem using a directory that is bound into the container - this helps reproducibility of results by keeping the container image immutable, it makes sure that you have all logs available for debugging if a job crashes, and it avoids inflating the container image file
    
