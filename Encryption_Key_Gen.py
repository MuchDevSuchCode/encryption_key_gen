import hashlib
import settings
import logging

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class encryption_key:
    def __init__(self, passphrase, salt):
        self.passphrase = passphrase
        self.salt = salt
        if salt == '':
            self.salt = settings.KEY_SALT
            print(f'Using Default Salt: {self.salt}')
        else:
            self.salt = salt
            print(f'Using Custom Salt: {self.salt}')
            

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