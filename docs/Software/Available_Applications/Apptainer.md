---
title: Apptainer - Containers on HPC
tags:
    - apptainer
    - container
    - docker
    - reproducibility
---

Apptainer simplifies the creation and execution of containers on compute clusters, ensuring software components are encapsulated for portability and reproducibility.  Apptainer is an open-source fork of the Singularity project and shares much of the same functionailty.  Apptainer is now the default on many HPCs worldwide.
Apptainer is distributed under the [BSD License](https://github.com/apptainer/apptainer/blob/main/LICENSE.md).

---

??? container "1. Configure your environment for Apptainer"


    By default, Apptainer will attempt to use your home directory for all operations, creating a hidden directory `~/.apptainer` for this purpose. Since home directories are limited to 20GB, we recommend redirecting these operations to the nobackup filesystem. This can be achieved by setting the following environment variables before running Apptainer ( we are using the hypothetical path `/nesi/nobackup/nesi12345/apptainer-cache` to demonstrate this. Please make sure to replace `nesi12345` with your project code and then `apptainer-cache` with a valid directory)

    ```bash
    export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"
    export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}
    mkdir -p $APPTAINER_CACHEDIR
    ```

    We recommend adding those environment variables to your `~/.bashrc` to make the future use cases of Apptainer. Please make sure to replace `/nesi/nobackup/nesi12345/apptainer-cache` with your nobackup directory. 

        ```bash
        echo 'export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"' >> ~/.bashrc
        echo 'export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}' >> ~/.bashrc
        ```

??? container "2. How to pull a container image from an upstream registry such as docker hub"
    
    Docker containers are primarily stored at the Docker Hub registry.  Docker images are OCI compliant and therefore can be built as Apptainer images, also known as Singularity Image Format (SIF) files. For example, if we want to pull the latest version of Redis, we would do the following:

    * Search and find the container registry for Redis in https://hub.docker.com. 
        * The Redis developers page should be one of the results, and it can be found here: https://hub.docker.com/r/redis/redis-stack

    * Now check the command in the Tag Summary section, 
        * It will show: `docker pull redis/redis-stack`  
        * In order to pull or build this as an apptainer, copy the last part of the command and create a URL: `docker://redis/redis-stack`
    * Now you can pull it with the command `apptainer pull <output_file> <Docker_image>
        * `<output_file>` is the name of the file to be saved once pulled.  You can call it whatever you like but it should be descriptive. File extension can be anything but it is ideal to use `.sif` making it easier to idenity as a container image. So in our example you would run:

    ```bash
    apptainer pull redis.sif docker://redis/redis-stack
    ```

??? container "3. How to build a container"

    Although we do not have a dedicated sandbox to build containers at the moment, `fakeroot` is enabled in both the login nodes and compute nodes allowing researchers to build containers as needed 

    * Since some container builds can consume a reasonable amount of CPU and memory, our recommendation is to do this via a Slurm job ( interactive or batch queue). We will demonstrate this via the latter option
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

    # create a build and cache directory on nobackup storage, this is unnecessary if you already setup
    # the cache and tmp directories from step one in our Apptainer docs.
    export APPTAINER_CACHEDIR="/nesi/nobackup/$SLURM_JOB_ACCOUNT/$USER/apptainer_cache"
    export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}
    mkdir -p ${APPTAINER_CACHEDIR}

    # build the container
    apptainer build --force --fakeroot my_container.sif my_container.def
    ```

    * **NOTES**

        * The method of using `fakeroot` is known to not work for all types of Apptainer containers. If you encounter an issue, please contact our support team: <support@nesi.org.nz>

        * If you encounter the following error when using a base Docker image in your Apptainer definition file
        it is likely due to an upstream issue (e.g. bad image on Dockerhub). In this case, try an older image version or a different base image.

            * ```bash
            error fetching image to cache: while building SIF from layers: conveyor failed to get: unsupported image-specific operation on artifact with type "application/vnd.docker.container.image.v1+json"
            ```


??? container "4. Running a container interactively and as a batch job"

    * To have a look at the contents of your container, you can connect to it using `apptainer shell containername`.  When you see your prompt change to `Apptainer>` you have ssuccessfully connected and are now running from within the container. 
        ```bash
        apptainer shell my_container.sif

        Apptainer>
        ```
        Exit the container by running the command `exit` which will bring you back to the **host** system 
        ```bash
        Apptainer> exit
        ```

    * To view metadata and configuration details about an Apptainer container image, use `apptainer inspect containername` 
        ```bash
        apptainer inspect my_container.sif
        
        Author: Bruce Wayne
        Description: Batmobile API
        Version: v1.0
        org.label-schema.build-arch: amd64
        org.label-schema.build-date: Monday_8_December_2025_11:0:48_NZDT
        org.label-schema.schema-version: 1.0
        org.label-schema.usage.apptainer.version: 1.4.0-1.el9
        org.label-schema.usage.singularity.deffile.bootstrap: docker
        org.label-schema.usage.singularity.deffile.from: ubuntu:24.04
        org.opencontainers.image.ref.name: ubuntu
        org.opencontainers.image.version: 24.04
        ```

    * `apptainer exec` command 

        - The `apptainer exec` command allows you to run a specific command inside an Apptainer container, making it ideal for executing scripts, tools, or workflows within the container’s environment. For example, you can run a Python script or query the container’s filesystem without entering an interactive shell. Let't say you have a python script ( let's call it *my_tensorflow.py*) using Tensorflow libraries  with a help menu and assuming you have Tensorflow container with all required libraries 

        ```bash
        apptainer exec tensorflow-latest-gpu.sif my_tensorflow.py --help
        ```
    * The `apptainer run` command, on the other hand, is designed to run the default process defined in the container (such as its runscript), providing a convenient way to start the container’s main application or service as intended by its creator. This is commonly used when you want to use the container as a standalone executable.
        ```bash
        apptainer run /nesi/project/nesi99999/containers/qgis.sif
        ```
        or the following would be equivalent:
        ```bash
        /nesi/project/nesi99999/containers/qgis.sif
        ```

    * Slurm template for running a container

        ```bash
        #!/bin/bash -e

        #SBATCH --job-name=container-job
        #SBATCH --time=01:00:00
        #SBATCH --mem=4G
        #SBATCH --ntasks=
        #SBATCH --cpus-per-task=4

        # Run container %runscript
        apptainer run tensorflow-latest-gpu.sif my_tensorflow.py some_argument
        ```

