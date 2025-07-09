import socket
from crypto_utils import generate_key_pair, encrypt_message, decrypt_message

public_key, private_key = generate_key_pair()

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 9999))

server_public_key = client_socket.recv(4096)
client_socket.send(public_key)

while True:
    message = input("[You]: ")
    encrypted = encrypt_message(message, server_public_key)
    client_socket.send(encrypted.encode())

    data = client_socket.recv(4096).decode()
    if not data:
        break
    decrypted = decrypt_message(data, private_key)
    print(f"[Server]: {decrypted}")
