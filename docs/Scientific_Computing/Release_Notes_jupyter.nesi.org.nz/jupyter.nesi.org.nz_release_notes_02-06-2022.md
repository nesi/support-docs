---
created_at: '2022-06-02T05:35:53Z'
hidden: false
label_names:
- releasenote
position: 0
title: jupyter.nesi.org.nz release notes 02/06/2022
vote_count: 1
vote_sum: 1
zendesk_article_id: 4905985717135
zendesk_section_id: 360001150156
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h2 id="ReleaseNotes-ReleaseUpdate-11.July2019">Release Update - 2. June 2022</h2>
<h2 id="ReleaseNotes-NewandImproved">New and Improved</h2>
<ul>
<li data-stringify-indent="0" data-stringify-border="0">Updated JupyterLab version to<span> v3.4.2</span>
</li>
<li data-stringify-indent="0" data-stringify-border="0"><span>Updated <a href="https://support.nesi.org.nz/hc/en-gb/articles/360004337836" target="_blank" rel="noopener">RStudio-on-NeSI</a> (v0.22.5): fix library path when using NeSI R package in RStudio (e.g. R-bundle-Bioconductor)</span></li>
<li data-stringify-indent="0" data-stringify-border="1">Plotly extension re-added (missing in the previous release)</li>
<li data-stringify-indent="0" data-stringify-border="0"><span>Added <a href="https://pypi.org/project/papermill/" target="_blank" rel="noopener">papermill</a> extension</span></li>
<li data-stringify-indent="0" data-stringify-border="0">
<span>Updated <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001600235" target="_blank" rel="noopener">NeSI Virtual Desktop</a> to v2.4.1</span>
<ul>
<li data-stringify-indent="0" data-stringify-border="0">
<pre class="c-mrkdwn__pre" data-stringify-type="pre"># Image changes
 - Update default Firefox version.
 - Update to use singularity 3.8.5.
 - Switched to rocky8 image.
 - Added chrome, strace, sview and xfce-terminal to image.
 - Added some libraries need for ANSYS
 - Added missing GLX libraries.

# Bug fixes
 - Fixed faulty startup messages 
 - Fixed entrypoint duplication issue.
 - unset 'SLURM_EXPORT_ENV' before starting desktop.

# Refactoring
 - Removed dependency on system vdt repo.
 - Removed faulty &amp; uneeded bind paths.
 - Removed debug by default and hardcoded verbose.
 - replaced VDT_HOME with XDG equiv</pre>
</li>
</ul>
</li>
</ul>