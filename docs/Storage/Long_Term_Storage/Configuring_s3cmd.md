---
created_at: 2025-10-01
description: "Freezer s3cmd configuration"
tags: 
  - Freezer
  - storage
  - config
  - s3cmd
---

To use Freezer and to configure `s3cmd`, you will need a current Freezer allocation. To apply for an allocation please go to [MyNeSI](https://my.nesi.org.nz/).

Currently Freezer is only available via specific access points, HPC3 and Mahuika. We are currently completing security hardening prior to opening Freezer to wider access.

### Configure s3cmd

You will need to configure the `s3cmd` tool before you use it for the first time. Configuring the `s3cmd` allows for user credentials and default buckets to be remembered. This will only need to be done once.

```sh
s3cmd --configure --multipart-chunk-size-mb=1024
```

Enter the following details when prompted in the terminal:

`Access Key`: Your NeSI user ID

`Secret Key`: This is the code from the 1-time link in your Freezer allocation email. Please let us know if you need to <a href="mailto:support@nesi.org.nz?subject=Reset%20Freezer%20Secret%20Key">reset this key</a>.

Please copy and paste the sections in <span style="color:blue">blue</span>.

<pre><code>Enter new values or accept defaults in brackets with Enter.
Refer to user manual for detailed description of all options.
Access key and Secret key are your identifiers for AWS S3. Leave them empty for using the env variables.
Access Key: <span style="color:green"><b>User ID</b></span>
Secret Key: <span style="color:green"><b>Your Freezer Secret Key</b></span>
Default Region: <span style="color:blue"><b>akl-1</b></span>
Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
S3 Endpoint: <span style="color:blue"><b>freezer.nesi.org.nz:7070</b></span>

Use "%(bucket)s.s3.amazonaws.com" to the target AWS S3. "%(bucket)s" and "%(location)s" vars can be used
if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket:  <span style="color:blue"><b>210.7.37.122:7070</b></span>
Encryption password is used to protect your files from reading
by unauthorized persons while in transfer to S3
Encryption password: <span style="color:green"><b>Leave blank, </b>press &lt;Enter&gt;</span>
Path to GPG program [/usr/bin/gpg]: <span style="color:green"><b>Leave blank, </b>press &lt;Enter&gt;</span>

When using secure HTTPS protocol all communication with AWS S3
servers is protected from 3rd party eavesdropping. This method is
slower than plain HTTP, and can only be proxied with Python 2.7 or newer
Use HTTPS protocol: <span style="color:blue"><b>Yes</b></span>
On some networks all internet access must go through a HTTP proxy.
Try setting it here if you can't connect to S3 directly
HTTP Proxy server name: <span style="color:green"><b>Leave blank, </b>press &lt;Enter&gt;</span>
</code></pre>

You will then be presented with a summary.
<pre><code>New settings:
  Access Key: User ID
  Secret Key: Your Freezer Secret Key
  Default Region: akl-1
  S3 Endpoint: freezer.nesi.org.nz:7070
  DNS-style bucket+hostname:port template for accessing a bucket: 210.7.37.122:7070
  Encryption password:
  Path to GPG program: /usr/bin/gpg
  Use HTTPS protocol: True
  HTTP Proxy server name:
  HTTP Proxy server port: 0
</code></pre>

Press `Y` to confirm.

<pre><code>Test access with supplied credentials? [Y/n] <span style="color:blue"><b>Y</b></span>
Please wait, attempting to list all buckets...
Success. Your access key and secret key worked fine :-)

Now verifying that encryption works...
Not configured. Never mind.

Save settings? [y/N] <span style="color:blue"><b>y</b></span>
Configuration saved to '/home/&lt;user_id&gt;/.s3cfg'
</code></pre>
