---
created_at: '2023-01-12T02:42:17Z'
tags: []
title: Data transfer between NeSI and a PC without NeSI two-factor authentication
vote_count: 1
vote_sum: 1
zendesk_article_id: 6198499650703
zendesk_section_id: 360000040596
---

This article shows how to transfer potentially large amounts of data
between NeSI and your personal computer, without requiring 2FA
(two-factor authentication) each time you initiate the transfer.  This
is particularly useful in the context of automated, or [scripted data
transfers](../../Storage/Data_Transfer_Services/Syncing_files_between_NeSI_and_another_computer_with_globus_automate.md).

The approach is based on using
[Globus](../../Storage/Data_Transfer_Services/Data_Transfer_using_Globus_V5.md)
and a guest collection on the source side. **Globus** allows you to copy
and synchronise files between NeSI's platforms and other computers,
including your personal computer.

A ***collection*** is a directory whose content can be shared. A
***guest collection*** allows you to share data without having to type
in your credentials each time your transfer files.

See this [support
page](../../Storage/Data_Transfer_Services/Data_Transfer_using_Globus_V5.md)
on how to set up Globus. Here, we assume you have an account on NeSI and
have registered and created an account on Globus.

## Step 1: Create a guest collection on NeSI

- Go to <https://app.globus.org/file-manager>
- In the "Collection" search box type **NeSI Wellington DTN V5** and
    select this collection
- *You may then need to log onto NeSI DTN to see the files*
- Find the root folder of your guest collection, the directory you
    would like to share, and
    - click on the “Share” button,
    - click on “Add Guest Collection”
    - provide a "Display Name"
    - press on "Create Collection"
- You should now see your new guest collection at
    <https://app.globus.org/collections?scope=administered-by-me>

![mceclip0.png](../../assets/images/Data_transfer_between_NeSI_and_a_PC_without_NeSI_two_factor_authentication.png)

## Step 2: Download and install Globus Connect Personal

On your personal computer, download "Globus Connect Personal" from
<https://app.globus.org/file-manager/gcp>. Versions exist for Mac,
Windows and Linux. Follow the instructions to install and set up the
software. Also see our support page about [Personal Globus Endpoint
Configuration](../../Storage/Data_Transfer_Services/Personal_Globus_Endpoint_Configuration.md).

## Step 3: Share a directory on your personal computer

- Launch "Globus Connect Personal" and go to "Preferences".
- Select "Access"
    - click on the "+" sign to share a new directory
    - navigate your directory and press "Open"
    - make the directory writable

Note: By default your entire home directory will be exposed. It is good
practice to only share specific directories. You can remove your home
directory by highlighting it and clicking on the "-" sign.

![mceclip1.png](../../assets/images/Data_transfer_between_NeSI_and_a_PC_without_NeSI_two_factor_authentication_0.png)

## Step 4: Test a file transfer

- Go to [https://app.globus.org](https://app.globus.org/collections)
- Log in
- In the "FILE MANAGER" tab, type the source and destination
    collections. The source path should be relative to the guest
    collection root. However, the destination path is absolute, as can
    be seen in the picture below.
- Click on the files you want to transfer and press "Start"

![mceclip3.png](../../assets/images/Data_transfer_between_NeSI_and_a_PC_without_NeSI_two_factor_authentication_1.png)
