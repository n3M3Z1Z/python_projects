#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import string

# Function to encrypt message using Caesar cipher
def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message

# Function to decrypt message using Caesar cipher
def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    decrypted_message = encrypted_message.translate(cipher)
    return decrypted_message

# Function to handle encryption button click
def encrypt_message():
    message = input_text.get("1.0", "end-1c")
    key = int(key_entry.get())
    encrypted_message = caesar_encrypt(message, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_message)

# Function to handle decryption button click
def decrypt_message():
    encrypted_message = input_text.get("1.0", "end-1c")
    key = int(key_entry.get())
    decrypted_message = caesar_decrypt(encrypted_message, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_message)


# Create main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x300")
root.configure(bg="#9370DB")  # Purple background color

# Create frame
frame = ttk.Frame(root, padding=20, style="Purple.TFrame")
frame.pack(expand=True, fill=tk.BOTH)

# Create custom style for purple theme
style = ttk.Style()
style.configure("Purple.TFrame", background="#9370DB")

# Create input label and text widget
input_label = ttk.Label(frame, text="Enter message:", style="Purple.TLabel")
input_label.pack()

input_text = tk.Text(frame, height=5, width=50)
input_text.pack(pady=5)

# Create key label and entry
key_label = ttk.Label(frame, text="Enter key (0-25):", style="Purple.TLabel")
key_label.pack()

key_entry = ttk.Entry(frame)
key_entry.pack(pady=5)

# Create buttons for encryption and decryption
encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt_message)
encrypt_button.pack(pady=5)

decrypt_button = ttk.Button(frame, text="Decrypt", command=decrypt_message)
decrypt_button.pack(pady=5)

# Create output label and text widget
output_label = ttk.Label(frame, text="Result:", style="Purple.TLabel")
output_label.pack()

output_text = tk.Text(frame, height=5, width=50)
output_text.pack(pady=5)

root.mainloop()
