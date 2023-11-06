---
created_at: '2021-10-04T19:55:45Z'
hidden: false
label_names:
- x11
- x forwarding
- x-forwarding
position: 0
title: X-Forwarding using the Ubuntu Terminal on Windows
vote_count: 9
vote_sum: -5
zendesk_article_id: 4407442866703
zendesk_section_id: 360000034315
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<ol dir="auto" type="1">
<li>
<a href="https://sourceforge.net/projects/xming/" target="_blank" rel="noopener">Download and install Xming from here</a>. Don't install an SSH client when prompted during the installation, if you are prompted for Firewall permissions after installing Xming close the window without allowing any Firewall permissions.</li>
<li>Open your Ubuntu terminal and install x11-apps with the command <code>sudo apt install x11-apps -y</code>.</li>
<li>Restart your terminal, start your Xming (there should be a desktop icon after installing it). You should now be able to X-Forward displays from the HPC when you log in (assuming you have completed the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_blank" rel="noopener">terminal setup instructions found here</a>).</li>
</ol>