import hashlib
import settings
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class encryption_key:
    def __init__(self, passphrase, salt):
        self.passphrase = passphrase
        self.salt = salt
        if salt == '':
            print('Using Default Salt')
            self.salt = settings.KEY_SALT
        else:
            print('Using Custom Salt')
            self.salt = salt

    def get_key(self):
        # Create PBKDF2 instance
        # print(self.salt)
        presalt = self.salt.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=settings.KEY_LENGTH,
            salt=presalt,
            iterations=settings.KEY_ITERATIONS,
            backend=default_backend()
        )
        # Generate derived key
        key = kdf.derive(self.passphrase.encode())

        # Generate hash
        aes512_hash = hashlib.sha512(key).hexdigest()
        return aes512_hash