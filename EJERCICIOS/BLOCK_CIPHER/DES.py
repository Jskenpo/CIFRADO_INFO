from Crypto.Cipher import DES
from os import urandom

key = urandom(8)

def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def textoBytes(texto):
    textoBytes = texto.encode('utf-8')
    pad_length = 8 - (len(textoBytes) % 8)
    return textoBytes + bytes([pad_length] * pad_length)

def unpad(texto):
    pad_length = texto[-1]  # Último byte indica la cantidad de padding agregado
    return texto[:-pad_length]

def cifrar(texto):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = textoBytes(texto)
    textoCifrado = cipher.encrypt(padded_text)
    return textoCifrado

def descifrar(textoCifrado):
    cipher = DES.new(key, DES.MODE_ECB)
    textoDescifrado = cipher.decrypt(textoCifrado)
    return unpad(textoDescifrado).decode('utf-8')

texto = leerArchivo('DES.txt')
print('Texto a cifrar:', texto)

textoCifrado = cifrar(texto)
print('Texto cifrado:', textoCifrado.hex())

textoDescifrado = descifrar(textoCifrado)
print('Texto descifrado:', textoDescifrado)
