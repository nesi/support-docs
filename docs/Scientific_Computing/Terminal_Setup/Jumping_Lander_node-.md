---
created_at: '2019-07-30T04:11:05Z'
hidden: true
position: 1
tags: []
title: Jumping Lander node.
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001076675
zendesk_section_id: 360000189696
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

!!! info Requirements
>
> -   Have your [connection to the NeSI
>     cluster](https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Standard-Terminal-Setup)
>     configured.

For the purposes of connecting to the cluster as specified in
(connecting to cluster) this is **included in the setup**. This page is
meant to show how an equivalent arrangement can be set up for
applications that **cannot make use of your existing tunnel**.

For applications that require a connection to the cluster, but cannot
make multiple hops, or have no way to enter a password it may be
necessary to forward a local connection across to the cluster.

**Local Port:** Any process connecting to `127.0. 0.1:<local port>` on
your local will be forwarded to the remote (in this case, the NeSI
cluster).

**Host Alias:** An alias for the socket of your main connection to the
cluster, `mahuika` or `maui` if you have set up your ssh config file as
described
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000625535).

**Remote Port:** Any process connecting to `127.0. 0.1:<remote port>` on
your remote will be forwarded to your local.

> -   ``` sl
>     ```

# MobaXterm
!!! info Tips
>
> -   MobaXterm has an internal terminal which acts like a linux
>     terminal and can be configured as described in the [Standard
>     Terminal
>     Setup](https://support.nesi.org.nz/hc/en-gb/articles/360000625535). 

MobaXterm has a GUI to setup and launch sessions with port forwarding,
click 'Tools &gt; MobaSSH Tunnel (port forwarding)':

-   specify the lander.nesi.org.nz as SSH server address (right, lower
    box, first line)
-   specify your user name (right, lower box, second line)
-   specify the remote server address, e.g. login.mahuika.nesi.org.nz 
    (right, upper box first line)
-    and at the remote server (right upper box, second line)
-   Specify the local port number on the local side (left)
-   Save

![sshTunnel.PNG](https://support.nesi.org.nz/hc/article_attachments/8295479596175)

# PuTTY

*Coming soon..*
!!! info What Next?
>
> -   Using
>     [JupyterLab ](https://support.nesi.org.nz/hc/en-gb/articles/360001093315)on
>     the cluster.
> -   [NiceDCV ](https://support.nesi.org.nz/hc/en-gb/articles/360000719156)
> -   [Paraview](https://support.nesi.org.nz/hc/en-gb/articles/360001002956-ParaView)
