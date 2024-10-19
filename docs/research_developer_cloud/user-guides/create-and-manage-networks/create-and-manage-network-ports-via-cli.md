---
hidden: false
label_names:
- instance
- launch
position: 2
title: Create and manage network ports via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

First we need to get a few details, `Network ID` we want to connect to the network port to, `the Subnet ID` we want to connect the IP to and the `IP Address` we want to assign to the network port unless you want it to be assigned an IP from the DHCP

Run the following command to get the `Network ID`

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

Take note of the `Network ID` and the `Subnet ID`

!!! note
    For this example we will use the `azimuth-demo` network so the `Network ID: d780f680-9640-430f-813f-dbf2128b445c` and the `Subnet ID: 70dc21e9-d8f4-4232-bda9-2f0a0d508105`

Should you not know the IP range of the subnet run the following command to get the IP address range from that chosen subnet

```
openstack subnet show SUBNET_ID
```

Example response below using the `Subnet ID: 70dc21e9-d8f4-4232-bda9-2f0a0d508105`

```
openstack subnet show 70dc21e9-d8f4-4232-bda9-2f0a0d508105
```

``` { .sh .no-copy }
+----------------------+--------------------------------------+
| Field                | Value                                |
+----------------------+--------------------------------------+
| allocation_pools     | 192.168.100.2-192.168.100.254        |
| cidr                 | 192.168.100.0/24                     |
| created_at           | 2023-08-11T02:47:17Z                 |
| description          |                                      |
| dns_nameservers      |                                      |
| dns_publish_fixed_ip | False                                |
| enable_dhcp          | True                                 |
| gateway_ip           | 192.168.100.1                        |
| host_routes          |                                      |
| id                   | 70dc21e9-d8f4-4232-bda9-2f0a0d508105 |
| ip_version           | 4                                    |
| ipv6_address_mode    | None                                 |
| ipv6_ra_mode         | None                                 |
| name                 | azimuth-demo                         |
| network_id           | d780f680-9640-430f-813f-dbf2128b445c |
| project_id           | 4f07cc254d6c4471805d49bae1f739b9     |
| revision_number      | 0                                    |
| segment_id           | None                                 |
| service_types        |                                      |
| subnetpool_id        | None                                 |
| tags                 |                                      |
| updated_at           | 2023-08-11T02:47:17Z                 |
+----------------------+--------------------------------------+
```

Take note of the `allocation_pools` as that will specify the pool of IP addresses

## Create a network port

Run the following command to create a network port 

```
openstack port create --network NETWORK_ID --description PORT_DESCRIPTION --fixed-ip subnet=SUBNET_ID,ip-address=IP_ADDRESS --enable PORT_NAME
```

Using the example IDs we prepared earlier it will look like this

```
openstack port create --network d780f680-9640-430f-813f-dbf2128b445c --description wiki-network-port --fixed-ip subnet=70dc21e9-d8f4-4232-bda9-2f0a0d508105,ip-address=192.168.100.60 --enable Wiki-Network-Port-CLI
```

We have specified the `Network ID` as the `azimuth-demo` network, with the `Subnet ID` within that network and assigning that network port an IP address of `192.168.100.60`, we also gave it a description and a friendly name.

The response from the command

