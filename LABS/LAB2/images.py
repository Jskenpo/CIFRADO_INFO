import base64 as b64
import numpy as np
from PIL import Image
import conversions as conv 
import keys as k 


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = b64.b64encode(image_file.read())
    return encoded_string.decode("utf-8")

def descifrar_imagen(base64_cifrado, llave):
    # Convertir Base64 a binario
    binario_cifrado = conv.base64_a_binariox(base64_cifrado)

    # Expandir la llave para igualar la longitud del binario cifrado
    llave_binaria = ''.join(format(ord(c), '08b') for c in (llave * (len(binario_cifrado) // len(llave)) + llave[:len(binario_cifrado) % len(llave)]))

    # Aplicar XOR
    binario_descifrado = k.xor_binario(binario_cifrado, llave_binaria)

    # Convertir binario a bytes
    imagen_original = conv.binario_a_bytes(binario_descifrado)

    # Guardar la imagen
    with open("imagen_recuperada.png", "wb") as f:
        f.write(imagen_original)

def cargar_imagen(ruta, size=None):
    img = Image.open(ruta).convert("RGB")  # Convertir a RGB
    if size:
        img = img.resize(size)  # Ajustar tamaño si es necesario
    return np.array(img)

def aplicar_xor(imagen1, imagen2):
    return np.bitwise_xor(imagen1, imagen2)