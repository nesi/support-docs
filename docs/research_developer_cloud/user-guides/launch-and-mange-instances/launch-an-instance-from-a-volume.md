---
hidden: false
label_names:
- instance
- launch
- cli
- volume
position: 2
title: Launch an Instance from a volume
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

You can create a volume from an existing image, volume, or snapshot. This procedure shows you how to create a volume from an image, and use the volume to boot an instance.

List the available images.

```
openstack image list
```

``` { .sh .no-copy }
+--------------------------------------+----------------------------------------------------------+--------+
| ID                                   | Name                                                     | Status |
+--------------------------------------+----------------------------------------------------------+--------+
| 701e29ac-8963-4cf9-b90a-e1b14095866d | CentOS-Stream-8                                          | active |
| 42ebfb1b-f136-4947-ae1a-025ad57b369c | CentOS-stream8-baremetal                                 | active |
| 386c661a-4c30-4f09-b536-511a862102b4 | FedoraCoreOS35                                           | active |
| fe8c98d3-7a87-4b5b-9f9e-0f967c53f9bd | FedoraCoreOS37                                           | active |
| 622c4f3f-8e62-4c81-8809-69b0a34a28e0 | PostgreSQL-Ubuntu-20.04.4                                | active |
| 3936d736-e5bb-4024-a361-512fd40413bc | RockyLinux-8.5                                           | active |
| eb40dbb5-7da6-4784-b47c-f417c9d3b126 | RockyLinux-8.6                                           | active |
| 2b00f364-1bd0-432c-91f9-8d1adda6fc9f | RockyLinux-8.6-OFED-5.7                                  | active |
| f366dd3a-5353-47dd-9e92-662055125174 | RockyLinux-8.7                                           | active |
| b443a9a2-32d1-48c1-8d84-bcc10adbb0c3 | RockyLinux-8.7-OFED-5.8                                  | active |
| 1276db65-e5de-4721-b2db-666a73929b3e | Ubuntu-22.10-Wiki-Test                                   | active |
| ab67f1b1-44f9-4465-9a68-82cc35ed69c0 | Ubuntu-Bionic-18.04                                      | active |
| d73ef17b-6b0a-4148-b3b2-f4edcf2e480e | Ubuntu-Focal-20.04                                       | active |
| ce869c9d-35bb-46be-9b6d-d74d4035e2f8 | Ubuntu-Focal-20.04-baremetal                             | active |
| 885d01da-777b-4e67-a1ec-e114e4c2786e | Ubuntu-Focal-20.04-mark-testing-dib-2022-06-30T12:47:00Z | active |
| a5c9b7b2-e77b-4094-99ac-db0cf5181da5 | Ubuntu-Jammy-22.04                                       | active |
| 05f13645-2ac7-44ce-aa1c-64f31ca42761 | Ubuntu-Jammy-22.04-DEMOCREDS                             | active |
| c7e208cb-6521-422b-8d00-1b8f003c4646 | Ubuntu20.04                                              | active |
| 728719c2-0a75-4411-a8fa-3230fa5d50e5 | Ubuntu22.04                                              | active |
| a13f3659-eed9-411c-9a33-f1584fd00328 | Windows-Server-2012-R2-Eval                              | active |
| 8814f28f-1dbd-4253-84e8-8e45032855c6 | Windows-Server-2019                                      | active |
| 15f3eebe-4c15-4565-a4f8-7369f072b50d | cirros-0.4                                               | active |
| 534b8b78-f455-4f85-bd21-13c2b1b14e3e | cirros-0.5                                               | active |
| 64dead14-9c5a-41c3-b4d6-a122a2ca8f28 | linux-test-snapshot                                      | active |
| d479470d-ab6d-40d6-afc9-04f5f253404d | linux-test-to-boot-2                                     | active |
| 40ed5c78-c970-4182-a9c8-27e18a6a4251 | linux-test-to-boot-cli                                   | active |
| 5a8e5595-d893-4d1c-8600-d7982f3915bb | ood-keycloak-1                                           | active |
| 04e1a31a-adee-4af2-935e-0e6e7c4b3193 | test-break                                               | active |
| 1a0480d1-55c8-4fd7-8c7a-8c26e52d8cbd | ubuntu-jammy-server-cloudimg                             | active |
+--------------------------------------+----------------------------------------------------------+--------+
```

