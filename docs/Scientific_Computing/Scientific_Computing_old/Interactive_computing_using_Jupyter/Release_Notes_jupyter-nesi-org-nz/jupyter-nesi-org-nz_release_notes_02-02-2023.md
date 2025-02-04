---
created_at: '2023-02-02T03:42:47Z'
tags:
- releasenote
title: jupyter.nesi.org.nz release notes 02/02/2023
vote_count: 0
vote_sum: 0
zendesk_article_id: 6325030048655
zendesk_section_id: 360001150156
search:
  boost: 0.1
---

## New and Improved

-   Updated JupyterHub to v2.3.1
-   Updated JupyterLab to v3.5.3
-   Switched to Python 3.10 for running JupyterLab (kernels are
    unaffected)
    -   Note: if you have previously installed Python packages in your
        home directory using Python 3.10, we recommend cleaning out your
        *~/.local/Python-3.10-gimkl-2022a* directory, as it could
        conflict with our JupyterLab installation, and consider
        [Installing packages in a Python virtual environment](../../Supported_Applications/Python.md#installing-packages-in-a-python-virtual-environment)
        instead
