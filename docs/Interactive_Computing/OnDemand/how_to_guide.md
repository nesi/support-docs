---
tags:
    - interactive
    - r
description: Getting Started With NeSI onDemand
title: NeSI OnDemand how-to guide
---

## How to log in

Go to  [**OnDemand**](https://ondemand.nesi.org.nz/). It will automatically take you to the Tuakiri login screen.

Log in with your institutional credentials.

??? info "First Time Login"

    If you haven't logged into OnDemand or our HPC platforms before, part of the login process will include a step to setup additional authentication credentials.

    ![OnDemand login 1](../../assets/images/ondemand_login_0.png)


    * Select your affiliated institution, and log in using your institutional account. Example below shows the University of Auckland login screen.

    ![ondmenad login 2](../../assets/images/ondemand_login_1.png)

    After logging in, you will be asked to set up an 6-digit code. This is additional authentication in addition to your institutional MFA. We are currently enforcing an additional security layer, as the institutions federated by Tuakiri all have different security policies.
    
    ![OnDemand login 3](../../assets/images/ondemand_login_2.png)

    Scan the barcode with your preferred authenticator app (e.g. Google Authenticator), and enter the 6-digit code along with a device name (e.g. my mobile) and Submit and you are good to go.

    Once you have set up your additional authentication credentials, you will be shown the following screen, where you can enter the 6-digit code from your authenticator app.

    ![ondemand login 4](../../assets/images/ondemand_login_3.png)

    After successfully logging in, you will be presented with the following OnDemand screen.

    ![ondemand login success](../../assets/images/OOD_Desktop_08Jun2025.png)

### OnDemand home page

![OnDemand home](../../assets/images/OOD_desktop.png)

1. <kbd>Files</kbd> <kbd>Home Directory</kbd> : Access to OnDemand file explorer
    - Default landing path for the file explorer is your home directory
    - There is a `00_nesi_projects` directory within home which contains symlinks to all project and nobackup directories you have access to.
    Refer to [Interactive file explorer](#interactive-file-explorer)

2. <kbd>Clusters</kbd>><kbd>>_NeSI HPC Shell Access</kbd>
    - Allows us to access HPC login nodes directly from OnDemand.

3. <kbd>My Interactive Sessions</kbd>
    - List all of the currently running sessions associated with my user account

4. **Applications**
    - Currently available apps for interactive computing.

## How to launch an Application

From the home page, you can click on the app you would like to launch, e.g. JupyterLab, and you will be taken to the following screen.

![OnDemand Jupyter icon](../../assets/images/OOD_jupyterlab_icon.png){.center}

![OnDemand new form](../../assets/images/OOD_jupyter_form.png)

!!! bell "How much resources to request"

    Ideally start with the least amount of resources and scale accordingly. In other words, be as efficient as possible ☺️

    | Form attributes        | Maximum value |
    | ---------------------- | ------------- |
    | **Number of hours**    | 24            |
    | **Number of cores**    | 4             |
    | **Memory per job(GB**) | 32GB          |
    
![OnDemand new start](../../assets/images/OOD_jupyter_session_starting.png)

Once the session is ready, you will see a button labeled <kbd>Connect to Jupyter</kbd> (or other app of your choice), which upon clicking will take you to the JupyterLab in this example as seen below:

![OnDemand Apps](../../assets/images/jupyter_apps.png)

## Interactive file explorer

If you would like to access your project or nobackup filesystem via the Interactive file explorer ( not the terminal), 
please use the <kbd>00_nesi_project</kbd> parent directory which contains symlinks to all filesystems you have access to.

### OnDemand App

![Files App](../../assets/images/OOD_files_app.png)

### Jupyter file explorer

![File Explorer Jupyter](../../assets/images/OOD_jupyter_fileexplorer.png)

## VS Code file explorer

![OOD_VSCode_fileexplorer](../../assets/images/how_to_guide_OOD_VSCode_fileexplorer.png)

## Access the terminal in OnDemand

### OnDemand App

![mahuika_shell_access](../../assets/images/how_to_guide_mahuika_shell_access.png)

### Jupyter terminal

![jupyterlab_terminal](../../assets/images/how_to_guide_jupyterlab_terminal.png)

### VS Code terminal

![OOD_VS_Code_terminal](../../assets/images/how_to_guide_OOD_VS_Code_terminal.png)

## Additional Setup Steps

You may be asked to authenticate your terminal session when you access Mahuika through the terminal. For example:

```bash
(user.name@login.hpc.nesi.org.nz) Authenticate at https://iam.nznesi.io?user_code=STUV-WXYZ and press ENTER.
```

If you see this, enter the given webpage into a browser and proceed to authenticate yourself.

If you would like to prevent this from happening in the future, type the following into the terminal once you have authenticated yourself and have access to Mahuika through the terminal:

```bash
setup_ssh_key
```

This will set up an SSH key in your Mahuika home directory, and will automatically authenticate you when accessing Mahuika through OnDemand. You will see a message like this:

```bash
user.name@login03:~$ setup_ssh_key 
Generated new ed25519 key: /home/user.name/.ssh/mahuika_ssh_key
Added public key to /home/user.name/.ssh/authorized_keys
```
