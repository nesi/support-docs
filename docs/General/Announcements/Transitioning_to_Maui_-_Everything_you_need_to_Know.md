To make your transition experience (from Kupe to Māui) as seamless as
possible, there are several important steps and points you need to take
into consideration. **Please read this entire article before trying to
access Māui.**

**Note: **Please
[report](mailto:support@nesi.org.nz?subject=Reporting%20an%20error%20in%20the%20Transition%20to%20Maui%20documentation)
errors in the details provided here. As we will update the content on
this page to correct errors or add new information *do refresh this page
from time to time*.

Documentation & Training Information
------------------------------------

We are in the process of completely refreshing the [user support
website](https://support.nesi.org.nz), providing access to information
categorised by:

-   **[Getting
    Started](https://support.nesi.org.nz/hc/en-gb/categories/360000013856)** --
    all you need to know about the NeSI HPCs and how to apply for a
    Research Project Allocation, create an account on the new HPCs and
    login
-   **[Scientific
    Computing](https://support.nesi.org.nz/hc/en-gb/categories/360000013836)**
    -- all you need to know about how to run jobs, what software is
    available, links to training material, user guides and manuals, etc.
-   [**Storage**](https://support.nesi.org.nz/hc/en-gb/categories/360000014696)
    -- covering the file systems, I/O performance considerations,
    recovery of files, data transfer services, etc.
-   [**General**](https://support.nesi.org.nz/hc/en-gb/categories/200261597-General)
    -- including [important
    announcements](https://support.nesi.org.nz/hc/en-gb/sections/200732737)
    and [frequently asked
    questions](https://support.nesi.org.nz/hc/en-gb/sections/360000039036)
-   User Support -- coming soon

If you have a problem -- please look on the support website before
raising a ticket. The search function works well.

Getting Started
---------------

### Already have a NeSI Account

If you already have a NeSI account (and if required, a 2nd Factor
Token), you are good to go, simply:

1.  If you are using two-factor authentication, simply login to
    `lander02.nesi.org.nz`, then
2.  ssh to `login.maui.nesi.org.nz` as you would have done on Kupe.

There is more detail
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000161315-Logging-in-to-the-HPCs). 
But if you are not able to login, then contact <support@nesi.org.nz>
**before doing anything else, such as a password reset**.

### New to NeSI

If you are new to NeSI -- there are some initial steps that you must
take (one-time only):

1.  Create a [My NeSI
    Account](https://support.nesi.org.nz/hc/en-gb/articles/360000159715-Creating-a-NeSI-Account) and
    accept the Acceptable Use [Terms and
    Conditions](https://www.nesi.org.nz/services/high-performance-computing/guidelines/acceptable-use-policy).
2.  Reset the temporary
    [password](https://support.nesi.org.nz/hc/en-gb/articles/360000335995-Resetting-Your-Password)
    to one of your choosing that conforms to the [NeSI Password
    Policy](https://support.nesi.org.nz/hc/articles/360000336015). While
    special characters meet the password policy, we have seen problems
    with their use. It may be best to not use special characters.

If you must access NeSI from outside NIWA you will need to set up
[two-factor
authentication](https://support.nesi.org.nz/hc/en-gb/articles/360000203075-Setting-Up-Two-Factor-Authentication).

If using two factor authentication, then you will be ready to log on to
the NeSI lander node, then to jump to a Māui login node.

-   To log on to Māui, follow the instructions
    [here](https://support.nesi.org.nz/hc/en-gb/articles/360000161315-Logging-in-to-the-HPCs).

Other Important Information
---------------------------

[This link](https://support.nesi.org.nz/hc/en-gb/sections/360000034335)
provides useful information about the new HPCs.

You can gain a better understanding of the Māui filesystems
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas).
In particular, please note:

-   Māui (shared with Mahuika), i.e. the HPCF, has a very large, very
    high performance scratch file system called `/nesi/nobackup`. You
    should do most of your computing in this file system.
-   Data in `/nesi/nobackup` will be automatically removed from time to
    time.
-   We are developing a nearline data service to help you move data off
    disk and onto tape, and vice versa.

Details of how the workload manager (Slurm) is configured (for NeSI
users) on Māui can be
found [here](https://support.nesi.org.nz/hc/en-gb/articles/360000204116-M%C4%81ui-Slurm-Partitions).
In particular, please note:

-   We have introduced a `nesi_debug` quality of service (QoS) for rapid
    turnaround of test jobs. Each user may only have one job using the
    `nesi_debug` QoS setting at any time.
-   You will now need to specify the Slurm partition in which your job
    will run.
-   There is a Slurm primer
    [here](https://support.nesi.org.nz/hc/en-gb/articles/360000359576-Primer-Slurm-Usage)
    that provides additional information about how to submit jobs
    between the Māui and Māui\_Ancil Slurm clusters.

You should have access to the same software you used Kupe. See how to
[find
modules](https://support.nesi.org.nz/hc/en-gb/articles/360000360576-Finding-Software)
using the -S option on Māui (which will also be available of Māui\_Ancil
nodes in November).  Notice too that we are introducing a [new support
model](https://support.nesi.org.nz/hc/en-gb/articles/360000170355-NeSI-Application-Support-Model).

The following link provides information on how to [compile and link
software](https://support.nesi.org.nz/hc/en-gb/articles/360000336076-Compiling-software-on-M%C4%81ui)
on Māui:

If you run into a problem, please put in a
[ticket](https://support.nesi.org.nz/hc/en-gb/requests/new).

### Significant Change to Software Stack

While all relevant software has been migrated from kupe, kupe\_mp and
the Virtual Labs, a few important changes have been made:

-   There is now a clearer separation between the maui\_ancil, and
    Virtual Labs (CS500) and maui (XC50) software stacks: the maui
    software stack only contains software needed for large jobs (e.g.,
    XIOS and the grib\_api library), while general tools and libraries
    (e.g., Anaconda, NCO, and Mule) can now only be found on the
    maui\_ancil and Virtual Lab machines. This ensures that we make best
    use of system capabilities, and **avoid single core jobs running on
    maui** (i.e. XC50).
-   The maui\_ancil and Virtual Labs software stack now uses a more
    recent GNU toolchain based on GCC v7.1.0, to benefit from Intel
    Skylake architecture capabilities. Module names have therefore
    changed slightly with respect to Kupe.
-   To avoid clutter, older versions of the same software have not been
    migrated, with the exception of NCL.

Data Synchronisation
--------------------

Unless you have advised us otherwise, all the data you have stored on
Kupe's  `/home, /nesi/project`, and `/nesi/nobackup` filesystems has
been transferred to Māui's `/home, /nesi/project`, and `/nesi/nobackup`
filesystems. 

**Syncing will continue until you delete the files**:

-   `/home/<user name>/KUPE_SYNC`
-   `/nesi/project/<project_id>/KUPE_SYNC`
-   `/nesi/nobackup/<project_id>/KUPE_SYNC`

From either Kupe or Māui. 

**Until you delete these files any file you create on Māui will be
removed at the next sync.**

### Data Loss Risk Mitigation

The HPCF `/home, /nesi/project` and `/nesi/nobackup` filesystems were
\"snapshoted\" at 6 pm on 19-Sep-2018.  Accordingly, should the final
phase of syncing between Kupe and the HPCF delete files that you did not
want deleted, they will be recoverable back to the state they were in at
the time of these snapshots. This
[link](https://support.nesi.org.nz/hc/en-gb/articles/360000207315-Recover-from-the-Snapshot-home-only-)
explains how to recover deleted data from a snapshot of the /home
filesystem on the HPCF.

**NOTE WELL**: If you do recover your data from a snapshot, you MUST 
remove the `KUPE_SYNC` file - otherwise at the next sync your data will
be deleted again.

Personal /nesi/nobackup Directories
-----------------------------------

Please recall the information we have [previously provided re personal
home
directories](https://support.nesi.org.nz/hc/en-gb/articles/360000431415-Kupe-to-Maui-Data-Migration)
on /nesi/nobackup. In particular that:

\"On the HPCF your personal directory will be set to Read Only.  This
will allow you to copy relevant data into the correct project directory
(e.g. to `/nesi/nobackup/niwa00111/bloggs`), as it is not possible to
support personal nobackup directories on the HPCF.\"

File System Quotas
------------------

Unlike on Kupe, [filesystem capacity and inode
quotas](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas)
are being enforced on the HPCF.  To determine how much data you have,
and what your current quotas are use:

`nn_check_quota --help`

Then re-run with the appropriate settings.

We will need to set new quotas for all users and projects transitioning
from Kupe to Māui (i.e. the shared HPCF filesystems). You should review
the purpose of each filesystem as explained
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas),
and the [associated
permissions](https://support.nesi.org.nz/hc/en-gb/articles/360000205435-File-Permissions),
then consider what quotas are needed to support your research project,
then submit a [request for a
change](mailto:support@nesi.org.nz?subject=Requesting%20a%20change%20quota%20on%20Maui)
in quota.

 

This does not apply to NIWA Forecast Operations on Kupe.

 
