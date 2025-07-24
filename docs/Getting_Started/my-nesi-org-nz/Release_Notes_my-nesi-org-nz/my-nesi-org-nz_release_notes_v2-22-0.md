---
created_at: '2024-04-30T19:53:24Z'
tags:
- releasenote
title: my.nesi.org.nz release notes v2.22.0
search:
  boost: 0.1
---

## New and Improved

- Project Request page updates:
    - We added additional questions that ask for more background information about your project.
    - We made the grant selection field easier to use with a drop down list. The list is now searchable.
    - We added the capability to have more supervisors if needed by adding new members and selecting the supervisor tick box.
    - We improved the saving feature to avoid losing any values from any draft requests.
    - We added new fields that ask for more information about the type of storage needed.
    - We now require the email addresses for grant PI as well as the main supervisor.
    - We added default values for the project start date, the Mahuika compute units, and the storage fields.

- Allocation renewal updates:
    - We now ask in the renewal form if this allocation is linked to a grant or not.
    - We now check that the end date of a grant is after the start date of the allocation request. Only valid grants from previous allocations will be carried forward.

- All support links, including link to release notes, now point to NeSI's new documentation site, docs.nesi.org.nz.
    All inquiries or feedback should be sent via email to either support@nesi.org.nz or support@cloud.nesi.org.nz.

- For added security, project owners will be asked to review their members every year. A notification banner will be displayed annually as a reminder.

## Fixes

- Users with Mahuika allocations can now see the total compute values used to date in their current allocation, displayed in the project details section of their MyNeSI dashboard (green box at top of page).

If you have any questions about any of the updates or fixes, please
{% include "partials/support_request.html" %}.