Note the ID of the image that you want to use to create a volume.

!!! note
    We will use the Ubuntu-Jammy-22.04 image with the ID `a5c9b7b2-e77b-4094-99ac-db0cf5181da5`

We also need to list the available flavors.

```
openstack flavor list
```

``` { .sh .no-copy }
+--------------------------------------+-------------------------+--------+------+-----------+-------+-----------+
| ID                                   | Name                    |    RAM | Disk | Ephemeral | VCPUs | Is Public |
+--------------------------------------+-------------------------+--------+------+-----------+-------+-----------+
| 0f71f1e2-d327-41f9-87e3-0f6c29f51af1 | gb.bm.gpu               | 524288 |  240 |         0 |    48 | True      |
| 1281555c-6bcb-42e4-a48e-98352dcd0fd0 | compute1.2cpu4ram       |   4096 |   30 |         0 |     2 | True      |
| 14505c86-765f-4971-a36f-1e867216dccf | memory1.4cpu16ram       |  16384 |   30 |         0 |     4 | True      |
| 1dbac08-d9a9-4c27-8534-57293785433e  | balanced1.32cpu64ram    |  65536 |   30 |         0 |    32 | True      |
| 2d02e6a4-3937-4ed3-951a-8e27867ff53e | balanced1.8cpu16ram     |  16384 |   30 |         0 |     8 | True      |
| 2e7b7cc7-9e29-4ff2-98dd-03dbb99dbb5c | compute1.16cpu32ram     |  32768 |   30 |         0 |    16 | True      |
| 3276cd5f-c96a-4e05-960f-f4f197142c98 | memory1.1cpu4ram        |   4096 |   30 |         0 |     1 | True      |
| 3b5a6e01-d3ad-49e3-a4f8-183c04444330 | balanced1.1cpu2ram      |   2048 |   30 |         0 |     1 | True      |
| 4a0425c8-7494-473e-a5bb-acc91c378615 | c1.cpu128.ram448.disk30 | 458752 |   30 |         0 |   128 | True      |
| 4e8af724-f66d-4072-a692-114126de25a0 | compute1.1cpu2ram       |   2048 |   30 |         0 |     1 | True      |
| 4ec785be-a422-4207-9daa-cbb71c61f9ed | devtest1.4cpu4ram       |   4096 |   30 |         0 |     4 | True      |
| 674fa81a-69c7-4bf7-b3a9-59989fb63618 | balanced1.16cpu32ram    |  32768 |   30 |         0 |    16 | True      |
| 6b2e76a8-cce0-4175-8160-76e2525d3d3d | balanced1.2cpu4ram      |   4096 |   30 |         0 |     2 | True      |
| 7af5c672-43e7-4296-9608-5974394851b8 | memory1.2cpu8ram        |   8192 |   30 |         0 |     2 | True      |
| 7ffa092c-e75a-4cb5-be9f-db8c749e8801 | compute1.4cpu8ram       |   8192 |   30 |         0 |     4 | True      |
| 8aef7f54-1ed6-4275-a38c-3f1e61afabd9 | memory1.16cpu64ram      |  65536 |   30 |         0 |    16 | True      |
| 94ba9177-cb98-4b04-870c-9a696e1c5327 | memory1.32cpu128ram     | 131072 |   30 |         0 |    32 | True      |
| 9d536959-dd7a-4532-b0b7-db8bb8a72ddb | compute1.8cpu16ram      |  16384 |   30 |         0 |     8 | True      |
| b46e184c-0dcb-44b2-a53f-c2b8eff676c9 | compute1.32cpu64ram     |  65536 |   30 |         0 |    32 | True      |
| d6c2e93a-d430-44ca-822b-79a4b882c0c3 | piotr-gpu               | 131072 |  100 |         0 |     8 | True      |
| d6e3a25a-4f9e-4c87-9342-77f807ead537 | memory1.8cpu32ram       |  32768 |   30 |         0 |     8 | True      |
| e07cfee1-43af-4bf6-baac-3bdf7c1b88f8 | balanced1.4cpu8ram      |   8192 |   30 |         0 |     4 | True      |
| e3a1ec6d-9513-4b9f-9580-671c4eee1c21 | devtest1.2cpu2ram       |   2048 |   30 |         0 |     2 | True      |
| ee55c523-9803-4296-91be-1c34e986baaa | devtest1.1cpu1ram       |   1024 |   30 |         0 |     1 | True      |
+--------------------------------------+-------------------------+--------+------+-----------+-------+-----------+
```

