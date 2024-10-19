---
hidden: false
label_names:
- instance
- resize
position: 2
title: Resizing an Instance via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

When resizing an instance via the CLI there are few details you will need, the `Instance ID` for the compute instance you want to resize and the `Flavor ID` you want to resize the instance to.

Run the following command to return a list of servers within your project space

```
openstack server list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------------+-----------+---------------------------------------------------------------------------+--------------------------+-----------------------+
| ID                                   | Name                     | Status    | Networks                                                                  | Image                    | Flavor                |
+--------------------------------------+--------------------------+-----------+---------------------------------------------------------------------------+--------------------------+-----------------------+
| 6a91e5a1-cf20-4fc5-9b7c-edc2bf1b8de4 | kahu-disk-test           | ACTIVE    | NeSI-Internal-Sandbox=10.1.0.147, 163.7.177.51                            | N/A (booted from volume) | balanced1.4cpu8ram    |
+--------------------------------------+--------------------------+-----------+---------------------------------------------------------------------------+--------------------------+-----------------------+
```

Taking note of the `Instance ID`

!!! note
    For this example we will use `6a91e5a1-cf20-4fc5-9b7c-edc2bf1b8de4`

Then run the following command to return a list of flavors

```
openstack flavor list
```

``` { .sh .no-copy }
+--------------------------------------+-------------------------+--------+------+-----------+-------+-----------+
| ID                                   | Name                    |    RAM | Disk | Ephemeral | VCPUs | Is Public |
+--------------------------------------+-------------------------+--------+------+-----------+-------+-----------+
| 1281555c-6bcb-42e4-a48e-98352dcd0fd0 | compute1.2cpu4ram       |   4096 |   30 |         0 |     2 | True      |
| 14505c86-765f-4971-a36f-1e867216dccf | memory1.4cpu16ram       |  16384 |   30 |         0 |     4 | True      |
| 1dbac08-d9a9-4c27-8534-57293785433e  | balanced1.32cpu64ram    |  65536 |   30 |         0 |    32 | True      |
| 2d02e6a4-3937-4ed3-951a-8e27867ff53e | balanced1.8cpu16ram     |  16384 |   30 |         0 |     8 | True      |
| 2e7b7cc7-9e29-4ff2-98dd-03dbb99dbb5c | compute1.16cpu32ram     |  32768 |   30 |         0 |    16 | True      |
| 3276cd5f-c96a-4e05-960f-f4f197142c98 | memory1.1cpu4ram        |   4096 |   30 |         0 |     1 | True      |
| 3b5a6e01-d3ad-49e3-a4f8-183c04444330 | balanced1.1cpu2ram      |   2048 |   30 |         0 |     1 | True      |
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
| d6e3a25a-4f9e-4c87-9342-77f807ead537 | memory1.8cpu32ram       |  32768 |   30 |         0 |     8 | True      |
| e07cfee1-43af-4bf6-baac-3bdf7c1b88f8 | balanced1.4cpu8ram      |   8192 |   30 |         0 |     4 | True      |
| e3a1ec6d-9513-4b9f-9580-671c4eee1c21 | devtest1.2cpu2ram       |   2048 |   30 |         0 |     2 | True      |
| ee55c523-9803-4296-91be-1c34e986baaa | devtest1.1cpu1ram       |   1024 |   30 |         0 |     1 | True      |
+--------------------------------------+-------------------------+--------+------+-----------+-------+-----------+
```

Take note of the `Flavor ID`

!!! note
    For this example we will resize to balanced1.2cpu4ram with an id of `6b2e76a8-cce0-4175-8160-76e2525d3d3d`

Taking the Instance ID and Flavor ID we will add those to the following command

```
openstack server resize --flavor <FLAVOUR_ID> <INSTANCE_ID>
```

Using our example values the command will look like this

```
openstack server resize --flavor 6b2e76a8-cce0-4175-8160-76e2525d3d3d 6a91e5a1-cf20-4fc5-9b7c-edc2bf1b8de4
```

You will not get a response from the endpoint on success

So you will want to run the following command to see when its in the state of `verify_resize`

```
openstack server show <INSTANCE_ID>
```

This will return the server details and there will be the status

``` { .sh .no-copy }
| status                              | VERIFY_RESIZE
```

You will then need to run the command below to verify the resize

```
openstack server resize confirm <INSTANCE_ID>
```

Using the example values the command will be the following

```
openstack server resize confirm 6a91e5a1-cf20-4fc5-9b7c-edc2bf1b8de4
```

Again there wont be a response from the endpoint so we will call the command `openstack server show` again to confirm the status of the instance

```
openstack server show <INSTANCE_ID>
```

The status of the instance should now be `ACTIVE`

``` { .sh .no-copy }
| status                              | ACTIVE
```

You should also see the new `flavor` that the instance has been resized too

``` { .sh .no-copy }
| flavor                              | balanced1.2cpu4ram (balanced1.2cpu4ram)
```