---
created_at: '2019-10-13T21:21:07Z'
hidden: false
label_names: []
position: 18
title: MobaXterm Crashes on NeSI clusters (Update - Resolved)
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001206795
zendesk_section_id: 200732737
---

## Update - 2020/03/13 

MobaXterm is acting up again, we recommend disabling the SCP browser (as
shown in the 2019/11/01 update), or using a [different terminal
application](https://support.nesi.org.nz/hc/en-gb/articles/360001016335-Choosing-and-Configuring-Software-for-Connecting-to-the-Clusters).

## Update (Resolved) - 2019-12-18

Disabling the "Remote-monitoring (experimental)" in the SSH settings
seems to resolve this issue. If this does not resolve this issue for you
please let us know.

![moba3\_update2.png](../includes/moba3_update2.png)

## Update - 2019/11/01

Disabling the SSH-browser under your session settings will cause the
crashes to stop, however this will also remove your ability to transfer
files.

![no\_scp.png](../includes/no_scp.png)

## 2019/10/14

Over the past month we have had multiple reports of MobaXterm crashing
to desktop without warning when connecting to a NeSI cluster. This bug
does not appear to have been introduced in a particular patch or update
of MobaXterm.  
  
If this issue has affected you, please [contact NeSI
Support](mailto:support@nesi.org.nz?subject=MobaXterm%20Issues&body=Operating%20System%20Version:%20%0D%0A%0A%0ACrash%20triggered%20when:%20%0D%0A%0A%0AProblem%20started%20occurring:%20%0D%0A%0A%0AOn%20the%20Cluster:%0D%0A%0A%0AIf%20you%20can,%20please%20also%20include%20your%20MobaXterm%20config%20file.%20This%20can%20be%20found%20at%20%60%60C:%5CUsers%5C%3Cusername%3E%5CDocuments%5CMobaXterm%5CMobaXterm.ini%60%60)
with the following information.

 

-   Operating System Version (If you open 'cmd' it will be the first
    line displayed, e.g. <span class="code">Microsoft Windows \[Version
    10.0.17134.1006\]</span>)

-   How regularly the crash occurs (always, occasionally, etc), and when
    did it start.

-   What seems to trigger the crash (After x minutes, first key press,
    moving files, etc).

-   What cluster were you on (mahuika, Māui, maui\_ancil).

<!-- -->

-   MobaXterm config file, <span class="code">MobaXterm.ini</span>,  
    This can be found
    `C:\Users\<username>\Documents\MobaXterm\MobaXterm.ini` for the
    installer edition, or in the same file as the executable for the
    portable edition.

Thanks for your assistance.

##  

 

 
