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

1.  Download MobaXTerm
    [here](https://mobaxterm.mobatek.net/download-home-edition.html)
    -   Use the Portable Edition if you don\'t have administrator rights
        on your machine. This is the recommended way for NIWA
        researchers.
    -   Otherwise, choose freely the Portable or Installer Edition.
2.  To set up a session, Click \'Session\' in the top left corner:
3.  In \"SSH\",
    -   Set the remote host to `login.mahuika.nesi.org.nz` for Mahuika
        users or `login.maui.nesi.org.nz` for Māui users.
    -   Enable the \"Specify username\" option and put your Username in
        the corresponding box.
4.  In the \"Advanced SSH settings\"
    -   Set SSH-browser type to \'**SCP (enhanced speed)**\'.
    -   Optionally, tick the \'Follow SSH path\' button.

```{=html}
<!-- -->
```
6.  In the "Network settings" tab:
    -   Select \"SSH gateway (jump host)\" to open a popup window
    -   In this window enter `lander.nesi.org.nz`{.highlighter-rouge} in
        the "Gateway host" field, as well as your NeSI username in the
        Username field for the gateway SSH server then select OK to
        close the window.

![mceclip4.png](https://support.nesi.org.nz/hc/article_attachments/4411672582031/mceclip4.png)

![mceclip5.png](https://support.nesi.org.nz/hc/article_attachments/4411672594191/mceclip5.png)

7.  Click \'OK\' on the open window, usually this will start a new
    session immediately. *See usage below.*

> ### WARNING {#moba-bug}
>
> There is a bug which causes some users to be repeatedly prompted
> `<username>@lander.nesi.org.nz's password:`{.sample}\
> This can be resolved by clicking \"OK\" each time you are prompted
> then logging in as normal once you are prompted for your
> `First Factor:`{.sample} or `Password:`{.sample}.\
> See [Login
> Troubleshooting](https://support.nesi.org.nz/hc/en-gb/articles/360000570215)
> for more details

Usage
-----

You will see your saved session in the left hand panel under
\'Sessions\'. Double click to start.

![mceclip6.png](https://support.nesi.org.nz/hc/article_attachments/4411680807951/mceclip6.png)

You will be prompted by dialogue box.

    Login Password (First Factor):

Enter your password.

    Authenticator Code (Second Factor):

Enter your second factor six digit number (no space).

Then Mahuika users may be prompted again:

    Login Password:

Enter your password again

Māui users will instead be prompted with:

    Password:

Māui users must enter their password combined with their second factor.
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
