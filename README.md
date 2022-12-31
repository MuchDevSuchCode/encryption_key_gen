# PBKDF + HMAC Key Generator
Generate secure passphrases and encryption keys with zero trust.

## Purpose:
This tool allows for secure passphrase/encryption key generation from a known salt and phrase/password, using the PBKDF2 + HMAC derivation function. This ensures that users can generate cryptographically strong passwords, passphrases and encryption keys from easy to remember phrases, sentences, etc. 

Many technical tasks require cryptographically strong passphrases, such as file encryption, certificate keys/stores, etc. One historical challenge is that while these keys/passphrases may be strong, they must be stored to ensure they aren't lost or forgotten.

The idea here is that a user may remember a phrase, passphrase, password, or other familiar sentence, and securely derive an encryption key for use in another application, such as VeraCrypt, password managers, etc. Since the user never stores the password or passphrase in a file, cloud service, etc., but rather, uses it to derive a cryptographically strong key programmatically, security is enhanced significantly. 

Users may configure variables such as output key length, iterations, etc. In addition, this app will generate a "key file" that may be used for added security. The key file can also be deleted at an automated interval to ensure it doesn't reside on disk indefinitely. 

Lastly, for added security a quick change in code/comments allows a user to define both the salt and passphrase, from their memory, prior to generation of a key. Doing so significantly increases the security of the derivation process.

## How To:
- Checkout the source code by running the command: `git clone git@github.com:MuchDevSuchCode/encryption_key_gen.git`. 
- Change directories using `cd encryption_key_gen/`.
- Ensure you have all dependencies by typing `pip3 install -r requirements.txt`.
- Run the app by typing `python3 main.py`

### When creating a passphrase or key for the first time:
- Ensure that you set all of you parameters in the settings.py file or remember them.
- Generate your passphrase or key, using your salt and password.
- Copy/Paste the output passphrase/key to whatever app, tool, site, etc. that you're securing.
- Repeat the process again anytime you need to access said storage, site, tool, etc. 

## Best Practices:
- Remember that, while this tool seeks to derive a strong encryption key or passphrase, its output is only as good as it's input. It is NOT recommended to use things like pet names, previously used passwords, dates of birth, or other details that can be easily guessed or found about you. 
- Once you generate your passphrase/key, and use it in production, do NOT adjust your parameters. Changing any values such as key length, algorithm, iterations, etc. will result in a different passphrase/key being generated in the future and will likely result in loss of access to your assets. 
- Do NOT forget your seed/phrase or you will not be able to re-generate your encryption key/passphrase in the future. 

## App Settings - settings.py 
```
- KEY_ALGORITHM = "SHA256"  # Encryption Algorithm - Not implemented yet.
- KEY_LENGTH = 128          # Encryption Key Length
- KEY_SALT = "ABCDE12345"   # Enter a Static Salt - Please do not leave the default, this is for example purposes.
- KEY_ITERATIONS=500000     # Number of PBKDF Iterations
- KEYFILE_NAME = "key"      # By default the key file is named "key". Change the name here to anything you like - Not implemented yet.
- KEY_EXPIRATION = 120      # Defines how long to leave the key file on the hard disk before deleting it. This is in seconds.
```

## TO Do:
- Add support for key file enablement/disablement and file name conventions.
- Add a list of valid parameters for the PBKDF function within the settings file.