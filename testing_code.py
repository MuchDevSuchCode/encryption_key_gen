import hashlib
import os
import time
import getpass
import settings

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

if os.path.exists("key"):
  print(f"Deleting pre-existing key file...")
  os.remove("key")
else:
  print(f"No key file found, continuing...")

# Create salt
salt = settings.KEY_SALT.encode()  # If you prefer to manually enter your salt and passphrase, comment this line and uncomment the two lines below.
# salt = getpass.getpass("Enter your salt: ")
# salt = salt.encode()
# print(salt)

# Get user supplied password
password = getpass.getpass("Passphrase: ")

# Create PBKDF2 instance
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=settings.KEY_LENGTH,
    salt=salt,
    iterations=settings.KEY_ITERATIONS,
    backend=default_backend()
)

# Generate derived key
key = kdf.derive(password.encode())

# Generate hash
aes512_hash = hashlib.sha512(key).hexdigest()

# Print results
# print("Salt: " + salt.hex())
print("Hash: " + aes512_hash)

f = open("key", "a")
f.write(f'{key}')
f.close()

time.sleep(settings.KEY_EXPIRATION)
print(f'Removing key file...')
os.remove("key")
