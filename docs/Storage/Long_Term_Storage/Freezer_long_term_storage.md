---
created_at: 2025-04-04
description: "Our Freezer service allows you to store your data on tape for long term storage."
tags: 
  - Freezer
  - storage
---

Freezer, powered by Versity, is our completely redesigned long-term storage service to support research data. It consists of a staging area (disk) connected to a tape library. Users gain access to more persistent storage space for their research data, in return for slower access to those files that are stored on tape. We recommend that you use Freezer for larger datasets that you will only need to access occasionally and will not need to change in situ. The retrieval of data may be delayed, due to tape handling, queuing of the freezer backend service and size of the data to be ingested or retrieved.

Due to the tape storage backend, Freezer is intended for use with relatively large files and should not be used for a large number of small files. Freezer is compatible with the common Amazon Web Services Simple Storage Service (AWS S3) cloud protocol and existing tools such as those used for accessing AWS S3 service.

## Getting started

Before getting started, you will need an allocation and credentials. To apply for an allocation go to [MyNeSI](https://my.nesi.org.nz/).
Once onboarded, you can start to use Freezer. Currently Freezer is only available via specific access points, HPC3 and Mahuika. We are currently completing security hardening prior to opening Freezer to wider access.

### Interacting with Freezer

We recommend using `s3cmd` for interacting with Freezer. The `s3cmd` tool is available by default on HPC3 and Mahuika. It is not necessary to load any modules to use it.
