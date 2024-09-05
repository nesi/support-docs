# NeSI OnDemand Release Notes

## Release Notes 0.2.0

### Release Summary

NeSI OnDemand is NeSI’s new offering for providing researchers with access to JupyterLab and RStudio. We are adopting Open OnDemand technology, which enables us to build and extend the catalogue of web based applications.

This is our first release to a group of early access users for feedback around NeSI OnDemand and the new login process.

### Features

- As a new step forward from Jupyter.NeSI, we have a new interactive environment NeSI OnDemand where you can launch NeSI apps for your research.
  - Currently accessible via https://163-7-144-39.sslip.io/

- Apps currently supported
  - JupyterLab with the following kernels: Python 3.8.2 (gimkl-2020a), Python 3.9.5 (gimkl-2020a), Python 3.10.5 (gimkl-2022a), and Python 3.11.3 (gimkl-2022a) 
  - RStudio

- Additional Apps (under development)
  - In addition to the two core apps above, we have the following applications accessible, but are still under development, and are unsupported. We will update you with more information in the future releases as they stabilise.
  - Virtual desktop
  - Matlab
  - VS Code-Server

- New login process for the NeSI systems going forward
  - NeSI is adopting a new Tuakiri based single sign on process for logging in to all NeSI services. This will mean that you won’t have to set up a separate NeSI account and password in order to be able to access NeSI services in the future.
  - To ensure the security of our system, we have an additional OTP (one-time password) that is enforced on top of your institutional login. Over time, we will smooth out the user experience for setting this up and the frequency of having to enter the OTP.
