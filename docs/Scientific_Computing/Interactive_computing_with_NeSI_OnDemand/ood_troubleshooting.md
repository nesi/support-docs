# NeSI OnDemand - Troubleshooting 



## "Error -- can't find user for …" messages

If you see this message after logging in, please reach out to us at [support@nesi.org.nz](mailto:support@nesi.org.nz) and we will be able to fix this problem.

## UX, wording, information display

Due to this environment being our test build, you may encounter many internal technical terms that will be addressed through future iterations.

## User home folder default content

Pre-populated with [Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos] folders, which is different to NeSI default.


## NeSI OnDemand Current limitations¶

| Limitation                                |  What are the missing functions/commands associated with this|
--------------------------------------------|--------------------------------------------------------------|
|1. OnDemand apps  are not exposed to HPC3 Slurm | Commands such as `sbatch`, `sacct`, `squeue` , `scancel` will not work from OnDemand apps|
|2. Missing user Namespaces in Kubernetes pods will interfere with some Apptainer operations| Although we can run `apptainer pull` command, `apptainer exec,run,shell` commands can not be executed due to missing user Namespaces|

!!! quote ""


    🙋 If you to come across above limitations, please consider switching to a HPC3 login node via `Cluster` > `NeSI HPC Shell access` via OnDemand home page

    <p align="center">
    <img src="https://raw.githubusercontent.com/nesi/support-docs/main/docs/assets/images/OOD_howtoaccesslogin_node_shell.png" alt="image-20240903-112029" width="800">
    </p>


