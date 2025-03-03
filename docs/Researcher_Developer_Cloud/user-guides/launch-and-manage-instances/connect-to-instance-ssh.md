# Connect to your instance by using SSH

To use SSH to connect to your instance, use the downloaded keypair file. You will also need to ensure you have created and assigned a `Security group` to your instance that allows connections on port 22.

Read Create and Manage Security Groups via [Dashboard](../create-and-manage-networks/with_the_dashboard/manage-security-groups-with-the-dashboard.md) or [CLI](../create-and-manage-networks/with_the_CLI/manage-security-groups-via-cli.md) to create one that allows port 22 if you have not done so already. You will then need to add that to the Instance if you havent already via the [Dashboard](with_the_dashboard/manage-security-groups-of-an-Instance-via-the-dashboard.md#attach-a-security-group) or [CLI](with_the_CLI/manage-security-groups-of-an-Instance-via-the-cli.md#adding-a-security-group-to-an-instance)

!!! note
    The user name is `ubuntu` for the Ubuntu cloud images on FlexiHPC. We have a list of default users for the most common cloud images in [Default user for images](default-user-nesi-images.md)

Insure your instance has a `floating ip` associated with it. If you need to assign one then check the following Assign Floating IP to an Instance via the Dashboard

Copy the `floating ip` address for your instance.

Use the **ssh** command to make a secure connection to the instance. For example:

```
ssh -i MyKey.pem ubuntu@10.0.0.2
```

!!! note
    A `MyKey.pem` private key is a key kept secret by the SSH user on their client machine. The user must never reveal the private key to anyone, including the server (server administrator), to ensure the their identity is never compromised.
    Please look at [Create and Manage Keypairs](../create-and-manage-keypairs/index.md) to create or import a keypair for use on the RDC

At the prompt, type `yes`.
