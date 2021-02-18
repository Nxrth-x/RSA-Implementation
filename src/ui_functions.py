# Dependencies
import io
import tkinter as tk
import rsa
import tkinter.ttk as ttk
import tkinter.filedialog

class Functions:
    def __init__(self, public_key, private_key, encrypt_text, decrypt_text):
        self.entry_public_key = public_key
        self.entry_private_key = private_key
        self.txt_encrypt = encrypt_text
        self.txt_decrypt = decrypt_text

    def render_entry(self, reference, value):
        reference.delete(0, tk.END)
        reference.insert(0, value)

    def render_text(self, reference, value):
        reference.delete("1.0", tk.END)
        reference.insert("1.0", value)

    def open_text_file(self):
        try:
            with io.open(self.get_file(), mode="r", encoding="utf-8") as file:
                content = file.read()
            return content
        except:
            return "Error!"

    def open_key_file(self):
        try:
            with io.open(self.get_file(), mode="r", encoding="utf-8") as file:
                public, private = file.readlines()
            return public, private
        except:
            return "Error!", "Error!"

    def get_file(self):
        return tkinter.filedialog.askopenfilename(initialdir="/", title="Choose a file", filetypes=(("Text files", "*.txt"),("All files", "*.*")))

    def get_path(self):
        return tkinter.filedialog.askdirectory(initialdir="/", title="Choose a directory")

    def generate_keys(self):
        public, private = rsa.generate_keys()
        self.render_entry(self.entry_public_key, public)
        self.render_entry(self.entry_private_key, private)

    def get_keys_from_file(self):
        
        public, private = self.open_key_file()
        public.strip()
        private.strip()
        self.render_entry(self.entry_public_key, public)
        self.render_entry(self.entry_private_key, private)
        
    def save_keys_to_file(self):
        public = self.entry_public_key.get()
        private = self.entry_private_key.get()

        try:
            if(public and private):
                keys = [self.entry_public_key.get()+"\n", self.entry_private_key.get()]
                path = self.get_path()
                
                with io.open(f"{path}/keys.txt", mode="w", encoding="utf-8") as file:
                        file.writelines(keys)
                with io.open(f"{path}/public.txt", mode="w", encoding="utf-8") as file:
                        file.writelines(self.entry_public_key.get()+"\n")
            else:
                self.render_entry(self.entry_public_key, "Error! Both fields must be filled.")
        except:
            self.render_entry(self.entry_public_key, "Error while saving the file!")

    def open_plain_text(self):
        content = self.open_text_file()
        self.render_text(self.txt_encrypt, content)

    def save_file(self):
        try:
            content = self.txt_decrypt.get("1.0", tk.END)
            if(len(content)>1):
                path = self.get_path()
                with io.open(f"{path}/encrypt-it.txt", mode="w", encoding="utf-8") as file:
                        file.write(content)
            else:
                self.render_text(self.txt_decrypt, "Error! Field must be filled")
        except:
            self.render_text(self.txt_decrypt, "Error while saving the file!")

    def encrypt(self):
        message = self.txt_encrypt.get("1.0", tk.END)
        key = self.entry_public_key.get().split(' ')
        if(key and len(message)>1):
            self.render_text(self.txt_decrypt, rsa.encrypt(message, key))
        else:
            self.render_text(self.txt_decrypt, "Error!")
        
    def decrypt(self):
        message = self.txt_encrypt.get("1.0", tk.END)
        key = self.entry_private_key.get().split(' ')
        if(key and len(message)>1):
            self.render_text(self.txt_decrypt, rsa.decrypt(message, key))
        else:
            self.render_text(self.txt_decrypt, "Error!")
