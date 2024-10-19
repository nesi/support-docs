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

## List images

You are able to list the images that you have uploaded to the FlexiHPC platform using the command `openstack image list --<private/shared>`

```
openstack image list --private
```

``` { .sh .no-copy }
+--------------------------------------+------------------------+--------+
| ID                                   | Name                   | Status |
+--------------------------------------+------------------------+--------+
| 64dead14-9c5a-41c3-b4d6-a122a2ca8f28 | linux-test-snapshot    | active |
| d479470d-ab6d-40d6-afc9-04f5f253404d | linux-test-to-boot-2   | active |
| 40ed5c78-c970-4182-a9c8-27e18a6a4251 | linux-test-to-boot-cli | active |
| 5a8e5595-d893-4d1c-8600-d7982f3915bb | ood-keycloak-1         | active |
| 04e1a31a-adee-4af2-935e-0e6e7c4b3193 | test-break             | active |
+--------------------------------------+------------------------+--------+
```

```
openstack image list --shared
```

``` { .sh .no-copy }
+--------------------------------------+------------------------------+--------+
| ID                                   | Name                         | Status |
+--------------------------------------+------------------------------+--------+
| 2282be79-1b79-434b-9974-162b533dab00 | Ubuntu-22.10-Wiki-Test       | active |
| 1a0480d1-55c8-4fd7-8c7a-8c26e52d8cbd | ubuntu-jammy-server-cloudimg | active |
+--------------------------------------+------------------------------+--------+
```

Adding `--long` to either command will present more information regarding the image

```
openstack image list --shared --long
```

``` { .sh .no-copy }
+--------------------------------------+------------------------------+-------------+------------------+-----------+----------------------------------+--------+------------+-----------+----------------------------------+------+
| ID                                   | Name                         | Disk Format | Container Format |      Size | Checksum                         | Status | Visibility | Protected | Project                          | Tags |
+--------------------------------------+------------------------------+-------------+------------------+-----------+----------------------------------+--------+------------+-----------+----------------------------------+------+
| 2282be79-1b79-434b-9974-162b533dab00 | Ubuntu-22.10-Wiki-Test       | raw         | bare             | 740491264 | 91c3094a3ff142ce651034d41aa860c3 | active | shared     | False     | 4f07cc254d6c4471805d49bae1f739b9 |      |
| 1a0480d1-55c8-4fd7-8c7a-8c26e52d8cbd | ubuntu-jammy-server-cloudimg | qcow2       | bare             | 688193536 | e05c516fa30cf6c0fd47930449b85ac7 | active | shared     | False     | 4f07cc254d6c4471805d49bae1f739b9 |      |
+--------------------------------------+------------------------------+-------------+------------------+-----------+----------------------------------+--------+------------+-----------+----------------------------------+------+
```

## Updating an image

If you need to modify the image details or metadata, the general practice is to create a new image with the desired changes rather than directly editing the existing one. After creating the new image, you can delete the old image if it's no longer needed.

If you need to update an Image this can be done via the Dashboard

## Deleting an image

Using the same command `openstack image list --<private/shared>` get the `image id` as you will need to supply that to the following command

```
openstack image delete image_id
```

!!! info
    Deleting an image that has been used to create a compute instance will fail until that instance has been deleted