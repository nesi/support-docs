> ### Requirements {#prerequisites}
>
> -   Have an [active account and
>     project.](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects)
> -   Set up your [Linux
>     Password.](https://support.nesi.org.nz/hc/en-gb/articles/360000335995)
> -   Set up Second [Factor
>     Authentication.](https://support.nesi.org.nz/hc/en-gb/articles/360000203075)
> -   Windows operating system.

Setting up MobaXterm as shown below will allow you to connect to the
Cluster with less keyboard inputs as well as allow use of the file
transfer GUI.

1.  Download the Installer Edition of MobaXTerm
    [here](https://mobaxterm.mobatek.net/download-home-edition.html).
2.  To set up a session, Click \'Sessions \> New Session\':
3.  In \"Basic SSH settings\",
    -   Set the remote host to `login.mahuika.nesi.org.nz` for Mahuika
        users or `login.maui.nesi.org.nz` for Maui users.
    -   Enable the \"Specify username\" option and put your Username in
        the corresponding box.
4.  In \"Advanced SSH settings\"
    -   Set SSH-browser type to **SCP**.
    -   Optionally, tick the \'Follow SSH path\' button.

<!-- -->

6.  In the "Network settings" tab:
    -   Enable \"Connect through SSH gateway (jump host)\"
    -   Enter `lander.nesi.org.nz`{.highlighter-rouge} in the "Gateway
        SSH server" field, as well as your NeSI username in the User
        field for the gateway SSH server.

![MobaXterm\_loginWindow.JPG](https://support.nesi.org.nz/hc/article_attachments/360002833995/MobaXterm_loginWindow.JPG)

7.  Click \'OK\', usually this will start a new session immediately.
    *See usage below.*

> ### WARNING {#moba-bug}
>
> There is a bug which causes some users to be repeatedly prompted
> \<username\>\@lander.nesi.org.nz\'s password:\
> This can be resolved by clicking \"OK\" each time you are prompted
> then logging in as normal once you are prompted for your First Factor:
> or Password:.\
> See [Login
> Troubleshooting](https://support.nesi.org.nz/hc/en-gb/articles/360000570215)
> for more details

Usage
-----

You will see your saved session in the left hand panel under
\'Sessions\'. Double click to start.

![moba3.png](https://support.nesi.org.nz/hc/article_attachments/360002490096/moba3.png)

You will be prompted by dialogue box.

    Login Password (First Factor):

Enter your password.

    Authenticator Code (Second Factor):

Enter your second factor six digit number (no space).

Then Mahuika users may be prompted again:

    Login Password:

Enter your password again

Maui users will instead be prompted with:

    Password:

Maui users must enter their password combined with their second factor.
For example, if your password is \"Password\" and your current second
factor is \"123456\" then you must enter \"Password123456\".

> ### Tip {#warn}
>
> If you choose to save your password, the process will be the same
> minus the prompts for First Factor.

> ### What Next? {#prerequisites}
>
> -   [Moving files to/from a
>     cluster.](https://support.nesi.org.nz/hc/en-gb/articles/360000578455)
