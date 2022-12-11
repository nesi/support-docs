> ### Requirements
>
> -   Be a [member of an active
>     project.](https://support.nesi.org.nz/hc/en-gb/articles/360000693896-Applying-to-join-a-NeSI-project)
> -   Windows 10 with [WSL
>     enabled.](https://support.nesi.org.nz/hc/en-gb/articles/360001075575)

Currently the native Windows command prompt (even with WSL enabled) does
not support certain features, until this is fixed we recommend using the
Ubuntu LTS Terminal.

1.  Open the Microsoft store, search for 'Ubuntu', find and install
    'Ubuntu 18.04 LTS' or  'Ubuntu 20.04 LTS'   
      
    ![ubuntu5.png](mkdocs/includes/images/ubuntu5.png)![ubuntu6.png](mkdocs/includes/images/ubuntu6.png)  
      
      
2.  Close the “Add your Microsoft account.. dialogue box as you do not
    need an account for the installation.You may have to click “Install”
    for a second time (If the above dialogue box reappears, close as
    before and download/install will begin.  
      
    ![ubuntu3.png](mkdocs/includes/images/ubuntu3.png)  
     ![ubuntu4.png](mkdocs/includes/images/ubuntu4.png)  
      
3.  Launch “Ubuntu 18.04 LTS” from start menu and wait for the first
    time installation to complete.
4.  As you are running Ubuntu on Windows for the first time, it will
    require to be configured. Once the installation was complete, you
    will be prompted to “Enter new UNIX username” and press
    &lt;Enter&gt;. This username can be anything you want.  
      
    ![ubuntu1.png](mkdocs/includes/images/ubuntu1.png)  
      
5.  Now, type in a new password for the username you picked and press
    &lt;Enter&gt;. (Again this password is anything you want). Then
    retype the password to confirm and press &lt;Enter&gt;  
      
    ![ubuntu2.png](mkdocs/includes/images/ubuntu2.png)
6.  To create a symbolic link to your Windows filesystems in your home
    directory run the following command replacing c with the name of
    your Windows filesystems found in /mnt/. 

        ln -s /mnt/c/Users/YourWindowsUsername/ WinFS

> ### What Next?
>
> -   Set up your [SSH config
>     file](https://support.nesi.org.nz/hc/en-gb/articles/360000625535).
