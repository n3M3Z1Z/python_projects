#!/usr/bin/env python3

#Import

import string

#define encryption

def caesar_encrypt(message, key):

	shift = key % 26
	cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

	encrypted_message = message.lower().translate(cipher)

	return encrypted_message

# define decryption 

def caesar_decrypt(encrypted_message, key):

	shift = 26 - (key % 26)
	cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

	message = encrypted_message.translate(cipher)
	return message

message = 'Terror Hamster from hell, no lets be serious hamsters are tasty, just like chicken or caesar salad'
key = 7

#Set the pieces togther

encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message  = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')
