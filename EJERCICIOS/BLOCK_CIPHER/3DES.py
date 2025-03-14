from Crypto.Cipher import DES3
from os import urandom
from Crypto.Util.Padding import pad, unpad

# Tamaño de la clave para 3DES (16 o 24 bytes)
KEY_SIZE = 24
BLOCK_SIZE = 8  # Bloque de 8 bytes para 3DES

# Generar clave aleatoria (debe ser múltiplo de 8)
key = urandom(KEY_SIZE)

# Asegurar que la clave sea válida para 3DES (necesita ser de 16 o 24 bytes)
while len(key) not in (16, 24):
    key = urandom(KEY_SIZE)

# Generar IV aleatorio de 8 bytes
iv = urandom(BLOCK_SIZE)

def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def cifrar_3des(mensaje):
    """Cifra un mensaje con 3DES en modo CBC."""
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    mensaje_cifrado = cipher.encrypt(pad(mensaje.encode(), BLOCK_SIZE))
    return mensaje_cifrado

def descifrar_3des(mensaje_cifrado):
    """Descifra un mensaje con 3DES en modo CBC."""
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    mensaje_descifrado = unpad(cipher.decrypt(mensaje_cifrado), BLOCK_SIZE)
    return mensaje_descifrado.decode()

# Mensaje a cifrar
mensaje = leerArchivo('3des.txt')
print(f"Mensaje original: {mensaje}")

# Cifrar el mensaje
mensaje_cifrado = cifrar_3des(mensaje)
print(f"Mensaje Cifrado: {mensaje_cifrado}")

# Descifrar el mensaje
mensaje_descifrado = descifrar_3des(mensaje_cifrado)
print(f"Mensaje Descifrado: {mensaje_descifrado}")