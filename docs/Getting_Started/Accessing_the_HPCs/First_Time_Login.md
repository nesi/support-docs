---
created_at: '2018-05-18T03:56:37Z'
tags:
- 2fa
- access
- mfa
- token
---

!!! prerequisite
    -  Have a [NeSI account](../Accounts-Projects_and_Allocations/Creating_a_NeSI_Account_Profile.md).  
    -  Be a member of an [active project](../Accounts-Projects_and_Allocations/Creating_a_NeSI_Account_Profile.md).  
    -  Have a device with an authentication app.

1. Go to [**NeSI OnDemand**](https://ondemand.nesi.org.nz/). It will automatically take you to the Tuakiri login screen.
    If you haven't logged into NeSI OnDemand or HPC3 before, part of the login process will include a step to setup a new 2FA.
    ![alt text](../../assets/images/ondemand_login_0.png)

2. Select your affiliated institution, and log in using your institutional account. Example below shows the University of Auckland login screen.
    ![alt text](../../assets/images/ondemand_login_1.png)

3. If it is your first time logging in, you will be asked to set up your 2FA (2-Factor Authentication) for NeSI. This is in addition to your institutional 2FA.
    ![alt text](../../assets/images/ondemand_login_2.png)
  
Note: if your device is not trusted (step 6 ), you will be asked everytime to enter your OTP (one-time password) for NeSI.
  
4. Scan the barcode with your preferred authenticator app (e.g. Google Authenticator), and enter the one-time code (6 digit number) along with a device name (e.g. my mobile) and Submit and you are good to go.

5. Once you have already set up NeSI OTP, you will be shown the following screen instead of the one above, where you can enter the 6 digit number from your authenticator app.
    ![alt text](../../assets/images/ondemand_login_3.png)

6. You are now asked about your current device: do you trust it or not?  
-  If this device is a shared computer (e.g. university computer where you have to delete cookies), please do not trust it: click No. This means that you will need to enter your OTP everytime you log.
-  If this device is your own laptop and you are using your home secure non shared network, you can trust it: click Yes. This will allow you to log in without 2FA for 7 days.
![alt text](../../assets/images/ondemand_login_4.png). 

If you have trusted your device, you have to enter a name for this device. This name must be unique. E.g. you cannot trust two devices the same day with the same name, this will fail. 

7. For the moment, you will be prompted again. Press yes.
    ![alt text](../../assets/images/login_freeipaaccess.png)

8. After successfully logging in, you will be presented with the following NeSI OnDemand screen.
    ![image-20240903-112029](../../assets/images/OOD_Desktop_08Jun2025.png)
