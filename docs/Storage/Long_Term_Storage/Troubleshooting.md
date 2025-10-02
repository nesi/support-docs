---
created_at: 2025-10-01
description: "Common issues when using Freezer"
tags: 
  - Freezer
  - storage
---

## Upload or Retrieval taking a long time
Uploading or retrieving data can sometimes take longer than expected. `tmux` is a terminal multiplexer, a multiplexer enables the creation and control of multiple terminals from a single screen.  It also allows the detachment of a screen to run in the background with the ability to re-attach and start where you left off.

An example of starting and using a `tmux` session:
``` sh
# create new tmux session called 'data_transfer'
tmux new -s freezer_transfer

# cd to directory containing files to upload
cd /nesi/nobackup/<project_id>/myproject

# put data 'your_folder' into Freezer bucket
s3cmd put --recursive --verbose your_folder s3://<freezer-bucket>/your_directory/your_folder
```
To detatch from the current `tmux` session by:
<kbd>ctrl</kbd> + <kbd>b</kbd>, then <kbd>d</kbd>

Detatching the `tmux` session, allows you to close your primary terminal and logoff while the upload continues. 

To reattach to the session:

``` sh
tmux attach -t freezer_transfer
```

The tmux session(s) will remain until you terminate it, or the node is rebooted.

More information can be found on the web, here are some good references:

- [Shortcut keys and cheat sheet](https://tmuxcheatsheet.com)
- [Getting started Guide](https://linuxize.com/post/getting-started-with-tmux/)

## Incorrect Secret Key
`Test failed: 403 (SignatureDoesNotMatch)`

An incorrect secret has been entered. Please let us know if you need to <a href="mailto:support@nesi.org.nz?subject=Reset%20Freezer%20Secret%20Key">reset this key</a>.

<pre><code>Test access with supplied credentials? [Y/n] <span style="color:blue"><b>Y</b></span>
Please wait, attempting to list all buckets...
ERROR: Test failed: 403 (SignatureDoesNotMatch): The request signature we calculated does not match the signature you provided. Check your key and signing method. 
Retry configuration? [Y/n] <span style="color:blue"><b>Y</b></span>
Enter new values or accept defaults in brackets with Enter. 
Refer to user manual for detailed description of all options. 
Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables. 
Access Key [userid123]: 
</code></pre>

## Testing access with supplied credentials

`ERROR: Test failed: Request failed for: /?delimiter=%2F  ` and `' freezer.nesi.org.nz' (found at least ' ')`

If you see this message when testing access with your credentials during configuration, this suggests that there is an extra white space '&nbsp;'. Please make sure there are no blank spaces if you are copy and pasting while configuring s3cmd.

<pre><code>Test access with supplied credentials? [Y/n] <span style="color:blue"><b>Y</b></span>
Please wait, attempting to list all buckets...
WARNING: Retrying failed request: /?delimiter=%2F (URL can't contain control characters. ' freezer.nesi.org.nz' (found at least ' ')) 
WARNING: Waiting 3 sec... 
WARNING: Retrying failed request: /?delimiter=%2F (URL can't contain control characters. ' freezer.nesi.org.nz' (found at least ' ')) 
WARNING: Waiting 6 sec... 
WARNING: Retrying failed request: /?delimiter=%2F (URL can't contain control characters. ' freezer.nesi.org.nz' (found at least ' ')) 
WARNING: Waiting 9 sec... 
WARNING: Retrying failed request: /?delimiter=%2F (URL can't contain control characters. ' freezer.nesi.org.nz' (found at least ' ')) 
WARNING: Waiting 12 sec... 
WARNING: Retrying failed request: /?delimiter=%2F (URL can't contain control characters. ' freezer.nesi.org.nz' (found at least ' ')) 
WARNING: Waiting 15 sec... 
ERROR: Test failed: Request failed for: /?delimiter=%2F  
</code></pre>
