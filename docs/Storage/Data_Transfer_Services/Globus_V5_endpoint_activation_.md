---
created_at: '2021-08-27T03:41:37Z'
hidden: false
label_names: []
position: 2
title: 'Globus V5 endpoint activation '
vote_count: 2
vote_sum: 0
zendesk_article_id: 4405630948495
zendesk_section_id: 360000040596
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

 

## Activating an Endpoint

When you select an endpoint to transfer data to/from, you may be asked
to authenticate with that endpoint:

![mceclip0.png](../../assets/images/Globus_V5_endpoint_activation_.png)  
Transfers are only possible once you have supplied credentials that
authenticate your access to the endpoint. This process is known as
"activating the endpoint".  The endpoint remains active for 24 hours.  

The NeSI Wellington DTN V5 endpoint is protected by a second factor
authentication (2FA-same as accessing NeSI clusters).  In the
'**Username'** field, enter your Māui/Mahuika username. In the
'**Password'** field, your `Password` will be equal to
`Login Password (First Factor)` +
`Authenticator Code (Second Factor)` e.g. `password123456`. (***Do
not*** use any additional characters or spaces between your password and
the token number.)

                     
 ![mceclip0.png](../../assets/images/Globus_V5_endpoint_activation__0.png)

Check the status of your endpoints at
<https://www.globus.org/app/console/endpoints>[ ](https://www.globus.org/app/console/endpoints)

## Managing Endpoint Activation

If a transfer is in progress and will not finish in time before your
credentials expire, that transfer will pause and you will need to
reauthenticate for it to continue.

 

 
