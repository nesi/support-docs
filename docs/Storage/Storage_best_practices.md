# Storage Best Practises

This page will guide you through best practices for storing your data on Mahuika

## The 3,2,1 Rule

The 3,2,1 rule is a best practise of backing up data to minimise lose of mission critical data. The rule is

* **3 Copies**: Keep your original data plus two backups.
* **2 Media Types**: Store backups on different media (e.g., Internal Hard Drive, External Hard Drives, Cloud, Network Attached Device, High Capacity Storage).
* **1 Offsite**: Keep one copy physically separate (e.g., cloud, offsite drive) to survive local disasters.

## What are `home`, `project` and `nobackup` directories for?

`home`: This directory is for storing files that are central for performing your simulations and calculations on Mahuika. This includes program installations, conda environments and other virtual environments.

`project`: This directory is for storing files that you want to keep for long periods of time that you access regularly. This includes important research files you do not want deleted and you access regularly, and can include conda environments and other virtual environments that are too large for `home`. 

`nobackup`: This directory is for storing larger files that are temporary. In this case, temporary may be for short (seconds) to long (90 days) amounts of time. Examples include `temp` files, files that you only need for less than 3 months at a time, OTHER EXAMPLES. 

## I would like to run a job, what directory should I run it in?

It is best practice to perform calculations in the following order:

1. Perform your calculations in `nobackup`. `nobackup` is a large storage space (usually on the order of TBs) that gives you space to perform your calculations. 
2. After analysis, any data you want to keep for further analysis and that you will access regularly should be kept in `project`.
3. If you have GBs or TBs of data that you need to keep on Mahuika but don't have enough space on `project` and do not access regularly, you should consider moving this data onto Freezer. Freezer is designed to keep mass amounts of data on that you will only need to access every few months. [Click here for more information about Freezer](Long_Term_Storage/Freezer_long_term_storage.md). 
4. `project` is limited in space, so any data you can move off of Mahuika should be when you are either done with the data, or you can do analysis of the data on your own computer. See [I would like to move data off Mahuika. What are my options?](#i-would-like-to-move-data-off-mahuika-what-are-my-options)

## I would like to move data off Mahuika. What are my options?

This will depend on what resources your group can budget for and what high capacity storage (HCS) your university offers. 

### Storage options for Universities around New Zealand

If you are working at a New Zealand university, the following links provide information about what each university offers in terms of storage solutions:

* University of Auckland: https://research-hub.auckland.ac.nz/managing-research-data/research-data-storage/choosing-data-storage
* Auckland University of Technology (Check): https://www.aut.ac.nz/student-life/studying/it-services/saving-your-files
* Massey University: https://www.massey.ac.nz/study/library/researcher-support/research-data-management/store-your-research-data/
* University of Waikato (Check): https://www.waikato.ac.nz/students/support-services/student-ict/storage/
* Victoria University of Wellington: https://libguides.victoria.ac.nz/research-data-management/store
* Canterbury University: https://www.canterbury.ac.nz/research/eresearch-at-canterbury/research-data-storage
* Lincoln University (Check): 
* University of Otago: https://ask.otago.ac.nz/knowledgebase/article/KA-10003729/en-us

### High Capacity Storage (HCS) Options

High capacity storage are offer by various intitutes around New Zealand. Here are some options:

* University of Auckland: https://research-hub.auckland.ac.nz/managing-research-data/research-data-storage/research-drive
* Massey University: See 'Network disk space allocation at Massey' in  https://www.massey.ac.nz/study/library/researcher-support/research-data-management/store-your-research-data/
* Victoria University of Wellington: https://intranet.wgtn.ac.nz/services-resources/digital-solutions/research-services/solar
* University of Otago: https://www.otago.ac.nz/its/services/file-storage-and-server-services/high-capacity-central-file-storage-hcs

### Network Attached Storage (NAS) Devices and Hard Drives

Based on your group's resources, it may be an option to purchase a Network Attached Storage (NAS) device or hard drives to store data onsite. 


