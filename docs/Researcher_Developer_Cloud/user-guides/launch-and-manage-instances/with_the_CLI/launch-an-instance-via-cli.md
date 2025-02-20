---
hidden: false
label_names:
- instance
- launch
- cli
position: 2
title: Launch an Instance via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

Before you can launch an instance via the CLI, gather the following parameters:

- The `instance source` can be an image, snapshot, or block storage volume that contains an image or snapshot.

- A `name` for your instance.

- The `flavor` for your instance, which defines the compute, memory, and storage capacity of nova computing instances. A flavor is an available hardware configuration for a server. It defines the size of a virtual server that can be launched.

- Access and security credentials, which include one or both of the following credentials:

    - A `key pair` for your instance, which are SSH credentials that are injected into images when they are launched. Create at least one key pair for each project. If you already have generated a key pair with an external tool, you can import it into OpenStack. You can use the key pair for multiple instances that belong to that project. Read [Create and Manage Key Pairs](../../create-and-manage-keypairs/index.md) if you would like to know more.

    - A `security group` that defines which incoming network traffic is forwarded to instances. Security groups hold a set of firewall policies, known as security group rules.

- The `network` to attach the instance too.

- If needed, you can assign a **floating (public) IP address** to a running instance to make it accessible from outside the cloud.

- You can also attach a block storage device, or **volume**, for persistent storage.

!!! note
    Instances that use the default security group cannot, by default, be accessed from any IP address outside of the cloud. If you want those IP addresses to access the instances, you must modify the rules for the security group. Read How to add/update and remove security groups for more information.

After you gather the parameters that you need to launch an instance, you can launch it from an image or a volume.

## Gather parameters to launch an instance

List the available flavors.

``` { .sh .copy }
openstack flavor list
```

Note the ID of the flavor that you want to use for your instance:

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

List the available images.

```
openstack image list
```

Note the ID of the image from which you want to boot your instance:

``` { .sh .no-copy }
+--------------------------------------+----------------------------------------------------------+--------+
| ID                                   | Name                                                     | Status |
+--------------------------------------+----------------------------------------------------------+--------+
| 701e29ac-8963-4cf9-b90a-e1b14095866d | CentOS-Stream-8                                          | active |
| 42ebfb1b-f136-4947-ae1a-025ad57b369c | CentOS-stream8-baremetal                                 | active |
| f94a4d02-661f-4df7-bb50-ad08ad89f816 | Centos-8.4-AGR                                           | active |
| 386c661a-4c30-4f09-b536-511a862102b4 | FedoraCoreOS35                                           | active |
| fe8c98d3-7a87-4b5b-9f9e-0f967c53f9bd | FedoraCoreOS37                                           | active |
| 622c4f3f-8e62-4c81-8809-69b0a34a28e0 | PostgreSQL-Ubuntu-20.04.4                                | active |
| 3936d736-e5bb-4024-a361-512fd40413bc | RockyLinux-8.5                                           | active |
| eb40dbb5-7da6-4784-b47c-f417c9d3b126 | RockyLinux-8.6                                           | active |
| 2b00f364-1bd0-432c-91f9-8d1adda6fc9f | RockyLinux-8.6-OFED-5.7                                  | active |
| f366dd3a-5353-47dd-9e92-662055125174 | RockyLinux-8.7                                           | active |
| b443a9a2-32d1-48c1-8d84-bcc10adbb0c3 | RockyLinux-8.7-OFED-5.8                                  | active |
| 9933eb25-b0c1-4ef2-b199-25e916c79906 | Ubuntu-20-AGR                                            | active |
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
| 04e1a31a-adee-4af2-935e-0e6e7c4b3193 | test-break                                               | active |
+--------------------------------------+----------------------------------------------------------+--------+
```

List the available security groups.

```
openstack security group list
```

Note the ID of the security group you want to attach to the instance:

``` { .sh .no-copy }
+--------------------------------------+----------------------------------------------------------------+---------------------------------------------------------+----------------------------------+------+
| ID                                   | Name                                                           | Description                                             | Project                          | Tags |
+--------------------------------------+----------------------------------------------------------------+---------------------------------------------------------+----------------------------------+------+
| 7200b28f-9089-4797-a094-39f1995e6f0c | SSH Allow All                                                  | This is an open SSH that allows anyone to connect to 22 | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| b24e8bef-969a-4938-8b18-0a33769b181d | kubeapi_whitelist                                              |                                                         | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| b5d30ed4-13b3-4f7a-bc5a-c48175566ea3 | My-Security-Group                                              | This is my security group                               | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| f2f15d6f-2a04-4196-8102-a058042694b3 | default                                                        | Default security group                                  | 4f07cc254d6c4471805d49bae1f739b9 | []   |
+--------------------------------------+----------------------------------------------------------------+---------------------------------------------------------+----------------------------------+------+
```

If you have not created any security groups, you can read How to add/update and remove security groups

You can view rules for a specified security group:

```
openstack security group rule list b5d30ed4-13b3-4f7a-bc5a-c48175566ea3
```

List the available key pairs, and note the key pair name that you use for SSH access.

```
openstack keypair list
```

List the available networks.

```
openstack network list
```

Note the ID for the network

``` { .sh .no-copy }
+--------------------------------------+--------------------------------+--------------------------------------+
| ID                                   | Name                           | Subnets                              |
+--------------------------------------+--------------------------------+--------------------------------------+
| 33d0c11b-b659-4b77-9afc-5676fe965839 | external                       | 5c2644ad-7253-42f5-ad69-40970b84dea6 |
| d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | NeSI-Training-Test             | f5715775-270c-4230-bfa7-fdbdf51352dc |
+--------------------------------------+--------------------------------+--------------------------------------+
```

!!! note
    The recommend Network ID to take note of is the network that has the same name as your project. If external access is required then after creating the compute instance a floating ip is the recommend way to gain this external access.

## Launch an instance

You can launch an instance from various sources.

- [Launch an instance from an image](launch-an-instance-from-an-image.md)

- [Launch an instance from a volume](launch-an-instance-from-a-volume.md)
