# pcpo
USATU labs

Usage:
  - Clone repo
  ```
  git clone https://github.com/Lomank123/pcpo.git
  ```
  - Setup and activate venv

    - Open cmd

    - Go to project root folder (root folder contains `.gitignore` and `requirements.txt` files)

    - Run:
    ```
    python -m venv path\to\root\folder\venv
    ```
    Notice that in the end there will be a name for your virtual env folder, python will create it automatically. My path to root folder: `D:\Python\usatu\pcpo`, so for me it'll look like this: `python -m venv D:\Python\usatu\pcpo\venv`

    - Activate with:
    ```
    path\to\root\folder\venv\Scripts\activate.bat
    ```
    (Run this command in `cmd`, not in `PowerShell`!)
    
    After activation your `cmd` will look like this:
    ```
    (venv) @ D:\Python\usatu\pcpo
    ```

  - Install the dependencies to your virtual env:
  ```
  pip install -r requirements.txt
  ```
  - Go to `/pcpo` folder and run `start.bat` file
  - After migrations shut down the server with `CTRL+C` and run:
  ```
  python manage.py createsuperuser
  ```
  Then simply type dummy values and run server again with: `start.bat`
  - In your browser go to http://127.0.0.1:8000/home to open home page
  - You can also access to admin board which is located on http://127.0.0.1:8000/admin
