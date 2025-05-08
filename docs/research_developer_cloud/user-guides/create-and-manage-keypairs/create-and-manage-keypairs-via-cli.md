---
hidden: false
label_names:
- keypairs
- create
- manage
- cli
position: 1
title: Create and manage keypairs via CLI
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

## Create a new Keypair

Running the following command will generate a new SSH keypair for use on the RDC

``` { .sh }
openstack keypair create KEY_PAIR_NAME
```

You will get a response from the server that contains your private key


``` { .sh .no-copy }
-----BEGIN OPENSSH PRIVATE KEY-----
A BIG STRING OF NUMBERS AND LETTERS
-----END OPENSSH PRIVATE KEY-----
```

You will need to take that output and save it to a file. An example below on how to do that:

```
nano ~/.ssh/id_rdc_key
```

That will open up and empty file in `nano` called `~/.ssh/id_rdc_key`

You will then want to take the `private key` response and paste that into the file within your text editor and save it.

You should now have a file under `~/.ssh` called `idc_rdc_key`

We will need to change its permissions so that only you can read and write to the file, run the following command:

```
chmod 0600 ~/.ssh/id_rdc_key
```

## Import a Keypair

To import a keypair that you have for use on the RDC the command is the same as the create expect with a new parameter

```
openstack keypair create --public-key PUBLIC_KEY_FILE KEY_PAIR_NAME
```

You will need to replace `PUBLIC_KEY_FILE` with the Public Key file location on your machine, running the above command will give no response so you will need to list the key pairs to see if its been successfuly created

## List your Keypairs

Running the below command will list all your keypairs that are on the RDC

```
openstack keypair list
```

``` { .sh .no-copy }
$ openstack keypair list
+------------+-------------------------------------------------+------+
| Name       | Fingerprint                                     | Type |
+------------+-------------------------------------------------+------+
| wiki-test  | d5:0a:41:68:e0:84:fc:08:b6:cc:34:23:d8:9a:b4:c3 | ssh  |
+------------+-------------------------------------------------+------+
```

## Details of a Keypair

Running the below command will show details about the key pair

```
openstack keypair show KEY_PAIR_NAME
```

``` { .sh .no-copy }
$ openstack keypair show wiki-test
+-------------+-------------------------------------------------+
| Field       | Value                                           |
+-------------+-------------------------------------------------+
| created_at  | 2023-11-02T20:28:15.000000                      |
| fingerprint | d5:0a:41:68:e0:84:fc:08:b6:cc:34:23:d8:9a:b4:c3 |
| id          | wiki-test                                       |
| is_deleted  | False                                           |
| name        | wiki-test                                       |
| private_key | None                                            |
| type        | ssh                                             |
| user_id     | fb9a3d02c89e4cfdbe64658ad43ece97                |
+-------------+-------------------------------------------------+
```

Adding the paramter `--public_key` will output the public key for that key pair

```
openstack keypair show --public-key KEY_PAIR_NAME
```

``` { .sh .no-copy }
$ openstack keypair show --public-key wiki-test
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILW2gFl/ax1FW1y5u2ihfJfPow7fFbX/aFsZ4Wv49yY4
```

## Delete a Keypair

To delete a keypair from the RDC run the below command

```
openstack keypair delete KEY_PAIR_NAME
```

Their will be no response from the server so running the list command will confirm that the keypair has been removed.
    