``` { .sh .no-copy }
+-------------------------+---------------------------------------------------------------------------------------------------------+
| Field                   | Value                                                                                                   |
+-------------------------+---------------------------------------------------------------------------------------------------------+
| admin_state_up          | UP                                                                                                      |
| allowed_address_pairs   |                                                                                                         |
| binding_host_id         | None                                                                                                    |
| binding_profile         | None                                                                                                    |
| binding_vif_details     | None                                                                                                    |
| binding_vif_type        | None                                                                                                    |
| binding_vnic_type       | normal                                                                                                  |
| created_at              | 2023-08-29T01:29:45Z                                                                                    |
| data_plane_status       | None                                                                                                    |
| description             | wiki-network-port                                                                                       |
| device_id               |                                                                                                         |
| device_owner            |                                                                                                         |
| device_profile          | None                                                                                                    |
| dns_assignment          | fqdn='host-192-168-100-60.openstacklocal.', hostname='host-192-168-100-60', ip_address='192.168.100.60' |
| dns_domain              |                                                                                                         |
| dns_name                |                                                                                                         |
| extra_dhcp_opts         |                                                                                                         |
| fixed_ips               | ip_address='192.168.100.60', subnet_id='70dc21e9-d8f4-4232-bda9-2f0a0d508105'                           |
| id                      | 09e94e3f-ee9e-42f5-851e-a9b4d957b563                                                                    |
| ip_allocation           | None                                                                                                    |
| mac_address             | fa:16:3e:05:c9:dd                                                                                       |
| name                    | Wiki-Network-Port-CLI                                                                                   |
| network_id              | d780f680-9640-430f-813f-dbf2128b445c                                                                    |
| numa_affinity_policy    | None                                                                                                    |
| port_security_enabled   | True                                                                                                    |
| project_id              | 4f07cc254d6c4471805d49bae1f739b9                                                                        |
| propagate_uplink_status | None                                                                                                    |
| qos_network_policy_id   | None                                                                                                    |
| qos_policy_id           | None                                                                                                    |
| resource_request        | None                                                                                                    |
| revision_number         | 1                                                                                                       |
| security_group_ids      | f2f15d6f-2a04-4196-8102-a058042694b3                                                                    |
| status                  | DOWN                                                                                                    |
| tags                    |                                                                                                         |
| trunk_details           | None                                                                                                    |
| updated_at              | 2023-08-29T01:29:45Z                                                                                    |
+-------------------------+---------------------------------------------------------------------------------------------------------+
```

Should you not want to assign an IP yourself and allow the DHCP to assign it then run the command without the `ip-address `parameter like below

```
openstack port create --network NETWORK_ID --description PORT_DESCRIPTION --fixed-ip subnet=SUBNET_ID --enable PORT_NAME
```

Command with response

```
openstack port create --network d780f680-9640-430f-813f-dbf2128b445c --description wiki-network-port --fixed-ip subnet=70dc21e9-d8f4-4232-bda9-2f0a0d508105 --enable Wiki-Network-Port-CLI
```

``` { .sh .no-copy }
+-------------------------+------------------------------------------------------------------------------------------------------------+
| Field                   | Value                                                                                                      |
+-------------------------+------------------------------------------------------------------------------------------------------------+
| admin_state_up          | UP                                                                                                         |
| allowed_address_pairs   |                                                                                                            |
| binding_host_id         | None                                                                                                       |
| binding_profile         | None                                                                                                       |
| binding_vif_details     | None                                                                                                       |
| binding_vif_type        | None                                                                                                       |
| binding_vnic_type       | normal                                                                                                     |
| created_at              | 2023-08-29T01:38:28Z                                                                                       |
| data_plane_status       | None                                                                                                       |
| description             | wiki-network-port                                                                                          |
| device_id               |                                                                                                            |
| device_owner            |                                                                                                            |
| device_profile          | None                                                                                                       |
| dns_assignment          | fqdn='host-192-168-100-182.openstacklocal.', hostname='host-192-168-100-182', ip_address='192.168.100.182' |
| dns_domain              |                                                                                                            |
| dns_name                |                                                                                                            |
| extra_dhcp_opts         |                                                                                                            |
| fixed_ips               | ip_address='192.168.100.182', subnet_id='70dc21e9-d8f4-4232-bda9-2f0a0d508105'                             |
| id                      | d91d923e-a91f-4e00-baa9-eda3ba842dd5                                                                       |
| ip_allocation           | None                                                                                                       |
| mac_address             | fa:16:3e:35:5a:e1                                                                                          |
| name                    | Wiki-Network-Port-CLI                                                                                      |
| network_id              | d780f680-9640-430f-813f-dbf2128b445c                                                                       |
| numa_affinity_policy    | None                                                                                                       |
| port_security_enabled   | True                                                                                                       |
| project_id              | 4f07cc254d6c4471805d49bae1f739b9                                                                           |
| propagate_uplink_status | None                                                                                                       |
| qos_network_policy_id   | None                                                                                                       |
| qos_policy_id           | None                                                                                                       |
| resource_request        | None                                                                                                       |
| revision_number         | 1                                                                                                          |
| security_group_ids      | f2f15d6f-2a04-4196-8102-a058042694b3                                                                       |
| status                  | DOWN                                                                                                       |
| tags                    |                                                                                                            |
| trunk_details           | None                                                                                                       |
| updated_at              | 2023-08-29T01:38:28Z                                                                                       |
+-------------------------+------------------------------------------------------------------------------------------------------------+
```

