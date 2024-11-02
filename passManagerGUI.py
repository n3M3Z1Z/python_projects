#!/usr/bin/env python3

# Import Section
import hashlib
import getpass
import tkinter as tk
from tkinter import messagebox

# Build the password manager
password_manager = {}

# Function to create an account
def create_account():
    global password_manager
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_manager[username] = hashed_password
        messagebox.showinfo("Success", "Account created successfully!")
    else:
        messagebox.showerror("Error", "Username and password are required fields.")

# Function to log in
def login():
    global password_manager
    username = username_entry.get()
    password = password_entry.get()
    if username in password_manager.keys() and hashlib.sha256(password.encode()).hexdigest() == password_manager[username]:
        messagebox.showinfo("Success", "Login successful!")
        return True
    else:
        messagebox.showerror("Error", "Invalid username or password")
        return False

# Function to set password
def set_password():
    global password_manager
    username = username_entry.get()
    if username in password_manager.keys():
        new_password = password_entry.get()
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        password_manager[username] = hashed_password
        messagebox.showinfo("Success", "Password updated successfully!")
    else:
        messagebox.showerror("Error", "User not found.")

# Main function build
def main():
    global username_entry, password_entry
    # GUI Setup
    root = tk.Tk()
    root.title("User Authentication System")
    root.geometry("300x200")
    root.configure(bg="royal blue")

    # Username Entry
    username_label = tk.Label(root, text="Username:", bg="royal blue", fg="white")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    # Password Entry
    password_label = tk.Label(root, text="Password:", bg="royal blue", fg="white")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Buttons
    create_button = tk.Button(root, text="Create Account", command=create_account)
    create_button.pack(pady=5)
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=5)
    set_password_button = tk.Button(root, text="Set Password", command=set_password)
    set_password_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
