---
created_at: 2026-10-12
description: The steps to start using Mahuika, from creating an account and getting a project to logging in and running your first job.
tags:
    - account
    - access
---


To use Mahuika you need an account, and you need to be a member of a project.
These steps take you from having neither to running your first job.


## Get access to Mahuika

1. **Create an account.**
    Log in to [my.nesi.org.nz](https://my.nesi.org.nz) with your institution's login and fill in your details.
    See [Creating an Account](Creating_an_Account.md).
2. **Get a project.**
    Either [apply for a new project](Projects/Applying_for_a_New_Project.md),
    or [join an existing project](Projects/Applying_to_Join_a_Project.md) by sending its owner your username.
    An approved project usually comes with an [allocation](Allocations/What_is_an_allocation.md) of compute and storage.
3. **Log in for the first time.**
    [First Time Login](Accessing_the_HPCs/First_Time_Login.md) sets up the authenticator app you use to log in.
    After that, [choose how to connect](Accessing_the_HPCs/Connecting_to_the_Cluster.md):
    in your web browser with OnDemand, or in a terminal over SSH.
4. **Run your first job.**
    The [Introduction to HPC](../Tutorials/Introduction_To_HPC/What_Is_an_HPC.md) tutorial walks you through it.
    If you have used a cluster before, go straight to the [Batch Computing Guide](../Batch_Computing/Batch_Computing_Guide.md).

If you get stuck at any step, see [Getting Help](Getting_Help/Contacting_Support.md).

## Words you will see

Account
:   Your access to Mahuika. You create it by logging in to my.nesi.org.nz with your institution's login.

Username
:   The name you log in to Mahuika with. To find it, log in to my.nesi.org.nz, and under **Account** click **My HPC Account**.

Project
:   A piece of research work on Mahuika, with an owner and members.
    Each project has a project code, such as `nesi99991`, which you give as the `--account` in your Slurm scripts.

Allocation
:   The amount of compute and storage a project can use over a set period.
    See [What Is an Allocation?](Allocations/What_is_an_allocation.md)
