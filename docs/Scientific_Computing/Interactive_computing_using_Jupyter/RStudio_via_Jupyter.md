 
-

> ### Note {#prerequisites}
>
> This functionality is experimental and may break or be removed in the
> future.

The [RStudio on NeSI](https://github.com/nesi/rstudio_on_nesi) GitHub
repository contains a Python package that will help you run RStudio
Server Open Source via our Jupyter service.

Once installed, it will add an option in the main interface of
JupyterLab to start an instance of RStudio Server within your Jupyter
session. Note that the RStudio Server will not outlive the Jupyter
session.

The following steps will set up RStudio on NeSI:

1.  In a (JupyterLab) terminal, configure a password for RStudio Server:
    -   echo "my_secret_password" > ~/.rstudio_server_password

2.  Install the Python package:
    -   module purge && module load JupyterLab
            pip install --user git+https://github.com/nesi/rstudio_on_nesi

3.  Restart your Jupyter session and click on the RStudio icon to start
    it in a separate tab of your browser. When starting RStudio Server,
    the username requested is your NeSI username and the password is the
    one you defined in step 1 above.

Note that at the current time there is no integration with NeSI
environment modules.

Inviting Feedback
-----------------

Please [provide feedback on the
implementation](https://portal.productboard.com/2k2ojgehbq7ovnyzmcjp1nxg/c/133-rstudio?utm_medium=social&utm_source=portal_share)
and share with us what is working well or not so well for you and what
else you would like to see supported.
