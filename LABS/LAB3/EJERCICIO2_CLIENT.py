import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_message(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(message.encode(), AES.block_size))

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.42.95', 9999))

    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    
    # Enviar la clave y el IV al servidor primero (simulación)
    client.sendall(key + iv)

    while True:
        message = input("Escribe un mensaje (o 'exit'): ")
        if message.lower() == 'exit':
            break
        encrypted = encrypt_message(message, key, iv)
        client.sendall(encrypted)
        print("Mensaje cifrado enviado:", encrypted.hex())

    client.close()

if __name__ == "__main__":
    main()