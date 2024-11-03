import os
import hashlib

# Function to calculate SHA-256 hash of a file
def calculate_hash(file_path):
    # Open the file in binary mode ('rb' means 'read binary')
    with open(file_path, 'rb') as f:
        sha256 = hashlib.sha256()  # Create a SHA-256 hash object
        while True:
            data = f.read(65536)  # Read the file 64KB at a time
            if not data:
                break
            sha256.update(data)  # Update the hash object with the read data
    return sha256.hexdigest()  # Return the hexadecimal digest of the hash

# Function to check integrity of files in a folder
def check_integrity(folder_path):
    checksums = {}  # Dictionary to store filename-checksum pairs
    checksum_file = os.path.join(folder_path, 'Checksummen.txt')  # Path to Checksummen.txt

    # Check if Checksummen.txt already exists
    if os.path.exists(checksum_file):
        # If it exists, read existing checksums from the file
        with open(checksum_file, 'r') as f:
            for line in f:
                if ',' in line:
                    filename, checksum = line.strip().split(',')
                    checksums[filename] = checksum

    # Calculate checksums for all files in the folder
    with open(checksum_file, 'w') as f:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                current_checksum = calculate_hash(file_path)
                checksums[filename] = current_checksum
                f.write(f"{filename},{current_checksum}\n")  # Write filename and checksum to file

    # Compare calculated checksums with stored ones
    for filename, stored_checksum in checksums.items():
        current_checksum = calculate_hash(os.path.join(folder_path, filename))
        if current_checksum != stored_checksum:
            print(f"Integrity check failed for file: {filename}")

    print("Integrity check completed.")


# Example usage
folder_to_check = '/path/to/your/folder'  # Replace with the path to your folder
check_integrity(folder_to_check)
