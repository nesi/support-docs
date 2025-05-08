---
hidden: false
label_names:
- identity
- create
- manage
- cli
title: Creating and Managing EC2 Credentials via CLI
---

## Overview

For using the OpenStack S3 API:s you need to generate an additional set of credentials. These can then be used to store data in the Swift Object store for applications that don’t have native Swift support but do support the S3 interfaces.

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

## Create and fetch credentials using the CLI

Running the below command will generate EC2 credentials

``` { .sh }
openstack ec2 credentials create
```

With the following ouput

``` { .sh .no-copy }
+------------+----------------------------------------------------------------------------------------------------------------+
| Field      | Value                                                                                                          |
+------------+----------------------------------------------------------------------------------------------------------------+
| access     | <USER_ACCESS_TOKEN>                                                                                            |
| links      | {'self': 'https://keystone.akl-1.cloud.nesi.org.nz/v3/users/<USER_ID>/credentials/OS-EC2/<USER_ACCESS_TOKEN>'} |
| project_id | <PROJECT_ID>                                                                                                   |
| secret     | <USERS_SECRET_TOKEN>                                                                                           |
| trust_id   | None                                                                                                           |
| user_id    | <USER_ID>                                                                                                      |
+------------+----------------------------------------------------------------------------------------------------------------+
```

Note the `access` field and the `secret` field. These are the 2 fields required to interact with the s3 protocol.

The below command will fetch all EC2 credentails associated with the user

``` { .sh }
openstack ec2 credentials list
```

``` { .sh .no-copy }
+---------------------+----------------------+--------------+-----------+
| Access              | Secret               | Project ID   | User ID   |
+---------------------+----------------------+--------------+-----------+
| <USER_ACCESS_TOKEN> | <USERS_SECRET_TOKEN> | <PROJECT_ID> | <USER_ID> |
+---------------------+----------------------+--------------+-----------+
```

## Delete credentials using the CLI

Use the access key to refer to the credentials you wish to delete:

``` { .sh }
openstack ec2 credentials delete USER_ACCESS_TOKEN
```
