from cryptography.fernet import Fernet

key = Fernet.generate_key()
my_f = Fernet(key)
print(my_f.encrypt("hello my name is walter hardwell white".encode()))