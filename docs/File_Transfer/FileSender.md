# FileSender

FileSender is a service that allows users to send vast amounts of data easily and securely. It is possible to send and receive data _via_ a web-based graphical user interface (GUI) as well as _via_ an API. These instructions show how to use both the web-based GUI and API to send and receive data using FileSender.

## Using FileSender: Web-based GUI

### Sending Data using the FileSender Web-based GUI

1. Go to [https://filesender.reannz.co.nz](https://filesender.reannz.co.nz)
2. If asked, click **Login** and Sign-in through your Tuakiri login. You may not need to do this if you have already signed into FileSender before.
3. You can then drag & drop or click to select a file to transfer or you can select an entire directory to upload to FileSender

### Receiving Data using the FileSender Web-based GUI

1. Go to your emails where you should have been sent an email from FileSender.
2. Click on the **Download link** in the email link. This will take you to a FileSender website where you can download your files.
3. You will be presented a list of the files that you can download. Click on the <img src="../../assets/images/filesender_download_icon.png" alt="FileSender Download Icon" width="20"/> icon. This will download your file to you downloands folder on your computer.

If you would like to download all files together in a tar or zip file, you can do this by clicking on the **Download as single (.zip) file** or the **Download as single (.tar) file** button.

## Using the FileSender API in the Terminal

### Sending Data using the FileSender API in the Terminal

To send data to your FileSender account using the FileSender API, we first have to download the FileSender API and set it up:

1. Go to [https://filesender.reannz.co.nz](https://filesender.reannz.co.nz)
2. If asked, click **Login** and Sign-in through your Tuakiri login. You may not need to do this if you have already signed into FileSender before.
3. Click **My profile** at the top-right of the page.
4. Near the bottom of the page under **Remote authentication**, click the **New API secret** button. This will create a new authenticator secret key.
5. In the terminal on the machine you would like to send/receive data from, type:

    ```sh
    curl -o ~/filesender.py https://raw.githubusercontent.com/filesender/filesender/master3/scripts/client/filesender.py
    ```

6. In the terminal on the machine you would like to send/receive data from, type:

    ```sh
    mkdir -p ~/.filesender
    ```

7. Open the `filesender.py.ini` file (e.g. `nano ~/.filesender/filesender.py.ini` to open with the text editor `nano`) and add the following, where you need to replace:

    * `TUAKIRI_LOGIN_EMAIL` with your Tuakiri login email (This is your university or industrial email)
    * `FILESENDER_API_KEY` with the new authenticator secret key from step 4.

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
python3 ~/filesender.py -p -r person-to-send-to@emailserver.edu research-data-file.txt
```

where:

* `person-to-send-to@emailserver.edu`: This is the email address of the persion that you would like to send your data to. This can be any email address, not necessarily an educational email address. This can also be your own email address if you are wanting move data between your local machine and mahuika.
* `research-data-file.txt` This is the file you would like to send. This can be any file.

!!! warning

    This may take some time if you are uploading a big file.

You can send multiple files by tarballing the files up:

```bash
tar -cvf tarball_file.tar folder_to_tarball
```

To untar the tarball:

```bash
tar -xvf tarball_file.tar
```

### Receiving Data using the FileSender API in the Terminal

1. Go to your emails where you should have been sent an email from FileSender.
2. Click on the **Download link** in the email link. This will take you to a FileSender website where you can download your files.
3. You will be presented a list of the files that you can download. Right-click on the <img src="../../assets/images/filesender_download_icon.png" alt="FileSender Download Icon" width="20"/> icon and click **Copy Link Address**
4. In your terminal (in either your local machine or Mahuika), type:

    ```bash
    curl -O -J -L -R "<copied_website>"
    ```

    NOTE: replace **<copied_website>** with the path you copied. Keep the double quotation "" marks as these are needed.

5. You will see your file download to through your terminal.
