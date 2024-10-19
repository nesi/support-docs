---
hidden: false
label_names:
- instance
- resize
position: 2
title: Manage Security Groups of an Instance via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

When adding or removing `Security Groups` from an instance via the CLI there are few details you will need, the `Instance ID` for the compute instance you want to adjust and the `Security Group ID` you want to add or remove from the instance.

Run the following command to return a list of servers within your project space

```
openstack server list
```

``` { .sh .no-copy }
+--------------------------------------+-----------+--------+-------------------------------+-------------------------------+--------------------+
| ID                                   | Name      | Status | Networks                      | Image                         | Flavor             |
+--------------------------------------+-----------+--------+-------------------------------+-------------------------------+--------------------+
| 4f69a45d-78ad-48e7-b427-5694c8b09e45 | kahu-test | ACTIVE | NeSI-Training-Prod=10.1.0.250 | NeSI-FlexiHPC-Rocky-9.3_cloud | balanced1.2cpu4ram |
+--------------------------------------+-----------+--------+-------------------------------+-------------------------------+--------------------+

```

Taking note of the `Instance ID`

!!! note
    For this example we will use `4f69a45d-78ad-48e7-b427-5694c8b09e45`

Then run the following command to return a list of Security Groups

```
openstack security group list
```

``` { .sh .no-copy }
+--------------------------------------+----------------+------------------------+----------------------------------+------+
| ID                                   | Name           | Description            | Project                          | Tags |
+--------------------------------------+----------------+------------------------+----------------------------------+------+
| 050e0ec4-1416-46f2-98a0-b492f2c8d81b | ssh-allow-all  |                        | 1b899a2883da444fa6b31172dcebbc56 | []   |
| 08749b3c-f8aa-443e-a881-80f6009fff59 | http           |                        | 1b899a2883da444fa6b31172dcebbc56 | []   |
| 0ed77965-05bf-438e-b4e4-89060f814c4c | SSH Allow All  |                        | 1b899a2883da444fa6b31172dcebbc56 | []   |
| b713d80c-1b7d-4991-b387-514261e59b94 | 6443_Allow_ALL |                        | 1b899a2883da444fa6b31172dcebbc56 | []   |
| cdad3d6b-a726-4020-a6a3-7c20b1afc79f | https          |                        | 1b899a2883da444fa6b31172dcebbc56 | []   |
| e73a47e9-cc3a-4986-95f9-c3d101c3d448 | default        | Default security group | 1b899a2883da444fa6b31172dcebbc56 | []   |
+--------------------------------------+----------------+------------------------+----------------------------------+------+
```

Take note of the `ID`

!!! note
    For this example we will use the id `050e0ec4-1416-46f2-98a0-b492f2c8d81b` to add `ssh-allow-all` to our instance

## Adding a Security Group to an Instance

Taking the Instance ID and Security Group ID we will add those to the following command

```
openstack server add security group <INSTANCE_ID> <SECURITY_GROUP_ID>
```

Using our example values the command will look like this

```
openstack server add security group 4f69a45d-78ad-48e7-b427-5694c8b09e45 050e0ec4-1416-46f2-98a0-b492f2c8d81b
```

You will not get a response from the endpoint on success

So you will want to run the following command to see if the Security Group was added

```
openstack server show <INSTANCE_ID>
```

This will return the server details and there will be the security_groups field with the newly added group

``` { .sh .no-copy }
| security_groups                     | name='ssh-allow-all'                                          |
|                                     | name='default'                                                |
```

## Removing a Security Group to an Instance

Taking the Instance ID and Security Group ID we will add those to the following command

```
openstack server remove security group <INSTANCE_ID> <SECURITY_GROUP_ID>
```

Using our example values the command will look like this

```
openstack server remove security group 4f69a45d-78ad-48e7-b427-5694c8b09e45 050e0ec4-1416-46f2-98a0-b492f2c8d81b
```

You will not get a response from the endpoint on success

So you will want to run the following command to see if the Security Group was removed

```
openstack server show <INSTANCE_ID>
```

This will return the server details and there will be the security_groups field with the removed group not present

``` { .sh .no-copy }
| security_groups                     | name='ssh-allow-all'                                          |
```