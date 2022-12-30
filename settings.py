#PBKDF-HMAC Settings
KEY_ALGORITHM = "SHA256"  # Encryption Algorithm
KEY_LENGTH = 128          # Encryption Key Length
KEY_SALT = "ABCDE12345"   # Enter a Static Salt - Please do not leave the default, this is for example purposes.
KEY_ITERATIONS=500000     # Number of PBKDF Iterations

# App SEttings

KEYFILE_NAME = "key"      # By default the keyfile is named "key". Change the name here to anything you like.
KEY_EXPIRATION = 120      # Defines how long to leave the keyfile on the hard disk before deleting it.
