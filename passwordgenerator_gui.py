#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import random
import string

# Function to generate a password
def generate_password(length: int = 25):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

# Function to generate and display password
def generate_and_display_password():
    length = int(length_spinbox.get())
    password = generate_password(length)
    password_text.delete(1.0, tk.END)
    password_text.insert(tk.END, password)

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#E8FFB7")  # Lemon green background color

# Create frame
frame = ttk.Frame(root, padding=20, style="Green.TFrame")
frame.pack(expand=True, fill=tk.BOTH)

# Create custom style for lemon green theme
style = ttk.Style()
style.configure("Green.TFrame", background="#E8FFB7")
style.configure("Green.TLabel", background="#E8FFB7")

# Create password label
password_label = ttk.Label(frame, text="Generated password:", style="Green.TLabel")
password_label.pack(pady=(0, 10))

# Create password text widget
password_text = tk.Text(frame, height=1, width=30)
password_text.pack(pady=(0, 10))

# Create spinbox for password length
length_spinbox_label = ttk.Label(frame, text="Password Length:", style="Green.TLabel")
length_spinbox_label.pack()

length_spinbox = ttk.Spinbox(frame, from_=1, to=100, width=5)
length_spinbox.pack(pady=(0, 10))

# Create generate button
generate_button = ttk.Button(frame, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

root.mainloop()