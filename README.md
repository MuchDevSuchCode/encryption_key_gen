# encryption_key_gen
A python tool that allows secure passphrase/encryption key generation from a known salt and phrase/password.

Purpose:
The idea is that the user may remember a phrase, passphrase, password, or other familiar sentence, and securely derive an encryption key for use in another application, such as veracrypt. Since the user never stores the password or passphrase in a file, but rather, uses it to dervice a cryptographically stronger key programatically, security is enhanced significantly. 

Users may define variables such as output key length, iterations, etc. In addition, this app will generate a "key file" that may be used for added security. The key file can also be deleted at an automated interval to ensure it doesn't reside on disk indefinately. 

Lastly, for added security a quick change in code/comments allows a user to define both the salt and passphrase, from their memory, prior to generation of a key. Doing so significantly inceases the security of the dervivation process.