---
tags: 
    - globus
    - freezer
    - file transfer
---


The Globus Collection to Freezer is called: `{{ globus_collection_freezer}}`.
You will need to authenticate using your Freezer (S3) credentials. Please let us know if you would like some assistance or are having any difficulties with this service.

## Requirements

You will need to have a Globus account to access Freezer via Globus. Please see the page on [first time Globus set up](First_Time_Setup.md) for information on getting a Globus account.

## Setting up Freezer Credentials in Globus

1. Go to the File Manager tab of [your Globus page](https://app.globus.org/file-manager?two_pane=true) in the left hand menu bar.
    Under the `Collection` field, search for and select the {{ globus_collection_freezer}} collection, then click the blue `Continue` button.
    ![Globus_Freezer_Collection.png](../../assets/images/Globus_Freezer_Collection.png)

2. You will need to authenticate with an identity from NeSI Keycloak. Click on `Use my user_id@iam.nesi.org.nz identity` text.
    ![Globus_Transfer_5.png](../../assets/images/Globus_Transfer_5.png)

3. In the next window, click `Allow`.
    ![Globus_Freezer_Manage_Data.png](../../assets/images/Globus_Freezer_Manage_Data.png)

    !!! info
        Steps 4 & 5 may not be required

4. To set up your credentials, please click `Continue`. You will be shown a Globus page requiring you to sign in to Mahuika. 
    ![Globus_Freezer_Require_Credentials.png](../../assets/images/Globus_Freezer_Require_Credentials.png)

5. Fill in your Mahuika Username and Secret Key. Please let us know if you have lost your Freezer Secret Key. We can <a href="mailto:support@nesi.org.nz?subject=Reset%20Freezer%20Secret%20Key"> reset your Freezer key</a>, but you will also need to reset your Freezer config on Mahuika.

    In the following sections, please enter:

    * `AWS IAM Access Key ID`: `user_id`
    * `AWS IAM Secret Key`: `Freezer Secret Key`

    ![Globus_Freezer_Credentials.png](../../assets/images/Globus_Freezer_Credentials.png)

    Please click `Save` after you have entered your details. You will then be shown this page here if it is successful.

    ![Globus_Freezer_Credentials_Completed.png](../../assets/images/Globus_Freezer_Credentials_Completed.png)

## Freezer Endpoint

Note that modification times are preserved only for files.
- Files: The displayed modification date reflects the file's original modification time.
- Folders: Folder modification times are not preserved by the Globus Freezer collection and will always appear as 1 January 1970 (Unix epoch).

This is expected behaviour and does not affect the integrity or accessibility of your archived data.

1. Go to the File Manager on the left hand menu and search for the collection `{{ globus_collection_freezer}}`.
    ![Globus_Freezer_EP.png](../../assets/images/Globus_Freezer_EP.png)

2. Under 'Path', type in your Freezer bucket e.g., `nesi99991-12345` and press <kbd>Enter</kbd>. you should now see the contents of your bucket.
![Globus_Freezer_Load_Bucket.png](../../assets/images/Globus_Freezer_Load_Bucket.png)

If you initiate a transfer of offline data (only on tape - Glacier) from Freezer, the data will be automatically staged from tape before the transfer begins.

## Organizing Files Using Globus

We do NOT recommend organising or moving files or directories on Freezer using the Globus interface. Please use the s3cmd tool in these instances. Please see our [Freezer Guide](../../Storage/Long_Term_Storage/Freezer_Guide.md) for more information.
