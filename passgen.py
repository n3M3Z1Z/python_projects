#!/usr/bin/env python3

import random
import string

# Define and specify the function!

def generate_password(length: int = 25):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

# Output Section


password = generate_password()
print(f"Generated password: {password}")
