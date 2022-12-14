---
created_at: '2021-08-27T03:30:10Z'
hidden: false
label_names: []
position: 3
title: Globus V5 Paths, Permissions, Storage Allocation
vote_count: 0
vote_sum: 0
zendesk_article_id: 4405623499791
zendesk_section_id: 360000040596
---

## Globus default directory

If you point Globus File Manager to an endpoint collection where you
have an account/access, it will open a single panel pointing to the root
path directory, displayed as '`/home/<username>`'.

![mceclip0.png](../includes/mceclip0.png)

###  On NeSI's Māui/Mahuika clusters this means:

<table>
<thead>
<tr class="header">
</tr>
</thead>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>

 

For more information about NeSI filesystem, check
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas).

## Performing Globus transfers to/from Māui/Mahuika

-   If transferring files off the cluster, move/copy files onto
    `/nesi/project` or `/nesi/nobackup` first, via your HPC access
-   Sign in to Globus and navigate the file manager to the path
    associated with your project (viz. `/nesi/project/<project_code>` or
    `/nesi/nobackup/<project_code>`)
-   Click the "two-panels" area in the file manager and select the other
    endpoint
-   Select source of transfer
-   Transfer data (from), using the appropriate "start" button
-   If transferring files onto the cluster, the fastest location will be
    `/nesi/nobackup/<project_code>`

### Tips

1.  Globus bookmarks can be created for `/nesi/project` or
`/nesi/nobackup` paths and these bookmarks pinned.

2.  Symbolic links can be created in your *project* directories and
*nobackup* directories to enable easy moving of files to and from.  
To create a symbolic link from a first to a second directory and
vice-versa (using *full* paths for &lt;first&gt; and &lt;second&gt;):

    $ cd <first>
    $ ln -s <full_path_to_second> <alias_to_second>
     
    $ cd <second>
    $ ln -s <full_path_to_first>  <alias_to_first>

Alias can be any value which is convenient to you. .i.e. easy to
identify  
After you do this, there will be an alias listed in each directory that
points to the other directory. You can see this with the **ls** command,
and **cd** from each to the other using its alias.

 
