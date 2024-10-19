---
hidden: false
label_names:
- identity
- create
- manage
- cli
title: Creating and Managing Application Credentials via CLI
---

!!! note
    The openstack CLI will need to be setup to interact with the FlexiHPC system. Please read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) to interact with FlexiHPC to get started.

## Create Application Credential

Running the below command will generate a new `Application Credential`

```
openstack application credential create
    [--secret <secret>]
    [--role <role>]
    [--expiration <expiration>]
    [--description <description>]
    [--unrestricted]
    [--restricted]
    [--access-rules <access-rules>]
    <name>
```

`--secret <secret>`
:   Secret to use for authentication. If not provided, one will be generated

`--role <role>`
:   Roles to authorize (name or ID) (repeat option to set multiple values), if not provided this will default to same roles as the user that creates it

`--expiration <expiration>`
:   Sets an expiration date for the application credential, format of YYYY-mm-ddTHH:MM:SS, if not provided, the application credential will not expire.

`--description <description>`
:   Application credential description

`--unrestricted`
:   Enable application credential to create and delete other application credentials and trusts

!!! warning
    This is potentially dangerous behavior and is disabled by default

`--restricted`
:   Prohibit application credential from creating and deleting other application credentials and trusts, this is enabled by default.

`--access-rules <access-rules>`
:   Either a string or file path containing a JSON-formatted list of access rules, each containing a request method, path, and service, for example ‘[{“method”: “GET”, “path”: “/v2.1/servers”, “service”: “compute”}]’

`name`
:   Name of the application credential

Command example below with only a name supplied

```
openstack application credential create wiki-test-app-creds
```

``` { .sh .no-copy }
+--------------+----------------------------------------------------------------------------------------+
| Field        | Value                                                                                  |
+--------------+----------------------------------------------------------------------------------------+
| description  | None                                                                                   |
| expires_at   | None                                                                                   |
| id           | 0f81c516aa6e443dba0aec93b0bbd87e                                                       |
| name         | wiki-test-app-creds                                                                    |
| project_id   | 4f07cc254d6c4471805d49bae1f739b9                                                       |
| roles        | heat_stack_owner reader _member_ load-balancer_member member                           |
| secret       | <APPLICATION_CREDS_SECRET>                                                             |
| system       | None                                                                                   |
| unrestricted | False                                                                                  |
| user_id      | fb9a3d02c89e4cfdbe64658ad43ece97                                                       |
+--------------+----------------------------------------------------------------------------------------+
```

!!! note
    Once the `Application Credentails` are created the secret will be displayed. You need to take note of this now as there is no way to get that secret again and a new `Application Credential` will need to be created should you misplace it.

## List Application Credentials

Running the below command will list all `Application Credentials` in your project

```
openstack application credential list
```

``` { .sh .no-copy }
+----------------------------------+---------------------+----------------------------------+-------------+------------+
| ID                               | Name                | Project ID                       | Description | Expires At |
+----------------------------------+---------------------+----------------------------------+-------------+------------+
| 0f81c516aa6e443dba0aec93b0bbd87e | wiki-test-app-creds | 4f07cc254d6c4471805d49bae1f739b9 | None        | None       |
+----------------------------------+---------------------+----------------------------------+-------------+------------+
```

## Show Application Credentials details

Running the below command will present additional details about the Application Credentials

```
openstack application credential show APPLICATION_CRED_ID
```

``` { .sh .no-copy }
+--------------+--------------------------------------------------------------+
| Field        | Value                                                        |
+--------------+--------------------------------------------------------------+
| description  | None                                                         |
| expires_at   | None                                                         |
| id           | 0f81c516aa6e443dba0aec93b0bbd87e                             |
| name         | wiki-test-app-creds                                          |
| project_id   | 4f07cc254d6c4471805d49bae1f739b9                             |
| roles        | reader load-balancer_member _member_ member heat_stack_owner |
| system       | None                                                         |
| unrestricted | False                                                        |
| user_id      | fb9a3d02c89e4cfdbe64658ad43ece97                             |
+--------------+--------------------------------------------------------------+
```

## Deleting Application Credentials

Run the command `openstack application credential list` to get the `ID` of the `Application Credentials` you would like to delete

Then with the `ID` run the below command to delete it

```
openstack application credential delete APPLICATION_CRED_ID
```

There will be no response, so you can run the list command again to confirm deletion 