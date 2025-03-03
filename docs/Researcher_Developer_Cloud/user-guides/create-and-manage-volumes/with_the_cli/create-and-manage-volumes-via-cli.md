---
hidden: false
label_names:
- volumes
- create
- manage
- cli
position: 1
title: Create and manage volumes via CLI
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

## Create an empty volume

Running the following command will create a volume with 8 gibibytes (GiB) of space, and specify the availability zone. This is creates an empty volume that does not contain a file system or a partition table:

```
openstack volume create --size 8 --availability-zone nova my-new-volume
```

``` { .sh .no-copy }
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| attachments         | []                                   |
| availability_zone   | nova                                 |
| bootable            | false                                |
| consistencygroup_id | None                                 |
| created_at          | 2023-08-04T03:40:29.634209           |
| description         | None                                 |
| encrypted           | False                                |
| id                  | f297c807-1eb3-4b48-8438-04d995ca498a |
| multiattach         | False                                |
| name                | my-new-volume                        |
| properties          |                                      |
| replication_status  | None                                 |
| size                | 8                                    |
| snapshot_id         | None                                 |
| source_volid        | None                                 |
| status              | creating                             |
| type                | ceph-ssd                             |
| updated_at          | None                                 |
| user_id             | fb9a3d02c89e4cfdbe64658ad43ece97     |
+---------------------+--------------------------------------+
```

To verify that your volume was created successfully, list the available volumes:

```
openstack volume list
```

``` { .sh .no-copy }
+--------------------------------------+---------------+-----------+------+-------------+
| ID                                   | Name          | Status    | Size | Attached to |
+--------------------------------------+---------------+-----------+------+-------------+
| f297c807-1eb3-4b48-8438-04d995ca498a | my-new-volume | available |    8 |             |
+--------------------------------------+---------------+-----------+------+-------------+
```

If your volume was created successfully, its status is `available`. If its status is `error`, you might have exceeded your quota.

## Attach a volume to an instance

Attach your volume to a server, specifying the server ID and the volume ID:

```
openstack server add volume <COMPUTE INSTANCE ID> <VOLUME ID> --device /dev/vdb
```

Show information for your volume:

```
openstack volume show f297c807-1eb3-4b48-8438-04d995ca498a
```

The output shows that the volume is attached to the server with ID `84c6e57d-a6b1-44b6-81eb-fcb36afd31b5`, is in the nova availability zone, and is bootable.

``` { .sh .no-copy }
+------------------------------+--------------------------------------+
| Field                        | Value                                |
+------------------------------+--------------------------------------+
| attachments                  | [{u'device': u'/dev/vdb',            |
|                              |        u'server_id': u'84c6e57d-a    |
|                              |           u'id': u'573e024d-...      |
|                              |        u'volume_id': u'573e024d...   |
| availability_zone            | nova                                 |
| bootable                     | false                                |
| consistencygroup_id          | None                                 |
| created_at                   | 2023-08-04T03:40:29.000000           |
| description                  | None                                 |
| encrypted                    | False                                |
| id                           | f297c807-1eb3-4b48-8438-04d995ca498a |
| multiattach                  | False                                |
| name                         | my-new-volume                        |
| os-vol-tenant-attr:tenant_id | 4f07cc254d6c4471805d49bae1f739b9     |
| properties                   |                                      |
| replication_status           | None                                 |
| size                         | 8                                    |
| snapshot_id                  | None                                 |
| source_volid                 | None                                 |
| status                       | available                            |
| type                         | ceph-ssd                             |
| updated_at                   | 2023-08-04T03:40:29.000000           |
| user_id                      | fb9a3d02c89e4cfdbe64658ad43ece97     |
+------------------------------+--------------------------------------+
```

## Detach a volume from an instance

Detach your volume from a server, specifying the server ID and the volume ID:

```
openstack server remove volume <COMPUTE INSTANCE ID> <VOLUME ID>
```

Show information for your volume:

```
openstack volume show f297c807-1eb3-4b48-8438-04d995ca498a
```

The output shows that the volume is no longer attached to the server:

``` { .sh .no-copy }
+------------------------------+--------------------------------------+
| Field                        | Value                                |
+------------------------------+--------------------------------------+
| attachments                  | []                                   |
| availability_zone            | nova                                 |
| bootable                     | false                                |
| consistencygroup_id          | None                                 |
| created_at                   | 2023-08-04T03:40:29.000000           |
| description                  | None                                 |
| encrypted                    | False                                |
| id                           | f297c807-1eb3-4b48-8438-04d995ca498a |
| multiattach                  | False                                |
| name                         | my-new-volume                        |
| os-vol-tenant-attr:tenant_id | 4f07cc254d6c4471805d49bae1f739b9     |
| properties                   |                                      |
| replication_status           | None                                 |
| size                         | 8                                    |
| snapshot_id                  | None                                 |
| source_volid                 | None                                 |
| status                       | available                            |
| type                         | ceph-ssd                             |
| updated_at                   | 2023-08-04T03:40:29.000000           |
| user_id                      | fb9a3d02c89e4cfdbe64658ad43ece97     |
+------------------------------+--------------------------------------+
```

## Resize a volume

To resize your volume, you must first detach it from the server if it is current. To detach the volume from your server, pass the server ID and volume ID to the following command:

```
openstack server remove volume <COMPUTE INSTANCE ID> <VOLUME ID>
```

This command does not provide any output.

```
openstack volume list
```

``` { .sh .no-copy }
+--------------------------------------+---------------+-----------+------+-------------+
| ID                                   | Name          | Status    | Size | Attached to |
+--------------------------------------+---------------+-----------+------+-------------+
| f297c807-1eb3-4b48-8438-04d995ca498a | my-new-volume | available |    8 |             |
+--------------------------------------+---------------+-----------+------+-------------+
```

Note that the volume is now available.

Resize the volume by passing the volume ID and the new size (a value greater than the old one) as parameters:

```
openstack volume set f297c807-1eb3-4b48-8438-04d995ca498a --size 10
```

This command does not provide any output.

## Delete a volume

To delete your volume, you must first detach it from the server. Delete the volume the volume ID:

```
openstack volume delete f297c807-1eb3-4b48-8438-04d995ca498a
```

This command does not provide any output.

List the volumes again, and note that the status of your volume is `deleting`:

```
openstack volume list
```

``` { .sh .no-copy }
+----------------+-----------------+-----------+------+-------------+
|       ID       |   Display Name  |  Status   | Size | Attached to |
+----------------+-----------------+-----------+------+-------------+
| f297c807-1e... |  my-new-volume  |  deleting |  8   |             |
+----------------+-----------------+-----------+------+-------------+
```

When the volume is fully deleted, it disappears from the list of volumes:

``` { .sh .no-copy }
+--------------------------------------+------+-----------+------+-------------+
| ID                                   | Name | Status    | Size | Attached to |
+--------------------------------------+------+-----------+------+-------------+
| d0d686e9-bcfe-499b-850d-50f4a998ad81 |      | available |   30 |             |
+--------------------------------------+------+-----------+------+-------------+
```
