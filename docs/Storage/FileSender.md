# FileSender

FileSender is a service that allows users to send vast amounts of data easily and securely. It is possible to send and receive data _via_ a web-based graphical user interface (GUI) as well as _via_ an API. These instructions show how to use both the web-based GUI and API to send and receive data using FileSender.

## Using the FileSender API in the Terminal

### Sending Data using the FileSender API in the Terminal

To send data to your FileSender account using the FileSender API, we first have to download the FileSender API and set it up:

1. Go to https://filesender.reannz.co.nz
2. If asked, click **Login** and Sign-in through your Tuakiri login. You may not need to do this if you have already signed into FileSender before.
3. Click **My profile** at the top-right of the page. 
4. Near the bottom of the page under **Remote authentication**, click the **New API secret** button. This will create a new authenticator secret key.
5. In the terminal on the machine you would like to send/receive data from, type: 

    ```sh
    curl -O https://raw.githubusercontent.com/filesender/filesender/master3/scripts/client/filesender.py
    ```

6. In the terminal on the machine you would like to send/receive data from, type: 

    ```sh
    mkdir -p ~/.filesender
    ```

7. Open the `filesender.py.ini` file (e.g. `nano ~/.filesender/filesender.py.ini` to open with the text editor `nano`) and add the following, where you need to replace:

    a. `TUAKIRI_LOGIN_EMAIL` with your Tuakiri login email (This is your university or industrial email)
    
    b. `FILESENDER_API_KEY` with the new authenticator secret key from step 4.

    ```sh
    [system]
    base_url = https://filesender.reannz.co.nz/rest.php
    default_transfer_days_valid = 10

    [user]
    username = TUAKIRI_LOGIN_EMAIL
    apikey = FILESENDER_API_KEY
    ```

    Close and save with `ctrl x`, `ctrl y`, `Enter`

After setting up the FileSender API, you can upload files to FileSender by typing into the terminal (where you downloaded `filesender.py` into):

```bash
python3 filesender.py -r person-to-send-to@emailserver.edu research-data-file.txt
```
where:

* `person-to-send-to@emailserver.edu`: This is the email address of the persion that you would like to send your data to. This can be any email address, not necessarily an educational email address. 
* `research-data-file.txt` This is the file you would like to send. This can be any file.

You can send multiple files by tarballing the files up:

```bash
tar -cvf tarball_file.tar folder_to_tarball
```

### Receiving Data using the FileSender API in the Terminal

## Using FileSender: Web-based GUI

### Sending Data using the FileSender Web-based GUI

### Receiving Data using the FileSender Web-based GUI
