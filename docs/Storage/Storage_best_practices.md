# Storage Best Practises

This page will guide you through best practices for storing your data on Mahuika. 

## What are `home`, `project` and `scratch` directories for?

`home`: This directory is for storing files that are central for performing your simulations and calculations on Mahuika. This includes program installations, conda environments and other virtual environments. 

`project`: This directory is for storing files that you want to keep for long periods of time that you access regularly. This includes important research files you do not want deleted and you access regularly, and can include conda environments and other virtual environments that are too large for `home`. 

`scratch`: This directory is for storing raw data and larger files that are temporary. In this case, temporary may be for short (seconds) to long (90 days) amounts of time. Examples include `temp` files, files that you only need for less than 3 months at a time, OTHER EXAMPLES. 

You can find more information about these directories in the [Filesystems and Quotas page](File_Systems_and_Quotas/Filesystems_and_Quotas.md). 

## I would like to run a job, what directory should I run it in?

It is best practice to perform your calculations/simulations in the following order:

1. Perform your calculations/simulations in `scratch`. `scratch` is a large storage space (usually on the order of TBs) that gives you space to perform your calculations/simulations. 
2. After analysis, any data you want to keep for further analysis and that you will access regularly should be kept in `project`.
3. If you have GBs or TBs of data that you need to keep on Mahuika but don't have enough space on `project` and do not access regularly, you should consider moving this data onto Freezer. Freezer is designed to keep mass amounts of data on that you will only need to access every few months. [Click here for more information about Freezer](Long_Term_Storage/Freezer_long_term_storage.md). 
4. `project` is limited in space, so any data you can move off Mahuika should be when you are either done with the data, or you can do analysis of the data on your own computer. See [I would like to move data off Mahuika. What are my options?](#i-would-like-to-move-data-off-mahuika-what-are-my-options)

## How should I store important data?: The 3,2,1 Rule

It is vital that files that are important to your work are backed up after you have processed them and want to move them off Mahuika. The 3,2,1 rule is best practise for storing and backing up files to minimise lose of mission critical data. The rule is:

* **3 Copies**: Keep your original data plus two backups.
* **2 Media Types**: Store backups on different media (e.g., internal hard drive, external hard drives, cloud, network attached storage device, high capacity storage, freezer).
* **1 Offsite**: Keep one copy physically separate (e.g., cloud, freezer, high capacity storage, offsite drive) to survive local disasters.

## What is Freezer (Storaging massive files on Mahuika long-term without auto-deletion)?

Freezer is a tape storage system that is designed to hold large amounts of data that are accessed infrequently. Freezer is a great way to keep large files (or a collection of large files) on Mahuika. See [Freezer long term storage](Long_Term_Storage/Freezer_long_term_storage.md) for more information about Freezer.

## I would like to move data off Mahuika. What are my options?

This will depend on what resources your group can budget for and what high capacity storage (HCS) your university offers. See [Moving files to and from the cluster](Moving_files_to_and_from_the_cluster.md) for more information about transfering data from Mahuika. 

### Storage options for Universities around New Zealand

If you are working at a New Zealand university, the following links provide information about what each university offers in terms of storage solutions:

* University of Auckland: https://research-hub.auckland.ac.nz/managing-research-data/research-data-storage/choosing-data-storage
* Auckland University of Technology: https://www.aut.ac.nz/student-life/studying/it-services/saving-your-files
* Massey University: https://www.massey.ac.nz/study/library/researcher-support/research-data-management/store-your-research-data/
* University of Waikato (Check): https://www.waikato.ac.nz/students/support-services/student-ict/storage/
* Victoria University of Wellington: https://libguides.victoria.ac.nz/research-data-management/store
* University of Canterbury: https://www.canterbury.ac.nz/research/eresearch-at-canterbury/research-data-storage
* Lincoln University (Check): 
* University of Otago: https://ask.otago.ac.nz/knowledgebase/article/KA-10003729/en-us

### High Capacity Storage (HCS) Options

High capacity storage are offered by various institutes around New Zealand. Here are some options: 

* University of Auckland: https://research-hub.auckland.ac.nz/managing-research-data/research-data-storage/research-drive
* Massey University: See 'Network disk space allocation at Massey' in https://www.massey.ac.nz/study/library/researcher-support/research-data-management/store-your-research-data/
* Victoria University of Wellington: https://intranet.wgtn.ac.nz/services-resources/digital-solutions/research-services/solar
* University of Otago: https://www.otago.ac.nz/its/services/file-storage-and-server-services/high-capacity-central-file-storage-hcs

### Cloud Storage options

Depending on your Data Policy and your university, the following cloud options may provide you space for storing data

* Google Drive: https://drive.google.com
* Microsoft OneDrive: https://onedrive.live.com
* Dropbox: https://www.dropbox.com

You can move data directly onto these clouds from Mahuika using rclone. See [the rclone documentation](https://rclone.org/docs/) for more information about how to copy data directly to a cloud provider in the terminal.

 