Running the below command will list the network ports within the project and we should be able to see our newly created one

```
openstack port list
```

``` { .sh .no-copy }
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| ID                                   | Name                  | MAC Address       | Fixed IP Addresses                                                             | Status |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| 09e94e3f-ee9e-42f5-851e-a9b4d957b563 | Wiki-Network-Port-CLI | fa:16:3e:05:c9:dd | ip_address='192.168.100.60', subnet_id='70dc21e9-d8f4-4232-bda9-2f0a0d508105'  | DOWN   |
| 0e1dc631-2c63-43b4-9bd2-fcdfbedb854c |                       | fa:16:3e:77:0d:c0 | ip_address='10.1.0.5', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc'        | ACTIVE |
| 19737c3e-5717-4d19-8717-d362c53f552a |                       | fa:16:3e:21:99:fa | ip_address='10.1.0.2', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc'        | ACTIVE |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
```

!!! note
    The full openstack documentation is [here](https://docs.openstack.org/python-openstackclient/pike/cli/command-objects/port.html#port-create) should you need more advanced parameters

## List network ports

Run the below command to list all network ports within your project

```
openstack port list
```

``` { .sh .no-copy }
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| ID                                   | Name                  | MAC Address       | Fixed IP Addresses                                                             | Status |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| 09e94e3f-ee9e-42f5-851e-a9b4d957b563 | Wiki-Network-Port-CLI | fa:16:3e:05:c9:dd | ip_address='192.168.100.60', subnet_id='70dc21e9-d8f4-4232-bda9-2f0a0d508105'  | DOWN   |
| 0e1dc631-2c63-43b4-9bd2-fcdfbedb854c |                       | fa:16:3e:77:0d:c0 | ip_address='10.1.0.5', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc'        | ACTIVE |
| 19737c3e-5717-4d19-8717-d362c53f552a |                       | fa:16:3e:21:99:fa | ip_address='10.1.0.2', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc'        | ACTIVE |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
```

## Attach network port to an Instance

If you also wish to attach the newly created `Network Port` to an instance then you will also need the `Instance ID`

Running the below will return a list of all instances within your project

```
openstack server list
```

``` { .sh .no-copy }
+--------------------------------------+---------------------+--------+----------------------------------------------+------------------------------+--------------------+
| ID                                   | Name                | Status | Networks                                     | Image                        | Flavor             |
+--------------------------------------+---------------------+--------+----------------------------------------------+------------------------------+--------------------+
| 610ee950-cdf8-425d-a3f3-52de500522ee | k8s-worker-node-1   | ACTIVE | NeSI-Training-Test=10.1.0.101, FLEXIHPC_IP   | Ubuntu-Focal-20.04           | balanced1.2cpu4ram |
| 10389ba9-15a9-48b0-91f3-b7cbccdce72b | k8s-worker-node-0   | ACTIVE | NeSI-Training-Test=10.1.0.81, FLEXIHPC_IP    | Ubuntu-Focal-20.04           | balanced1.2cpu4ram |
| af6fb776-b80e-49b9-a8d4-a1d88b272b63 | k8s-control-plane-0 | ACTIVE | NeSI-Training-Test=10.1.0.176, FLEXIHPC_IP   | Ubuntu-Focal-20.04           | balanced1.2cpu4ram |
| 6d1d5418-a70e-4996-a0f5-4f4c03cfd138 | ood-cluster-admin   | ACTIVE | NeSI-Training-Test=10.1.0.69, FLEXIHPC_IP    | N/A (booted from volume)     | devtest1.4cpu4ram  |
+--------------------------------------+---------------------+--------+----------------------------------------------+------------------------------+--------------------+
```

Take note of the `Instance ID`

!!! note
    For this example we will use `Instance ID: 6d1d5418-a70e-4996-a0f5-4f4c03cfd138`

We then want to list our network ports

```
openstack port list
```

``` { .sh .no-copy }
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| ID                                   | Name                  | MAC Address       | Fixed IP Addresses                                                             | Status |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| d91d923e-a91f-4e00-baa9-eda3ba842dd5 | Wiki-Network-Port-CLI | fa:16:3e:35:5a:e1 | ip_address='192.168.100.182', subnet_id='70dc21e9-d8f4-4232-bda9-2f0a0d508105' | DOWN   |
| f1c54ee3-80c5-468d-a1cb-2828c1fee5cc |                       | fa:16:3e:ad:6b:06 | ip_address='10.1.0.1', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc'        | ACTIVE |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
```

Take note of the `Network Port ID`

!!! note
    For this example we will use `d91d923e-a91f-4e00-baa9-eda3ba842dd5`

We then run the following command

```
openstack server add port INSTANCE_ID NETWORK_PORT_ID
```

Command with our example ID’s

```
openstack server add port 6d1d5418-a70e-4996-a0f5-4f4c03cfd138 d91d923e-a91f-4e00-baa9-eda3ba842dd5
```

There will be no response from the server so running the below command will display the new network port added to the instance

```
openstack server show 6d1d5418-a70e-4996-a0f5-4f4c03cfd138
```

``` { .sh .no-copy }
+-------------------------------------+----------------------------------------------------------------------------+
| Field                               | Value                                                                      |
+-------------------------------------+----------------------------------------------------------------------------+
| accessIPv4                          |                                                                            |
| accessIPv6                          |                                                                            |
| access_ipv4                         |                                                                            |
| access_ipv6                         |                                                                            |
| addresses                           | NeSI-Training-Test=10.1.0.69, 163.7.177.243; azimuth-demo=192.168.100.182  |
| adminPass                           | None                                                                       |
| admin_password                      | None                                                                       |
| availability_zone                   | nova                                                                       |
| block_device_mapping                | None                                                                       |
| block_device_mapping_v2             | None                                                                       |
| compute_host                        | None                                                                       |
| config_drive                        | True                                                                       |
| created                             | 2023-07-19T03:45:21Z                                                       |
| created_at                          | 2023-07-19T03:45:21Z                                                       |
| description                         | None                                                                       |
| disk_config                         | AUTO                                                                       |
| fault                               | None                                                                       |
| flavor                              | devtest1.4cpu4ram (devtest1.4cpu4ram)                                      |
| flavorRef                           | None                                                                       |
| flavor_id                           | None                                                                       |
| has_config_drive                    | True                                                                       |
| hostId                              | f40676c3043f50b6efeeefb163a9d9f7a0994b288b09dfddcdccac9b                   |
| host_id                             | f40676c3043f50b6efeeefb163a9d9f7a0994b288b09dfddcdccac9b                   |
| host_status                         | None                                                                       |
| hostname                            | ood-cluster-admin                                                          |
<TRIMMED.....>
| launched_at                         | 2023-07-19T03:45:28.000000                                                 |
+-------------------------------------+----------------------------------------------------------------------------+
```

You should see the additional network port under `addresses` for your instance

## Delete a network port

Run the command `openstack port list` and take note of the `Network Port ID`

```
openstack port list
```

``` { .sh .no-copy }
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| ID                                   | Name                  | MAC Address       | Fixed IP Addresses                                                             | Status |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| d91d923e-a91f-4e00-baa9-eda3ba842dd5 | Wiki-Network-Port-CLI | fa:16:3e:35:5a:e1 | ip_address='192.168.100.182', subnet_id='70dc21e9-d8f4-4232-bda9-2f0a0d508105' | DOWN   |
| f1c54ee3-80c5-468d-a1cb-2828c1fee5cc |                       | fa:16:3e:ad:6b:06 | ip_address='10.1.0.1', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc'        | ACTIVE |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
```

Take note of the ID for that network port

!!! note
    For this example we will use `d91d923e-a91f-4e00-baa9-eda3ba842dd5`

Then run the below command, supplying the `Network Port ID` you want to delete

```
openstack port delete NETWORK_PORT_ID
```

Command with our example ID

```
openstack port delete d91d923e-a91f-4e00-baa9-eda3ba842dd5
```

There is no response from the server so run `openstack port list` to see the network port has been removed

```
openstack port list
```

``` { .sh .no-copy }
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| ID                                   | Name                  | MAC Address       | Fixed IP Addresses                                                             | Status |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
| f1c54ee3-80c5-468d-a1cb-2828c1fee5cc |                       | fa:16:3e:ad:6b:06 | ip_address='10.1.0.1', subnet_id='f5715775-270c-4230-bfa7-fdbdf51352dc'        | ACTIVE |
+--------------------------------------+-----------------------+-------------------+--------------------------------------------------------------------------------+--------+
```