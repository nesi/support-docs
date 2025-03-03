---
hidden: false
label_names:
- Object Storage
- create
- manage
position: 1
title: Create and Manage Object Storage
vote_count: 1
vote_sum: 1
---

Object Storage within FlexiHPC is a file system storage that is primarily used for storing static data. Unlike other storage systems, object storage is independent of virtual machines and operating system type.

You are able to upload and download files from anywhere with network access using a few methods.

The general use case for object storage is storing data that you upload once and read or download many times. Its not the best for files that are being modified consistently.

There are a few ways to create and mange object storage within FlexiHPC

- [Creating and Managing object storage via the Dashboard](with_the_dashboard/create-and-manage-object-storage-with-the-dashboard.md)

- [Creating and Managing object storage via CLI](with_the_CLI/create-and-manage-object-storage-via-cli.md)

If you are looking to interact with the s3 Protocol then you need to also generate yourself some EC2 credentials

- [Creating and Managing EC2 credentials](creating-and-managing-ec2-credentials-via-cli.md)

Interacting with the FlexiHPC Object storage can be done a few ways outside of the dashboard.

- [Interacting with the S3 protocol with Boto3](using-boto3-to-interact-with-object-storage.md)

- [Using FlexiHPC object storage for Terraform state file](../launch-and-manage-instances/other_tools/deployment-of-an-instance-with-terraform.md#using-flexihpc-object-storage-to-store-the-terraform-state-file)

- [Accessing object storage with Cyberduck](using-cyberduck-to-interact-with-object-storage.md)
