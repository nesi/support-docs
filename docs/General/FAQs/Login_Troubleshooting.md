---
created_at: '2018-11-16T01:13:47Z'
hidden: false
position: 13
tags: []
title: Login Troubleshooting
vote_count: 4
vote_sum: 0
zendesk_article_id: 360000570215
zendesk_section_id: 360000039036
---


!!! prerequisite
    - Please make sure you have followed the recommended setup. See [Choosing and Configuring Software for Connecting to the Clusters](../../Getting_Started/Accessing_the_HPCs/Choosing_and_Configuring_Software_for_Connecting_to_the_Clusters.md) for more information.
    - Most terminals do not give an indication of how many characters have been typed when entering a password.
    - Paste is not usually bound to `ctrl` + `V` and will vary based on your method of access.

## Repeatedly asking for First and Second Factor

In addition to using an incorrect First/Second factor there are several
other issues that will cause a similar looking failure to log in.

```sh
Login Password:
Login Password:
Login Password:
```

OR

```sh
Login Password (First Factor): 
Authenticator Code (Second Factor):
Login Password (First Factor): 
Authenticator Code (Second Factor):
Login Password (First Factor): 
Authenticator Code (Second Factor):
```

### Try logging in to `lander` directly

You can test what part of your connection has failed by first running:

```sh
ssh <user>@lander.nesi.org.nz
```

**If this succeeds**: Run the following:

``` sl
ssh login.<mahuika/maui>.nesi.org.nz
```

**If this fails:** Are you logging in to the correct cluster?
Mahuika/Maui have separate access control, also Māui requires your
password input in a different format, see
[here](../../General/FAQs/Mahuika_Maui_Differences.md).

**If this succeeds**: If you are using a bash terminal, confirm your
.ssh config is [set up
correctly](../../General/FAQs/Logging_in_to_the_HPCs.md#recLinux).

If you are using a ssh client like *MobaXterm* or *WinSCP* make sure
your session is [set up
correctly](../../Getting_Started/Accessing_the_HPCs/Choosing_and_Configuring_Software_for_Connecting_to_the_Clusters.md).

### Check you are a member of an active project

If you are not a member of an active project, or your project has no
active allocation, you will not be able to log in. You should be able to
find whether you have any active projects with active
allocations [here](https://my.nesi.org.nz/html/view_projects).

### Confirm you are using the correct username and password

The most common cause of login failure is using incorrect login details.
Make sure you are using your NeSI Username and the password you set when
first logging into the Lander node. See
[my.nesi.org.nz](https://my.nesi.org.nz/).

### Check the time on your device

If the device you are using as authentication token is not using
NZST/NZDT, or is not keeping the correct time, the second factor code
generated will be invalid. Even an error of a few seconds can be enough
to invalidate the second factor code.

If your device can't keep time properly for whatever reason, please
contact the person or team responsible for supporting it.

### Ensure you're not reusing the same 6-digit code from your token

Login will fail if the same 6-digit code is used to access the Māui or
Mahuika login node after it has been used to access the lander node, or
for consecutive login attempts to any node. If in doubt, wait 30 seconds
for a new token to be generated.

### Ensure the correct Second Factor token is being used

Two-factor authentication is becoming a common security measure. Many
people have multiple tokens and occasionally mix them up.

### Wait four hours

Six failed login attempts within five minutes will trigger a four-hour
lockout. Users experiencing login issues can inadvertently trigger the
lockout, making diagnosing the original issue much more difficult.  

## Connection closed by .... (MobaXterm)

### Skip password prompts

There is a known MobaXterm bug in which a user who has set a second
factor and is trying to log in to the lander node will be prompted
multiple times for 'Password' before being prompted for 'First Factor'.
(On the lander node, you should only be prompted for a 'password' if you
have no Second Factor set up.)

These initial prompts can be skipped through by pressing 'Enter'. Any
input before pressing Enter will cause the login to fail.

The expected processes is as follows:

```sh
ssh <user>@lander.nesi.org.nz 
<user>@lander.nesi.org.nz's password: <Enter>
<user>@lander.nesi.org.nz's password: <Enter>
<user>@lander.nesi.org.nz's password: <Enter>
Login Password (First Factor): 
Authenticator Code (Second Factor):
```

*Note: Sometimes MobaXterm will prompt with a dialogue box.*

### Update your MobaXTerm client

Occasionally an outdated client can cause errors.  
MobaXterm can be updated through: 'help&gt;check for updates'

### Reinstall your MobaXTerm client

## Asked for 'Password' instead of 'First Factor'

### Check password status

Using [my.nesi.org.nz](https://my.nesi.org.nz/) and confirm you have an authentication token registered.

### See [above](#skip-password-prompts)

## Authentication token manipulation error

This occurs when your authentication token is out of sync. You will have
to reset your token though [my.nesi.org.nz](https://my.nesi.org.nz/).

## Nothing here has helped?

 {% include "partials/support_request.html" %}.

Helpful things to include:

- The client you are using (WSL, MobaXterm, Mac terminal, Linux,
    etc.).
- The nature of the problem, including the precise text of any error
    message you have been receiving.
  - Did you start out having one login problem and are now getting a
        different one? If so, when did the change happen, and were you
        doing anything in particular related to logging in at the time
        things changed?
- Have you successfully logged in in the past? if so when was the last
    time you successfully logged in, and to what NeSI cluster?
- Has anything administrative and relevant to NeSI access changed
    since you last logged in? For example:
  - Have you opened or joined any new NeSI projects, or have any of
        your existing NeSI projects closed?
    - Have any of your NeSI projects been granted new allocations, had
        a previously granted new allocation actually start, or had an
        existing allocation modified?
    - Have any of your NeSI projects' existing allocations ended?
    - Have any of your NeSI projects had a disk space quota change?
    - Have you changed your institutional username and password, moved
        to a different institution, or started a new job at an
        institution while also keeping your position at your old
        institution? Might NeSI know about any of these changes?
- What have you tried so far?
- Are you on the NIWA network, the NIWA VPN, or neither?