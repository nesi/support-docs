---
hidden: false
label_names:
- object storage
- create
- manage
- cli
position: 1
title: Create and manage object storage via CLI
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

## Create new container

Running the below command will generate a new container within the projects object storage

``` { .sh }
openstack container create <CONTAINER_NAME>
```

You will get a response from the server that looks like the following


``` { .sh .no-copy }
+-------------+------------------+-----------------------------+
| account     | container        | x-trans-id                  |
+-------------+------------------+-----------------------------+
| AUTH_<GUID> | <CONTAINER_NAME> | tx00000<X_TRANS_GUID>-akl-1 |
+-------------+------------------+-----------------------------+
```

## List containers

Running the below command will list all containers within the projects object storage

``` { .sh }
openstack container list
```
``` { .sh .no-copy }
+------------------+
| Name             |
+------------------+
| a-test-container |
| boto3-test       |
| cli-container    |
| terraform-state  |
+------------------+
```

The command `openstack container list` also has some additional parameters

`--prefix <prefix>`
:   Filter the list using a prefix, example if we use the prefix `a` then the only container returned would the `a-test-container`

`--marker <marker>`
:   Start anchor for paging is used when you wish to return a specified list of containers should you have a lot of them

`--end-marker <end-marker>`
:   End anchor for paging

`--limit <num-containers>`
:   Limit the number of containers returned

`--long`
:   List additional fields in output that contain the amount of space used and number of files inside the container

`--all`
:   List all containers (default is 10000)

## Display container details

Running the below command will display additional details about the container specified

``` { .sh }
openstack container show CONTAINER_NAME
```
``` { .sh .no-copy }
+----------------+---------------------------------------+
| Field          | Value                                 |
+----------------+---------------------------------------+
| account        | AUTH_<AUTH_TOKEN>                     |
| bytes_used     | 0                                     |
| container      | <CONTAINER_NAME>                      |
| object_count   | 0                                     |
| storage_policy | default-placement                     |
+----------------+---------------------------------------+
```

## Save container contents local

Running the below command will save all the container contents to your local directory where you run the command

``` { .sh }
openstack container save CONTAINER_NAME
```

## Delete container

Run the `openstack container list` command first to get the name of the container you wish to delete

``` { .sh }
openstack container list
```
``` { .sh .no-copy }
+------------------+
| Name             |
+------------------+
| a-test-container |
| boto3-test       |
| cli-container    |
| terraform-state  |
+------------------+
```

Then run the below command to delete the container you wish to remove

``` { .sh }
openstack container delete CONTAINER_NAME
```

Your container should then be removed, however should you container contain any files you will get the following error

``` { .sh .no-copy}
openstack container delete a-test-container
Conflict (HTTP 409) (Request-ID: tx00000a9dff65235cbe523-0064dadec9-a09387f-akl-1)
```

Supplying the `--recursive, -r` parameter will delete all files within that container before deleting it

``` { .sh }
openstack container delete --recursive <CONTAINER_NAME>
```