# Dependencies
import ui_functions
import tkinter as tk
import tkinter.ttk as ttk

"""
====================
     Main window    
====================
"""
root = tk.Tk()
root.title("ENCRYPT-IT")
root.geometry("800x600")
root.resizable(False, False)

"""
===============
     Title     
===============
"""
lbl_title = ttk.Label(root, text="ENCRYPT-IT")
lbl_title.config(font=("Arial", 42))
lbl_title.place(relx=0.5, y=60, anchor=tk.CENTER)
lbl_text = ttk.Label(root, text="Implementation of the RSA algorithm").place(relx=0.5, y=110, anchor=tk.CENTER)


"""
===============
     Inputs    
===============
"""

### Entry ###

#Public key
lbl_public_key = ttk.Label(root, text="Public key").place(x=10, y=140)
entry_public_key = ttk.Entry(root, width=90)
entry_public_key.place(x=75, y=140)

#Private key
lbl_private_key = ttk.Label(root, text="Private key").place(x=10, y=170)
entry_private_key = ttk.Entry(root, width=90)
entry_private_key.place(x=75, y=170)

### Text ###

#Encrypt text
txt_encrypt = tk.Text(root, width=80, height=7)
txt_encrypt.place(x=10, y=240)

#Decrypt text
txt_decrypt = tk.Text(root, width=80, height=7)
txt_decrypt.place(x=10, y=370)


"""
================
     Functions 
================
"""
functions = ui_functions.Functions(entry_public_key, entry_private_key, txt_encrypt, txt_decrypt)


"""
===============
     Buttons   
===============
"""

#Keys
btn_open_keys = ttk.Button(root, text="\nOpen\n", command=functions.get_keys_from_file)
btn_open_keys.place(x=630, y=138)

btn_save_keys = ttk.Button(root, text="\nSave\n", command=functions.save_keys_to_file)
btn_save_keys.place(x=710, y=138)

btn_generate_keys = ttk.Button(root, text="Generate keys", width=128, command=functions.generate_keys)
btn_generate_keys.place(x=10, y=200)

#Files
btn_open_text = ttk.Button(root, text="\n\n\nOpen\n\n\n", width=18, command=functions.open_plain_text).place(x=665, y=242)
btn_save_text = ttk.Button(root, text="\n\n\nSave\n\n\n", width=18, command=functions.save_file).place(x=665, y=370)

#Encrypt - Decrypt
btn_encrypt = ttk.Button(root, text="\n\nEncrypt\n\n", width=62, command=functions.encrypt).place(x=10, y=505)
btn_decypt = ttk.Button(root, text="\n\nDecrypt\n\n", width=62, command=functions.decrypt).place(x=400, y=505)

"""
=========================
     Runs main window   
========================= 
"""
root.mainloop()