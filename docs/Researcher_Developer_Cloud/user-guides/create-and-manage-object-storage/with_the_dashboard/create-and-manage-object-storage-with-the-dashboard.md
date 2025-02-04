---
hidden: false
label_names:
- object storage
- create
- manage
- dashboard
position: 1
title: Create and manage object storage via the dashboard
---

## Creating an object storage container

Log into the [NeSI FlexiHPC Dashboard](https://dashboard.cloud.nesi.org.nz/)

Select the project you would like to deploy the new instance too (Use the project selector on the top left-hand side):

<figure markdown>
  ![Alt text](../../../assets/images/flexi/project-selector.png)
</figure>

Open the `Project` tab, open the `Object Storage` tab and select the `Containers` category

Click `+ Container`.

<figure markdown>
  ![Alt text](../../../assets/images/flexi/object-storage-overview.png)
</figure>

Within the `Create Container` dialog you have a few options

`Container Name`
:   A friendly name for your container. It must not contain “/” in its name.

`Storage Policy`
:   This defaults to default-placement and is the only option available at this time.

`Container Access`
:   You have a choice between `public` or `not-public`

    A `Public` container will allow anyone with the public URL to gain access to your objects in the container

Once you have given the container a name and decided if its public or private click `Submit` to create the container.

## Deleting an object storage container

!!! note
    You are not able to delete a container if there are items present within it. Please delete all items before attempting to delete the container.

Log into the [NeSI FlexiHPC Dashboard](https://dashboard.cloud.nesi.org.nz/)

Select the project you would like to deploy the new instance too (Use the project selector on the top left-hand side):

<figure markdown>
  ![Alt text](../../../assets/images/flexi/project-selector.png)
</figure>

Open the `Project` tab, open the `Object Storage` tab and select the `Containers` category

Select the container you would like to delete and it should highlight with blue

<figure markdown>
  ![Alt text](../../../assets/images/flexi/object-storage-container-overview.png)
</figure>

Hovering over the `Trashcan Icon` should show a tooltip that says *Delete Container* and clicking it should present a `Confirm Delete` dialog.

If you are certain that you wish to delete the container click `Delete` and the container should be removed

## Upload a file to a storage object container

!!! note
    Files uploaded into a FlexiHPC storage via the dashboard are saved as a binary/octet-stream which means they are only downloaded when they are requested via the URL.

    There is also an issue where the public URL provided via the dashboard doesn't auth correctly so you are unable to view/download files. 

    The URL that currently works should you wish to view/download a file from object storage looks like the following https://object.akl-1.cloud.nesi.org.nz/*CONTAINER_NAME*/*FILE_NAME*

Log into the [NeSI FlexiHPC Dashboard](https://dashboard.cloud.nesi.org.nz/)

Select the project you would like to deploy the new instance too (Use the project selector on the top left-hand side):

<figure markdown>
  ![Alt text](../../../assets/images/flexi/project-selector.png)
</figure>

Open the `Project` tab, open the `Object Storage` tab and select the `Containers` category

Select the container you would like to delete and it should highlight with blue

<figure markdown>
  ![Alt text](../../../assets/images/flexi/object-storage-container-overview.png)
</figure>

On the far right there should be 3 icons, `Upload File` `+ Folder` and `Delete Item`

Click the `Upload File` icon and within the `Upload File` dialog clicking `Choose File` should allow you to browse to the file on your local machine. You are also able to give it a different name should you so choose.

<figure markdown>
  ![Alt text](../../../assets/images/flexi/object-storage-upload-dialog.png)
</figure>

Clicking `Upload File` will now begin to upload that file to the object storage container. The time it takes to complete the upload will depend on the file size and the network upload speed.

## Create a folder like structure in an object storage container

We say folder like structure as that is what it looks like from the dashboards perspective, however under lying this the structure is flat.

Log into the [NeSI FlexiHPC Dashboard](https://dashboard.cloud.nesi.org.nz/)

Select the project you would like to deploy the new instance too (Use the project selector on the top left-hand side):

<figure markdown>
  ![Alt text](../../../assets/images/flexi/project-selector.png)
</figure>

Open the `Project` tab, open the `Object Storage` tab and select the `Containers` category

Select the container you would like to delete and it should highlight with blue

<figure markdown>
  ![Alt text](../../../assets/images/flexi/object-storage-container-overview.png)
</figure>

On the far right there should be 3 icons, `Upload File` `+ Folder` and `Delete Item`

Clicking `+ Folder` will present you with the `Create Folder` dialog.

Fill in the *Folder Name* and click `Create Folder`
