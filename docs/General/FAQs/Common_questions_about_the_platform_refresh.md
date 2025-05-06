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

We're all moving to the new platforms starting in May 2025.
[View our current timeline here](https://docs.nesi.org.nz/General/Announcements/migration_timeline_and_transition_plan/).
If you are enthusiastic to be among the first groups to try the new resources, [get in touch](mailto:support@nesi.org.nz).

## Do I need to move my data or software?

We have copied your `/home` and `/project` directories to our new high-performance WEKA storage on the new platforms.
To keep the WEKA copy of your data as fresh as possible, we are repeatedly syncing your directories from GPFS to WEKA until you have fully migrated.
More details for understanding what data gets migrated can be [read here](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/).

## What project data is being moved?

- `/home` and `/project` directories are already copied to the new storage and are being continuously updated to capture any changes you’re making.
- By default, `/nesi/nobackup` is not migrated. If you want any of this data, you can override the default and force data to be copied.
[Follow the instructions here](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/) so that you have everything you need for starting work on the new platforms. {% include "partials/support_request.html" %} if you need help.

## Will the software package I use be available on the new platforms?

All software currently supported on Mahuika's Milan nodes will be deployed. To view a list of software currently running on Mahuika,
[visit our Supported Applications page](https://docs.nesi.org.nz/Scientific_Computing/Supported_Applications/) in our Support Documentation site.
If you haven't tried running your code on the Milan nodes yet, [visit this guide for instructions](https://docs.nesi.org.nz/General/Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform/).

## Will a long system outage be required as part of the migration of data and projects?

We have one outage scheduled so far:

- **19/20 May**: [Outage](https://status.nesi.org.nz/incidents/3y3ttj57fts6) to move our user identity and project admin platforms. Impacts:
    - Mahuika and Māui HPC clusters will be unaffected for ssh users
    - Users will not be able to login to my.nesi.org.nz or use interactive compute services (OnDemand, Jupyter)
    - Users will not be able to log-in to the new HPC platform (running jobs will be unaffected)

Overall, we're running the migration in stages to avoid any lengthy outages and to maintain a smooth user experience.

## Do I need to create a user account?

All existing NeSI users will be migrated to the new systems. Your existing user account will work on the new systems, though you will be required to reset your password and second factor.

## When can I start running jobs on the new platform?

We're all moving to the new platforms starting in May 2025.
[View our current timeline here](https://docs.nesi.org.nz/General/Announcements/migration_timeline_and_transition_plan/).
If you are enthusiastic to be among the first groups to try the new resources,
[get in touch](mailto:support@nesi.org.nz).

## I'm currently running on Mahuika, will something change for me?

The platform NeSI has selected to replace Mahuika is similar to Mahuika's AMD Milan compute nodes.
We're using these current Milan nodes to validate any issues.
If you are already using the Milan nodes to support your work, no action is required from you at this point.
If you are using Mahuika's Broadwell nodes or Māui, we recommend you
[test your workloads on Milan](https://docs.nesi.org.nz/General/Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform/) now.

## I'm currently running on Māui, will something change for me?

NeSI access to the Māui HPC platform will end on 23 May. Some projects on Māui will move to the new NeSI infrastructure.
We have been in touch with those Māui projects and given them a small allocation on Mahuika which can be used to validate the software they need is available (or can be built) on Mahuika's AMD Milan nodes and works as expected.
All members of the Māui project can use this Mahuika allocation.
Visit this [how-to guide for instructions](https://docs.nesi.org.nz/General/Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform/)
of how to test your workloads on Milan.

## Does this affect Nearline?

All NeSI compute and storage services will leverage the new infrastructure.
The new service is called Freezer and it will initially offer a similar long-term tape-based solution storing a single copy of data.
We will look at the roadmap for this service once we’ve completed migration.
We’re currently migrating your data from Nearline to Freezer so that it is ready and waiting for you on the new platform.
[Read our latest update](https://docs.nesi.org.nz/General/Announcements/update_to_nearline_service/) for more details on that process.

## I have more questions that aren't covered here. Where can I go or who can I talk to for more information?

Reach out anytime - no question is too small. We are ready to respond - email us at [support@nesi.org.nz](mailto:support@nesi.org.nz)
and we also invite you to join our [weekly Online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/) to chat with us one-to-one.