Note the ID of the flavor that you want to use

!!! note
    We will use the `balanced1.1cpu2ram` flavor with an ID `3b5a6e01-d3ad-49e3-a4f8-183c04444330`

Get a list of networks

```
openstack network list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------------------+--------------------------------------+
| ID                                   | Name                           | Subnets                              |
+--------------------------------------+--------------------------------+--------------------------------------+
| 33d0c11b-b659-4b77-9afc-5676fe965839 | external                       | 5c2644ad-7253-42f5-ad69-40970b84dea6 |
| d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | NeSI-Training-Test             | f5715775-270c-4230-bfa7-fdbdf51352dc |
+--------------------------------------+--------------------------------+--------------------------------------+
```

Note the ID for the network that is not the external one and is named the same as your project space.

!!! note
    For this example we will use NeSI-Training-Test with an ID `d3a7ddb5-6582-42cf-978a-c99b4ed25ad4`

With we above values we then have 2 choices to booting an instance from a volume

- Create and boot from volume in a single step
> This option doesn't give us control over the volume creation process and only allows us to specify a size for our new volume

- Creating the volume first and boot from it
> This allows us to specify more then the size on creation, example is we might want to encrypt it

## Create and boot from volume in a single step

We will then create an instance from that image using the `--boot-from-volume` parameter

!!! note
    We highly recommend that you supply the parameter `--key-name` to allow connections with your SSH key

The command will look like the following

```
openstack server create --flavor <FLAVOR_ID> --network <NETWORK_ID> --image <IMAGE_ID> --boot-from-volume <VOULME_SIZE> --key-name <KEY_PAIR_NAME> --wait <INSTANCE_NAME>
```

Using or example values the command looks like the following

```
openstack server create --flavor 3b5a6e01-d3ad-49e3-a4f8-183c04444330 --network d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 --image a5c9b7b2-e77b-4094-99ac-db0cf5181da5 --boot-from-volume 80 --key-name kahus-key --wait Ubuntu_boot_volume
```

``` { .sh .no-copy }
+-----------------------------+----------------------------------------------------------+
| Field                       | Value                                                    |
+-----------------------------+----------------------------------------------------------+
| accessIPv4                  |                                                          |
| accessIPv6                  |                                                          |
| addresses                   | NeSI-Training-Test=10.1.0.57                             |
| adminPass                   | rCs2E9BP2RZu                                             |
| config_drive                | True                                                     |
| created                     | 2023-09-03T22:06:56Z                                     |
| flavor                      | memory1.4cpu16ram (14505c86-765f-4971-a36f-1e867216dccf) |
| hostId                      | c79c5b9fc6c64341b07c0408e401a28ad0b20aa123a250f77fd8c249 |
| id                          | ddc5d676-db4e-4fd3-b0c9-14b91a1f16d5                     |
| image                       | N/A (booted from volume)                                 |
| key_name                    | kahus-key                                                |
| name                        | Ubuntu_boot_volume                                       |
| progress                    | 0                                                        |
| project_id                  | 4f07cc254d6c4471805d49bae1f739b9                         |
| properties                  |                                                          |
| security_groups             | name='default'                                           |
| status                      | ACTIVE                                                   |
| updated                     | 2023-09-03T22:07:04Z                                     |
| user_id                     | fb9a3d02c89e4cfdbe64658ad43ece97                         |
| volumes_attached            | id='0aa677c7-072b-4241-a70a-05a4de020596'                |
+-----------------------------+----------------------------------------------------------+
```

