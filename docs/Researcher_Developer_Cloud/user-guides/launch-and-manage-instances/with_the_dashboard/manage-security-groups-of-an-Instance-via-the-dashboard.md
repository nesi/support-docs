---
hidden: false
label_names:
- instance
- resize
position: 2
title: Manage Security Groups of an Instance via the Dashboard
vote_count: 1
vote_sum: 1
---

Log into the [NeSI FlexiHPC Dashboard](https://dashboard.cloud.nesi.org.nz/)

Select the project you would like to deploy the new instance too (Use the project selector on the top left-hand side):

<figure markdown>
  ![Alt text](../../../assets/images/flexi/project-selector.png)
</figure>

Open the `Project` tab, open the `Compute` tab and select `Instances` then select the compute instance you want to manage.

## Attach a Security Group

Under the `Actions` menu on the far right, select `Edit Security Groups`

<figure markdown>
  ![Alt text](../../../assets/images/flexi/instance-action-menu.png)
</figure>

Within the `Edit Instance` dialog you will have 2 columns

`All Security Groups`
:   These are all security groups created in your project

`Instance Security Groups`
:   These are the security groups attached to your instance

<figure markdown>
  ![Alt text](../../../assets/images/flexi/manage-security-groups-dialog.png)
</figure>

Clicking the `+` icon from the `All Security Groups` column will add them to the `Instance Security Groups` column

<figure markdown>
  ![Alt text](../../../assets/images/flexi/manage-security-groups-add-dialog.png)
</figure>

Once the desired `Secuirty Groups` have been added you then click `save`


## Remove a Security Group

Under the `Actions` menu on the far right, select `Edit Security Groups`

<figure markdown>
  ![Alt text](../../../assets/images/flexi/instance-action-menu.png)
</figure>

Within the `Edit Instance` dialog you will have 2 columns

`All Security Groups`
:   These are all security groups created in your project

`Instance Security Groups`
:   These are the security groups attached to your instance

<figure markdown>
  ![Alt text](../../../assets/images/flexi/manage-security-groups-add-dialog.png)
</figure>

Clicking the `-` icon from the `Instance Security Groups` column will remove it and add it to the `All Security Groups` column

<figure markdown>
  ![Alt text](../../../assets/images/flexi/manage-security-groups-dialog.png)
</figure>

Once the desired `Secuirty Groups` have been removed you then click `save`
