---
created_at: '2025-09-25T19:53:24Z'
tags:
- releasenote
title: my.nesi.org.nz release notes v2.42.0
search:
  boost: 0.1
---

## Fixed
- Improvements to the user experience around account and dashboard navigation:
  - The link from the HPC account page now correctly redirects to the Join Project page: https://my.nesi.org.nz/account/hpc-account now links to https://my.nesi.org.nz/projects/join.

  - Dashboard behavior has been corrected based on user status:
    - If a user is pending, clicking Dashboard now redirects to https://my.nesi.org.nz/account/profile.
    - If a user has no project, it redirects to https://my.nesi.org.nz/account/hpc-account.
    - If a user has projects, it redirects to https://my.nesi.org.nz/projects/list.

If you have any questions about any of the updates, please
{% include "partials/support_request.html" %}.
