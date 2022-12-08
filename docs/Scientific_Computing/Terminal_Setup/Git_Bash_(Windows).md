> ### Requirements {#prerequisites}
>
> -   Have a [NeSI
>     account.](https://support.nesi.org.nz/hc/en-gb/articles/360000159715-Creating-a-NeSI-Account)
>
> -   Be a member of an[active
>     project.](https://support.nesi.org.nz/hc/en-gb/articles/360000693896-Applying-to-join-a-NeSI-project)
>
First time setup {#recLinux}
----------------

Git Bash can be downloaded as part of Git
[here](https://git-scm.com/download/win).

The login process can be simplified with a few configurations.

1.  Open Git Bash and run `nano ~/.ssh/config` to open your ssh config
    file and add the following (replacing `<username>` with your
    username):

        Host mahuika
           User <username>
           Hostname login.mahuika.nesi.org.nz
           ProxyCommand ssh -W %h:%p lander
           ForwardX11 yes
           ForwardX11Trusted yes
           ServerAliveInterval 300
           ServerAliveCountMax 2

        Host maui
           User <username>
           Hostname login.maui.nesi.org.nz
           ProxyCommand ssh -W %h:%p lander
           ForwardX11 yes
           ForwardX11Trusted yes
           ServerAliveInterval 300
           ServerAliveCountMax 2

        Host lander
           User <username>
           HostName lander.nesi.org.nz
           ForwardX11 yes
           ForwardX11Trusted yes
           ServerAliveInterval 300
           ServerAliveCountMax 2

        Host *
           ControlMaster auto
           ControlPersist 1

    Close and save with ctrl x, y, Enter

2.  Ensure the permissions are correct by
    running `chmod 600 ~/.ssh/config`.

Usage
-----

Assuming you have followed the setup above you will be able to connect
to the clusters directly using;

    ssh mahuika

or

    ssh maui

As multiplexing is not configured *you will have to enter in your login
credentials every time you open a new terminal or try to move a file.*

    scp <path/filename> mahuika:~/

(For more info visit [data
transfer](https://support.nesi.org.nz/hc/en-gb/articles/360000578455-File-Transfer-with-SCP)).
