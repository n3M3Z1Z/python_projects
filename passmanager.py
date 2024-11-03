#!/usr/bin/env python3

# Import Section
import hashlib
import getpass

# Build the password manager
password_manager = {}

# Account Creation
def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password  # Save the username and hashed password
    print("Account created successfully!")

# Build the login section
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password")
        return None

# Set password function
def set_password(username):
    new_password = getpass.getpass("Enter your new password: ")
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Password updated successfully!")

# Main function build
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, 3 to set password, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            username = login()
            if username:
                print("Welcome,", username)
        elif choice == "3":
            username = login()
            if username:
                set_password(username)
        elif choice == "0":
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
