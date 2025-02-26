## Accessing object storage with Cyberduck

!!! note
    You will need [EC2 credentials](creating-and-managing-ec2-credentials-via-cli.md) to use Cyberduck

Cyberduck is a libre server and cloud storage browser for Mac and Windows with support for FTP, SFTP, WebDAV, Amazon S3, OpenStack Swift, Backblaze B2, Microsoft Azure & OneDrive, Google Drive and Dropbox.

## Installation

Cyberduck can be downloaded and installed from the [Cyberduck website](https://cyberduck.io/). You can also get it from the Windows Store or the Apple Mac App Store. Instructions for installing can be found at the respective locations.

## Connecting using Cyberduck

Once Cyberduck is installed you will want to start it and click on `Open Connection`

<figure markdown>
  ![Alt text](cyberduck-overview.png)
</figure>

Within the `Open Connection` dialog you will want to ensure that the dropdown has selected `Amazon S3`

<figure markdown>
  ![Alt text](cyberduck-connection-dialog.png)
</figure>

We then need to update the details to interact and auth with FlexiHPC

`Server`
:   Server should be updated to `object.akl-1.cloud.nesi.org.nz` and the port should be 443

`Access Key ID`
:   This should be the EC2 Credentials Access key token

`Secret Access Key`
:   This should be the EC2 Credentials Secret key token

<figure markdown>
  ![Alt text](cyberduck-connection-dialog-rdc.png)
</figure>

Click on `Connect` to open the connection

<figure markdown>
  ![Alt text](cyberduck-container-view.png)
</figure>
