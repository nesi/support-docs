---
created_at: '2021-08-27T03:18:13Z'
tags: []
title: Data Transfer using Globus
---

## Globus

Globus is a third-party service for transferring large amounts of data
between Globus Data Transfer Nodes (DTNs).

While NeSI supports use of other data transfer tools and protocols such
as `scp`, Globus provides the most comprehensive, efficient, and easy to
use service for NeSI users who need to move large data sets (more than a
few gigabytes at a time).

Using Globus, you can transfer
data between the NeSI HPC platform and a Globus endpoint created on your personal workstation or at your institution. With Globus, high
data transfer rates are achievable.

To use Globus to transfer data to/from NeSI platforms, you need:

1. A Globus account (see
  [Initial Globus Sign-Up and Globus ID](./Initial_Globus_Sign_Up-and_your_Globus_Identities.md))
2. An active NeSI account (see
  [Creating a NeSI Account](../../Getting_Started/Creating_an_Account.md))
3. Access privileges to the Globus endpoint/collection you
   plan on transferring data from or to. This endpoint/collection
   could be a personal one on your workstation, or it could be managed
   by your institution or a third party.

    - *Note: A NeSI user account does not create a Globus account, and
        similarly a Globus account does not create a NeSI user account. Nor
        can you, as the end user, link the two through any website.*

Both your accounts (NeSI and Globus) must exist before you try to use the NeSI DTN.

## Types of Globus endpoints or Data Transfer Nodes

Globus data transfers take place between *endpoints*. An endpoint is
nothing more than an operating system (Windows, Linux, etc) that has the
Globus endpoint software installed on it.

Endpoints come in two kinds:

- personal
- server

Within an endpoint users can access data via collections, with specific permissions settings for sharing with others.

## The NeSI Data Transfer Node

The Data Transfer Node (DTN) for the NeSI platforms is called 'NeSI HPC Storage'. This endpoint acts as an interface between our HPC
facility storage and a worldwide network of Globus endpoints.

The NeSI HPC Storage endpoint is an example of a *server endpoint*. These types of
endpoints are usually configured to access large capacity and
high-performance parallel filesystems. Endpoints can be unmanaged or
managed by a subscription. NeSI DTN is a server type, managed endpoint
(by NeSI subscription) which allows authorised users to provide data
transfer and data sharing services on behalf of their Globus accounts.

Your institution may have its own managed server endpoint, and if so we
encourage you to use that endpoint for your data transfers between your
institution and NeSI. You may need to apply to the person or group
administering the managed server endpoint, most likely your IT team, to
get access to the endpoint. Your institution may even have several
endpoints, in which case we recommend that you consider which one would
be best suited for your data transfer requirements. If you need any help,
{% include "partials/support_request.html" %} or
consult your institution's IT team.

If your institution doesn't have a managed server endpoint, you can set
up a personal endpoint using software provided by Globus (see below).
Please be aware that even if you set up a personal endpoint, you may
still need to consult your IT team in order to make it usable,
especially if your institution has an aggressive firewall.

## Transferring data using a managed endpoint

As an example, to move files between the NeSI HPC Storage endpoint and the Otago University high-capacity central
file storage (another managed server endpoint):