??? container "5.  Accessing a GPU via Apptainer"

    * If your Slurm job has requested access to an NVIDIA GPU (see GPU use on NeSI to learn how to request a GPU), an Apptainer container can transparently access it using the --nv flag:

        ```bash
        apptainer exec --nv my_container.sif
        ```
    * For an example, 

        ```bash
        apptainer exec --nv tensorflow-latest-gpu.sif my_tensorflow.py some_argument
        ```

??? container "6. Network Isolation & Ports"

    * Apptainer allows you to configure network isolation for containers using the `--net` flag with commands like `apptainer exeec --net`. By default, this isolates the container’s network to a loopback interface, meaning it cannot communicate with the host or external networks unless additional network types are specified. Administrators can enable advanced network types (such as bridge or ptp) for privileged users, but for most users, `--net` alone provides strong network isolation for security and reproducibility

        ```bash
        apptainer exec --nv --net --network=none my_container.sif 
        ```

    * You can run a service from within a container, such as web or DB server, but they must be configured to run on an unprivileged port.  Unprivileged ports are those > 1024, up to the maximum 65535

        ```bash
        Bootstrap: docker
        From: nginx
        Includecmd: no

        %post
            sed -i 's/80/8080/' /etc/nginx/conf.d/default.conf


        %startscript
        nginx
        ```

        Once the container is built you would start the container with the `apptainer instance` command:

        ```bash
        apptainer instance start nginx.sif nginx
        ```
        Remember to stop the instance once your work in completed:
        ```bash
        apptainer instance stop nginx
        ```



??? container "7. Tips & Best Practice"

    * Try to configure all software to run in user space without requiring privilege escalation via "sudo" or other privileged capabilities such as reserved network ports - although Apptainer supports some of these features inside a container on some systems, they may not always be available on the HPC or other platforms, therefore relying on features such as Linux user namespaces could limit the portability of your container
    * If your container runs an MPI application, make sure that the MPI distribution that is installed inside the container is compatible with the version of MPI on the cluster.
    * Write output data and log files to the HPC filesystem using a directory that is bound into the container - this helps reproducibility of results by keeping the container image immutable, it makes sure that you have all logs available for debugging if a job crashes, and it avoids inflating the container image file
    
