import hashlib
import settings

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class encryption_key:
    def __init__(self, password, salt='placeholder'):
        self.password = password
        if salt == '':
            self.salt = settings.KEY_SALT
        else:
            self.salt = salt
        print(self.salt)
        print(self.password)

    def get_key(self):
        # Create PBKDF2 instance
        print(self.salt)
        presalt = self.salt.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=settings.KEY_LENGTH,
            salt=presalt,
            iterations=settings.KEY_ITERATIONS,
            backend=default_backend()
        )
        # Generate derived key
        key = kdf.derive(self.password.encode())

        # Generate hash
        aes512_hash = hashlib.sha512(key).hexdigest()
        return aes512_hash


# Create salt
#salt = settings.KEY_SALT.encode()  # If you prefer to manually enter your salt and passphrase, comment this line and uncomment the two lines below.
# salt = getpass.getpass("Enter your salt: ")
# salt = salt.encode()
# print(salt)





# Print results
# print("Salt: " + salt.hex())

#print("Hash: " + aes512_hash)

#f = open("key", "a")
#f.write(f'{key}')
#f.close()

#time.sleep(settings.KEY_EXPIRATION)
#print(f'Removing key file...')
#os.remove("key")
