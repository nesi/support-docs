Globus default directory
------------------------

If you point Globus to an Endpoint where you have an account, it will
open a single panel pointing to the path of your home-directory there,
displayed as \'`/~/`\'.

![](https://support.nesi.org.nz/hc/article_attachments/360001968695/mceclip0.png){width="514"
height="378"}

###  On NeSI\'s Māui/Mahuika cluster this means:

  filesystem                        visible to Globus   storage   persistent   Globus usage                permissions
  --------------------------------- ------------------- --------- ------------ --------------------------- -----------------------
  `/home/`; or \'/\~/\'             yes (default)       20GB      yes          possible, not recommended   read and write access
  `/nesi/nobackup/<project_code>`   yes                 yes       no           yes                         read and write access
  `/nesi/project/<project_code>`    yes                 yes       yes          yes                         read only access

 

The `/nesi/project` filesystem for Globus file-transfers and sharing is

-   persistent
-   backed up

The `/nesi/nobackup` filesystem for Globus file-transfers and sharing
(which we\'ll call the *nobackup* filesystem henceforth) is

-   not persistent (see [Automatic cleaning of nobackup
    filesystem](https://support.nesi.org.nz/hc/en-gb/articles/360001162856))
-   not backed up

Every project has a large quota on the `/nesi/nobackup` filesystem for a
short period of time.

As the filesystem becomes full, files will be deleted according to their
age. Move your files off the *nobackup* filesystem if you want a
persistent copy of them. See the NeSI documentation
on [ filesystems](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas)
for more information.

Performing Globus transfers to/from Māui/Mahuika
------------------------------------------------

-   if transferring files off the cluster, move/copy files onto
    `/nesi/project` or `/nesi/nobackup` first
-   sign in to Globus and navigate the file manager to the  path
    associated with your project (viz. `/nesi/project/<project_code>` or
    `/nesi/nobackup/<project_code>`{style="font-size: 15px;"})
-   click the \"two-panels\" area in the file-manager  and select the
    other endpoint
-   select source of transfer
-   transfer data (from), using the appropriate \"start\" button
-   if transferring files onto the cluster, move files off
    `/nesi/project` or `/nesi/nobackup` after transfer

### Tips

1.  Globus bookmarks can be created for `/nesi/project` or
`/nesi/nobackup` paths, and these bookmarks pinned.

2.  Symbolic links can be created in your project directories and
*nobackup* directories to enable easy moving of files to and fro.\
To create a symbolic link from a first to a second directory and
vice-versa (using *full* paths for \<first\> and \<second\>):

    $ cd <first>
    $ ln -s <full_path_to_second> <alias_to_second>
     
    $ cd <second>
    $ ln -s <full_path_to_first>  <alias_to_first>

Here you substitute convenient values for these aliases.\
After you do this, there will be an alias listed in each directory which
points to the other directory. You can see this with the **ls** command,
and **cd** from each to the other using its alias.

 
