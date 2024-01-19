---
created_at: '2022-08-23T02:25:55Z'
hidden: false
tags:
- releasenote
title: jupyter.nesi.org.nz release notes 25/08/2022
vote_count: 0
vote_sum: 0
zendesk_article_id: 5362357660431
zendesk_section_id: 360001150156
---

## New and Improved

- Updated [RStudio-on-NeSI](../../Scientific_Computing/Interactive_computing_using_Jupyter/RStudio_via_Jupyter_on_NeSI.md)
    to v0.24.0
  - RStudio server v2022.07.1
  - Allow usage of NeSI environment modules in RStudio terminal (beta)
  - Allow usage of Slurm commands in RStudio terminal (beta)
- Updated [NeSI Virtual
    Desktop](../../Scientific_Computing/Interactive_computing_using_Jupyter/Virtual_Desktop_via_Jupyter_on_NeSI.md)
    to v2.4.3  
  - Utilising latest version of
        [Singularity](../../Scientific_Computing/Supported_Applications/Singularity.md)  

## Fixed

- RStudio
  - Addressed issue preventing user installation of rmarkdown when using R/4.1.0-gimkl-2020a
  - Addressed knitr PDF compilation when using R/4.2.1-gimkl-2022a
- NeSI Virtual Desktop
  - Added dependencies to fix OpenGL related issues
  - Internal refactoring for maintenance purpose of the permission
        with skeleton files in container build
