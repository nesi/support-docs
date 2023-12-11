---
created_at: '2023-11-22T03:10:45Z'
hidden: false
position: 0
tags:
- releasenote
title: jupyter.nesi.org.nz release notes 22/11/2023
vote_count: 0
vote_sum: 0
zendesk_article_id: 8422683604367
zendesk_section_id: 360001150156
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

## Fixed

-   We are now closing user sessions when the corresponding Jupyter
    server is stopped, to avoid idle sessions to linger on the host. We
    missed one case during the last release.

 

If you have any questions about any of the improvements or fixes,
please {% include "partials/support_request.html" %}.