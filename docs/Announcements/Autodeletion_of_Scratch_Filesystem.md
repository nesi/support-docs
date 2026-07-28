---
created_at: 2025-11-07
Title: Autodelete of Scratch Filesystem
description: A page sharing the details of changes to scratch filesystem deletion policy
tags: [announcement]
search:
---

We’re making some important updates to how your project’s temporary data is stored and managed on our HPC platforms. These changes will improve the availability and performance of our scratch filesystem (`/nesi/nobackup`).

## What is changing?

- Data stored in our scratch filesystem (`/nesi/nobackup`) that is not accessed for 90 days or more will be automatically deleted. This is a change from our previous timeframe of 120 days.
- Any folders that are empty after files have been deleted will also be deleted. 
- Scans and deletions will now happen on a fortnightly basis. You will still be provided two weeks notice before any data is deleted.
- There will be no exclusions to the 90-day auto-deletion process. If you need to store data for longer than 90 days, {% include "partials/support_request.html" %}

## When will this happen?

Update: This new policy has come into effect as of Wednesday 19 November. Our first scan was run to identify candidate files and project members with flagged files were notified by email (Subject to their [my.nesi.org.nz notification preferences](../Getting_Started/my-nesi-org-nz/Managing_Notification_Preferences.md)).

## How will I know if my data is flagged for deletion?

Prior to data being deleted, we’ll send you an email that identifies what has been marked for deletion. You can subscribe to or unsubscribe from receiving these notifications through [my.nesi.org.nz](https://my.nesi.org.nz).

You can also manually check at any time if you have any data scheduled for deletion — see [instructions for checking scheduled deletions](../Storage/Automatic_Cleaning_of_Nobackup.md).

## More information

Our Support Documentation has more details on how our auto-deletion cleaner works as well as advice for where to store different types of data on our HPC platform:

- [Automatic cleaning of nobackup file system](../Storage/Automatic_Cleaning_of_Nobackup.md)

- [Where should I store my data](../Getting_Started/FAQs/Where_should_I_store_my_data.md)


If you have any questions or would like to discuss your data storage needs in more detail, come to one of our [Weekly Online Office Hours](../Getting_Started/Weekly_Online_Office_Hours.md) or {% include "partials/support_request.html" %}.
