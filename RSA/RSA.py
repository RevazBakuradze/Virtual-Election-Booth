from RSA import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import *

def generate_keys():
    (public_key, private_key) = rsa.newKey(1024)

    with open('keys/public_key.pem') as f:
        f.write(public_key)