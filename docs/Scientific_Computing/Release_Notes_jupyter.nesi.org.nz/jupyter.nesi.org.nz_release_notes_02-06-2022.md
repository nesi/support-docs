Release Update - 2. June 2022 {#ReleaseNotes-ReleaseUpdate-11.July2019}
-----------------------------

New and Improved {#ReleaseNotes-NewandImproved}
----------------

-   Updated JupyterLab version to v3.4.2
-   Updated
    [RStudio-on-NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360004337836)
    (v0.22.5): fix library path when using NeSI R package in RStudio
    (e.g. R-bundle-Bioconductor)
-   Plotly extension re-added (missing in the previous release)
-   Added [papermill](https://pypi.org/project/papermill/) extension
-   Updated [NeSI Virtual
    Desktop](https://support.nesi.org.nz/hc/en-gb/articles/360001600235)
    to v2.4.1
    -   # Image changes
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
             - Removed faulty & uneeded bind paths.
             - Removed debug by default and hardcoded verbose.
             - replaced VDT_HOME with XDG equiv
