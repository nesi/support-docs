---
tags:
- jupyter
- hub
- home
- lab
- notebook
- ondemand
- rstudio
title: NeSI OnDemand how-to guide
---

!!! info
     NeSI OnDemand is in development and accessible to early access users only.
     If you are interested in helping us test it please [contact us](mailto:support@nesi.org.nz).


# NeSI OnDemand how-to guide

## How to log in

Go to [NeSI OnDemand](https://ondemand.nesi.org.nz/). It will automatically take you to the Tuakiri login screen.

![image-20240903-110950](https://github.com/user-attachments/assets/2eccbaad-cd70-489b-9938-663f3fd30082)

Select your affiliated institution, and log in using your institutional account. Example below shows the University of Auckland login screen.

![image-20240903-111115 (1)](https://github.com/user-attachments/assets/d1006331-8128-421a-b678-16b29fe74a0e)

After logging in, you will be asked to set up your OTP (one-time password) for NeSI. This is an OTP in addition to your institutional 2FA. We are currently enforcing an additional layer of OTP to make sure our system is secure, as the institutions federated by Tuakiri all have different security policies. We aim to improve this step as we iterate, so that you won’t be asked for the two different OTPs every time you try to log in.

![image-20240903-111555](https://github.com/user-attachments/assets/4ba7b6bd-a5de-4fc9-a11a-f52154f5587b)

Scan the barcode with your preferred authenticator app (e.g. Google Authenticator), and enter the one-time code (6 digit number) along with a device name (e.g. my mobile) and Submit and you are good to go.

Once you have already set up NeSI OTP, you will be shown the following screen instead of the one above, where you can enter the 6 digit number from your authenticator app.

![image-20240903-111247](https://github.com/user-attachments/assets/8d84be5d-347f-4a86-8b35-576cb55ffdee)

After successfully logging in, you will be presented with the following NeSI OnDemand screen.

![image-20240903-112029](https://github.com/user-attachments/assets/f4aed975-0f47-4e08-b783-d96271a56374)



## How to launch JupyterLab / RStudio

From the home screen, you can click on the app you would like to launch, e.g. JupyterLab, and you will be taken to the following screen.

![image-20240903-112130](https://github.com/user-attachments/assets/62e37323-4a8f-48ba-b7a5-613c218b43a6)

You can select the number of cores and memory needed and click on Launch to start the application. Currently our system is reserved with limited number of virtual CPUs and RAM, so selecting a value too high on the number will result in a failure message. On successful launch, you will see a screen similar to below:

![image-20240903-112408](https://github.com/user-attachments/assets/b428b472-4612-4116-b815-6a8c17637a6a)

Once the session is ready, you will see a button labeled Connect to Jupyter (or other app of your choice), which upon clicking will take you to the JupyterLab in this example as seen below:

![image-20240903-112553](https://github.com/user-attachments/assets/c106b182-7f4a-494c-a48d-d67e97ef2dbf)



## How to access your project directory

For this test release, you will be presented only with our ephemeral storage, and access to the research files you have in Mahuika/Maui will be linked in a future release.



## OTP token reset process (lost OTP device)

Please contact support@nesi.org.nz with NeSI OnDemand as a part of the subject line and we will get back to you ASAP.
