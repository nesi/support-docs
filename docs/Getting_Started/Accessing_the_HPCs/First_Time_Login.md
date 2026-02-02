---
created_at: '2018-05-18T03:56:37Z'
tags:
- MFA
- access
- mfa
- token
- ondemand
- login
- mynesi
---

!!! prerequisite
    -  Have an [account](../Creating_an_Account.md).  
    -  Be a member of an [active project](../Creating_an_Account.md).  
    -  Have a device with an authentication app.

!!! note
    On 01 July 2025, New Zealand eScience Infrastructure (NeSI) was integrated into the Crown company, Research and Education Advanced Network New Zealand (REANNZ) Ltd.
    NeSI's services and technologies are now hosted by REANNZ as a national eResearch Infrastructure Platform.
    Some of our tools (as pictured in the screenshot below) will retain a 'NeSI' brand as we transition our services and develop a longer-term strategy for this integrated platform.

1. Log into [my.nesi](http://my.nesi.org.nz)

2. Go to [**OnDemand**](https://ondemand.nesi.org.nz/). It will automatically take you to the Tuakiri login screen.
    ![alt text](../../assets/images/ondemand_login_0.png)

3. Select your affiliated institution, and log in using your institutional account. Example below shows the University of Auckland login screen.
    ![alt text](../../assets/images/ondemand_login_1.png)

4. If you haven't logged into OnDemand or our HPC platforms before, you will need to set up new authentication credentials. This is in addition to your institutional MFA process.
    ![alt text](../../assets/images/ondemand_login_2.png)
  
    !!! note
        If your device is not trusted (step 6 ), you will be asked every time to enter your 6-digit code (linked to your additional authentication credentials) for our HPC platforms.
  
5. Scan the barcode with your preferred authenticator app (e.g. Google Authenticator), and enter the 6-digit code along with a device name (e.g. my mobile) and click 'Submit'.

6. Once you have set up your additional authentication credentials, you will be shown the following screen instead of the one above, where you can enter the 6-digit code from your authenticator app.
    ![alt text](../../assets/images/ondemand_login_3.png)

7. You are now asked about your current device: do you trust it or not?  
    - Do not trust shared computers (e.g. a university computer where you have to delete cookies) or if you are using incognito or private windows: click No. This means that you will need to enter your 6-digit code every time you log in.
    - If the device is your personal laptop and you are using a secure network, you can trust it: click Yes. This will allow you to log in without additional authentication for 7 days.

    ![alt text](../../assets/images/ondemand_login_4.png).

    If you have trusted your device, you have to enter a name for this device. This name must be unique. E.g. you cannot trust two devices the same day with the same name.

    See [What is a trusted device?](https://docs.nesi.org.nz/Getting_Started/FAQs/What_Is_A_Trusted_Device/) for more information.

8. You will be prompted again to confirm that you initiated this sequence as a security measure against remote phishing. Click 'Yes' if you want to proceed with access. Click 'No' if you did not initiate this authentication process.

    ![alt text](../../assets/images/login-grantaccess.png).

9. After successfully logging in, you will be presented with the following OnDemand screen.

    ![image-20240903-112029](../../assets/images/OOD_Desktop_08Jun2025.png)
