---
created_at: '2018-05-18T03:56:37Z'
hidden: false
label_names:
- 2fa
- access
- mfa
- token
position: 1
title: Setting Up Two-Factor Authentication
vote_count: 6
vote_sum: -6
zendesk_article_id: 360000203075
zendesk_section_id: 360000034315
---

> ### Requirements
>
> You must:
>
> -   Have a [NeSI
>     account](https://support.nesi.org.nz/hc/en-gb/articles/360000159715).
> -   Be a member of an [active
>     project](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects).
> -   Have [set up your NeSI account
>     password](https://support.nesi.org.nz/hc/en-gb/articles/360000335995-Setting-Up-and-Resetting-Your-Password).
> -   Have a device with an authentication app.

##  Authentication App

In order to generate your second factor, which you will require in order
to access to any NeSI cluster, you will need a device with an
authentication app, such as Authy or Google Authenticator installed on
your device (generally a smartphone, but there are also authentication
apps which work through the browser like Authy).

If you some reason you can't do this, please contact NeSI support.

 

## Linking a device to your account

1.  Log in to [My NeSI](https://my.nesi.org.nz) via your browser.

2.  Click **My HPC Account** on left hand panel  and then **Setup
    Two-Factor Authentication device**

    <img src="../includes/authentication_factor_setup.png" alt="authentication_factor_setup.png" width="560" height="210" />

3.  Click the "**Setup Two-Factor Authentication device**" link.  
    ![](../includes/mceclip0.png)
4.  After clicking on "Continue" you will retrieve the QR code.
5.  Open your Authy or Google Authenticator app and click on the add
    button and select "**Scan a barcode**". Alternatively, if you are
    not able to scan the barcode from your device you can manually enter
    the provided authentication code into your authentication app.

## The second-factor token

The <span class="wysiwyg-underline">6 digit code</span> displayed on
your app can now be used as the second factor in the
authentication process.  
This code rotates every 30 seconds, and it **can only be used once**.
This means that you can only try logging in to the lander node once
every 30 seconds.

> ### What next?
>
> -   [Getting access to the
>     cluster](https://support.nesi.org.nz/hc/en-gb/articles/360001016335)
