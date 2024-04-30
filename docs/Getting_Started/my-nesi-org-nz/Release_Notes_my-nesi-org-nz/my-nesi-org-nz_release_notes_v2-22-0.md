---
created_at: '2024-04-30T19:53:24Z'
tags:
- releasenote
title: my.nesi.org.nz release notes v2.22.0
vote_count: 0
vote_sum: 0
---

## New and Improved

- Project Request pages update
    - We have added more information with the different fields required to be filled in.
    - We have made the grant selection easier use with a drop down list. The list is now searchable.
    - We have added the capability to have more supervisors if needed by adding new members and selecting the supervisor tick box.
    - We have improved the saving feature to avoid losing any values from any draft request.
    - We are asking more information about the type of storage needed.
    - We are now requiring the email addresses for grant PI as well as the main supervisor.
    - We have added default values for the project start date as well as the Mahuika compute units an the storage fields.

- Allocation renewal update
    - In the request, you will be now asked to inform us if this allocation is linked to a grant or not.
    - Only valid grants from previous allocations will be carried forward: we are now checking
        that the end date of the grant is after the start date of the allocation request.

- All support links are now redirected to docs.nesi.org.nz including the release notes.
    All contacts or feedbacks will be through emails either support@nesi.org.nz or support@cloud.nesi.org.nz.

- Projects owners will be asked to review their members
    every year for security reasons: a banner will be displayed annually.

## Fixes

- Used compute units values in the current allocation are now 
    correctly displayed Mahuika allocation only in the project details green box.

If you have any questions about any of the improvements or fixes, please
{% include "partials/support_request.html" %}.
