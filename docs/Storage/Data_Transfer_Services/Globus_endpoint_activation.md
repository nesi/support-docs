---
created_at: '2021-08-27T03:41:37Z'
tags: 
    - data
    - globus
---

## Activating an Endpoint

When you select an endpoint to transfer data to/from, you may be asked
to authenticate with that endpoint.

![mceclip0.png](../../assets/images/Globus_V5_endpoint_activation.png)  
Transfers are only possible once you have supplied credentials that
authenticate your access to the endpoint. This process is known as
"activating the endpoint". The endpoint remains active for 24 hours.  

The NeSI HPC Storage endpoint is protected by Tuakiri authentication, similar to accessing theNeSI cluster. 

Check the status of your endpoints at [https://www.globus.org/app/console/endpoints](https://www.globus.org/app/console/endpoints)

## Managing Endpoint Activation

If a transfer is in progress and will not finish in time before your
credentials expire, that transfer will pause and you will need to
reauthenticate for it to continue.
