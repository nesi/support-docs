---
hidden: false
label_names:
- images
- upload
- manage
- CLI
position: 1
title: Upload an Image via CLI
vote_count: 1
vote_sum: 1
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

To upload an image to FlexiHPC we will be using the command `openstack image create` to upload the image.

Using Ubuntu as an example, we will upload a new Ubuntu 22.10 (kinetic) image. Heading to the Ubuntu cloud images [link](https://cloud-images.ubuntu.com/kinetic/current/) for Kinetic images we want to select the image that has the description `QCow2 UEFI/GPT Bootable disk image with linux-kvm KVM optimised kernel` 

With that download and accessible from your CLI we can upload it to FlexiHPC

```
openstack image create --file /path/to/your/image-file --disk-format disk_format --container-format container_format image_name
```

Replace the placeholders with the appropriate values depending on your environment:

`/path/to/your/image-file`
:   The local path to the image file you want to upload.

`disk_format`
:   The format of the image on disk, e.g., qcow2, raw, vhd, vmdk, etc. If your unsure then set the format to qcow2

!!! note
    When it comes to the different image formats we generally follow the very basic guideline for them.

    Images in the `QCOW2` format are for running a single compute instance.

    Images in the `RAW` format are for running multiple compute instances.

    If you wish to convert to another format please read Converting Images between formats

`container_format`
:   The format of the container for the image, e.g., bare, ovf, aki (kernel image), etc. If you are unsure here then set the format to bare

`image_name`
:   The name you want to give to the uploaded image.

If we run the command with the supplied settings

```
openstack image create --file ~/openstackcli/iso/kinetic-server-cloudimg-amd64-disk-kvm.img --disk-format qcow2 --container-format bare Ubuntu-22.10-Wiki-Test
```

The command window will process silently as it uploads it to the FlexiHPC platform. We should then get a response from the FlexiHPC Platform

``` { .sh .no-copy }
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field            | Value                                                                                                                                                                      |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| container_format | bare                                                                                                                                                                       |
| created_at       | 2023-08-01T02:55:50Z                                                                                                                                                       |
| disk_format      | qcow2                                                                                                                                                                      |
| file             | /v2/images/1276db65-e5de-4721-b2db-666a73929b3e/file                                                                                                                       |
| id               | 1276db65-e5de-4721-b2db-666a73929b3e                                                                                                                                       |
| min_disk         | 0                                                                                                                                                                          |
| min_ram          | 0                                                                                                                                                                          |
| name             | Ubuntu-22.10-Wiki-Test                                                                                                                                                     |
| owner            | 4f07cc254d6c4471805d49bae1f739b9                                                                                                                                           |
| properties       | locations='[]', os_hidden='False', owner_specified.openstack.md5='', owner_specified.openstack.object='images/Ubuntu-22.10-Wiki-Test', owner_specified.openstack.sha256='' |
| protected        | False                                                                                                                                                                      |
| schema           | /v2/schemas/image                                                                                                                                                          |
| status           | queued                                                                                                                                                                     |
| tags             |                                                                                                                                                                            |
| updated_at       | 2023-08-01T02:55:50Z                                                                                                                                                       |
| visibility       | shared                                                                                                                                                                     |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

!!! note
    Adding `--wait` to the end of the command will give you a progress bar rather then returning with the status `queued`

We should then be able to use the `id` returned to launch an instance from either the [Dashboard](../launch-and-mange-instances/launch-an-instance-via-dashboard.md) or the [CLI](../launch-and-mange-instances/launch-an-instance-via-cli.md)

