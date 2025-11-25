import json
import os
import sys
import base64
from getpass import getpass

# Dependency check
try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    print("Error: 'cryptography' library is required.")
    print("Please install it using: pip install cryptography")
    sys.exit(1)

def decrypt_vault(file_path, hex_key):
    """
    Decrypts a LifeVault JSON file using AES-GCM.
    """
    try:
        # Load the encrypted vault file
        with open(file_path, 'r') as f:
            vault_data = json.load(f)

        # Extract components
        ciphertext_hex = vault_data.get('ciphertext')
        iv_hex = vault_data.get('iv')

        if not ciphertext_hex or not iv_hex:
            print("[-] Invalid vault file format.")
            return

        # Convert hex strings back to bytes
        key = bytes.fromhex(hex_key)
        iv = bytes.fromhex(iv_hex)
        ciphertext = bytes.fromhex(ciphertext_hex)

        # Initialize AES-GCM
        aesgcm = AESGCM(key)

        # Decrypt
        # Note: Web Crypto API usually doesn't append AAD by default in simple implementations,
        # but if it did, it would be passed here.
        decrypted_bytes = aesgcm.decrypt(iv, ciphertext, None)
        
        # Decode JSON
        decrypted_data = json.loads(decrypted_bytes.decode('utf-8'))

        return decrypted_data

    except ValueError as e:
        print("\n[!] Decryption Failed: Invalid Key or Corrupted Data.")
        print(f"Debug info: {e}")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")

def display_secrets(data):
    print("\n" + "="*60)
    print(f"🔓 VAULT UNLOCKED: {len(data)} entries found")
    print("="*60 + "\n")

    for idx, entry in enumerate(data, 1):
        print(f"[{idx}] {entry.get('category', 'General').upper()}: {entry.get('title')}")
        print(f"    User:   {entry.get('username')}")
        print(f"    Secret: {entry.get('secret')}")
        if entry.get('notes'):
            print(f"    Notes:  {entry.get('notes')}")
        print("-" * 60)

def main():
    print("""
    ██╗     ██╗███████╗███████╗██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
    ██║     ██║██╔════╝██╔════╝██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
    ██║     ██║█████╗  █████╗  ██║   ██║███████║██║   ██║██║     ██║   
    ██║     ██║██╔══╝  ██╔══╝  ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║   
    ███████╗██║██║     ███████╗ ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║   
    ╚══════╝╚═╝╚═╝     ╚══════╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝   
                                                        
    -- OFFLINE RECOVERY TOOL --
    """)

    # 1. Get File
    file_path = input("Enter path to .vault file (e.g., my_legacy.vault): ").strip()
    if not os.path.exists(file_path):
        print("[-] File not found.")
        return

    # 2. Get Key
    print("\nEnter the Master Key provided by the Vault Creator.")
    key_input = getpass("Master Key (Input hidden): ").strip()

    # 3. Decrypt
    decrypted_data = decrypt_vault(file_path, key_input)

    if decrypted_data:
        display_secrets(decrypted_data)
        
        save_choice = input("\nSave decrypted data to text file? (y/n): ").lower()
        if save_choice == 'y':
            with open("RECOVERED_DATA.txt", "w") as f:
                json.dump(decrypted_data, f, indent=4)
            print("[+] Data saved to RECOVERED_DATA.txt. DELETE THIS FILE AFTER USE.")

if __name__ == "__main__":
    main()