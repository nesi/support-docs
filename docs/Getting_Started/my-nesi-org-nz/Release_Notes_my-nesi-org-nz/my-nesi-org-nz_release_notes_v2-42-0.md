---
created_at: '2025-09-25T19:53:24Z'
tags:
- releasenote
title: my.nesi.org.nz release notes v2.42.0
search:
  boost: 0.1
---

## Fixed
- We've made improvements to the user experience around account and dashboard navigation:
  - The link from the HPC Account page [(https://my.nesi.org.nz/account/hpc-account)](https://my.nesi.org.nz/account/hpc-account) now correctly redirects to the Join Project page [(https://my.nesi.org.nz/projects/join)](https://my.nesi.org.nz/projects/join).

  - Navigation to the Dashboard is now guided by a user's account status:
    - If a user is pending, clicking Dashboard redirects to https://my.nesi.org.nz/account/profile.
    - If a user has no project, clicking Dashboard redirects to https://my.nesi.org.nz/account/hpc-account.
    - If a user has one or more projects, clicking Dashboard redirects to https://my.nesi.org.nz/projects/list.

If you have any questions about any of the updates, please
{% include "partials/support_request.html" %}.
