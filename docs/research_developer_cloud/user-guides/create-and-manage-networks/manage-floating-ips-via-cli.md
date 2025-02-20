---
hidden: false
label_names:
- instance
- launch
position: 2
title: Manage Floating IPs via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.


Use the `openstack` commands to manage floating IP addresses.

## List floating IP address information

To list all floating IP addresses that are allocated to the current project, run:

```
openstack floating ip list
```

``` { .sh .no-copy }
+--------------------------------------+---------------------+------------------+--------------------------------------+--------------------------------------+----------------------------------+
| ID                                   | Floating IP Address | Fixed IP Address | Port                                 | Floating Network                     | Project                          |
+--------------------------------------+---------------------+------------------+--------------------------------------+--------------------------------------+----------------------------------+
| 1c59da88-9b5c-4214-930e-8447cebd3980 | <FLEXIHPC_IP>       | None             | None                                 | 33d0c11b-b659-4b77-9afc-5676fe965839 | 4f07cc254d6c4471805d49bae1f739b9 |
+--------------------------------------+---------------------+------------------+--------------------------------------+--------------------------------------+----------------------------------+
```

## Associate floating IP addresses

You can assign a floating IP address to a project and to an instance.

Run the following command to allocate a floating IP address to the current project. By default, the floating IP address is allocated from the `external` pool. The command outputs the allocated IP address:

```
openstack floating ip create external
```

``` { .sh .no-copy }
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| created_at          | 2023-07-27T01:29:31Z                 |
| description         |                                      |
| dns_domain          |                                      |
| dns_name            |                                      |
| fixed_ip_address    | None                                 |
| floating_ip_address | <FLEXIHPC_IP>                        |
| floating_network_id | 33d0c11b-b659-4b77-9afc-5676fe965839 |
| id                  | 5c8781cd-399b-4b37-8ced-41ca4a38c128 |
| name                | <FLEXIHPC_IP>                        |
| port_details        | None                                 |
| port_id             | None                                 |
| project_id          | 4f07cc254d6c4471805d49bae1f739b9     |
| qos_policy_id       | None                                 |
| revision_number     | 0                                    |
| router_id           | None                                 |
| status              | DOWN                                 |
| subnet_id           | None                                 |
| tags                | []                                   |
| updated_at          | 2023-07-27T01:29:31Z                 |
+---------------------+--------------------------------------+
```

List all project instances with which a floating IP address could be associated.

```
openstack server list
```

``` { .sh .no-copy }
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
| ID                                   | Name                                  | Status | Networks                                     | Image                    | Flavor             |
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
| 8b08a4fb-7372-4269-a583-9dbc91779ffe | test-instance-wiki                    | ACTIVE | NeSI-Training-Test=10.1.0.134                | Ubuntu-Jammy-22.04       | devtest1.2cpu2ram  |
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
```

Note the server ID to use.

List ports associated with the selected server.

```
openstack port list --device-id SERVER_ID
```

``` { .sh .no-copy }
+--------------------------------------+------+-------------------+---------------------------------------------------------------------------+--------+
| ID                                   | Name | MAC Address       | Fixed IP Addresses                                                        | Status |
+--------------------------------------+------+-------------------+---------------------------------------------------------------------------+--------+
| 09c1ebd1-0fa0-40ec-98ef-bae2417f33ef |      | fa:16:3e:14:0c:32 | ip_address='10.1.0.134', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc' | ACTIVE |
+--------------------------------------+------+-------------------+---------------------------------------------------------------------------+--------+
```

Note the port ID to use.

Associate an IP address with an instance in the project, as follows:

```
openstack floating ip set --port PORT_ID FLOATING_IP_ADDRESS
```

For example:

```
openstack floating ip set --port 09c1ebd1-0fa0-40ec-98ef-bae2417f33ef <FLEXIHPC_IP>
```

The instance is now associated with two IP addresses:

```
openstack server list
```

``` { .sh .no-copy }
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
| ID                                   | Name                                  | Status | Networks                                     | Image                    | Flavor             |
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
| 8b08a4fb-7372-4269-a583-9dbc91779ffe | test-instance-wiki                    | ACTIVE | NeSI-Training-Test=10.1.0.134, <FLEXIHPC_IP> | Ubuntu-Jammy-22.04       | devtest1.2cpu2ram  |
+--------------------------------------+---------------------------------------+--------+----------------------------------------------+--------------------------+--------------------+
```

After you associate the IP address and configure security group rules for the instance, the instance is publicly available at the floating IP address.

## Disassociate floating IP addresses

To disassociate a floating IP address from an instance:

```
openstack floating ip unset --port PORT_ID FLOATING_IP_ADDRESS
```

To remove the floating IP address from a project:

```
openstack floating ip delete FLOATING_IP_ADDRESS
```

The IP address is returned to the pool of IP addresses that is available for all projects. If the IP address is still associated with a running instance, it is automatically disassociated from that instance.