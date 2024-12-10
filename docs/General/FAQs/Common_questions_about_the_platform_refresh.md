---
description: Common questions researchers have about NeSI's platform refresh in 2024.
status: new
tags: [refresh]
search:
  boost: 2
---

NeSI is evolving its technology platform to ensure Aotearoa's national eResearch infrastructure and services are more accessible, responsive, and flexible to your needs. For more details [visit the NeSI website](https://www.nesi.org.nz/platform-refresh).

Along the way, we'll use this page to share answers to some of the most common questions we're hearing from you.

## When is this happening?

All new hardware has been delivered to the Waipapa Taumata Rau University of Auckland Tamaki Data Centre and installation of new power and cooling capabilities in the data centre was completed in late October. We'll keep you updated as our timelines are confirmed. If you are enthusiastic to be among the first groups to try the new platform, please [get in touch](mailto:support@nesi.org.nz).

## Do I need to move my data or software?

Projects and data will be migrated in staggered phases as systems become available. Starting the week of 16 December 2024, we will begin copying project data from the current NeSI systems to our new high performance storage platform. We are copying home, and project data, starting with project directories. You can continue to read and write data to/from the current storage system during this process, and carry on using NeSI services as usual. Once all data has been migrated and our new HPC service is officially brought online and ready for you to run jobs, we will be in contact to help you get started on the new system.
We will have more information to share later in January 2025 that provide additional details and a path for user migration onto the new platforms. 

## Will the software package I use be available on the new platforms?

All software currently supported on Mahuika's Milan nodes will be deployed. To view a list of software currently running on Mahuika, [visit our Supported Applications page](https://docs.nesi.org.nz/Scientific_Computing/Supported_Applications/) in our Support Documentation site. If you haven't tried running your code on the Milan nodes yet, [visit this guide for instructions](https://docs.nesi.org.nz/General/Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform/).

## Will a long system outage be required as part of the migration of data and projects?

We're planning to run migration in stages in order to avoid any lengthy outages and to maintain a smooth user experience. We'll share information ongoing as we stage releases of various services and migrations of data and projects.

## Do I need to create a user account?

All existing NeSI users will be migrated to the new systems. Your existing user account will work on the new systems, though you will be required to reset your password and second factor.

## When can I start running jobs on the new platform?

Early access to OnDemand, NeSI's interactive computing environment, is currently available for users who do not require access to a Slurm cluster, GPUs, or high-performance filesystem. NeSI OnDemand provides easy web-accessible access to Jupyter and RStudio, with more apps (eg. MatLab and Virtual Desktops) available over the coming months. This initial release of NeSI OnDemand currently only supports sessions with up to 64 GB memory. For more information, [visit our support documentation](https://docs.nesi.org.nz/Scientific_Computing/Interactive_computing_with_NeSI_OnDemand/).

## I'm currently running on Mahuika, will something change for me?

The platform NeSI has selected to replace Mahuika is similar to Mahuika's AMD Milan compute nodes. We're using these current Milan nodes to validate any issues. If you are already using the Milan nodes to support your work, no action is required from you at this point. If you are using Mahuika's Broadwell nodes or Māui, we recommend you [test your workloads on Milan](https://docs.nesi.org.nz/General/Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform/) now.

## I'm currently running on Māui, will something change for me?

Some projects on Māui will move to the new NeSI infrastructure. We have been in touch with those Māui projects and given them a small allocation on Mahuika which can be used to validate the software they need is available (or can be built) on Mahuika's AMD Milan nodes and works as expected. All members of the Māui project can use this Mahuika allocation. Visit this [how-to guide for instructions](https://docs.nesi.org.nz/General/Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform/) of how to test your workloads on Milan.

## Does this affect Nearline?

All NeSI compute and storage services will leverage the new infrastructure. Nearline is changing, leveraging different technology to deliver an easier to use cold storage solution. Called NeSI Freezer, it will initially offer a similar long-term tape-based solution storing a single copy of data. We will look at the roadmap for this service once we’ve completed migration. We began moving Nearline data to NeSI Freezer in September 2024. We are moving Nearline data in stages and contacting you individually by email when we are ready to move your project.

## I have more questions that aren't covered here. Where can I go or who can I talk to for more information?

Reach out anytime - no question is too small. We are ready to respond - email us at [support@nesi.org.nz](mailto:support@nesi.org.nz) and we also invite you to join our [weekly Online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/) to chat with us one-to-one.
