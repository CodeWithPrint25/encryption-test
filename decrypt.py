# Notice; Please run through voldemort.py (encrption script) or else this'll not work
# Import Some Stuff
import os
from cryptography.fernet import Fernet
from tqdm import tqdm
import time
import random

files = []

# Make sure not to mess with important files
for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


# Open the key
with open("thekey.key", "rb") as key_file:
    key = key_file.read()

f = Fernet(key)


# Decrypt Files
for file in tqdm(files, desc="Decrypting files"):
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
    time.sleep(random.uniform(0.5, 1.5))

# Show decrypted files
print(f"Decrypted Files: {files}")
