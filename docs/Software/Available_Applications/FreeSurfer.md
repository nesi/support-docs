[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
[//]: <> (APPS PAGE BOILERPLATE END)


## Prerequisites

!!! quote ""

    * You will be required to obtain a license (it's free) from http://surfer.nmr.mgh.harvard.edu/registration.html
    * Once obtained, save it as *license.txt* ( original filename ) and save it anywhere in the filesystem. ( ideally, home or project directory)


## Slurm template to run FreeSurfer

* FreeSurfer container/s is/are stored in `/opt/nesi/container/FreeSurfer` ( this is an image pulled from https://hub.docker.com/r/freesurfer/freesurfer)
* We provide a sample dataset which can be used for a test run. This is stored in `/opt/nesi/container/FreeSurfer/data`

!!! quote ""

    ```bash linenums="1"

    #!/bin/bash -e 

    #SBATCH --job-name      freesurfer-test 
    #SBATCH --cpus-per-task 2
    #SBATCH --mem           2G
    #SBATCH --time          00:30:00
    #SBATCH --output        slog/%j.out

    module purge >/dev/null 2>&1
    module load Apptainer

    echo "Starting at: $(date)"

    # Set up FreeSurfer environment variables
    export SUBJECTS_DIR=$PWD/subjects_dir
    mkdir -p $SUBJECTS_DIR

    # Path to your FreeSurfer license file
    export FS_LICENSE=${PWD}/license.txt
    # Make sure the license file exists and is readable
    if [ ! -f "$FS_LICENSE" ]; then
        echo "ERROR: License file not found at $FS_LICENSE"
        exit 1
    fi


    # Path to container and data
    CONTAINER=/opt/nesi/container/FreeSurfer/freesurfer-7.4.1.aimg
    TEST_DATA=${PWD}/data/T1.nii.gz

    # Run a minimal recon-all, passing SUBJECTS_DIR into the container
    apptainer exec \
      --env SUBJECTS_DIR=$SUBJECTS_DIR \
      --env FS_LICENSE=$FS_LICENSE \
      --bind $SUBJECTS_DIR:$SUBJECTS_DIR \
      --bind $(dirname $TEST_DATA):$(dirname $TEST_DATA) \
      --bind $(dirname $FS_LICENSE):$(dirname $FS_LICENSE) \
      $CONTAINER \
      recon-all -i $TEST_DATA -sd $SUBJECTS_DIR -s test_subject -autorecon1 -no-isrunning

    echo "Job finished at: $(date)"
    ```
    **Environment Variables**

    ```bash

    # Set up FreeSurfer environment variables
    export SUBJECTS_DIR=$PWD/subjects_dir
    mkdir -p $SUBJECTS_DIR

    # Path to your FreeSurfer license file
    export FS_LICENSE=${PWD}/license.txt
    ```

    - `SUBJECTS_DIR`: This environment variable tells FreeSurfer where to store and find subject data. In this script, it's set to a directory named "subjects_dir" in the current working directory.
    - `FS_LICENSE`: FreeSurfer requires a license file to run. This environment variable points to that file, which in this case is expected to be in the current working directory.

    **Apptainer Options**

    - `exec`: Runs a command within the container
    - `--env VARIABLE=VALUE`: Passes environment variables into the container
        - Both `SUBJECTS_DIR` and `FS_LICENSE` are passed so FreeSurfer knows where to find subjects and the license
    - `--bind SOURCE:DESTINATION`: Mounts a directory from the host into the container
        - Three bind mounts are used:
            - The subjects directory
            - The directory containing the input data
            - The directory containing the license file
        - The `$(dirname $PATH)` syntax extracts the directory portion of a file path