!!! info
    Log in to the [NeSI File Manager](https://transfer.nesi.org.nz/file-manager) where you are able to search for DTNs in the Collection field.
    [Listing of available endpoints on the New Zealand Data Transfer Platform](National_Data_Transfer_Platform.md)

Find the NeSI endpoint by typing in "NeSI HPC Storage". Select the
endpoint "NeSI HPC Storage" from the list, and you will be asked
to authenticate your access to the endpoint.

Click Continue to the next step.

You'll be asked to select an identity to continue.
Choose **&lt;username&gt;@iam.nesi.org.nz**.

- *Note:*
OpenID Connect (OIDC) in Globus is used to enable secure authentication and authorization for accessing resources within the Globus ecosystem, particularly on Globus Connect Server endpoints. If this is your first login, you may be asked to *bind* your primary identity to the OICD login, and you will need to allow that.

The NeSI HPC Storage endpoint is protected by Tuakiri
authentication.

After the login, you will navigate to the default root (display as "/") path, then you could change the path to

\(1\) your ***/home/&lt;username&gt;*** directory,

\(2\) project directory (read-only)
***/nesi/project/&lt;project\_code&gt;***

\(3\) project sub-directories of
***/nesi/nobackup/&lt;project\_code&gt;*** - see
[Globus Paths,Permissions, Storage Allocation](./Globus_Paths-Permissions-Storage_Allocation.md).  
  
Navigate to your selected directory. e.g. the `nobackup` filesystem
`/nesi/nobackup/<project_code>` and select the two-endpoint panel
for transfer.

![mceclip3.png](../../assets/images/Data_Transfer_using_Globus_V8.png)

Select the target endpoint and authenticate.

When you have activated endpoints in both transfer windows, you can
start transferring files between them.

![mceclip4.png](../../assets/images/Data_Transfer_using_Globus_V9.png)

Select files you wish to transfer and select the corresponding "Start"
button:  
  
![mceclip5.png](../../assets/images/Data_Transfer_using_Globus_V10.png)

To find other NeSI endpoints, type in "nesi#":

![filemanage\_nesi.png](../../assets/images/Data_Transfer_using_Globus_V11.png)

## In brief

- Sign in to the NeSI Globus Web App <https://transfer.nesi.org.nz/>.
  You will be taken to the *File Manager* page
  <https://transfer.nesi.org.nz/file-manager>
- If this is your first time, you will need to create a Globus
  account.
- Open the two-endpoint panel
  ![two_endpoint.png](../../assets/images/Data_Transfer_using_Globus_V12.png){: style="height:2em;"} located
  on the top-right of the *File Manager* page.
- Select the Endpoints you wish to move files between (start typing
  "nesi#" to see the list of NeSI endpoints to select from).
  [Authenticate](./Globus_endpoint_activation.md)
  at both endpoints.
- At Globus.org the endpoint **defaults to
  `/home/<username>` path** (represented by `~`) on the NeSI platform. We do not recommend uploading data to your home directory, as
  home directories are very small. Instead, navigate to an appropriate
  project directory under /nobackup (see
  [Globus Paths, Permissions,  Storage  Allocation](./Globus_Paths-Permissions-Storage_Allocation.md)).
- Transfer the files by clicking the appropriate
  ![start.png](../../assets/images/Data_Transfer_using_Globus_V13.png){: style="height:1em;"} button
  depending on the direction of the transfer.
- Check your email for confirmation about the job completion report.

## Transferring data using a personal endpoint

To transfer files to/from your laptop, desktop computer or any other
system you control, configure it as a [Globus Personal
Endpoint](https://www.globus.org/globus-connect-personal) (see
[Personal Globus Endpoint Configuration](./Personal_Globus_Endpoint_Configuration.md)
for transfers between personal endpoints).

## File sharing

To share files with others outside your filesystem,
see [https://docs.globus.org/how-to/share-files/](https://docs.globus.org/how-to/share-files/).

## Using Globus to transfer data to or from the cloud

Globus connectors enable a uniform interface for accessing, moving, and
sharing across a variety of cloud providers. We do not currently have a
connector subscription (note a subscription is required per cloud
provider) so we can't use globus to transfer to/from cloud storage. If
you see this as key for you, please {% include "partials/support_request.html" %}.

Our current advice for moving data to or from the cloud is to use tools
such as Rclone ([https://rclone.org/](https://rclone.org/)) or the
cloud CLI's such as aswcli for S3 [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/) or
gcloud CLI
([https://cloud.google.com/sdk/gcloud](https://cloud.google.com/sdk/gcloud)).
If you have any trouble or would like further advice, please {% include "partials/support_request.html" %}.
