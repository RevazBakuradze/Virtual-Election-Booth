'''
Thank you Aleksandr Molchagin for helping me writing keys in the file! 
You are the legend

https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
'''

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
public_key = private_key.public_key()

# Only for CTF
def get_private_key():
    return private_key

# For voters
def get_private_key():
    return public_key

# For voters to encrypt their vote + validation number
# Votes have to be in binary form, so pass b"message" as a parameter
def encrypt(message):
    ciphertext = public_key.encrypt(message, padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(), label=None
            )
        )

    return ciphertext

# Only for CTF to decrypt votes + validation numbers
def decrypt(ciphertext):
    plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),label=None
        )
    )
    return plaintext

# Only for testing purposes
def test_encryption_decryption_works():
    message = b"Oh, hello there. Just testing :-)"
    ciphertext = encrypt(message)
    decrypted_msg = decrypt(ciphertext)
    print(ciphertext)
    print(decrypted_msg)