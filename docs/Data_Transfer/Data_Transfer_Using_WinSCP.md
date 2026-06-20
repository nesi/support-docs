---
created_at: 2026-02-04
description: How to copy files to the REANNZ HPC using WinSCP.
tags:
    - file_transfer
title:  WinSCP (Windows)
---

!!! prerequisite
    [WinSCP-PuTTY Setup Windows](../Getting_Started/Accessing_the_HPCs/WinSCP-PuTTY_Setup_Windows.md)

**Transfer Mode:** There are known issues using the default _Automatic_ transfer mode.  Some files, including source code files (aka text files), can be transferred with erroneous line endings. This will cause scripts or jobs to fail.  If you see extra _^M_ charcaters in your files (easily seen with the `cat -v` command, this means your files have been transferred incorrectly.  A worksround that sometimes works is to switch the WinSCP transfer mode to _Binary_

We recommend using a different file transfer client.

**Multiple Authentication:**  As WinSCP uses multiple tunnels for file transfer you will be required
to authenticate again on your first file operation of the session. 
