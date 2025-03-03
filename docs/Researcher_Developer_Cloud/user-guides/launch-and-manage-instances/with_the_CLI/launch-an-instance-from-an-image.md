---
hidden: false
label_names:
- instance
- launch
- cli
- image
position: 2
title: Launch an Instance from an Image
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read 
    [Setting up your CLI environment](../../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

    We highly recommend that you supply the parameter `--key-name` to allow connections with your SSH key

After you gather required parameters, run the following command to launch an instance. Specify the server `name`, `flavor ID`, and `image ID`.

```
openstack server create --flavor FLAVOR_ID --image IMAGE_ID --key-name KEY_NAME --security-group SEC_GROUP_ID --network NETWORK_ID INSTANCE_NAME
```

Example with the values supplied

```
openstack server create --flavor e3a1ec6d-9513-4b9f-9580-671c4eee1c21 --image a5c9b7b2-e77b-4094-99ac-db0cf5181da5 --key-name test-key-pair --security-group 7200b28f-9089-4797-a094-39f1995e6f0c --network d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 test-instance-wiki
```

``` { .sh .no-copy }
+-----------------------------+-----------------------------------------------------------+
| Field                       | Value                                                     |
+-----------------------------+-----------------------------------------------------------+
| OS-DCF:diskConfig           | MANUAL                                                    |
| OS-EXT-AZ:availability_zone |                                                           |
| OS-EXT-STS:power_state      | NOSTATE                                                   |
| OS-EXT-STS:task_state       | scheduling                                                |
| OS-EXT-STS:vm_state         | building                                                  |
| OS-SRV-USG:launched_at      | None                                                      |
| OS-SRV-USG:terminated_at    | None                                                      |
| accessIPv4                  |                                                           |
| accessIPv6                  |                                                           |
| addresses                   |                                                           |
| adminPass                   | <PASSWORD HERE>                                           |
| config_drive                |                                                           |
| created                     | 2023-07-26T22:51:53Z                                      |
| flavor                      | devtest1.2cpu2ram (e3a1ec6d-9513-4b9f-9580-671c4eee1c21)  |
| hostId                      |                                                           |
| id                          | 8b08a4fb-7372-4269-a583-9dbc91779ffe                      |
| image                       | Ubuntu-Jammy-22.04 (a5c9b7b2-e77b-4094-99ac-db0cf5181da5) |
| key_name                    | test-key-pair                                             |
| name                        | test-instance-wiki                                        |
| progress                    | 0                                                         |
| project_id                  | 4f07cc254d6c4471805d49bae1f739b9                          |
| properties                  |                                                           |
| security_groups             | name='7200b28f-9089-4797-a094-39f1995e6f0c'               |
| status                      | BUILD                                                     |
| updated                     | 2023-07-26T22:51:53Z                                      |
| user_id                     | fb9a3d02c89e4cfdbe64658ad43ece97                          |
| volumes_attached            |                                                           |
+-----------------------------+-----------------------------------------------------------+
```

A status of `BUILD` indicates that the instance has started, but is not yet online.

A status of `ACTIVE` indicates that the instance is active.

Copy the server ID value from the `id` field in the output. Use the ID to get server details or to delete your server.

Check if the instance is online

```
openstack server list
```

The list shows the ID, name, status, and private (and if assigned, public) IP addresses for all instances in the project to which you belong:

``` { .sh .no-copy }
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
| ID                                   | Name                                  | Status | Networks                                     | Image                    | Flavor             |
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
| 8b08a4fb-7372-4269-a583-9dbc91779ffe | test-instance-wiki                    | ACTIVE | NeSI-Training-Test=10.1.0.134                | Ubuntu-Jammy-22.04       | devtest1.2cpu2ram  |
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
```

If the status for the instance is `ACTIVE`, the instance is online.

If you would like to access your Compute instance outside the FlexiHPC platform you will need to associate a `floating ip` to your instance. Reading [Manage Floating IPs via CLI](../../create-and-manage-networks/with_the_CLI/manage-floating-ips-via-cli.md), You should then be able to connect to your instance using ssh which is explained more in [Connect to your instance by using SSH](../connect-to-instance-ssh.md).
