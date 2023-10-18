---
created_at: '2023-10-13T00:14:22Z'
hidden: false
label_names: []
position: 0
title: Globus Quick Start Guide
vote_count: 0
vote_sum: 0
zendesk_article_id: 8117557125391
zendesk_section_id: 360000040596
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
This is intended to be a quick-start guide, for more information, please
see our other Globus articles here: [Globus
documentation](https://support.nesi.org.nz/hc/en-gb/sections/360000040596)

Globus is a third-party service for transferring large amounts of data
between two Globus Data Transfer Nodes (DTNs). To use Globus to transfer
data to or from NeSI, you need:

1.  A Globus account
2.  Globus endpoints

 

## Globus Account

Please note that a Globus account is not the same as a NeSI account. You
will need both Globus and NeSI accounts.

To get a Globus account, go to <https://transfer.nesi.org.nz/> and sign
up using one of the available options on the page. Please note that the
"existing organizational login" is somewhat limited, if your
organisation is not listed, please sign in (sign up) using any of the
other methods.

<img src="../../assets/images/8149105856015_0.name_me.png" width="398"
height="436" alt="Globus_login.png" />

For a more detailed instructions please see [Creating a NeSI
Account](https://support.nesi.org.nz/hc/en-gb/articles/360000159715).

 

## Globus Endpoint Activation

To transfer data, you need access to two endpoints. One on NeSI (NeSI
Wellington DTN V5), the other for example to Otago University's central
file storage. You will also need the appropriate read and write
permissions from where you're copying to and from. Please note that the
NeSI `project` directory is read only, and `nobackup` is read and write.

A list of some Institutional endpoints can be found here:
[National-Data-Transfer-Platform](https://support.nesi.org.nz/hc/en-gb/articles/360000931775-National-Data-Transfer-Platform)

To activate the NeSI endpoint click go to
<https://transfer.nesi.org.nz/>  and click "file manager" on the menu
bar on the left.

1.  Next to "Collection", search for "NeSI Wellington DTN V5", select
    it, then click "Continue".
2.  In the '**Username'** field, enter your NeSI HPC username. In the
    '**Password'** field, the password is
    `Login Password (First Factor)` +
    `Authenticator Code (Second Factor)` e.g. `password123456`. Please
    do not save your password as it will change every time due to the
    2nd factor requirement.

<img src="../../assets/images/8149067986063_0.name_me.png" width="296"
height="340" alt="NeSI_Globus_Authenticate.png" />

You can also set up your own personal endpoint: [Globus personal
endpoint](https://support.nesi.org.nz/hc/en-gb/articles/360000217915).

 

## Transferring Data

To transfer data, activate your two endpoints and navigate to the
appropriate folders, then select the files or folders of interest. To
transfer the data, select one of the two directional arrows. In the
image below, the 'config' folder is being trasnferred from the location
on the right, to the location on the left.

![Globus\_transfer\_data.png](../../assets/images/8149738412815_0.name_me.png)

To see the progress of the transfer, please click 'Activity' on the left
hand menu bar.

 

 

 
