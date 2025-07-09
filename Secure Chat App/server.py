import socket
from crypto_utils import generate_key_pair, decrypt_message
import threading

public_key, private_key = generate_key_pair()

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    conn.send(public_key)  # Send server's public key

    client_public_key = conn.recv(4096)  # Receive client's public key

    while True:
        data = conn.recv(4096).decode()
        if not data:
            break
        decrypted = decrypt_message(data, private_key)
        print(f"[Client]: {decrypted}")

        reply = input("[You]: ")
        encrypted = encrypt_message(reply, client_public_key)
        conn.send(encrypted.encode())

    conn.close()

def encrypt_message(msg, client_key):
    from crypto_utils import encrypt_message
    return encrypt_message(msg, client_key)

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 9999))
server_socket.listen(1)

print("[*] Waiting for connection on port 9999...")
conn, addr = server_socket.accept()
threading.Thread(target=handle_client, args=(conn, addr)).start()
