from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import urandom

# Tamaño de la clave AES (16, 24 o 32 bytes)
KEY_SIZE = 32  # AES-256
BLOCK_SIZE = 16  # Bloque de 16 bytes para AES

# Generar clave y vector de inicialización aleatorios
key = urandom(KEY_SIZE)
iv = urandom(BLOCK_SIZE)  # Necesario solo para CBC

def leer_archivo(nombre_archivo):
    """Lee un archivo en modo binario y devuelve su contenido."""
    with open(nombre_archivo, 'rb') as archivo:
        return archivo.read()

def escribir_archivo(nombre_archivo, contenido):
    """Escribe datos en un archivo en modo binario."""
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(contenido)

def cifrar_aes(texto, modo):
    """Cifra el contenido usando AES en modo ECB o CBC."""
    if modo == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif modo == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("Modo no válido. Usa 'ECB' o 'CBC'.")
    
    texto_cifrado = cipher.encrypt(pad(texto, BLOCK_SIZE))
    return texto_cifrado

def descifrar_aes(texto_cifrado, modo):
    """Descifra el contenido usando AES en modo ECB o CBC."""
    if modo == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif modo == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("Modo no válido. Usa 'ECB' o 'CBC'.")
    
    texto_descifrado = unpad(cipher.decrypt(texto_cifrado), BLOCK_SIZE)
    return texto_descifrado

# Leer imagen
imagen = leer_archivo('AES_Image.png')

# Cifrar en ECB y CBC
imagen_cifrada_ecb = cifrar_aes(imagen, 'ECB')
imagen_cifrada_cbc = cifrar_aes(imagen, 'CBC')

# Guardar imágenes cifradas
escribir_archivo('imagen_ecb.png', imagen_cifrada_ecb)
escribir_archivo('imagen_cbc.png', imagen_cifrada_cbc)

# Descifrar las imágenes
imagen_descifrada_ecb = descifrar_aes(imagen_cifrada_ecb, 'ECB')
imagen_descifrada_cbc = descifrar_aes(imagen_cifrada_cbc, 'CBC')

# Guardar imágenes descifradas
escribir_archivo('imagen_descifrada_ecb.png', imagen_descifrada_ecb)
escribir_archivo('imagen_descifrada_cbc.png', imagen_descifrada_cbc)

print("Cifrado y descifrado completado.")
