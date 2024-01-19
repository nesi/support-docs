---
created_at: '2022-06-02T05:35:53Z'
hidden: false
tags:
- releasenote
title: jupyter.nesi.org.nz release notes 02/06/2022
vote_count: 1
vote_sum: 1
zendesk_article_id: 4905985717135
zendesk_section_id: 360001150156
---

## Release Update - 2. June 2022

## New and Improved

- Updated JupyterLab version to v3.4.2
- Updated [RStudio-on-NeSI](../../Scientific_Computing/Interactive_computing_using_Jupyter/RStudio_via_Jupyter_on_NeSI.md) (v0.22.5): fix library path when using NeSI R package in RStudio (e.g. R-bundle-Bioconductor)
- Plotly extension re-added (missing in the previous release)
- Added [papermill](https://pypi.org/project/papermill/) extension
- Updated [NeSI Virtual Desktop](../../Scientific_Computing/Interactive_computing_using_Jupyter/Virtual_Desktop_via_Jupyter_on_NeSI.md) to v2.4.1
    - Image changes
        - Update default Firefox version.
        - Update to use singularity 3.8.5.
        - Switched to rocky8 image.
        - Added chrome, strace, sview and xfce-terminal to image.
        - Added some libraries need for ANSYS
        - Added missing GLX libraries.
    - Bug fixes
        - Fixed faulty startup messages
        - Fixed entrypoint duplication issue.
        - unset `SLURM_EXPORT_ENV` before starting desktop.
    - Refactoring
        - Removed dependency on system vdt repo.
        - Removed faulty & unneeded bind paths.
        - Removed debug by default and hardcoded verbose.
        - replaced `VDT_HOME` with XDG equiv
