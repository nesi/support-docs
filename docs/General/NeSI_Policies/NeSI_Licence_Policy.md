---
created_at: '2019-08-07T03:50:45Z'
hidden: false
label_names: []
position: 12
title: NeSI Licence Policy
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001097936
zendesk_section_id: 360000224835
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>With very few exceptions, NeSI does not hold software licences of its own. If you wish to use any of the proprietary software installed on the NeSI cluster, you, or more likely your institution or department, will need to have an appropriate licence.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>Slurm and many other applications use the American spelling of the noun, "<em>license</em>".</p>
</blockquote>
<h1>Licence Servers</h1>
<p>The most common method of licence control is using 'floating' network licences hosted on an external server. In order for a user on a NeSI cluster to check out a licence, the address of that server must be known, and a firewall exception made for NeSI IP addresses (see below).</p>
<p>NeSI's public-facing IP addresses are:</p>
<pre><code>202.36.29.252
202.36.29.253
103.229.249.252
103.229.249.253</code></pre>
<h2>Institutional Licences</h2>
<p>A list of already established licence server connections can be found in the NeSI support documentation for the relevant software. Provided you are a member of the listed institution or faculty you should be able to use the software without any set-up.</p>
<p>If you believe you should have access to a licence but do not, or would like to organise remote use of your institution's licence, please <a href="mailto:support@nesi.org.nz" target="_self">email NeSI Support</a> and cc: your own IT services.</p>
<h2>Personal or Research Group Licences</h2>
<p>You are welcome to make your own licence arrangements, if your institution doesn't have a licence or you need to access extra features of the software that aren't included in your institution's default package. This may involve you setting up an additional licence server at your institution, or on a personal machine. Your licence server must run on a computer that has a static IP address and is visible on the public internet. Setting up your computer in this way and securing it is beyond the scope of this article, but will involve talking to your institution's IT department or to your internet service provider (ISP).</p>
<h1>Licence Files</h1>
<p>An alternative to licence servers, used by some programs, is a licence file that contains a code issued to that user or group during the registration process.</p>
<p>This approach is simpler for us to set up, as there is no need to communicate with a remote licence server. However, the onus is on the licensee to provide us with a copy of the licence file. Generally this will be done during installation of the software.</p>
<p>It is important for us to know who is eligible to use any particular licence file, so that we don't accidentally allow unauthorised persons to use a given piece of software.</p>
<h1>Software without built-in licence management</h1>
<p>Some software packages do not provide their own licence management systems (servers, files, etc.). The owners of these packages rely on us as the system administrators to prevent unauthorised use.</p>
<p>Access to such a piece of software is usually by adding people to a NeSI-maintained group of authorised users, which we refer to as a "software group". Among NeSI users, only members of the software group for that particular package will be permitted to see or interact with the package.</p>
<p>Before adding any particular person to a software group, we may ask to see a licence agreement allowing that person to use the software. We may also check to see whether the licence agreement forbids the person from using the software on NeSI.</p>
<blockquote class="blockquote-warning">
<h3 id="warning2">Warning</h3>
<p>Some licence agreements are quite restrictive in terms of where, or on what sort of machine, a licensee may run the program. For example, the licence may require one or more of the following:</p>
<ul>
<li>The software may only be run on one computer (node) at a time.</li>
<li>Any computer on which the software is run must be owned by the user's employing institution, operated by employees of that institution, or both.</li>
<li>There may be other restrictions, like a limit to the number of simultaneous tasks or threads you are permitted to run.</li>
</ul>
<p>We may not have seen your licence agreement, and even if we have, we're not intellectual property lawyers. Just because we grant you access to a piece of software it doesn't necessarily mean you're authorised to use it in the way you intend. <strong>It is your responsibility to ensure that your use of the software on NeSI complies with the terms of your licence or is otherwise permitted by law.</strong></p>
</blockquote>
<h1>Slurm Tokens<span style="font-size: 15px;"> </span>
</h1>
<p>We encourage the use of Slurm licence tokens in your batch scripts, for example:</p>
<pre><code>#SBATCH --licenses ansys_hpc@uoa_foe:60,ansys_r@uoa_foe</code></pre>
<p>will request 60 'hpc' licences and 1 'research' licence from the University of Auckland Engineering licence server. This will prevent your job starting until the specified number of licences is available.</p>
<p>By not including the correct number of Slurm licence tokens you run the risk of a job failing on startup (your job will have to re-queue), or worse, idling until a licence becomes available (wasting CPU hours and likely leading to a timeout).</p>
<p>The names of the Slurm licence tokens are included in the application-specific documentation.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>Slurm licence reservations work independently of the licence server. Not including a Slurm token will not prevent your job from running, not will including one modify how your job runs (only <em>when</em> it runs).</p>
</blockquote>