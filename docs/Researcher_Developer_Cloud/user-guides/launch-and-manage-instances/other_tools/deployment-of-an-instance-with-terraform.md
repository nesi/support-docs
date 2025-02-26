---
hidden: false
label_names:
- instance
- resize
title: Deployment of an instance with Terraform
position: 10
---

!!! note
    You will need to have Terraform installed on the machine that will be executing the commands. Follow the [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) link from the official documentation. We also highly recommend that you use [Application Credentials](../../create-and-manage-identity/creating-and-managing-application-credentials-with-the-dashboard.md) to do any automation

Please make sure you have download the `clouds.yaml` file for your application credentials and its sitting in the directory `~/.config/openstack/`

Generating Application Credentials is covered [here](../../create-and-manage-identity/creating-and-managing-application-credentials-with-the-dashboard.md)

Normally creating a folder space for Terraform projects can be a good thing as this ensures the Terraform state file doesn't clash with another.

Once you are in an empty folder, example `terraform-example-flexihpc`, we will need to create a file called `main.tf`

Inside this file we will need to define the provider

``` hcl
provider "openstack" {
  cloud = "NAME_IN_CLOUDS_YAML"
}
```

Replace the placeholder `NAME_IN_CLOUDS_YAML` with the name of your openstack section in the clouds.yaml file. An example `clouds.yaml` with multiple entries looks like the following:

``` { .yaml .no-copy }
clouds:
  openstack-entry-1:
    auth:
      auth_url: https://keystone.akl-1.cloud.nesi.org.nz
      application_credential_id: "APP_CREDS_ID"
      application_credential_secret: "APP_CREDS_SECRET"
    interface: "public"
    identity_api_version: 3
    auth_type: "v3applicationcredential"
    verify: false
  openstack-entry-2:
    auth:
      auth_url: https://keystone.akl-1.cloud.nesi.org.nz
      application_credential_id: "APP_CREDS_ID"
      application_credential_secret: "APP_CREDS_SECRET"
    region_name: "akl-1"
    interface: "public"
    identity_api_version: 3
    auth_type: "v3applicationcredential"
    verify: false
```
You will want to be using the name `openstack-entry-X` as your the value in `NAME_IN_CLOUDS_YAML`

Then within the same file we want to define the compute instance

``` hcl
resource "openstack_compute_instance_v2" "compute_instance" {
  name            = "compute-instance-0"
  flavor_id       = "FLEXIHPC_FLAVOR_ID"
  image_id        = "FLEXIHPC_IMAGE_ID"
  key_pair        = "FLEXIHPC_KEY_PAIR_NAME"
  security_groups = ["FLEXIHPC_SECURITY_GROUP_NAME"]

  network {
    name = "FLEXIHPC_NETWORK_NAME"
  }
}
```

Replace the placeholders `FLEXIHPC_FLAVOR_ID`, `FLEXIHPC_IMAGE_ID`, `FLEXIHPC_KEY_PAIR_NAME`, `FLEXIHPC_SECURITY_GROUP_NAME`, and `FLEXIHPC_NETWORK_NAME` with appropriate values from your OpenStack environment.

The network name is normally the same as your FlexiHPC project name.

Then we want to apply a floating IP to the instance so we can connect from outside the FlexiHPC platform

``` hcl
resource "openstack_networking_floatingip_v2" "floating_ip" {
  pool = "external"
}

resource "openstack_compute_floatingip_associate_v2" "floating_ip_association" {
  floating_ip = openstack_networking_floatingip_v2.floating_ip.address
  instance_id = openstack_compute_instance_v2.compute_instance.id
}
```

The floating IP pool is `external` within the FlexiHPC platform.

Once all the above is filled in then you only need to run the standard terraform commands

```
terraform init
```

This will initialize the terraform directory with all the required modules

Then we run the command to create our resources

```
terraform apply
```

Terraform will prompt you to confirm the changes. Type "yes" to proceed with the creation of the compute instance and the floating IP association.

Terraform will then provision the compute instance and associate the floating IP to it.

Remember that this is a basic example, and you might need to adapt it to your specific FlexiHPC environment and configurations.

The full `main.tf` file for completeness

``` hcl title="main.tf"
terraform {
required_version = ">= 0.14.0"
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "~> 1.51.1"
    }
  }
}

provider "openstack" {
  cloud = "NAME_IN_CLOUDS_YAML"
}

resource "openstack_compute_instance_v2" "compute_instance" {
  name            = "compute-instance-0"
  flavor_id       = "FLEXIHPC_FLAVOR_ID"
  image_id        = "FLEXIHPC_IMAGE_ID"
  key_pair        = "FLEXIHPC_KEY_PAIR_NAME"
  security_groups = ["FLEXIHPC_SECURITY_GROUP_NAME"]

  network {
    name = "FLEXIHPC_NETWORK_NAME"
  }
}

resource "openstack_networking_floatingip_v2" "floating_ip" {
  pool = "external"
}

resource "openstack_compute_floatingip_associate_v2" "floating_ip_association" {
  floating_ip = openstack_networking_floatingip_v2.floating_ip.address
  instance_id = openstack_compute_instance_v2.compute_instance.id
}
```

## Using FlexiHPC object storage to store the Terraform state file

Should you wish to not include the terraform state file within the git repo then you will want to update the above with a the backend that you wish to store that file

Within the first chunk of the file you want to add the following so it looks like this

``` hcl
terraform {
required_version = ">= 0.14.0"
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "~> 1.51.1"
    }
  }

  backend "s3" {
    bucket = "<CONTAINER_NAME>"
    key    = "state/terraform.tfstate"
    endpoint   = "https://object.akl-1.cloud.nesi.org.nz/"
    sts_endpoint = "https://object.akl-1.cloud.nesi.org.nz/"
    access_key = "<EC2 User Access Token>"
    secret_key = "<EC2 User Secret Token>"
    #region = "us-east-1"
    force_path_style = "true"
    skip_credentials_validation = "true"
  }
}
```

We have added the `backend "s3"` chunk to the `terraform` block

`<CONTAINER_NAME>`
:   The container name within FlexiHPC object storage. You can create this either via the [dashboard](../../create-and-manage-object-storage/with_the_dashboard/create-and-manage-object-storage-with-the-dashboard.md) or [CLI](../../create-and-manage-object-storage/with_the_CLI/create-and-manage-object-storage-via-cli.md)

You will need to update the following after generating [EC2 Credentials](../../create-and-manage-identity/index.md)

`<EC2 User Access Token>`
:   The EC2 Credentials Access Token

`<EC2 User Secret Token>`
:   The EC2 Credentials User Secret

Save that file and run

``` { .sh }
terraform init -reconfigure
```

This will reconfigure the backend to store the state file on FlexiHPC, you can also pass `-migrate-state` instead of `-reconfigure` should you have a state file that you want to move there from a previous run.

Your terraform state file should now be configured and stored on FlexiHPC object storage
