# PBKDF + HMAC Key Generator
Generate secure passphrases and encryption keys with zero trust.
## Purpose:
This tool allows for secure passphrase/encryption key generation from a known salt and phrase/password, using the PBKDF2 + HMAC derivation function. This ensures that users can generate cryptographically strong passwords, passphrases and encryption keys from easy to remember phrases, sentences, etc. 

Many technical tasks require cryptographically strong passphrases, such as file encryption, certificate keys/stores, etc. One historical challenge is that while these keys/passphrases may be strong, they must be stored to ensure they aren't lost or forgotten.

The idea here is that a user may remember a phrase, passphrase, password, or other familiar sentence, and securely derive an encryption key for use in another application, such as VeraCrypt, password managers, etc. Since the user never stores the password or passphrase in a file, cloud service, etc., but rather, uses it to derive a cryptographically strong key programmatically, security is enhanced significantly. 

Users may configure variables such as output key length, iterations, etc. In addition, this app will generate a "key file" that may be used for added security. The key file can also be deleted at an automated interval to ensure it doesn't reside on disk indefinitely. 

Lastly, for added security a quick change in code/comments allows a user to define both the salt and passphrase, from their memory, prior to generation of a key. Doing so significantly increases the security of the derivation process.

## App Settings - settings.py 
- KEY_ALGORITHM = "SHA256"  # Encryption Algorithm - Not implemented yet.
- KEY_LENGTH = 128          # Encryption Key Length
- KEY_SALT = "ABCDE12345"   # Enter a Static Salt - Please do not leave the default, this is for example purposes.
- KEY_ITERATIONS=500000     # Number of PBKDF Iterations
- KEYFILE_NAME = "key"      # By default the key file is named "key". Change the name here to anything you like - Not implemented yet.
- KEY_EXPIRATION = 120      # Defines how long to leave the key file on the hard disk before deleting it. This is in seconds.

## TO Do:
- Add support for key file enabledment and file name conventions.
- Add a list of valid parameters for the PBKDF function within the settings file.