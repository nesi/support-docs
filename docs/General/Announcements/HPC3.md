---
created_at: 2025-05-05
description: All you need to know about the new NeSI HPC
tags: 
    - HPC3
    - refresh
---

## Before you Start

Before using the new cluster, please read all of:

- [Differences between Mahuika and the new HPC](../FAQs/Mahuika_HPC3_Differences.md)
- [Known Issues on the new HPC](Known_Issues_HPC3.md) - Are we ready for *your* workflow?
- [Using the new copy of your data](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/#using-the-new-weka-copy-of-your-data) (a section of the [Data Migration](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/) page)
    - Do your new files keep disappearing?
    - [Stop the Synchronisation of your Data](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/####halting-the-synchronisation-from-GPFS-entirely)
- [Standard Terminal Setup HPC3](../../Scientific_Computing/Terminal_Setup/Standard_Terminal_Setup.md)

If you hit a problem please check the above pages first, and then if not answered there email [support@nesi.org.nz](mailto:support@nesi.org.nz) or come to our [Online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/) which are currently happening daily.

!!! WARNING Warning
    Before running any substantial/production jobs on the new HPC, you ***MUST*** stop the synchronisation of your data from GPFS to WEKA, otherwise you will lose any new work you do on the new HPC. See the section on
    [Stop the Synchronisation of your Data](https://docs.nesi.org.nz/Storage/File_Systems_and_Quotas/Moving_to_the_new_filesystem/####halting-the-synchronisation-from-GPFS-entirely)

    and if you don't understand it, please ask for help in the [Online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/) or email [

## Other Links

- [Migration Timeline](migration_timeline_and_transition_plan.md)
- [Common questions about the platform refresh](../FAQs/Common_questions_about_the_platform_refresh.md)
- [Preparing your code for use on NeSI's new HPC platform](Preparing_your_code_for_use_on_NeSIs_new_HPC_platform.md)
- [Update to Nearline Service](update_to_nearline_service.md)
