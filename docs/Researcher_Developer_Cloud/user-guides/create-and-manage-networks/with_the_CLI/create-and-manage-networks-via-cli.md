---
hidden: false
label_names:
- instance
- launch
position: 2
title: Create and manage network via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. 
    Please read [Setting up your CLI environment](../../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

## Create a network

Running the below command will generate a network without a subnet

```
openstack network create NETWORK_NAME
```

Our example command with response

```
openstack network create wiki-net
```

``` { .sh .no-copy }
+---------------------------+--------------------------------------+
| Field                     | Value                                |
+---------------------------+--------------------------------------+
| admin_state_up            | UP                                   |
| availability_zone_hints   |                                      |
| availability_zones        |                                      |
| created_at                | 2023-09-10T21:10:02Z                 |
| description               |                                      |
| dns_domain                |                                      |
| id                        | 15274353-ceae-476c-a374-dc7142a676f4 |
| ipv4_address_scope        | None                                 |
| ipv6_address_scope        | None                                 |
| is_default                | False                                |
| is_vlan_transparent       | None                                 |
| mtu                       | 8942                                 |
| name                      | wiki-net                             |
| port_security_enabled     | True                                 |
| project_id                | 4f07cc254d6c4471805d49bae1f739b9     |
| provider:network_type     | None                                 |
| provider:physical_network | None                                 |
| provider:segmentation_id  | None                                 |
| qos_policy_id             | None                                 |
| revision_number           | 1                                    |
| router:external           | Internal                             |
| segments                  | None                                 |
| shared                    | False                                |
| status                    | ACTIVE                               |
| subnets                   |                                      |
| tags                      |                                      |
| tenant_id                 | 4f07cc254d6c4471805d49bae1f739b9     |
| updated_at                | 2023-09-10T21:10:02Z                 |
+---------------------------+--------------------------------------+
```

Take note of the `id` that is returned for the new network

!!! note
    Our `id` from above is `15274353-ceae-476c-a374-dc7142a676f4`

## Create a network subnet

Running the below command will generate a subnet for the network that you supply the id from

```
openstack subnet create SUBNET_NAME --network NETWORK_ID --subnet-range IP_RANGE_CIDR
```

Our example command using the id from above will look like the following

```
openstack subnet create wiki-subnet --network  15274353-ceae-476c-a374-dc7142a676f4 --subnet-range 192.0.2.0/24
```

``` { .sh .no-copy }
+----------------------+--------------------------------------+
| Field                | Value                                |
+----------------------+--------------------------------------+
| allocation_pools     | 192.0.2.2-192.0.2.254                |
| cidr                 | 192.0.2.0/24                         |
| created_at           | 2023-09-10T21:11:13Z                 |
| description          |                                      |
| dns_nameservers      |                                      |
| dns_publish_fixed_ip | False                                |
| enable_dhcp          | True                                 |
| gateway_ip           | 192.0.2.1                            |
| host_routes          |                                      |
| id                   | ae9277e7-0a2c-4325-8eb1-33ad86eec974 |
| ip_version           | 4                                    |
| ipv6_address_mode    | None                                 |
| ipv6_ra_mode         | None                                 |
| name                 | wiki-subnet                          |
| network_id           | 15274353-ceae-476c-a374-dc7142a676f4 |
| project_id           | 4f07cc254d6c4471805d49bae1f739b9     |
| revision_number      | 0                                    |
| segment_id           | None                                 |
| service_types        |                                      |
| subnetpool_id        | None                                 |
| tags                 |                                      |
| updated_at           | 2023-09-10T21:11:13Z                 |
+----------------------+--------------------------------------+
```

## List all networks and subnets

Running the below command will list all networks within your project

```
openstack network list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------------------+--------------------------------------+
| ID                                   | Name                           | Subnets                              |
+--------------------------------------+--------------------------------+--------------------------------------+
| 15274353-ceae-476c-a374-dc7142a676f4 | wiki-net                       | ae9277e7-0a2c-4325-8eb1-33ad86eec974 |
| 33d0c11b-b659-4b77-9afc-5676fe965839 | external                       | 5c2644ad-7253-42f5-ad69-40970b84dea6 |
| 79029286-80ad-4923-a2e6-7d1216a9f2be | rally_verify_88403f86_qmojdKSJ |                                      |
| bcfd4714-ef9c-4c0b-aa58-ad8bcc1a999e | rally_verify_51cf3f2d_mQ0taHVb |                                      |
| d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | NeSI-Training-Test             | f5715775-270c-4230-bfa7-fdbdf51352dc |
| d780f680-9640-430f-813f-dbf2128b445c | azimuth-demo                   | 70dc21e9-d8f4-4232-bda9-2f0a0d508105 |
+--------------------------------------+--------------------------------+--------------------------------------+
```

Running the below will list all subnets within your project

```
openstack subnet list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------+--------------------------------------+------------------+
| ID                                   | Name               | Network                              | Subnet           |
+--------------------------------------+--------------------+--------------------------------------+------------------+
| 5c2644ad-7253-42f5-ad69-40970b84dea6 | external           | 33d0c11b-b659-4b77-9afc-5676fe965839 | 163.7.177.0/24   |
| 70dc21e9-d8f4-4232-bda9-2f0a0d508105 | azimuth-demo       | d780f680-9640-430f-813f-dbf2128b445c | 192.168.100.0/24 |
| ae9277e7-0a2c-4325-8eb1-33ad86eec974 | wiki-subnet        | 15274353-ceae-476c-a374-dc7142a676f4 | 192.0.2.0/24     |
| f5715775-270c-4230-bfa7-fdbdf51352dc | NeSI-Training-Test | d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | 10.1.0.0/24      |
+--------------------------------------+--------------------+--------------------------------------+------------------+
```

## Delete a subnet

Run the below command to list out all subnets

```
openstack subnet list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------+--------------------------------------+------------------+
| ID                                   | Name               | Network                              | Subnet           |
+--------------------------------------+--------------------+--------------------------------------+------------------+
| 5c2644ad-7253-42f5-ad69-40970b84dea6 | external           | 33d0c11b-b659-4b77-9afc-5676fe965839 | 163.7.177.0/24   |
| 70dc21e9-d8f4-4232-bda9-2f0a0d508105 | azimuth-demo       | d780f680-9640-430f-813f-dbf2128b445c | 192.168.100.0/24 |
| ae9277e7-0a2c-4325-8eb1-33ad86eec974 | wiki-subnet        | 15274353-ceae-476c-a374-dc7142a676f4 | 192.0.2.0/24     |
| f5715775-270c-4230-bfa7-fdbdf51352dc | NeSI-Training-Test | d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | 10.1.0.0/24      |
+--------------------------------------+--------------------+--------------------------------------+------------------+
```

Take note of the subnet id that you wish to delete

!!! note
    For our example we will use `ae9277e7-0a2c-4325-8eb1-33ad86eec974`

We then run the following command while supplying it with the id we have chosen to delete

```
openstack subnet delete SUBNET_ID
```

The server will not give a response if successful so you will need to run `openstack subnet list` to confirm its removal

```
openstack subnet list
```

Using our example id our command and list looks like the following

```
openstack subnet delete ae9277e7-0a2c-4325-8eb1-33ad86eec974
```

``` { .sh .no-copy }
+--------------------------------------+--------------------+--------------------------------------+------------------+
| ID                                   | Name               | Network                              | Subnet           |
+--------------------------------------+--------------------+--------------------------------------+------------------+
| 5c2644ad-7253-42f5-ad69-40970b84dea6 | external           | 33d0c11b-b659-4b77-9afc-5676fe965839 | 163.7.177.0/24   |
| 70dc21e9-d8f4-4232-bda9-2f0a0d508105 | azimuth-demo       | d780f680-9640-430f-813f-dbf2128b445c | 192.168.100.0/24 |
| f5715775-270c-4230-bfa7-fdbdf51352dc | NeSI-Training-Test | d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | 10.1.0.0/24      |
+--------------------------------------+--------------------+--------------------------------------+------------------+
```

## Delete a network

Run the below command to list all networks

```
openstack network list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------------------+--------------------------------------+
| ID                                   | Name                           | Subnets                              |
+--------------------------------------+--------------------------------+--------------------------------------+
| 15274353-ceae-476c-a374-dc7142a676f4 | wiki-net                       | ae9277e7-0a2c-4325-8eb1-33ad86eec974 |
| 33d0c11b-b659-4b77-9afc-5676fe965839 | external                       | 5c2644ad-7253-42f5-ad69-40970b84dea6 |
| 79029286-80ad-4923-a2e6-7d1216a9f2be | rally_verify_88403f86_qmojdKSJ |                                      |
| bcfd4714-ef9c-4c0b-aa58-ad8bcc1a999e | rally_verify_51cf3f2d_mQ0taHVb |                                      |
| d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | NeSI-Training-Test             | f5715775-270c-4230-bfa7-fdbdf51352dc |
| d780f680-9640-430f-813f-dbf2128b445c | azimuth-demo                   | 70dc21e9-d8f4-4232-bda9-2f0a0d508105 |
+--------------------------------------+--------------------------------+--------------------------------------+
```

Take note of the network id we want to remove

!!! note
    For our example we will use `15274353-ceae-476c-a374-dc7142a676f4`

Then run the below command while supplying the id for the network you wish to remove

```
openstack network delete NETWORK_ID
```

There will be no response from the server when you send the command so will need to list the networks to confirm removal.

Example command and list response

```
openstack network delete 15274353-ceae-476c-a374-dc7142a676f4
```

```
openstack network list
```

``` { .sh .no-copy }
+--------------------------------------+--------------------------------+--------------------------------------+
| ID                                   | Name                           | Subnets                              |
+--------------------------------------+--------------------------------+--------------------------------------+
| 33d0c11b-b659-4b77-9afc-5676fe965839 | external                       | 5c2644ad-7253-42f5-ad69-40970b84dea6 |
| 79029286-80ad-4923-a2e6-7d1216a9f2be | rally_verify_88403f86_qmojdKSJ |                                      |
| bcfd4714-ef9c-4c0b-aa58-ad8bcc1a999e | rally_verify_51cf3f2d_mQ0taHVb |                                      |
| d3a7ddb5-6582-42cf-978a-c99b4ed25ad4 | NeSI-Training-Test             | f5715775-270c-4230-bfa7-fdbdf51352dc |
| d780f680-9640-430f-813f-dbf2128b445c | azimuth-demo                   | 70dc21e9-d8f4-4232-bda9-2f0a0d508105 |
+--------------------------------------+--------------------------------+--------------------------------------+
```
