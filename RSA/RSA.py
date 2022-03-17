'''
Thank you Aleksandr Molchagin for helping me writing keys in the file! 
you are the legenda
'''


import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
    with open("keys/private_key.pem", "wb+") as private_key_file_obj:
        with open("keys/public_key.pem", "wb+") as public_key_file_obj:

            private_key = rsa.generate_private_key(
                                public_exponent=65537,
                                key_size=2048,
                            )
            public_key = private_key.public_key()

            private_key_bytes = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )

            private_key_file_obj.write(private_key_bytes)
            public_key_bytes = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            public_key_file_obj.write(public_key_bytes)

# Generate Public and Private Keys for CTF
generate_keys()