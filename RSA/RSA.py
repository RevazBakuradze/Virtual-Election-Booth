from xmlrpc.client import ServerProxy
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    with open("private_key.pem", "rb") as private_key_file:
        private_key_file = serialization.load_pem_private_key(private_key_file.read(), password=None)

    # pem = private_key.private_bytes(
    #     encoding=serialization.Encoding.PEM,
    #     format=serialization.PrivateFormat.PKCS8,
    #     encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword') # serialization.NoEncryption
    # )

    public_key = private_key.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("public_key.pem", "rb") as public_key_file:
        public_key_file = serialization.load_pem_private_key(public_key_file.read(), password=None)

    # pem.splitlines()[0]

generate_keys()