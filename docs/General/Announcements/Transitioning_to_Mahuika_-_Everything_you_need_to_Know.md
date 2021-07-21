To make your transition experience as seamless as possible, there are
several important steps and points you need to take into consideration.
**Please read this entire article before trying to access Mahuika.**

**Note: **Please
[report](mailto:support@nesi.org.nz?subject=Reporting%20an%20error%20in%20the%20Transition%20to%20Mahuika%20documentation)
errors in the details provided here - we will update the content on this
page as soon as possible. So do refresh this page from time to time.

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

As new services are made available, we will add new information to this
website.

### Training Opportunities

-   We are providing [Training
    Opportunities](https://www.nesi.org.nz/news/2018/07/nesi-new-platforms-user-training-dates-confirmed-registration-now-open)
    at a number of locations. To register, please fill in the relevant
    section in the link.
-   However, if you plan to attend training, you must complete the three
    steps specified at \"Getting Started\" (below) before attending your
    training session.

Getting Started
---------------

Before you can log on to Mahuika, there are some initial (one-time only)
steps you need to take:

1.  Create a [My NeSI
    Account](https://support.nesi.org.nz/hc/en-gb/articles/360000159715-Creating-a-NeSI-Account) and
    accept the new Acceptable Use [Terms and
    Conditions](https://www.nesi.org.nz/services/high-performance-computing/guidelines/acceptable-use-policy).
2.  Reset the temporary
    [password](https://support.nesi.org.nz/hc/en-gb/articles/360000335995-Resetting-Your-Password)
    to one of your choosing that conforms to the [NeSI Password
    Policy](https://support.nesi.org.nz/hc/articles/360000336015).
3.  Set up [two-factor
    authentication](https://support.nesi.org.nz/hc/en-gb/articles/360000203075-Setting-Up-Two-Factor-Authentication).

Once you have completed these tasks, you will be ready to log on to the
NeSI lander node (analogous to the Pan login node), then to jump to a
Mahuika login node (analogous to a Pan build node).

-   To log on to Mahuika, follow the instructions
    [here](https://support.nesi.org.nz/hc/en-gb/articles/360000161315-Logging-in-to-the-HPCs).

Other important information
---------------------------

-   [This
    link](https://support.nesi.org.nz/hc/en-gb/sections/360000034335)
    provides useful information about the new HPCs.
-   You can gain a better understanding of the Mahuika filesystems
    [here](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas).
    In particular, please note:
    -   Mahuika has a very large, very high performance scratch file
        system called `/nesi/nobackup`. This file system replaces the
        \"scratch\" and \"checkpoint\" file systems on Pan. You should
        do most of your computing in this file system.
    -   Data in `/nesi/nobackup` will be automatically removed from time
        to time.
    -   We are developing a nearline data service to help you move data
        off disk and onto tape, and vice versa.
-   Details of how the workload manager (Slurm) is configured on Mahuika
    can be
    found [here](https://support.nesi.org.nz/hc/en-gb/articles/360000204076-Mahuika-Slurm-Partitions).
    In particular, please note:
    -   We have introduced a \"debug\" quality of service (QoS) for
        rapid turnaround of test jobs. Each user may only have one job
        using the \"debug\" QoS setting at any time.
    -   You will now need to specify the Slurm partition in which your
        job will run.
    -   There is a Slurm primer
        [here](https://support.nesi.org.nz/hc/en-gb/articles/360000359576-Primer-Slurm-Usage)
        for new users.
-   This
    [link](https://support.nesi.org.nz/hc/en-gb/articles/360000350215-Primer-for-Pan-Users)
    should help Pan users understand some of the *key differences*
    between Pan and Mahuika.
-   You should have access to the [software you used on
    Pan](https://support.nesi.org.nz/hc/articles/360000360576), but
    notice that we are introducing a [new support
    model](https://support.nesi.org.nz/hc/en-gb/articles/360000170355-NeSI-Application-Support-Model).
-   The following link provides information on how to [compile and link
    software](https://support.nesi.org.nz/hc/en-gb/articles/360000329015-Compiling-software-on-Mahuika)
    on Mahuika:
-   If you run into a problem, please put in a
    [ticket](https://support.nesi.org.nz/hc/en-gb/requests/new).

Very Important Information: Data
--------------------------------

Your Pan file system data has been (and will continue to be)
synchronised to Mahuika. This process runs every night, so that data you
have created "today" will not yet be on Mahuika (it will be there
tomorrow!).

### Data from your Home Directory

On Mahuika, you will find your Pan home directory files in the directory
`/home/<username>/pan_home` (and sub-directories thereof). When you
decide to stop using Pan.

1.  [Before you copy any files Please Note: ]{.wysiwyg-color-red}
    -   [To help you get started, we have added simple `.bashrc` and
        `.bashrc_profile` files to your home directory on Mahuika, i.e.
        `/home/<username>`. The equivalent files from your home
        directory on Pan (and possibly other dot files such as
        `.profile`, `.cshrc`, `.tcshrc` and `.login` ) are still in
        `/home/<username>/pan_home`.]{.wysiwyg-color-black}[ ]{.wysiwyg-color-red}
    -   If you use the copy command below with the "`n`" option, then
        the simple  `.bashrc` and `.bashrc_profile` files will not get
        overwritten, but you may need to edit them to add any additional
        settings that are specific to your project etc.  If instead you
        copy your Pan `.bashrc` and `.bashrc_profile`  files into your
        Mahuika home directory then you will need to remove/modify any
        Pan-specific settings.  
2.  Copy the files you need from `/home/<username>/pan_home` (and its
    sub-directories) into `/home/<username>/` (and associated
    sub-directories).
    -   To copy all your Pan files into your Mahuika home directory in
        one go, you can use the command:\
        `cp -Trn --preserve=timestamps $HOME/pan_home $HOME`\
        -   This command will also copy your dot files, resource files
            and other invisible files whose names start with a `.`
        -   If you want to overwrite any similarly named files which are
            already present, remove the `-n` option.

Please note that we will continue to synchronise
`/home/<username>/pan_home` with your home directory on Pan until either
you ask us to stop, or Pan is decommissioned.

[[Do NOT (this is very important)]{.underline}]{.wysiwyg-color-red} work
in `/home/<username>/pan_home` (or any of its sub-directories). [Any
files you create or modify there will be deleted or reverted when we do
the nightly incremental synchronisation from Pan, and any files you
delete will be recreated with a version copied from Pan.]{.underline}

### Data from your Project Directory

As with home directories, on Mahuika you will find your Pan
`/projects/<project-id>` data (including sub-directories and their
contents) in the directory `/nesi/project/<project-id>/pan_project`.

When your project team is ready to stop using Pan for work on that
project, you should:

1.  Copy your files from `/nesi/project/<project-id>/pan_project` (and
    its sub-directories) into `/nesi/project/<project-id>/`.
    -   To copy all your Pan files into your Mahuika project directory
        in one go, you can use the command:\
        `cd /nesi/project/<project-id>` && cp \--preserve=timestamps
        -HTrn ./pan\_project ./\
        Note that the above command uses the a couple of switches to the
        `cp` command, e.g. to follow symbolic links and preserve
        timestamps.
    -   If you want to overwrite any similarly named files which are
        already present, remove the `-n` option.

Please note that we will continue to synchronise
`/nesi/project/<project-id>/pan_project` with the corresponding project
directory on Pan until until either you ask us to stop, or Pan is
decommissioned.

[[Do NOT (this is very important)]{.underline}]{.wysiwyg-color-red} work
in `/nesi/project/<project-id>/pan_project` or any of its
sub-directories.[Any files you create or modify there will be deleted or
reverted when we do the next incremental synchronisation from Pan, and
any files you delete will be recreated with a version copied from
Pan.]{.underline}

### Backups

All data on the `/home` and `/nesi/project` directories is [being backed
up]{.wysiwyg-underline .wysiwyg-color-red} daily.

**Note:** **`/nesi/project/<project-id>/pan_project`** is just a link to
another file system and its content is NOT backed up.

### Disk Space Quotas and Restrictions

These are described
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas)
(along with other important information), but in summary:

-   Your `/home` filesystem quota is 20 GB.
-   Your `/nesi/project/<project-id>` quotas are 100 GB, unless we have
    agreed otherwise.
-   The only quota on the `/nesi/nobackup/<project-id>` filesystem is
    the number of inodes you may use (presently 1,000,000 per Project)

During this transition phase your disk quotas have been adjusted to
allow you to work in your new `/home`
and`/nesi/project/<project-id> `filesystems without running into disk
quota issues.

If you have any issues, please raise a [support
ticket](mailto:support@nesi.org.nz?subject=Reporting%20a%20problem%20with%20the%20Transitioning%20to%20Mahuika%20Documentation),
and a member of our support team will get back to you.
