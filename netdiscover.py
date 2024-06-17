"""
+=================================================================================================+
|_____   __    __________________                                                                 |
|___  | / /______  /______  /__(_)_____________________   __________________  __ _____________  __|
|__   |/ /_  _ \  __/  __  /__  /__  ___/  ___/  __ \_ | / /  _ \_  ___/_  / / / ___  __ \_  / / /|
|_  /|  / /  __/ /_ / /_/ / _  / _(__  )/ /__ / /_/ /_ |/ //  __/  /   _  /_/ /____  /_/ /  /_/ / |
|/_/ |_/  \___/\__/ \__,_/  /_/  /____/ \___/ \____/_____/ \___//_/    _\__, /_(_)  .___/_\__, /  |
|                                                                      /____/    /_/     /____/   |
+=================================================================================================+
"""
from scapy.all import ARP, Ether, srp
import socket

# Create ARP packet
# Create Ethernet frame
# Combine Ethernet frame and ARP packet
def discover_devices(ip_range):
    try:
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

# Send packet and capture response
        result = srp(packet, timeout=3, verbose=0)[0]

# Parse response
        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})

        return devices

    except Exception as e:
        print(f"Error occurred during device discovery: {e}")
        return []

# Create a UDP socket
# Connect to a known external server
# Get the local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

# Get the local IP address
# Define the IP range to scan (e.g., '192.168.1.0/24')
if __name__ == "__main__":
    local_ip = get_local_ip()
    ip_range = local_ip.rsplit('.', 1)[0] + '.0/24'

    print(f"Scanning network {ip_range}...")

# Discover devices on the network
    devices = discover_devices(ip_range)

# Print out discovered devices
    if devices:
        print("\nDiscovered devices:")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    else:
        print("No devices found.")

