# encryption_key_gen
A python tool that allows secure passphrase/encryption key generation from a known salt and phrase/password.

Purpose:
The idea is that the user may remember a phrase, passphrase, password, or other familiar sentence, and securely derive an encryption key for use in another application, such as VeraCrypt. Since the user never stores the password or passphrase in a file, but rather, uses it to derive a cryptographically stronger key programmatically, security is enhanced significantly. 

Users may define variables such as output key length, iterations, etc. In addition, this app will generate a "key file" that may be used for added security. The key file can also be deleted at an automated interval to ensure it doesn't reside on disk indefinitely. 

Lastly, for added security a quick change in code/comments allows a user to define both the salt and passphrase, from their memory, prior to generation of a key. Doing so significantly increases the security of the derivation process.

App Settings - settings.py 
KEY_ALGORITHM = "SHA256"  # Encryption Algorithm - Not implimented yet.
KEY_LENGTH = 128          # Encryption Key Length
KEY_SALT = "ABCDE12345"   # Enter a Static Salt - Please do not leave the default, this is for example purposes.
KEY_ITERATIONS=500000     # Number of PBKDF Iterations
KEYFILE_NAME = "key"      # By default the keyfile is named "key". Change the name here to anything you like - Not implimented yet.
KEY_EXPIRATION = 120      # Defines how long to leave the keyfile on the hard disk before deleting it. This is in seconds.