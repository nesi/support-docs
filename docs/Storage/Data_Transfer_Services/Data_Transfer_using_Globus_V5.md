Globus
------

Globus is a third-party service for transferring large amounts of data
between Globus Data Transfer Nodes (DTNs). With Globus, very high data
transfer rates are achievable. This service allows data to be accessible
to any person who has a Globus account. The newest implementation (v5)
provides extra features and some key differences from the previous setup
that you can find
[here](https://docs.globus.org/globus-connect-server/). 

To use Globus on NeSI platforms, you need:

1.  A Globus account (see [Initial Globus Sign-Up and Globus
    Id](https://support.nesi.org.nz/hc/en-gb/articles/360000817476))
2.  An active NeSI account (see [Creating a NeSI
    Account](https://support.nesi.org.nz/hc/en-gb/articles/360000159715))
3.  Access privileges on the non-NeSI Globus endpoint/collection you
    plan on transferring data from or to. This other endpoint/collection
    could be a personal one on your workstation, or it could be managed
    by your institution or a third party.

-   *Note that a NeSI user account does not create a Globus account, and
    similarly a Globus account does not create a NeSI user account. Nor
    can you, as the end user, link the two through any website.*

Both your accounts (NeSI and Globus) must exist before you try to use
our DTN.

The NeSI Wellington DTN endpoint is protected by a second factor
authentication (2FA).

[The NeSI Data Transfer Node]{.wysiwyg-color-black}
---------------------------------------------------

The NeSI Data Transfer Node (DTN) acts as an interface between our HPC
facility storage and a worldwide network of Globus endpoints. This is
achieved using Globus.org, a web-based service that solves many of the
challenges encountered moving large volumes of data between systems.
While NeSI supports use of other data transfer tools and protocols such
as `scp`{.bash}, Globus provides the most comprehensive, efficient, and
easy to use service for NeSI users who need to move large data sets
(more than a few gigabytes at a time).

Types of Globus endpoints or Data Transfer Nodes
------------------------------------------------

Globus data transfers take place between *endpoints*. An endpoint is
nothing more than an operating system (Windows, Linux, etc) that has the
Globus endpoint software installed on it. Endpoints come in two kinds:
personal and server. Within a endpoint users can access data via
collections, with specific permissions and the ability to shared with
others.

The NeSI DTN is an example of a *server endpoint*. These type of
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
be best suited for your data transfer requirements. If you need any help
in regards to this, get in touch with us via <support@nesi.org.nz>, or
consult your institution\'s IT team.

If your institution doesn\'t have a managed server endpoint, you can set
up a personal endpoint using software provided by Globus (see below).
Please be aware that even if you set up a personal endpoint, you may
still need to consult your IT team in order to make it usable,
especially if your institution has an aggressive firewall.

Transferring data using a managed endpoint
------------------------------------------

As an example, to move files between the NeSI HPC Storage (accessible
from Māui and Mahuika) and the Otago University high-capacity central
file storage (another managed server endpoint):

::: {.callout .callout--info}
Log in to the [NeSI File
Manager](https://transfer.nesi.org.nz/file-manager){.external-link}
where you are able to search for DTNs in the *Collection* field.\
[Here](https://support.nesi.org.nz/hc/en-gb/articles/360000931775) is a
listing of available endpoints on the New Zealand Data Transfer
Platform.
:::

NeSI endpoints start with \"nesi\#\":

![filemanage\_nesi.png](https://support.nesi.org.nz/hc/article_attachments/4940171187343/filemanage_nesi.png)

Select the endpoint \"Nesi Wellington DTN V5\", and you will be asked to
authenticate your access to the endpoint. Click Continue to the next
step.

![mceclip0.png](https://support.nesi.org.nz/hc/article_attachments/4405622947215/mceclip0.png)

 

You can choose either of **\<username\>\@wlg-dtn-oidc.nesi.org.nz** or
NeSI Wellington OIDC Server (wlg-dtn-oidc.nesi.org.nz), they are all
linked to the same website. If this is your first time login, you may
ask to *bind* your primary identity to the OIDC login, you need to allow
that.

 

![mceclip1.png](https://support.nesi.org.nz/hc/article_attachments/4405622955791/mceclip1.png)

The NeSI Wellington DTN V5 endpoint is protected by a second factor
authentication (2FA-same as accessing NeSI clusters).  In the
\'**Username\'** field, enter your Māui/Mahuika username. In the
\'**Password\'** field, your `Password`{.c-mrkdwn__code
data-stringify-type="code"} will be equal to
`Login Password (First Factor)`{.c-mrkdwn__code
data-stringify-type="code"} +
`Authenticator Code (Second Factor)`{.c-mrkdwn__code
data-stringify-type="code"} e.g. `password123456`{.c-mrkdwn__code
data-stringify-type="code"}. (***Do not*** use any additional characters
or spaces between your password and the token number.)

                           
![mceclip0.png](https://support.nesi.org.nz/hc/article_attachments/4408962414351/mceclip0.png)

After the login, you will navigate to the default root(display as \"/\")
path, then you could change the path to

\(1) your ***/home/\<username\>*** directory,

\(2) project directory (read-only) ***/nesi/project/\<project\_code\>*** 

\(3) project sub-directories of ***/nesi/nobackup/\<project\_code\>***  -
see [Globus Paths, Permissions,  Storage
Allocation.](https://support.nesi.org.nz/hc/en-gb/articles/360000812776-Globus-Paths-Permissions-Storage-Allocation)\
\
Navigate to your selected directory. e.g. the *nobackup* filesystem
*/nesi/nobackup/\<project\_code\>* and select the two-endpoint panel for
transfer.

![mceclip3.png](https://support.nesi.org.nz/hc/article_attachments/4405623113615/mceclip3.png)

Select the target endpoint and authenticate.

When you have activated endpoints in both transfer windows, you can
start transferring files between them.

![mceclip4.png](https://support.nesi.org.nz/hc/article_attachments/4405623130383/mceclip4.png)

Select files you wish to transfer and select the corresponding \"Start\"
button:\
\
![mceclip5.png](https://support.nesi.org.nz/hc/article_attachments/4405623291791/mceclip5.png)

 

In brief:
---------

-   Sign in to the NeSI Globus Web App <https://transfer.nesi.org.nz/>.
    You will be taken to the *File Manager* page
    <https://transfer.nesi.org.nz/file-manager>
-   If this is your first time, you will need to create a Globus
    account.
-   Open the two-endpoint
    panel ![two\_endpoint.png](https://support.nesi.org.nz/hc/article_attachments/360001823596/two_endpoint.png){width="123"
    height="38"} located on the top-right of the *File Manager* page.
-   Select the Endpoints you wish to move files between (start typing
    \"nesi\#\" to see the list of NeSI DTNs to select from).
    [Authenticate](https://support.nesi.org.nz/hc/en-gb/articles/360000955535)
    at both endpoints.
-   At Globus.org the** **endpoint **[defaults]{.wysiwyg-underline} to
    \"/home/\<username\>\" path** (represented by \"/\~/\") on Mahuika
    or Māui. We do not recommend uploading data to your home directory,
    as home directories are very small. Instead, navigate to an
    appropriate project directory under /nobackup (see [Globus Paths,
    Permissions, Storage
    Allocation](https://support.nesi.org.nz/hc/en-gb/articles/360000812776-Globus-Paths-Permissions-Storage-Allocation)).
-   Transfer the files by clicking the
    appropriate ![start\_button.png](https://support.nesi.org.nz/hc/article_attachments/360001713755/start_button.png) button
    depending on the direction of the transfer.
-   Check your email for confirmation about the job completion report.

Transferring data using a personal endpoint
-------------------------------------------

To transfer files into/out of your laptop, desktop computer or any other
system you control, configure it as a [Globus Personal
Endpoint](https://www.globus.org/globus-connect-personal) (see [Personal
Globus Endpoint
Configuration](https://support.nesi.org.nz/hc/en-gb/articles/360000217915-Personal-Globus-Endpoint-Configuration) for
transfers between personal endpoints).

File sharing
------------

To share files with others outside your filesystem,
see <https://docs.globus.org/how-to/share-files/>
