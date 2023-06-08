---
created_at: '2021-10-04T19:55:45Z'
hidden: false
label_names:
- x11
- x forwarding
- x-forwarding
position: 0
title: X-Forwarding using the Ubuntu Terminal (Windows 10)
vote_count: 6
vote_sum: -2
zendesk_article_id: 4407442866703
zendesk_section_id: 360000034315
---

1.  [Download and install Xming from
    here](https://sourceforge.net/projects/xming/). Don't install an SSH
    client when prompted during the installation, if you are prompted
    for Firewall permissions after installing Xming close the window
    without allowing any Firewall permissions.
2.  Open your Ubuntu terminal and install x11-apps with the command
    `sudo apt install x11-apps -y`.
3.  In your Ubuntu terminal run the command
    `echo "export DISPLAY=localhost:0.0" >> ~/.bashrc`.
4.  Restart your terminal, start your Xming (there should be a desktop
    icon after installing it). You should now be able to X-Forward
    displays from the HPC when you log in (assuming you have completed
    the [terminal setup instructions found
    here](https://support.nesi.org.nz/hc/en-gb/articles/360000625535)).
