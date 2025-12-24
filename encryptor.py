from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate a new key and save to key.key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'key.key'.")

def load_key():
    """Load the key from key.key"""
    return open("key.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted)
    print(f"File '{filename}' encrypted as '{filename}.encrypted'.")

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    decrypted = f.decrypt(data)
    new_filename = filename.replace(".encrypted", ".decrypted")
    with open(new_filename, "wb") as file:
        file.write(decrypted)
    print(f"File '{filename}' decrypted as '{new_filename}'.")

def menu():
    while True:
        print("\n=== File Encryptor ===")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            filename = input("Enter filename to encrypt: ")
            if os.path.exists(filename):
                encrypt_file(filename)
            else:
                print("File not found!")
        elif choice == "3":
            filename = input("Enter filename to decrypt: ")
            if os.path.exists(filename):
                decrypt_file(filename)
            else:
                print("File not found!")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()

