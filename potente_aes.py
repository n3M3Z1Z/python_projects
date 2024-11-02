import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import binascii

# Generate AES key and IV
aes_key = os.urandom(32)  # 256-bit key
iv = os.urandom(16)  # 128-bit IV

# Encrypt message
def encrypt(text):
    # Pad the plaintext to be multiple of block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(text.encode('utf-8')) + padder.finalize()

    # Create AES cipher and encrypt
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_data) + encryptor.finalize()

    return binascii.hexlify(iv + encrypted_text).decode('utf-8')  # Include IV in the output

# Decrypt message
def decrypt(encrypted_text):
    encrypted_data = binascii.unhexlify(encrypted_text)
    iv = encrypted_data[:16]  # Extract IV from the beginning
    encrypted_message = encrypted_data[16:]

    # Create AES cipher and decrypt
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

    # Unpad the decrypted plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

    return decrypted_message.decode('utf-8')

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
app.title("AES Encrypt/Decrypt")
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
