## Interacting with the S3 protocol with Boto3

!!! note
    Prior to starting this you will need to have read [Setting up your CLI environment](../setting-up-your-CLI-environment/index.md) and ran the commands to generate [EC2 Credentials](creating-and-managing-ec2-credentials-via-cli.md)

    Boto3 documentation can be found [here](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

Since FlexiHPC object storage has the S3 protocol built on top of it you are able to use the python boto3 client to interact with it.

When doing python development it is recommend that you do so within a python venv. As this article wont be covering what a python venv is please have a read of the the following [documentation](https://docs.python.org/3/library/venv.html#) on the python website

Ensure your in a clean folder, for this example we will be in a new folder called `FLEXIHPC.Boto3.Example`

Once inside that folder we will make a python venv by ruining the below command

``` { .sh }
python3 -m venv boto3-dev
```

Once that has completed setting up the venv we want to activate that

``` { .sh }
. boto3-dev/bin/activate
```

We then need to bring in the boto3 module for python

``` { .sh }
pip3 install boto3
```

This will also bring in any other required modules.

Create a file called `main.py` and add the following to that file

``` { .py }
import boto3
import botocore

#boto3.set_stream_logger(name='botocore')  # this enables debug tracing
session = boto3.session.Session()
s3_client = session.client(
    service_name='s3',
    aws_access_key_id='EC2_ACCESS_TOKEN',
    aws_secret_access_key='EC2_SECRET_TOKEN',
    endpoint_url='https://object.akl-1.cloud.nesi.org.nz/',
    config=botocore.client.Config(signature_version='s3v4')
)

#List all buckets in the project
bucketsResponse = s3_client.list_buckets()

print('Buckets:')
for bucket in bucketsResponse['Buckets']:
    print(f'  {bucket["Name"]}')
```

You will need to change `EC2_ACCESS_TOKEN` and `EC2_SECRET_TOKEN` to the ones that were generated when you ran the commands to generate [EC2 Credentials](../create-and-manage-identity/index.md)

Save the file and call it using the python command

``` { .sh }
python3 main.py
```

The output should look similar to the below

``` { .sh .no-copy}
Buckets:
  boto3-test
  terraform-state
```

## Uploading a file to object storage

You will need to know the name of the container you wish to upload the file too. You can either get this from the [dashboard](create-and-manage-object-storage-with-the-dashboard.md) or [CLI](create-and-manage-object-storage-via-cli.md)

We then use the below code to upload a file to the container we specify

```
s3_client.upload_file(<FILE_LOCATION>, <BUCKET_NAME>, <FILENAME_ON_S3>)
```

`<FILE_LOCATION>`
:   The local location of the file you wish to upload to FlexiHPC object storage

`<BUCKET_NAME>`
:   The container name within FlexiHPC, example would be boto3-test

`<FILENAME_ON_S3>`
:   The name of the file as it would be presented on the FlexiHPC object storage

## Downloading a file from object storage

You will need to know the name of the container you wish to download the file from. You can either get this from the [dashboard](create-and-manage-object-storage-with-the-dashboard.md) or [CLI](create-and-manage-object-storage-via-cli.md)

We use the below code to download a file from the container we specify

```
with open('<FILENAME_ON_S3>', 'wb') as data:
    s3_client.download_fileobj('<BUCKET_NAME>', '<FILENAME_KEY>', data)
```

`<FILENAME_ON_S3>`
:   The name of the file as it would be presented on the FlexiHPC object storage

`<BUCKET_NAME>`
:   The container name within FlexiHPC, example would be boto3-test

`<FILENAME_KEY>`
:   This is generally the `<FILENAME_ON_S3>` however if its inside a folder then it might have that appended to the file name