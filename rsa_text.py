import tkinter as tk
from tkinter import messagebox
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA keys
key = RSA.generate(1024)
public_key = key.publickey()
private_key = key

# Encrypt message
def encrypt(text):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_text = cipher.encrypt(text.encode('utf-8'))
    return binascii.hexlify(encrypted_text).decode('utf-8')

# Decrypt message
def decrypt(encrypted_text):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(binascii.unhexlify(encrypted_text))
    return decrypted_text.decode('utf-8')

# Handle encrypt button click
def handle_encrypt():
    text = input_entry.get()
    if text:
        encrypted = encrypt(text)
        result_var.set(f"Encrypted Text:\n{encrypted}")
    else:
        messagebox.showwarning("Input Error", "Please enter a message to encrypt.")

# Handle decrypt button click
def handle_decrypt():
    encrypted_text = input_entry.get()
    if encrypted_text:
        try:
            decrypted = decrypt(encrypted_text)
            result_var.set(f"Decrypted Text:\n{decrypted}")
        except Exception:
            messagebox.showerror("Decryption Error", "Failed to decrypt the message. Ensure the input is correct.")
    else:
        messagebox.showwarning("Input Error", "Please enter a message to decrypt.")


# Set up the main window
app = tk.Tk()
app.title("RSA Encrypt/Decrypt")
app.configure(bg='#2f2f2f')

# Input field label
input_label = tk.Label(app, text="Enter your message:", bg='#2f2f2f', fg='white', font=('Helvetica', 12, 'bold'))
input_label.pack(pady=(10, 0))

# Input field
input_entry = tk.Entry(app, width=60, font=('Helvetica', 12))
input_entry.pack(pady=(5, 10))

# Result field
result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var, width=60, bg='#2f2f2f', fg='white', font=('Helvetica', 12, 'bold'), wraplength=500, justify='left')
result_label.pack(pady=(10, 10))

# Encrypt button
encrypt_button = tk.Button(app, text="Encrypt", command=handle_encrypt, bg='#1e90ff', fg='white', font=('Helvetica', 12, 'bold'), padx=10, pady=5)
encrypt_button.pack(pady=(5, 10))

# Decrypt button
decrypt_button = tk.Button(app, text="Decrypt", command=handle_decrypt, bg='#32cd32', fg='white', font=('Helvetica', 12, 'bold'), padx=10, pady=5)
decrypt_button.pack(pady=(5, 20))

# Run the app
app.mainloop()
