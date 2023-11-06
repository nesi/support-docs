---
created_at: '2018-05-23T03:17:56Z'
hidden: false
label_names: []
position: 4
title: XC50 Aries Network Architecture
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000208356
zendesk_section_id: 360000040036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>There are 4 dual socket nodes on blade, connected to a single Aries (switch) chip, and there are 16 Aries chips in a chassis connected to the backplane. On Māui, this implies each chassis contains 64 nodes, or 2,560 Skylake cores. There are 3 chassis in an XC50 cabinet, and two XC50 cabinets are an Electrical "group". Maui has 1.5 groups.</p>
<p class="wysiwyg-text-align-center" align="left"><img src="https://support.nesi.org.nz/hc/article_attachments/360000488576/UPM_html_2d91e9cdd34d272d.gif" alt="UPM_html_2d91e9cdd34d272d.gif" width="298" height="263"></p>
<p>The performance characteristics are:</p>
<ol>
<ol>
<li>Intra-Chassis
<ol class="lower-alpha">
<li>Backplane</li>
<li>15 links in the backplane</li>
<li>Rank 1 (green) Network</li>
<li>14 Gbps</li>
</ol>
</li>
<li>Intra-group
<ol class="lower-alpha">
<li>Copper cables</li>
<li>15 links in 5 connectors</li>
<li>Rank 2 (black) Network</li>
<li>14 Gbps</li>
</ol>
</li>
<li>Inter-group links
<ol class="lower-alpha">
<li>Optical</li>
<li>10 links in 5 connectors</li>
<li>Rank 3 (blue) Network</li>
<li>12.5 Gbps</li>
</ol>
</li>
</ol>
</ol>
<p>The centrepiece of the Aries network is dynamic routing through a large variety of different routes from Aries A to Aries B. Therewith the effective bandwidth is increased significantly. These dynamic routing on alternative paths is applied on all 3 levels of the network.</p>