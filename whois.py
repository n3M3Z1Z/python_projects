#!/usr/bin/env python3

# Import

import socket

# define the function

def whois_lookup(domain: str):
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{domain}\r\n".encode())
    response = s.recv(4096).decode()
    s.close()
    return response

# Example usage


print(whois_lookup("heidees.de"))
