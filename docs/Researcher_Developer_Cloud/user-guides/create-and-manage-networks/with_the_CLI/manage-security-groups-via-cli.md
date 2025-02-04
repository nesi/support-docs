---
label_names:
- security-groups
- launch
- cli
title: Manage Security groups via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. 
    Please read [Setting up your CLI environment](../../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

## Creating a Security Group

Run the following command to create a Security Group with a specified name and description.

```
openstack security group create --description FRIENDLY_DESCRIPTION NAME_FOR_GROUP
```

An example command to create a security group called `My_Wiki_SG`

```
openstack security group create --description "A testing group for wiki" My_Wiki_SG
```

We can check the security group is created by running

```
openstack security group list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------------+---------------------------------------------------------+----------------------------------+------+
| ID                                   | Name                     | Description                                             | Project                          | Tags |
+--------------------------------------+--------------------------+---------------------------------------------------------+----------------------------------+------+
| 339bd140-e6a0-4afd-9b24-029c3243e779 | My_Wiki_SG               | A testing group for wiki                                | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| 7200b28f-9089-4797-a094-39f1995e6f0c | SSH Allow All            | This is an open SSH that allows anyone to connect to 22 | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| b5d30ed4-13b3-4f7a-bc5a-c48175566ea3 | My-Security-Group        | This is my security group                               | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| f2f15d6f-2a04-4196-8102-a058042694b3 | default                  | Default security group                                  | 4f07cc254d6c4471805d49bae1f739b9 | []   |
+--------------------------------------+--------------------------+---------------------------------------------------------+----------------------------------+------+
```

## Create and manage Security Group rules

You can modify Security Group rules with the `openstack security group rule` command.

### Create new rules for a group

Allow access from all IP addresses (specified as IP subnet `0.0.0.0/0` in CIDR notation) for the port `8080`

```
openstack security group rule create --proto tcp --dst-port 8080 SECURITY_GROUP_ID
```

The command and response looks like the following

```
openstack security group rule create --proto tcp --dst-port 8080 339bd140-e6a0-4afd-9b24-029c3243e779
```

``` { .sh .no-copy }
+-------------------------+--------------------------------------+
| Field                   | Value                                |
+-------------------------+--------------------------------------+
| created_at              | 2023-08-10T00:59:36Z                 |
| description             |                                      |
| direction               | ingress                              |
| ether_type              | IPv4                                 |
| id                      | f0bce470-8d94-453f-9dfa-3e3e34b0c80e |
| name                    | None                                 |
| normalized_cidr         | 0.0.0.0/0                            |
| port_range_max          | 8080                                 |
| port_range_min          | 8080                                 |
| project_id              | 4f07cc254d6c4471805d49bae1f739b9     |
| protocol                | tcp                                  |
| remote_address_group_id | None                                 |
| remote_group_id         | None                                 |
| remote_ip_prefix        | 0.0.0.0/0                            |
| revision_number         | 0                                    |
| security_group_id       | 339bd140-e6a0-4afd-9b24-029c3243e779 |
| tags                    | []                                   |
| updated_at              | 2023-08-10T00:59:36Z                 |
+-------------------------+--------------------------------------+
```

If you check the rules again, you'll see the new one has been added

```
openstack security group rule list 339bd140-e6a0-4afd-9b24-029c3243e779
```

``` { .sh .no-copy }
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
| ID                                   | IP Protocol | Ethertype | IP Range  | Port Range | Direction | Remote Security Group | Remote Address Group |
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
| b0f0edd2-7a55-44b4-84a8-9650de36a7ec | None        | IPv6      | ::/0      |            | egress    | None                  | None                 |
| f0bce470-8d94-453f-9dfa-3e3e34b0c80e | tcp         | IPv4      | 0.0.0.0/0 | 8080:8080  | ingress   | None                  | None                 |
| f3925a01-5d47-4c55-ac73-1647cca5b739 | None        | IPv4      | 0.0.0.0/0 |            | egress    | None                  | None                 |
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
```

### Delete a Security Group rule

First, run the following command to view all Security Groups.

```
openstack security group list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------------+---------------------------------------------------------+----------------------------------+------+
| ID                                   | Name                     | Description                                             | Project                          | Tags |
+--------------------------------------+--------------------------+---------------------------------------------------------+----------------------------------+------+
| 339bd140-e6a0-4afd-9b24-029c3243e779 | My_Wiki_SG               | A testing group for wiki                                | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| 5150840c-9c27-45a9-91a1-61c5978de8ff | https                    |                                                         | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| 7200b28f-9089-4797-a094-39f1995e6f0c | SSH Allow All            | This is an open SSH that allows anyone to connect to 22 | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| 8873336a-02e6-4f84-8fd8-5aa3b929f955 | hpc-toolset-docker-ports | Docker Ports used for the HPC Toolset                   | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| b24e8bef-969a-4938-8b18-0a33769b181d | kubeapi_whitelist        |                                                         | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| b5d30ed4-13b3-4f7a-bc5a-c48175566ea3 | My-Security-Group        | This is my security group                               | 4f07cc254d6c4471805d49bae1f739b9 | []   |
| f2f15d6f-2a04-4196-8102-a058042694b3 | default                  | Default security group                                  | 4f07cc254d6c4471805d49bae1f739b9 | []   |
+--------------------------------------+--------------------------+---------------------------------------------------------+----------------------------------+------+
```

Locate the Security Group that you wish to remove a rule from and take note of its ID

!!! note
    For this example we are using `339bd140-e6a0-4afd-9b24-029c3243e779`

Running the following command will return all rules associated with that security group.

```
openstack security group rule list 339bd140-e6a0-4afd-9b24-029c3243e779
```

``` { .sh .no-copy }
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
| ID                                   | IP Protocol | Ethertype | IP Range  | Port Range | Direction | Remote Security Group | Remote Address Group |
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
| b0f0edd2-7a55-44b4-84a8-9650de36a7ec | None        | IPv6      | ::/0      |            | egress    | None                  | None                 |
| f0bce470-8d94-453f-9dfa-3e3e34b0c80e | tcp         | IPv4      | 0.0.0.0/0 | 8080:8080  | ingress   | None                  | None                 |
| f3925a01-5d47-4c55-ac73-1647cca5b739 | None        | IPv4      | 0.0.0.0/0 |            | egress    | None                  | None                 |
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
```

Take note of the Security Group Rule ID

!!! note
    For this example we will use f0bce470-8d94-453f-9dfa-3e3e34b0c80e

To delete a rule, run the following command with the correct rule ID.

```
openstack security group rule delete f0bce470-8d94-453f-9dfa-3e3e34b0c80e
```

Re-run the list command to confirm the rule has been deleted

```
openstack security group rule list 339bd140-e6a0-4afd-9b24-029c3243e779
```

``` { .sh .no-copy }
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
| ID                                   | IP Protocol | Ethertype | IP Range  | Port Range | Direction | Remote Security Group | Remote Address Group |
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
| b0f0edd2-7a55-44b4-84a8-9650de36a7ec | None        | IPv6      | ::/0      |            | egress    | None                  | None                 |
| f3925a01-5d47-4c55-ac73-1647cca5b739 | None        | IPv4      | 0.0.0.0/0 |            | egress    | None                  | None                 |
+--------------------------------------+-------------+-----------+-----------+------------+-----------+-----------------------+----------------------+
```

## Deleting a Security Group

Run the following to delete a Security Group

```
openstack security group delete SECURITY_GROUP_ID
```

!!! warning
    You cannot delete the `default` Security Group from your project. It's also not possible to delete a Security Group that is assigned to an instance.
