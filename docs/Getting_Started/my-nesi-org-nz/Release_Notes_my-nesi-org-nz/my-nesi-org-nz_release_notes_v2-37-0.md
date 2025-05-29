---
created_at: '2025-05-29T19:53:24Z'
tags:
- releasenote
title: my.nesi.org.nz release notes v2.37.0
search:
  boost: 0.1
---

## New and Improved

- Previously, compute allocation requests included separate fields for compute usage amounts on Mahuika and/or Maui. This has been updated to a single usage amount field, removing the need to specify a platform. If you have specific needs, you can add a comment indicating a desired platform or type of compute resource required. This change affects the following pages and forms:
    - *Projects / New Allocation Request*,  
    - *Projects / Apply for Project*,  
    - *Requests*.  
- A new *Freezer allocation* request form is available for NeSI's long-term storage platform.  
- The *Increase/Extend storage allocation* interface has been improved for better usability, now showing a list of allocations that can be increased or extended.  
- Updates in the *My HPC Account* and *NeSI Credentials* menus:  
    - The new 2025 HPC information is now permanently displayed.  
    - Mahuika and Māui login and second-factor authentication options are removed. If you experience any issues accessing Mahuika or Māui, please contact the support team.  
  

If you have any questions about any of the updates, please
{% include "partials/support_request.html" %}.
