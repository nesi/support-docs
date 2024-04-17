---
created_at: '2021-05-13T01:00:08Z'
tags: []
vote_count: 7
vote_sum: 3
zendesk_article_id: 360004337836
zendesk_section_id: 360001189255
---


!!! note
     This functionality is experimental and may introduce breaking changes
     in the future. These notes should be read in conjunction with NeSI's
     main [R support page](../../Scientific_Computing/Supported_Applications/R.md)
     Your feedback is welcome, please don't hesitate {% include "partials/support_request.html" %} to make suggestions.

## Getting started

RStudio can be accessed as a web application via [Jupyter on
NeSI](../../Scientific_Computing/Interactive_computing_using_Jupyter/Jupyter_on_NeSI.md).

In the JupyterLab interface, RStudio can be started using the
corresponding entry in the launcher.

![rstudio\_launcher.png](../../assets/images/RStudio_via_Jupyter_on_NeSI.png)

Clicking on this entry will open a separate tab in your web browser,
where RStudio will be accessible.

Once RStudio is launched, you should briefly see a login screen. It will
be auto-filled using a pre-generated password, unless you disabled
javascript in your web browser.

## Changing R version

You can configure a set of [environment modules](../../Getting_Started/Next_Steps/The_HPC_environment.md)
to preload before starting RStudio. This can be useful if you want to
change the version of the R interpreter or use NeSI's *R-Geo* or
*R-bundle-Bioconductor* modules.

The module needs to be entered in the configuration file
`~/.config/rstudio_on_nesi/prelude.bash`.

In the following example, we use the module that is built for R/4.2.1

``` sh
echo "module load R/4.2.1-gimkl-2022a" > ~/.config/rstudio_on_nesi/prelude.bash
```

Once your configuration file is ready, make sure to restart your Jupyter
session and re-launch RStudio for these changes to be taken into
account. Check that the correct version of R has loaded and that the
correct Library Paths are available. For R/4.2.1 the command
`.libPaths()` will return the following:

```r
.libPaths()
```

```out
[1] "/home/YOUR_USER_NAME/R/gimkl-2022a/4.2"                            
[2] "/opt/nesi/CS400_centos7_bdw/R/4.2.1-gimkl-2022a/lib64/R/library"
```

## Package Installation

To avoid read/write issues with a small temorary directory filling up,
in a terminal run the following two lines of code. These will setup a
larger directory that will allow for packages to be installed to your
personal library. NOTE: this is not creating a library.

```sh
mkdir -p /nesi/nobackup/<projectID>/rstudio_tmp
echo "TMP=/nesi/nobackup/<projectID>/rstudio_tmp" > .Renviron
```

Within RStudio run the command \`tempdir()\` which should return the
following (below), where \`Rtmpjp2rm8\` is a randomly generated folder
name, and is emptied with each new session. So will not fill up your
home directory.

```r
tempdir()
```

```out
[1] "/nesi/nobackup/<projectID>/rstudio_tmp/Rtmpjp2rm8"
```

The alternative is to install packages in a terminal session

## Advanced usage

RStudio runs in a [Singularity
container](../../Scientific_Computing/Supported_Applications/Singularity.md)
prepared by the NeSI team to run on
[jupyter.nesi.org.nz](https://jupyter.nesi.org.nz). The related code is
hosted on GitHub, in the
[rstudio\_on\_nesi](https://github.com/nesi/rstudio_on_nesi) repository.

To modify the content of the container, you need to adapt the
[Singularity definition file](https://github.com/nesi/rstudio_on_nesi/blob/main/conf/rstudio_server_on_centos7.def),
found in the `conf` folder of the repository, and then rebuild the
container.

Once your container is ready, upload it on NeSI and use the
configuration file `~/.config/rstudio_on_nesi/singularity_image_path` to
indicate the path of your container to the RStudio-on-NeSI plugin:

```sh
echo PATH_TO_CONTAINER > ~/.config/rstudio_on_nesi/singularity_image_path
```

Then restart your Jupyter session and launch a new RStudio session to
make use of your container.

If your RStudio session does not start, try to reload the page, in case
the reported failure is just due to the container taking too much time
to start.

If this does not work, you will need to investigate the errors. A good
place to start is looking at the log file from jupyter, for the current
session:

```sh
cat ~/.jupyter/.jupyterhub_${USER}_${SLURM_JOB_ID}.log
```

## Troubleshooting

### Error 500

If you get an error 500 after clicking on the launcher icon, this could
be due to RStudio taking too much time to start, which is interpreted as
a failure by JupyterLab. Please try to start RStudio again from the
launcher. If the problem persists, {% include "partials/support_request.html" %}.

![error\_500.PNG](../../assets/images/RStudio_via_Jupyter_on_NeSI_0.png)

If you have disabled javascript in your web browser, you will need
to enter your password manually in the RStudio login screen. To
retrieve the password, open a terminal in JupyterLab and enter the
following to print the password:

```sh
cat ~/.config/rstudio_on_nesi/server_password
```

### Error 599

RStudio fails to load, times out, fails to initialze  
If your RStudio session won't load, a possible solution is to delete the contents of the two hidden directories in your home directory.

- `.local/share/rstudio`
- `.local/share/rstudio_on_nesi`
