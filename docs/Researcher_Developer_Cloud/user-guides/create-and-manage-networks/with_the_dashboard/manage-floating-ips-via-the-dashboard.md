---
hidden: false
label_names:
- instance
- launch
position: 2
title: Manage Floating IPs via the Dashboard
vote_count: 1
vote_sum: 1
---

## Assign Floating IP address

Log into the [NeSI FlexiHPC Dashboard](https://dashboard.cloud.nesi.org.nz/)

Select the project you would like to deploy the new instance too (Use the project selector on the top left-hand side):

<figure markdown>
  ![Alt text](../../../assets/images/flexi/project-selector.png)
</figure>

Open the `Project` tab, open the `Network` tab and select `Floating IPs`

Click `Allocate IP to Project`

Within the `Allocate Floating IP` dialog you have the following options

`Pool`
:   The pool that the floating ip should be allocated from. There is only external currently so is set as the default.

`Description`
:   A friendly description for what this IP is used for

`DNS Domain`
:   TODO: Confirm with Sean what this means

`DNS Name`
:   TODO: Confirm with Sean what this means

!!! note
    The default settings are fine should you not wish to configure anything further.

Click `Allocate IP`

<figure markdown>
  ![Alt text](../../../assets/images/flexi/floating-ips.png)
</figure>

Under `Actions` click `Associate`

Within the `Managing Floating IP Associations` dialog you want to ensure the `IP Address` is the one you wish to assign, and under the `Ports to be assocaited` select the compute instance you wish to assign the IP too.

Click `Associate`

## Un-assign Floating IP address

Log into the [NeSI FlexiHPC Dashboard](https://dashboard.cloud.nesi.org.nz/)

Select the project you would like to deploy the new instance too (Use the project selector on the top left-hand side):

<figure markdown>
  ![Alt text](../../../assets/images/flexi/project-selector.png)
</figure>

Open the `Project` tab, open the `Network` tab and select `Floating IPs`

Under `Actions` click `Disassociate`

Within the `Confrim Disassociate` dialog confirm the IP you are disassociating

Click `Disassociate`
