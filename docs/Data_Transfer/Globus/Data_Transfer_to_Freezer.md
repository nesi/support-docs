---
tags: 
    - globus
    - freezer
    - file transfer
search:
  exclude: true
---

!!! note
    This service is still in the testing phase

We are currently trialing the transfer of data to and from Freezer using Globus. We currently have a new Globus Collection to Freezer called: `NeSI Freezer`. You will need to authenticate using your Freezer (S3) credentials. Please let us know if you would like some assistance or are having any difficulties with this service.

## Setting up Freezer Credentials

1. Go to the File Manager tab of [your Globus page](https://app.globus.org/file-manager?two_pane=true) in the left hand menu bar.
    Under the `Collection` field, search for and select the `NeSI Freezer` collection, then click the blue `Continue` button.
    ![Globus_Freezer_Collection.png](../../assets/images/Globus_Freezer_Collection.png)


2. You will need to authenticate with an identity from NeSI Keycloak. Click on `Use my user_id@iam.nesi.org.nz identity` text.
    ![Globus_Transfer_5.png](../../assets/images/Globus_Transfer_5.png)


3. In the next window, click `Allow`.
    ![Globus_Freezer_Manage_Data.png](../../assets/images/Globus_Freezer_Manage_Data.png)

4. To set up your credentials, please click `Continue`
    ![Globus_Freezer_Require_Credentials.png](../../assets/images/Globus_Freezer_Require_Credentials.png)

5. Fill in your Username and Secret Key. Please let us know if you have lost your Freezer Secret Key. We can reset this, but you will also need to reset your Freezer config on Mahuika (support@nesi.org.nz).

    In the following sections, please enter:

    * `AWS IAM Access Key ID`: `user_id`
    * `AWS IAM Secret Key`: `Freezer Secret Key`

    ![Globus_Freezer_Credentials.png](../../assets/images/Globus_Freezer_Credentials.png)


    Please click `Save` after you have entered your details. You will then be shown this page here if it is successful.

## Freezer Endpoint

1. Go to the File Manager on the left hand menu and search for the collection “NeSI Freezer” .
    ![Globus_Freezer_EP.png](../../assets/images/Globus_Freezer_EP.png)

2. Under 'Path', type in your Freezer bucket e.g., `nesi99991-12345` and press <kbd>Enter</kbd>. you should now see the contents of your bucket.
![Globus_Freezer_Load_Bucket.png](../../assets/images/Globus_Freezer_Load_Bucket.png)
