# NeSI OnDemand Current limitations¶

| Limitation                                |  What are the missing functions/commands associated with this|
--------------------------------------------|--------------------------------------------------------------|
|1. OnDemand apps  are not exposed to HPC3 Slurm | Commands such as `sbatch`, `sacct`, `squeue` , `scancel` will not work from OnDemand apps|
|2. Missing user Namespaces in Kubernetes pods will interfere with some Apptainer operations| Although we can run `apptainer pull` command, `apptainer exec,run,shell` commands can not be executed due to missing user Namespaces|

!!! quote ""


    🙋 If you to come across above limitations, please consider switching to a HPC3 login node via `Cluster` > `NeSI HPC Shell access` via OnDemand home page

    <p align="center">
    <img src="https://raw.githubusercontent.com/nesi/support-docs/main/docs/assets/images/OOD_howtoaccesslogin_node_shell.png" alt="image-20240903-112029" width="800">
    </p>



