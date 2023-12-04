---
created_at: '2019-07-15T04:12:01Z'
hidden: false
position: 1
tags: []
title: Ubuntu LTS terminal (Windows)
vote_count: 3
vote_sum: 3
zendesk_article_id: 360001050575
zendesk_section_id: 360000189696
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

!!! prerequisite Requirements
     -   Be a [member of an active
         project.](https://support.nesi.org.nz/hc/en-gb/articles/360000693896-Applying-to-join-a-NeSI-project)
     -   Windows with [WSL
         enabled.](../../Scientific_Computing/Terminal_Setup/Windows_Subsystem_for_Linux_WSL.md)

Currently the native Windows command prompt (even with WSL enabled) does
not support certain features, until this is fixed we recommend using the
Ubuntu LTS Terminal.

1.  Open the Microsoft store, search for 'Ubuntu', find and install the
    latest version of the Ubuntu LTS it should look something like 
    'Ubuntu 20.04 LTS' , though you may find a later version.  
      
    ![ubuntu5.png](../../assets/images/Ubuntu_LTS_terminal_Windows.png)![ubuntu6.png](../../assets/images/Ubuntu_LTS_terminal_Windows_0.png)  
      
      

2.  Close the “Add your Microsoft account.. dialogue box as you do not
    need an account for the installation.You may have to click “Install”
    for a second time (If the above dialogue box reappears, close as
    before and download/install will begin.  
      
    ![ubuntu3.png](../../assets/images/Ubuntu_LTS_terminal_Windows_1.png)
     
     ![ubuntu4.png](../../assets/images/Ubuntu_LTS_terminal_Windows_2.png)  
      

3.  Launch “Ubuntu 18.04 LTS” from start menu and wait for the first
    time installation to complete.

4.  As you are running Ubuntu on Windows for the first time, it will
    require to be configured. Once the installation was complete, you
    will be prompted to “Enter new UNIX username” and press
    &lt;Enter&gt;. This username can be anything you want.  
      
    ![ubuntu1.png](../../assets/images/Ubuntu_LTS_terminal_Windows_3.png)  
      

5.  Now, type in a new password for the username you picked and press
    &lt;Enter&gt;. (Again this password is anything you want). Then
    retype the password to confirm and press &lt;Enter&gt;  
      
    ![ubuntu2.png](../../assets/images/Ubuntu_LTS_terminal_Windows_4.png)

6.  To create a symbolic link to your Windows filesystems in your home
    directory run the following command replacing c with the name of
    your Windows filesystems found in /mnt/. 

    ``` sl
    ln -s /mnt/c/Users/YourWindowsUsername/ WinFS
    ```
!!! prerequisite What Next?
     -   Set up your [SSH config
         file](../../Scientific_Computing/Terminal_Setup/Standard_Terminal_Setup.md).
