---
created_at: '2018-11-30T00:32:25Z'
tags: 
    - ssh
    - windows
title: MobaXterm Setup (Windows)
description: How to set up cluster access using MobaXterm
vote_count: 5
vote_sum: 5
zendesk_article_id: 360000624696
zendesk_section_id: 360000189696
---

!!! prerequisite
     -   Have an [active account and project.](Creating_a_NeSI_Account_Profile.md)
     -   Set up your [Linux Password.](Setting_Up_and_Resetting_Your_Password.md)
     -   Set up Second [Factor Authentication.](Setting_Up_Two_Factor_Authentication.md)
     -   Windows operating system.

Setting up MobaXterm as shown below will allow you to connect to the
Cluster with less keyboard inputs as well as allow use of the file
transfer GUI.

1. [Download MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html)
    - Some users have reported having issues downloading files using
        MobaXterm 23.6. We suggest using version 23.5 instead.
    - Use the Portable Edition if you don't have administrator rights
        on your machine. This is the recommended way for NIWA
        researchers.
    - Otherwise, choose freely the Portable or Installer Edition.
2. To set up a session, Click 'Session' in the top left corner:
3. In "SSH",
    - Set the remote host to `login.mahuika.nesi.org.nz` for Mahuika
        users or `login.maui.nesi.org.nz` for Māui users.
    - Enable the "Specify username" option and put your Username in
        the corresponding box.
4. In the "Advanced SSH settings"
    - Set SSH-browser type to '**SCP (enhanced speed)**'.
    - Optionally, tick the 'Follow SSH path' button.
5. In the “Network settings” tab:
    - Select "SSH gateway (jump host)" to open a popup window
    - In this window enter `lander.nesi.org.nz` in the “Gateway host”
        field, as well as your NeSI username in the Username field for
        the gateway SSH server then select OK to close the window.

    ![mceclip4.png](MobaXterm_Setup_Windows.png)

    ![mceclip5.png](MobaXterm_Setup_Windows_0.png)

6. Click 'OK' on the open window, usually this will start a new session
    immediately. *See usage below.*

!!!  bug
     There is a bug which causes some users to be repeatedly prompted
     `<username>@lander.nesi.org.nz's password:`  
     This can be resolved by clicking "OK" each time you are prompted then
     logging in as normal once you are prompted for your `First Factor:` or
     `Password:`.  
     See [Login Troubleshooting](Login_Troubleshooting.md) for more
     details

## Usage

You will see your saved session in the left hand panel under 'Sessions'.
Double click to start.

![mceclip6.png](MobaXterm_Setup_Windows_1.png)

You will be prompted by dialogue box.

``` sh
Login Password (First Factor):
```

Enter your password.

``` sh
Authenticator Code (Second Factor):
```

Enter your second factor six digit number (no space).

Then Mahuika users may be prompted again:

``` sh
Login Password:
```

Enter your password again

Māui users will instead be prompted with:

``` sh
Password:
```

Māui users must enter their password combined with their second factor.
For example, if your password is "Password" and your current second
factor is "123456" then you must enter "Password123456".

!!! tip
     If you choose to save your password, the process will be the same
     minus the prompts for First Factor.

## Credential Manager

If you are using the built in credential manager you will have to make
sure to delete old entries when changing your password.

## Troubleshooting

### After Changing Password

If you are experiencing login issues after resetting your password, it
is likely due to an issue with MobaXterm saved sessions and Password
management system for saved session.

Two steps to try:

- Remove any previously saved sessions either related to `lander` OR
    `mahuika` from sessions panel on the left
- Access MobaXterm password management system as below and remove
    saved credentials
    - Go to **Settings**-&gt;**Configuration** and go to the
        **General** tab and click on **MobaXterm password management**
    - You will see the saved sessions for `lander` (and perhaps
        `mahuika` as well). I recommend removing all of it and restart
        MobaXterm before the next login attempt

Then setup a new session [according to the support doc instructions](MobaXterm_Setup_Windows.md)
as before.

!!! prerequisite "What Next?"
     -   [Moving files to/from a cluster.](Moving_files_to_and_from_the_cluster.md)