!!! warning
    Should you not provide a key file to the deployment you will need to remake the instance as by default the Flexi environment doesn't set passwords.

    Ubuntu and CentOS cloud images also don't allow password SSH by default.

## Creating the volume first and boot from it

Should you wish to have more control over the volume creation process we will first create the volume then boot an instance from that.

Cinder makes a volume bootable when `--image` parameter is passed.

```
openstack volume create --image IMAGE_ID --size SIZE_IN_GB bootable_volume
```

We will use the `Ubuntu-Jammy-22.04` image with the ID `a5c9b7b2-e77b-4094-99ac-db0cf5181da5` the command will look like

```
openstack volume create --image a5c9b7b2-e77b-4094-99ac-db0cf5181da5 --size 80 my_ubuntu_volume
```

``` { .sh .no-copy }
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| attachments         | []                                   |
| availability_zone   | nova                                 |
| bootable            | false                                |
| consistencygroup_id | None                                 |
| created_at          | 2023-08-09T21:57:52.675096           |
| description         | None                                 |
| encrypted           | False                                |
| id                  | 3dd489d8-7c44-4c59-b4af-0c804ddf4729 |
| multiattach         | False                                |
| name                | my_ubuntu_volume                     |
| properties          |                                      |
| replication_status  | None                                 |
| size                | 30                                   |
| snapshot_id         | None                                 |
| source_volid        | None                                 |
| status              | creating                             |
| type                | ceph-ssd                             |
| updated_at          | None                                 |
| user_id             | fb9a3d02c89e4cfdbe64658ad43ece97     |
+---------------------+--------------------------------------+
```

Take note of the volume ID

The following command is used to boot an instance from a volume

```
openstack server create --flavor <FLAVOR_ID> --volume <VOLUME_ID> --network <NETWORK_ID> --key-name <KEY_PAIR_NAME> <Instance Name>
```

We will supply the `balanced1.1cpu2ram` ID for flavor and our volume ID of `3dd489d8-7c44-4c59-b4af-0c804ddf4729` from the volume we created before

```
openstack server create --flavor 3b5a6e01-d3ad-49e3-a4f8-183c04444330 --volume 3dd489d8-7c44-4c59-b4af-0c804ddf4729 --network d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 --key-name kahus-key Ubuntu_From_Volume
```

``` { .sh .no-copy }
+-----------------------------+-----------------------------------------------------------+
| Field                       | Value                                                     |
+-----------------------------+-----------------------------------------------------------+
| accessIPv4                  |                                                           |
| accessIPv6                  |                                                           |
| addresses                   |                                                           |
| adminPass                   | MPu74uppSp4r                                              |
| config_drive                |                                                           |
| created                     | 2023-08-09T22:05:30Z                                      |
| flavor                      | balanced1.1cpu2ram (3b5a6e01-d3ad-49e3-a4f8-183c04444330) |
| hostId                      |                                                           |
| id                          | 2d4db443-eb48-4d64-8770-5624568f29ad                      |
| image                       | N/A (booted from volume)                                  |
| key_name                    | kahus-key                                                 |
| name                        | Ubuntu_From_Volume                                        |
| progress                    | 0                                                         |
| project_id                  | 4f07cc254d6c4471805d49bae1f739b9                          |
| properties                  |                                                           |
| security_groups             | name='default'                                            |
| status                      | BUILD                                                     |
| updated                     | 2023-08-09T22:05:30Z                                      |
| user_id                     | fb9a3d02c89e4cfdbe64658ad43ece97                          |
| volumes_attached            |                                                           |
+-----------------------------+-----------------------------------------------------------+
```

!!! warning
    Should you not provide a key file to the deployment you will need to remake the instance as by default the Flexi environment doesn't set passwords.

    Ubuntu and CentOS cloud images also don't allow password SSH by default.

To allow external access a floating IP will need to be provided to the newly created instance, following [Manage Floating IPs via CLI](../create-and-manage-networks/manage-floating-ips-via-cli.md) will complete this for you, You should then be able to connect to your instance using ssh which is explained more in [Connect to your instance by using SSH](connect-to-instance-ssh.md).