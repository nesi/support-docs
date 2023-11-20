---
created_at: '2018-09-20T23:07:16Z'
hidden: false
position: 0
tags: []
title: Why can't I log in using MobaXTerm?
vote_count: 15
vote_sum: -5
zendesk_article_id: 360000470655
zendesk_section_id: 360000039036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Recent changes to our authentication system have caused some problems
for people who log in to NeSI HPC systems using MobaXTerm on Windows.

To fix these problems, you will need to do the following:

## Upgrade or Re-install

Upgrade your MobaXTerm to the most recent stable version. You can
download the most recent stable version
from <https://mobaxterm.mobatek.net>.

## Switch Browser to SCP

If you have created saved sessions to connect to NeSI HPC facilities,
open the settings for each such saved session and under the "Advanced
SSH settings" tab, change the SSH browser type from SFTP to something
else, such as "SCP (enhanced speed)".

## Repeating password prompts

If you are prompted multiple times for password (rather than First
Factor), this is a bug. Entering any text will cause your login attempt
to fail. The expected procedure is as follows.

``` sl
ssh <user>@lander.nesi.org.nz
<user>@lander.nesi.org.nz's password: <Press Enter> 
<user>@lander.nesi.org.nz's password: <Press Enter> 
<user>@lander.nesi.org.nz's password: <Press Enter>
Login Password (First Factor):
Authenticator Code (Second Factor):
```

 

## Delete Saved Credentials

It's possible that, even with a fresh install of mobaXterm it is still
trying to use your old password from credential manager.

1.  Go to Settings-&gt;Configuration and go to the General tab and click
    on MobaXterm password management
2.  You should see the credentials for NeSI hosts (`lander`, `mahuika`,
    `maui`)
3.  Remove all entries.
4.  Restart MobaXterm
5.  Try logging in again

 

For more information about how to log in to our HPC facilities, please
see [this
article](https://support.nesi.org.nz/hc/articles/360000161315-Logging-in-to-the-HPCs),
and for more login troubleshooting
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000570215-Login-Troubleshooting).