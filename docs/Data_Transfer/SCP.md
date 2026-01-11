---
created_at: 2026-01-05
title: SCP (Secure Copy)
description: How to transfer data on the REANNZ HPC using SCP.
---

!!! prerequisite
    Have SSH setup as described in [Standard Terminal Setup](../Getting_Started/Accessing_the_HPCs/Standard_Terminal_Setup.md)

`scp` stands for Secure CoPy and operates in a similar way to regular cp
with the source file as the left term and destination on the right.
These commands make use of *multiplexing*, this means that if you
already have a connection to the cluster you will not be prompted for
your password.

On your **local terminal**, if you would like to:

* Move a file from your local machine to Mahuika:

    ```bash
    scp <path/filename> mahuika:<path/filename>
    ```

* Move a file from Mahuika to your local machine:

    ```bash
    scp mahuika:<path/filename> <path/filename>
    ```

!!! note
    - This will only work if you have set up aliases as described in
      [Terminal Setup](../Getting_Started/Accessing_the_HPCs/Standard_Terminal_Setup.md).
    - As the term 'mahuika' is defined locally, the above
      commands *only works when using a local terminal* (i.e. not on Mahuika).
    - If you are using Windows subsystem, the root paths are different
      as shown by Windows. e.g. `C:` is located at `/mnt/c/`
