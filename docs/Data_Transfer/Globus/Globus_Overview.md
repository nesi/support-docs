---
created_at: '2021-08-27T03:18:13Z'
tags: 
    - globus
    - file transfer
---

!!! note
    For other data transfer methods, see [Data_Transfer_Overiew](../Data_Transfer_Overview.md)

Globus is a data transfer service that can be used to move a large amount of data between Mahuika and another system such as your computer, a server, or your institute's high capacity storage system.

The following guide shows how to:

* [How to set up Globus for the first time](./First_Time_Setup.md)
* [How to set up a **free** Globus Subscription](./Signing_Up_To_Globus_Subscription.md)
* [How to add your computer to Globus (if you would like to transfer data to your computer)](./Add_Your_Computer_To_Globus.md)
* [How to transfer data to/from Mahuika](./Data_Transfer_using_Globus.md)
* [How to transfer data between endpoints other than Mahuika](./Data_Transfer_Between_Personal_Endpoints.md)

This page also contains other useful information on how to use Globus, including:

* [Adding Bookmarks](./Bookmarks.md)
* [Sharing Data with colleagues using Globus](./Share_Collections.md)
* [Automating Globus](./Syncing_files_with_globus_automate.md)
* [Using the Globus Command Line Interface (CLI) to transfer data](./Globus_CLI.md)

## When should I use Globus?

Globus has been set up for transferring large amounts of data to/from Mahuika to the outside world. 

* Do not use Globus if you are wanting to move data _within_ Mahuika (i.e. between or within your `home`, `project`, and `nobackup` directories). If you want to move data within Mahuika, consider using copy (`cp`), move (`mv`), [RClone](../RClone.md), or [Rsync](../Rsync.md). 

## Advantages of Globus

Globus allows users to transfer large amounts of data between systems. Some advantages of using Globus are that:

* It uses a web-based graphical user interface to help users navigate through file systems and transfer data.
* Globus will perform data transfers in the background, allowing you to shutdown your computer while the transfer continues (as long as you are not transferring data to your computer)
* If there are any disruptions to your transfer, Globus can resume from where it left off.

## Glossary

* Endpoints: Globus refers to computers, servers, and high capacity storage systems as endpoints.

## Quick Information

* Name of Mahuika endpoint: `NeSI HPC Storage` (_Note: This name was chosen for the endpoint prior NeSI's integration with REANNZ in 2025._)
* Name of NeSI Subscription: `New Zealand eScience Infrastructure Standard`
