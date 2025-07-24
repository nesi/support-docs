# NeSI OnDemand Release Notes

## 1.0.0 - Major version upgrade (20250515)

This release updates Open OnDemand to version 4.0.1.

### Features

- File system has been updated to use the production WEKA system, which is the same file system used with NeSI's new HPC cluster.
- Two additional apps have been added: Visual Studio Code Server and Virtual Desktop.
- Shell terminal has been added to the main menu that connects to the login node of the new HPC.
- Minor UI/UX improvements

## 0.3.2 - Fixes to ongoing bugs

Two bugs that have been an ongoing issue for the users have been fixed.

- Session starting incorrectly with missing port on the URL. This was due to the behind the scenes clean-up algorithm being too aggressive. This has now been fixed.
- Users with dots in the username could not launch sessions correctly. This has been fixed.

(This release is on Open OnDemand version 3.1.10)


## 0.3.1 - High memory option available in ondemand

This release enables high memory node to be selected by the users. Currently we support up to 32GB instance on the app launch.

It required work on K8s autoscaling and FreeIPA updates for auto-enrollment. Further work is needed for proper full autoscale, and will be coming up in the next release.

## 0.3.0 - initial release for Jupyter-only users

### Features

- JupyterLab and RStudio are available for researchers
- Tuakiri based login with OTP is ready
- Hosted on public URL: [https://ondemand.nesi.org.nz/](https://ondemand.nesi.org.nz/)
- Minor UX improvements

## 0.2.0 - initial internal release

NeSI OnDemand is NeSI’s new offering for providing researchers with access to JupyterLab and RStudio. We are adopting Open OnDemand technology, which enables us to build and extend the catalogue of web based applications.

This is our first release to a group of early access users for feedback around NeSI OnDemand and the new login process.

### Features

- As a new step forward from Jupyter.NeSI, we have a new interactive environment NeSI OnDemand where you can launch NeSI apps for your research.

    * Currently accessible via [https://ondemand.nesi.org.nz/](https://ondemand.nesi.org.nz/)

- Apps currently supported

    * JupyterLab with the following kernels: Python 3.8.2 (gimkl-2020a), Python 3.9.5 (gimkl-2020a), Python 3.10.5 (gimkl-2022a), and Python 3.11.3 (gimkl-2022a) 
    * RStudio

- Additional Apps (under development)

    * In addition to the two core apps above, we have the following applications accessible, but are still under development, and are unsupported. We will update you with more information in the future releases as they stabilise.
    * Virtual desktop
    * Matlab
    * VS Code-Server

- New login process for the NeSI systems going forward

    * NeSI is adopting a new Tuakiri based single sign on process for logging in to all NeSI services. This will mean that you won’t have to set up a separate NeSI account and password in order to be able to access NeSI services in the future.
    * To ensure the security of our system, we have an additional OTP (one-time password) that is enforced on top of your institutional login. Over time, we will smooth out the user experience for setting this up and the frequency of having to enter the OTP.

!!! Note

    We are in the early process of iterating and improving NeSI OnDemand. If you see any issues or suggestions, please let us know.

    - Please e-mail us on [support@nesi.org.nz](mailto:support@nesi.org.nz) with NeSI OnDemand as a part of the subject line and we will get back to you ASAP
    - Given that this is an early release, the SLA will not follow NeSI standard SLA (9am-5pm working days), and the environment may not be as stable as the production environment. We will support you with the best effort.

