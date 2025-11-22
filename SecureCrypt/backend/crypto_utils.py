from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate AES Key
def generate_aes_key():
    return Fernet.generate_key()

# AES Encrypt
def aes_encrypt(aes_key, message):
    cipher = Fernet(aes_key)
    return cipher.encrypt(message.encode())

# AES Decrypt
def aes_decrypt(aes_key, ciphertext):
    cipher = Fernet(aes_key)
    return cipher.decrypt(ciphertext).decode()

# RSA Key Pair Create
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# RSA Encrypt AES Key
def rsa_encrypt(public_key, aes_key):
    pub = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(pub)
    return cipher.encrypt(aes_key)

# RSA Decrypt AES Key
def rsa_decrypt(private_key, encrypted_aes):
    priv = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(priv)
    return cipher.decrypt(encrypted_aes)
