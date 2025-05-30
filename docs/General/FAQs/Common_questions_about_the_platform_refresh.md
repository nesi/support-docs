---
description: Common questions researchers have about NeSI's platform refresh.
status: new
tags: 
  - refresh
  - hpc3
search:
  boost: 2
---

NeSI is evolving its technology platform to ensure Aotearoa's national eResearch infrastructure and services are more accessible, responsive, and flexible to your needs. For more details [visit the NeSI website](https://www.nesi.org.nz/platform-refresh).

Along the way, we'll use this page to share answers to some of the most common questions we're hearing from you.

## When is this happening?

Migration is underway! The new platforms opened for existing NeSI users on May 15th.
[View our current timeline here](https://docs.nesi.org.nz/General/Announcements/migration_timeline_and_transition_plan/).

## Do I need to move my data or software?

We have copied your `/home` and `/project` directories to our new high-performance WEKA storage on the new platforms.
To keep the WEKA copy of your data as fresh as possible, we are repeatedly syncing your directories from GPFS to WEKA until you have fully migrated.
More details for understanding what data gets migrated can be [read here](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/).

## What project data is being moved?

- `/home` and `/project` directories are already copied to the new storage and are being continuously updated to capture any changes you’re making.
- By default, `/nesi/nobackup` is not migrated. If you want any of this data, you can override the default and force data to be copied.
[Follow the instructions here](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/) so that you have everything you need to work on the new platforms. {% include "partials/support_request.html" %} if you need help.

## How do I stop the automatic data synchronisation with Mahuika?

Once you are happy that all your data has been successfully copied to WEKA and you are ready to move to working entirely the new platform, please place a file named .GOODBYE_GPFS in the top directory of each of your three GPFS filesets (home, project, and nobackup) on Mahuika. [Read our instructions here](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/#halting-the-synchronisation-from-gpfs-entirely).

## Why does my new data on the new platforms keep disappearing?

Have you stopped the data synchronisation with Mahuika? That might be the reason, as anything copied over from Mahuika as part of the synchronisation process will overwrite your data on the new platforms. To stop the data synchronisation, [follow our instructions here](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/#halting-the-synchronisation-from-gpfs-entirely). If you've completed that step and your data on the new platforms is still disappearing, [send us an email](mailto:support@nesi.org.nz) and we'll work with you to troubleshoot the issue.

## Will the software package I use be available on the new platforms?

All software that was supported on Mahuika's Milan nodes is available on the new platforms. To view a list of software available,
[visit our Supported Applications page](https://docs.nesi.org.nz/Scientific_Computing/Supported_Applications/) in our Support Documentation site.

## Will a long system outage be required as part of the migration of data and projects?

Overall, we're running the migration in stages to avoid any lengthy outages and to maintain a smooth user experience. We've scheduled an outage for June 3-5 that will affect login on the new platforms. Jobs already running will not be affected. For details, [view and subscribe for system updates here](https://status.nesi.org.nz/incidents/3y3ttj57fts6).

## Do I need to create a user account?

All existing NeSI users will be migrated to the new systems. Your existing user account will work on the new systems, though you will be required to reset your password and second factor.

## When can I start running jobs on the new platform?

Existing NeSI users can login now. [View our guide here to get started](https://docs.nesi.org.nz/General/Announcements/HPC3/). The earlier you migrate the smoother your transition will be. We love working alongside you and resolving issues together. To keep doing that well, we need to work with you _now_ so we’re not troubleshooting under pressure later. We're aiming to onboard new users, projects and allocations in early June. 
[View our current timeline here](https://docs.nesi.org.nz/General/Announcements/migration_timeline_and_transition_plan/).

## Compared to Mahuika, what's different on the new platforms?

[This article](https://docs.nesi.org.nz/General/FAQs/Mahuika_HPC3_Differences/) presents a comparison of the differences between Mahuika and the new platforms. If you have questions about the new environment, [send us an email](mailto:support@nesi.org.nz) or come along to our [online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/).

## I'm currently running on Māui. Will something change for me?

For all NIWA-owned projects, Māui access remains until NIWA decommissions the platform (date TBC).
For any NIWA-owned projects with current Mahuika allocations, NeSI will email you directly to discuss migration plans.  
If you have any immediate questions or concerns about how migration will work for your project, please reach out to support@nesi.org.nz. If you are not sure if you are migrating or have questions about how the new platforms differ from Māui, [send us an email](mailto:support@nesi.org.nz) or come along to our [online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/).

## Does this affect Nearline?

All NeSI compute and storage services will leverage the new infrastructure.
The new service is called Freezer and it will initially offer a similar long-term tape-based solution storing a single copy of data.
We will look at the roadmap for this service once we’ve completed migration.
We’re currently migrating your data from Nearline to Freezer so that it is ready and waiting for you on the new platform.
[Read our latest update](https://docs.nesi.org.nz/General/Announcements/update_to_nearline_service/) for more details on that process.

## I have more questions that aren't covered here. Where can I go or who can I talk to for more information?

Reach out anytime - no question is too small. We are ready to respond - email us at [support@nesi.org.nz](mailto:support@nesi.org.nz)
and we also invite you to join our [Online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/) to chat with us one-to-one.

