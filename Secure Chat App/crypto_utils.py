from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def encrypt_message(message, public_key_bytes):
    recipient_key = RSA.import_key(public_key_bytes)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted = cipher_rsa.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_message_b64, private_key_bytes):
    private_key = RSA.import_key(private_key_bytes)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    encrypted = base64.b64decode(encrypted_message_b64.encode())
    return cipher_rsa.decrypt(encrypted).decode()
