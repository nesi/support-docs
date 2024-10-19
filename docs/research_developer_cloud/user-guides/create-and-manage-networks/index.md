---
hidden: false
label_names:
- networks
- create
- manage
position: 1
title: Create and Manage networks
vote_count: 1
vote_sum: 1
---

Within FlexiHPC you are able to use the default network that comes with the FlexiHPC Project or you are able to create your own with a specific IP range.

The networks within FlexiHPC are all `Software Defined Networks` so can overlap each other in different projects.

Networks can be created and managed in 2 ways

- [Create and Manage networks with the Dashboard](create-and-manage-networks-with-the-dashboard.md)

- [Create and Manage networks via CLI](create-and-manage-networks-via-cli.md)

Within the network tab you also have the following that you are able to manage

## Security Groups

A security group acts as a virtual firewall for servers and other resources on a network. It is a container for security group rules which specify the network access rules.

Security Groups can be created and managed within the FlexiHPC dashboard. However, advanced users can take advantage of the OpenStack CLI to manage Security Groups.

- [Create and Manage Security groups with the Dashboard](manage-security-groups-with-the-dashboard.md)

- [Manage Security groups via CLI](manage-security-groups-via-cli.md)

## Floating IPs

When an instance is created in FlexiHPC, it is automatically assigned a fixed IP address in the network to which the instance is assigned. This IP address is permanently associated with the instance until the instance is terminated.

However, in addition to the fixed IP address, a floating IP address can also be attached to an instance. Unlike fixed IP addresses, floating IP addresses can have their associations modified at any time, regardless of the state of the instances involved. This procedure details the reservation of a floating IP address from an existing pool of addresses and the association of that address with a specific instance.

If you wish to connect to an instance within the FlexiHPC platform from outside then these are required.

- [Manage Floating IPs with the Dashboard](manage-floating-ips-via-the-dashboard.md)

- [Manage Floating IPs with the CLI](manage-floating-ips-via-cli.md)

## Static IPs

If you wanted to create an instance with a fixed static IP address this can be achieved by using network ports. A port is a connection point for attaching a single device, such as the NIC of a server, to an OpenStack network. A network port also describes the associated network configuration, such as the MAC and IP addresses to be used on that port.

These network ports can be managed 2 ways

- [Create and Manage network ports with the Dashboard](create-and-manage-network-ports-with-the-dashboard.md)

- [Create and manage network ports via CLI](create-and-manage-network-ports-via-cli.md)