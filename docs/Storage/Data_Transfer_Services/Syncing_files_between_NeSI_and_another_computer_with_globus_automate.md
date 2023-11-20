---
created_at: '2023-01-12T20:45:15Z'
hidden: false
position: 10
tags: []
title: Sync'ing files between NeSI and another computer with globus-automate
vote_count: 0
vote_sum: 0
zendesk_article_id: 6202743496591
zendesk_section_id: 360000040596
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

It is common to generate large amounts of simulation data on NeSI and
then having to migrate the files to another computer for storage or
post-processing.

Here we show how to transfer data from NeSI to another computer
***programmatically***, that is without using a web graphical user
interface and ***without typing your credentials each time you initiate
the transfer***.

You can also use this approach to synchronise your files, that is to
copy only the files that don't yet exist at the destination point, or
refresh the files that have changed since you last triggered a transfer.

We'll assume that you have a NeSI account, you have registered at
<https://globus.org>, and have created a guest collections on NeSI and
and a private mapped collection on the destination computer (follow the
instructions [our corresponding support
page](https://support.nesi.org.nz/hc/en-gb/articles/6198499650703)). A
guest collection is directory whose content is shared via Globus.

## Step 1: Write a JSON file describing the transfer

On NeSI, create a file named `transfer_input.json` with the following
content:

``` sl
{
  "source_endpoint_id": "ENDPOINT1",
  "destination_endpoint_id": "ENDPOINT2",
  "transfer_items": [
    {
      "source_path": "SOURCE_FOLDER",
      "destination_path": "DESTINATION_FOLDER",
      "recursive": true
    }
  ],
  "sync_level": SYNC_LEVEL, 
  "notify_on_succeeded": true,
  "notify_on_failed": true,
  "notify_on_inactive": true,
  "verify_checksum": true
}
```

where

-   `ENDPOINT1` is the source endpoint UUID, which you can get
    <https://app.globus.org/collections> by clicking on the collection
    of your choice. Using a guest collection will allow you to transfer
    the data without two-factor authentication
-   `ENDPOINT2` is the destination UUID, e.g. your personal endpoint
    UUID, which may be for your private mapped collection if you're
    transferring to your personal computer
-   `SOURCE_FOLDER` is the **relative** path of the source folder in the
    source endpoint. This is a directory, it cannot be a file. Use "/"
    if you do not intend to transfer the data from sub-directories
-   `DESTINATION_FOLDER` is the **absolute** path of the destination
    folder in the destination endpoint when the destination is a private
    mapped collection
-   `SYNC_LEVEL` specifies the synchronisation level in the range 0-3.
    `SYNC_LEVEL=0` will transfer new files that do not exist on
    destination. Leaving this setting out will overwrite all the files
    on destination. Click
    [here](https://docs.globus.org/api/transfer/task_submit/#transfer_specific_fields)
    to see how other sync\_level settings can be used to update data in
    the destination directory based on modification time and checksums.

## Step 2: Initiate the transfer

Load the `globus-automate-client` environment module

``` sl
module purge && module load globus-automate-client/0.16.1.post1-gimkl-2022
```

then start the transfer using

``` sl
globus-automate action run --action-url https://actions.globus.org/transfer/transfer \
    --body transfer_input.json
```

The first printed line will display the `ACTION_ID`. You can monitor
progress with

``` sl
globus-automate action status --action-url \
    https://actions.globus.org/transfer/transfer ACTION_ID
```

or on the web at <https://app.globus.org/activity>.