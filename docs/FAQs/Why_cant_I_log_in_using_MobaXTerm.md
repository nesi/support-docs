---
created_at: '2018-09-20T23:07:16Z'
tags: []
title: Why can't I log in using MobaXTerm?
vote_count: 16
vote_sum: -4
zendesk_article_id: 360000470655
zendesk_section_id: 360000039036
---

Recent changes to our authentication system have caused some problems
for people who log in to NeSI HPC systems using MobaXTerm on Windows.

To fix these problems, you will need to do the following:

## Upgrade or Re-install

Upgrade your MobaXTerm to the most recent stable version. You can
download the most recent stable version
from [mobaxterm.mobatek.net](https://mobaxterm.mobatek.net).
!!! warning
     Some users have reported having issues downloading files using
     MobaXterm 23.6. We suggest using version 23.5 instead.

## Switch Browser to SCP

If you have created saved sessions to connect to NeSI HPC facilities,
open the settings for each such saved session and under the "Advanced
SSH settings" tab, change the SSH browser type from SFTP to something
else, such as "SCP (enhanced speed)".

## Repeating password prompts

If you are prompted multiple times for password (rather than First
Factor), this is a bug. Entering any text will cause your login attempt
to fail. The expected procedure is as follows.

```sh
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

1. Go to Settings-&gt;Configuration and go to the General tab and click
    on MobaXterm password management
2. You should see the credentials for NeSI hosts (`lander`, `mahuika`,
    `maui`)
3. Remove all entries.
4. Restart MobaXterm
5. Try logging in again

More information about [how to log in to our HPC facilities](../../Scientific_Computing/Getting_Started/Accessing_the_HPCs/Choosing_and_Configuring_Software_for_Connecting_to_the_Clusters.md),
and [login troubleshooting](../../General/FAQs/Login_Troubleshooting.md).
