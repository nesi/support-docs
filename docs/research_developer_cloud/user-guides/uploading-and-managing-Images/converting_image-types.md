---
hidden: false
label_names:
- images
- convert
position: 1
title: Converting Image types
vote_count: 1
vote_sum: 1
---

!!! note
    The following commands are generally run from the CLI, you dont need the Openstack CLI to complete these tasks just ensure you have `qemu-img` pakcage installed

Converting images from one format to another is generally straightforward and can be done from a single simple command

The `qemu-img convert` command can do conversion between multiple formats, including qcow2, qed, raw, vdi, vhd, and vmdk.

qemu-img format strings:

| Image Format | Argument to qemu-img |
|:-:|:-:|
| QCOW2 (KVM, Xen) | `qcow2` |
| QED (KVM) | `qed` |
| raw | `raw` |
| VDI (VirtualBox) | `vdi` |
| VHD (Hyper-V) | `vpc` |
| VMDK (VMware) | `vmdk` |

!!! note
    The main formats used in the RDC are either `RAW` or `QCOW2`


The following command example will convert a raw image file named `image.img` to a `qcow2` image file, the `-f` specifies the first image format and the `-O` specifies the output format

``` { .sh }
qemu-img convert -f raw -O qcow2 image.img image.qcow2
```

The following command example will convert a vmdk image file to a raw image file

``` { .sh }
qemu-img convert -f vmdk -O raw image.vmdk image.img
```

The following command example will convert a vmdk image file to a qcow2 image file

``` { .sh }
qemu-img convert -f vmdk -O qcow2 image.vmdk image.qcow2
```

!!! note
    The `-f format` flag is optional. If omitted, qemu-img will try to infer the image format.

    When converting an image file with Windows, ensure the virtio driver is installed. Otherwise, you will get a blue screen when launching the image due to lack of the virtio driver. Another option is to set the image properties as below when you update the image in the Image service to avoid this issue, but it will reduce virtual machine performance significantly.

    ``` { .sh }
    openstack image set --property hw_disk_bus='ide' image_name_or_id
    ```