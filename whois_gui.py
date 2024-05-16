#!/usr/bin/env python3

import socket
import tkinter as tk
from tkinter import ttk

# Function to perform whois lookup
def whois_lookup(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{domain}\r\n".encode())
    response = s.recv(4096).decode()
    s.close()
    return response

# Function to display whois lookup results in a new window
def display_results():
    domain = entry_domain.get()
    result = whois_lookup(domain)
    
    # Create new window for displaying results
    result_window = tk.Toplevel(root)
    result_window.title("Whois Lookup Results")
    
    # Create text widget to display results
    result_text = tk.Text(result_window, wrap=tk.WORD, width=80, height=20)
    result_text.insert(tk.END, result)
    result_text.pack(padx=10, pady=10)

# Function to toggle between light and dark themes
def toggle_theme():
    # Switching between light and dark themes
    if theme_button["text"] == "Dark Theme":
        root.configure(bg="white")
        frame.configure(bg="white")
        theme_button["text"] = "Light Theme"
    else:
        root.configure(bg="#1E1E1E")
        frame.configure(bg="#1E1E1E")
        theme_button["text"] = "Dark Theme"

# Create main window
root = tk.Tk()
root.title("Whois Lookup")
root.geometry("400x200")
root.configure(bg="#1E1E1E")

# Create frame
frame = ttk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Create domain label and entry
label_domain = ttk.Label(frame, text="Domain:", foreground="white", background="#1E1E1E")
label_domain.grid(row=0, column=0, pady=(0, 5))

entry_domain = ttk.Entry(frame, width=30)
entry_domain.grid(row=0, column=1, pady=(0, 5))

# Create lookup button
lookup_button = ttk.Button(frame, text="Lookup", command=display_results)
lookup_button.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Create theme button
theme_button = ttk.Button(root, text="Dark Theme", command=toggle_theme)
theme_button.pack(pady=10)

root.mainloop()