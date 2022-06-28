> ### Note {#prerequisites}
>
> This functionality is experimental and developing, which may introduce
> breaking changes in the future.
>
> If you would like to report a bug or propose a change see the GitHub
> repo
> [https://github.com/nesi/jupyter-matlab-proxy](https://github.com/nesi/jupyter-matlab-proxy?organization=nesi&organization=nesi)
> or contact NeSI support at <support@nesi.org.nz>.

Getting started
===============

MATLAB can be accessed as a web application via [Jupyter on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001555615).

In the JupyterLab interface, MATLAB can be started using the
corresponding entry in the launcher.

![matlab\_proxy\_icon.png](https://support.nesi.org.nz/hc/article_attachments/4620542958863/matlab_proxy_icon.png)
==================================================================================================================

Clicking on this entry will open a separate tab in your web browser,
where you will see the following status information page.

![image\_\_1\_.png](https://support.nesi.org.nz/hc/article_attachments/4620562032399/image__1_.png){width="497" height="206"}
=============================================================================================================================

MATLAB may take a few minutes to load, once it does you will be put
straight into the MATLAB environment. 

You can open the status page at any time by clicking the
[![](https://github.com/mathworks/jupyter-matlab-proxy/raw/main/img/tools_icon.png){width="61"
height="33"}](https://github.com/mathworks/jupyter-matlab-proxy/raw/main/img/tools_icon.png)
button.

> ### Note {#prerequisites}
>
> Your license must be valid for MATLAB 2021b or newer.

Licensing
=========

If you are a member of an institution that has access to MATLAB, the
corresponding network license will be selected. You can confirm this in
the info panel.

If you do not wish to use a network license you can click the \'Unset
License Server Address\' button.

![image\_\_3\_.png](https://support.nesi.org.nz/hc/article_attachments/4620518934031/image__3_.png){width="517" height="204"}
=============================================================================================================================

If you have no licence address set you can instead authenticate using a
MathWorks email address, provided you have a valid license associated to
your account.

![image\_\_4\_.png](https://support.nesi.org.nz/hc/article_attachments/4620518977423/image__4_.png){width="470" height="379"}
=============================================================================================================================

Troubleshooting
===============

As MATLAB via Jupyter on NeSI uses MATLAB 2021a, you will see a glibc
warning whenever you run a system command, and some system commands will
not work as intended.

For more details see
[MATLAB\#known\_bugs](https://support.nesi.org.nz/hc/en-gb/articles/212639047#known_bugs).

 

 
