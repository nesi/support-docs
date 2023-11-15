---
created_at: '2018-05-18T03:56:37Z'
hidden: false
position: 1
tags:
- 2fa
- access
- mfa
- token
title: Setting Up Two-Factor Authentication
vote_count: 6
vote_sum: -6
zendesk_article_id: 360000203075
zendesk_section_id: 360000034315
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

!!! info Requirements
     You must:
     -   Have a [NeSI
         account](https://support.nesi.org.nz/hc/en-gb/articles/360000159715).
     -   Be a member of an [active
         project](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects).
     -   Have [set up your NeSI account
         password](https://support.nesi.org.nz/hc/en-gb/articles/360000335995-Setting-Up-and-Resetting-Your-Password).
     -   Have a device with an authentication app.

##  Authentication App

In order to generate your second factor, which you will require in order
to access to any NeSI cluster, you will need a device with an
authentication app, such as Authy or Google Authenticator installed
(generally the device is a smartphone, but there are also authentication
apps which work through the browser like Authy).

If you some reason you can't do this, please contact NeSI support.

 

## Linking a device to your account

1.  Log in to [My NeSI](https://my.nesi.org.nz) via your browser.

2.  Click **My HPC Account** on left hand panel  and then **Setup
    Two-Factor Authentication device**

    <img src="../../assets/images/Setting_Up_Twactor_Authentication.png"
    width="560" height="210" alt="authentication_factor_setup.png" />

3.  Click the "**Setup Two-Factor Authentication device**" link.  
    <img src="../../assets/images/Setting_Up_Twactor_Authentication_0.png"
    style="max-width: 480px;" />

4.  After clicking on "Continue" you will retrieve the QR code.

5.  Open your Authy or Google Authenticator app and click on the add
    button and select "**Scan a barcode**". Alternatively, if you are
    not able to scan the barcode from your device you can manually enter
    the provided authentication code into your authentication app.

## The second-factor token

The 6 digit code displayed on your app can now be used as the second
factor in the authentication process.  
This code rotates every 30 seconds, and it **can only be used once**.
This means that you can only try logging in to the lander node once
every 30 seconds.
!!! info What next?
     -   [Getting access to the
         cluster](https://support.nesi.org.nz/hc/en-gb/articles/360001016335)
