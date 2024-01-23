---
created_at: '2023-10-13T00:14:22Z'
hidden: false
weight: 0
tags: []
title: Globus Quick Start Guide
vote_count: 0
vote_sum: 0
zendesk_article_id: 8117557125391
zendesk_section_id: 360000040596
---

This is intended to be a quick-start guide, for more detailed
information, please see our other Globus articles here: [Globus
documentation](https://support.nesi.org.nz/hc/en-gb/sections/360000040596)

Globus is a third-party service for transferring large amounts of data
between two Globus Data Transfer Nodes (DTNs). To use Globus to transfer
data to or from NeSI, you need:

1.  A NeSI account
2.  A Globus account
3.  Access to Globus DTNs or endpoint  
    -   Access to a DTN (e.g., at your home institution)
    -   Personal endpoint if no DTN is available

 

## Globus Account

Please note that a Globus account is not the same as a NeSI account. You
will need both Globus and NeSI accounts in order to transfer data to or
from NeSI HPC facilities.

To get a Globus account, go to <https://transfer.nesi.org.nz/> and sign
up using one of the available options on the page. Please note that the
"existing organizational login" is somewhat limited, if your
organisation is not listed, please sign in (sign up) using any of the
other methods.

![Globus\_login.png](../../assets/images/Globus_Quick_Start_Guide.png)

For more detailed instructions please see [Initial Globus Sign-Up, and
your Globus
Identities](../../Storage/Data_Transfer_Services/Initial_Globus_Sign_Up-and_your_Globus_Identities.md).

 

## Globus Endpoint Activation

A NeSI account is required in addition to a Globus account to transfer
data to or from NeSI facilities. *  
*

To transfer data, between two sites, you need to have access to a DTN or
endpoint at each location. For example, one on NeSI (NeSI Wellington DTN
V5), the other to University of Otago's central file storage. You will
also need the appropriate read and write permissions from where you're
copying to and from. Please note that the NeSI `project` directory is
read only, and `nobackup` is read and write.

A list of some Institutional endpoints can be found here:
[National-Data-Transfer-Platform](../../Storage/Data_Transfer_Services/National_Data_Transfer_Platform.md).
You can also set up your own [personal
endpoint](../../Storage/Data_Transfer_Services/Personal_Globus_Endpoint_Configuration.md)
to transfer data to or from your personal computer, however,
administrative access to your computer is required

To activate the NeSI endpoint click go to
<https://transfer.nesi.org.nz/>  and click "file manager" on the menu
bar on the left.

1.  Next to "Collection", search for "NeSI Wellington DTN V5", select
    it, then click "Continue".
2.  In the 'Username**'** field, enter your NeSI HPC username. In the
    'Password**'** field, the password is
    `Login Password (First Factor)` +
    `Authenticator Code (Second Factor)` e.g. `password123456`. Please
    **do not** save your password on "*Browser settings*" as it will
    change every time due to the 2nd factor requirement.

![NeSI\_Globus\_Authenticate.png](../../assets/images/Globus_Quick_Start_Guide_0.png)

 

 

## Transferring Data

To transfer data, activate your two endpoints and navigate to the
appropriate folders, then select the files or folders of interest. To
initiate the transfer, select one of the two directional arrows. In the
image below, the 'config' folder is being transferred from the location
on the right, to the location on the left.

![Globus\_transfer\_data.png](../../assets/images/Globus_Quick_Start_Guide_1.png)

To see the progress of the transfer, please click 'Activity' on the left
hand menu bar.

 

If you have any questions or issues using Globus to transfer data to or
from NeSI, email [support@nesi.org.nz](https://support@nesi.org.nz).

 

 

 