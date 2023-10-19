---
created_at: '2019-06-25T22:40:46Z'
hidden: false
label_names:
- terminal
- mobaxterm
- gitbash
- login
position: 2
title: Choosing and Configuring Software for Connecting to the Clusters
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001016335
zendesk_section_id: 360000034315
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Requirements</h3>
<ul>
<li>Have an <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects" target="_self">active account and project</a>.</li>
<li>Set up your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000335995" target="_blank" rel="noopener">NeSI Account Password</a>.</li>
<li>Set up <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000203075" target="_self">Two-Factor Authentication</a>.</li>
</ul>
</blockquote>
<p>Before you can start submitting work you will need some way of connecting to the NeSI clusters.</p>
<p>This is done by establishing an SSH (Secure SHell) connection, giving you access to a command line interface (bash) on the cluster. In order to set up such a connection, you will need a suitable Terminal (or equivalent application). The correct option for you depends on your operating system and level of experience.</p>
<h1 id="h_c1bbd761-1133-499b-a61a-57b9c4320a1a">Web Browser</h1>
<ul class="list-unstyled">
<li>
<h2>JupyterHub</h2>
<p>JupyterHub is a service providing access to Jupyter Notebooks on NeSI. A terminal similar to the other setups describe below can be accessed through the Jupyter Launcher.<br><br></p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What next?</h3>
<ul>
<li>More info on <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615#jupyter-term" target="_self">Jupyter Terminal</a>
</li>
<li>Visit <a href="https://jupyter.nesi.org.nz/hub/" target="_self">jupyter.nesi.org.nz</a>.</li>
</ul>
</blockquote>
</li>
</ul>
<h1 id="h_c1bbd761-1133-499b-a61a-57b9c4320a1a">Linux or Mac OS</h1>
<ul class="list-unstyled">
<li>
<h2>Terminal</h2>
<p>On MacOS or Linux you will already have a terminal emulator installed, usually called, "Terminal." To find it, simply search for "terminal".<br>Congratulations! You are ready to move to the next step.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What next?</h3>
<ul>
<li>Setting up your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">Default Terminal</a>
</li>
</ul>
</blockquote>
</li>
</ul>
<h1>Windows</h1>
<p>As Windows is not a "Unix-Like" operating system, getting access to a functional terminal requires some additional steps. There are several different options, listed in order of preference.</p>
<ul class="list-unstyled">
<li>
<h2>Ubuntu Terminal (Windows 10)</h2>
<blockquote class="blockquote-tip">
<h3 id="wsl-admin-tip">Note</h3>
<p>The Ubuntu Terminal and Windows Subsystem for Linux require administrative privileges to enable and install them. If your institution has not given you such privileges, consider using another option such as MobaXTerm Portable Edition (see below).</p>
</blockquote>
<p>This is the most functional replication of a Unix terminal available on Windows, and allows users to follow the same set of instructions given to Mac/Linux users. It may be necessary to enable Windows Subsystem for Linux (WSL) first.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What next?</h3>
<ul>
<li>Enabling <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075575" target="_self">WSL</a>
</li>
<li>Setting up the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001050575" target="_self">Ubuntu Terminal</a>
</li>
<li>Setting up <a href="https://support.nesi.org.nz/hc/en-gb/articles/4407442866703" target="_self">X-Forwarding</a>
</li>
</ul>
</blockquote>
</li>
<li>
<h2>MobaXterm</h2>
<p>In addition to being a terminal emulator, MobaXterm also includes several useful features like multiplexing, X11 forwarding and a file transfer GUI.</p>
<p>MobaXterm can be downloaded from <a href="https://mobaxterm.mobatek.net/download-home-edition.html" target="_self">here</a>. The portable edition will allow you to use MobaXterm without needing administrator privileges, however it introduces several bugs so we <em>highly</em> recommend using the installer edition if you have administrator privileges on your workstation or if your institution's IT team supports MobaXTerm.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What next?</h3>
<ul>
<li>Setting up <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000624696" target="_self">MobaXterm</a>
</li>
</ul>
</blockquote>
</li>
<li>
<h2>Using a Virtual Machine</h2>
<p>In order to avoid the problems of using a Windows environment, it may be advisable to install a Linux Virtual machine. This may be advantageous in other ways as many elements of scientific computing require a Linux environment, also it can provide a more user friendly place to become familiar with command line use.</p>
<p>There are multiple free options when it comes to VM software. We recommend <a href="https://www.virtualbox.org/wiki/Downloads" target="_self">Oracle VirtualBox</a>.</p>
<p>Further instructions on how to set up a virtual machine can be found <a href="https://blog.storagecraft.com/the-dead-simple-guide-to-installing-a-linux-virtual-machine-on-windows/" target="_self">here</a>.</p>
<p>Once you have a working VM you may continue following the instructions as given for <a href="#h_c1bbd761-1133-499b-a61a-57b9c4320a1a" target="_self">Linux/MacOS</a>.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What next?</h3>
<ul>
<li>Setting up a <a href="https://blog.storagecraft.com/the-dead-simple-guide-to-installing-a-linux-virtual-machine-on-windows/" target="_self">Virtual Machine</a>
</li>
</ul>
</blockquote>
</li>
<li>
<h2>WinSCP</h2>
<p>WinSCP has some advantages over MobaXterm (customisable, cleaner interface, open source), and some disadvantages (no built in X-server, additional authentication step). However, WinSCP setup is more involved than with MobaXterm, therefore we do not recommend it for new users.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What next?</h3>
<ul>
<li>Setting up <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000584256" target="_self">WinSCP</a>
</li>
</ul>
</blockquote>
</li>
<li>
<h2>Git Bash</h2>
<p>If you are using Git for version control you may already have Git Bash installed. If not it can be downloaded from <a href="https://git-scm.com/downloads" target="_self">here</a>.</p>
<p>Git Bash is perfectly adequate for testing your login or setting up your password, but lacks many of the features of MobaXterm or a native Unix-Like terminal. Therefore we do not recommend it as your primary terminal.</p>
</li>
<li>
<h2>Windows PowerShell</h2>
<p>All Windows computers have PowerShell installed, however it will only be useful to you if Windows Subsystem for Linux (WSL) is also enabled, instructions <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075575" target="_self">here</a>.</p>
<p>Like Git Bash, PowerShell is perfectly adequate for testing your login or setting up your password, but lacks many of the features of MobaXterm or a native Unix-Like terminal. Therefore we do not recommend it as your primary terminal.</p>
</li>
</ul>