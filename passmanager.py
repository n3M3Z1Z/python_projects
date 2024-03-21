#!/usr/bin/env python3

#Import Section

import hashlib
import getpass

#build the password manager

password_manager= {}

#Account Creation

def create_account():
	username = input("Enter your desired username: ")
	password = getpass.getpass("Enter your desired password: ")
	hashed_password = hashlib.sha256(password.encode()).hexdigest()
	print("Account created successfully!")

#Build the login section

def login():
	username = input("Enter your username. ")
	password = getpass.getpass("Enter your password. ")
	hashed_password = hashlib.sha256(password.encode()).hexdigest()
	if username in password_manager.keys() and password_manager[username] == hashed_password:
		print("Login Successfull!")
	else: 
		print ("Invalid username or password")

#main function build

def main(): 
	while True:
		choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
		if choice == "1":
			create_account()
		elif choice == "2":
			login()
		elif choice == "0":
			break
		else:
			print("Invalid Choice")

if __name__ == "__main__":
	main()
