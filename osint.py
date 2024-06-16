"""
               .-')                 .-') _  .-') _      _ (`-.              
              ( OO ).              ( OO ) )(  OO) )    ( (OO  )             
 .-'),-----. (_)---\_)  ,-.-') ,--./ ,--,' /     '._  _.`     \  ,--.   ,--.
( OO'  .-.  '/    _ |   |  |OO)|   \ |  |\ |'--...__)(__...--''   \  `.'  / 
/   |  | |  |\  :` `.   |  |  \|    \|  | )'--.  .--' |  /  | | .-')     /  
\_) |  |\|  | '..`''.)  |  |(_/|  .     |/    |  |    |  |_.' |(OO  \   /   
  \ |  | |  |.-._)   \ ,|  |_.'|  |\    |     |  |    |  .___.' |   /  /\_  
   `'  '-'  '\       /(_|  |   |  | \   |     |  |.-. |  |      `-./  /.__) 
     `-----'  `-----'   `--'   `--'  `--'     `--'`-' `--'        `--'      
"""
import subprocess
import sys
import tkinter as tk
from tkinter import scrolledtext
import socket
import requests
from bs4 import BeautifulSoup

# Function to install required modules
def install_missing_modules(modules):
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])

# List of required modules
required_modules = [
    'requests',
    'beautifulsoup4'
]

# Install missing modules
install_missing_modules(required_modules)

# Tkinter App
class OSINTFramework(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OSINT Framework")
        self.geometry("800x600")
        self.configure(bg="black")

# Labels
        self.create_label("Organization Domain:", 0)
        self.create_label("Results:", 1)

# Entries
        self.domain_entry = self.create_entry(0)
        self.results_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=20, bg="black", fg="green")
        self.results_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Start Button
        start_button = tk.Button(self, text="Start OSINT", command=self.start_osint, bg="green", fg="black")
        start_button.grid(row=2, column=0, columnspan=2, pady=10)

    def create_label(self, text, row):
        label = tk.Label(self, text=text, bg="black", fg="green")
        label.grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)

    def create_entry(self, row):
        entry = tk.Entry(self, bg="white", fg="black")
        entry.grid(row=row, column=1, padx=10, pady=5, sticky=tk.W+tk.E)
        return entry

    def start_osint(self):
        domain = self.domain_entry.get()
        if not domain:
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Please enter a domain.")
            return

        self.results_text.delete(1.0, tk.END)

# Gather information using OSINT techniques
        try:
            self.results_text.insert(tk.END, f"Domain: {domain}\n\n")

# DNS Lookup
            self.results_text.insert(tk.END, "DNS Information:\n")
            ip_addresses = set()
            try:
                ip_addresses.update(set([str(ip) for ip in socket.gethostbyname_ex(domain)[2]]))
            except socket.gaierror:
                pass
            self.results_text.insert(tk.END, f"IP Addresses: {', '.join(ip_addresses)}\n\n")

# Web scraping example (Basic example)
            self.results_text.insert(tk.END, "Web Scraping Example (Title of webpage):\n")
            try:
                response = requests.get(f"http://{domain}")
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.find('title').get_text()
                self.results_text.insert(tk.END, f"Title: {title}\n\n")
            except Exception as e:
                self.results_text.insert(tk.END, f"Error: {str(e)}\n\n")

        except Exception as e:
            self.results_text.insert(tk.END, f"Error: {str(e)}\n")

# Main function to run the application
if __name__ == "__main__":
    app = OSINTFramework()
    app.mainloop()