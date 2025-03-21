from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def pad_data(data):
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length] * padding_length)

def unpad_data(data):
    padding_length = data[-1]
    return data[:-padding_length]

def read_ppm_header(image_path):
    with open(image_path, "rb") as f:
        header = b""
        for _ in range(3):  # Leer las 3 primeras líneas
            header += f.readline()
        data = f.read()
    return header, data

def encrypt_image(image_path, output_path_ecb, output_path_cbc, key):
    # Leer cabecera y datos de la imagen
    header, pixel_data = read_ppm_header(image_path)
    img = Image.open(image_path).convert('L')
    original_size = img.size

    # Padding para ajustar a múltiplos de 16
    padded_data = pad_data(pixel_data)

    # Generar cifradores AES
    iv = get_random_bytes(16)
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    cipher_cbc = AES.new(key, AES.MODE_CBC, iv)

    # Cifrar
    encrypted_data_ecb = cipher_ecb.encrypt(padded_data)
    encrypted_data_cbc = cipher_cbc.encrypt(padded_data)

    # Guardar archivos cifrados con la cabecera
    save_encrypted_image(output_path_ecb, header, encrypted_data_ecb)
    save_encrypted_image(output_path_cbc, header, encrypted_data_cbc)

    # Guardar IV
    with open("iv.bin", "wb") as f:
        f.write(iv)

def decrypt_image(encrypted_path, output_path, key, mode, iv=None):
    # Leer cabecera
    header, encrypted_data = read_ppm_header(encrypted_path)

    # Crear cifrador
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == AES.MODE_CBC and iv is not None:
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("IV requerido para CBC")

    # Descifrar y quitar padding
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad_data(decrypted_data)

    # Guardar imagen descifrada con su cabecera
    with open(output_path, "wb") as f:
        f.write(header + unpadded_data)

def save_encrypted_image(output_path, header, encrypted_data):
    with open(output_path, 'wb') as f:
        f.write(header + encrypted_data)

key = get_random_bytes(16)

image_path = "tux.ppm"
output_ecb = "imagen_ecb.ppm"
output_cbc = "imagen_cbc.ppm"
decrypted_ecb = "imagen_decifrada_ecb.ppm"
decrypted_cbc = "imagen_decifrada_cbc.ppm"

encrypt_image(image_path, output_ecb, output_cbc, key)

with open("iv.bin", "rb") as f:
    iv = f.read()

decrypt_image(output_ecb, decrypted_ecb, key, AES.MODE_ECB)
decrypt_image(output_cbc, decrypted_cbc, key, AES.MODE_CBC, iv)

print("Cifrado y descifrado completado 🚀")


#comparar imagenes con matplotlib

image_paths = {
    "Original": "tux.ppm",
    "Cifrado ECB": "imagen_ecb.ppm",
    "Cifrado CBC": "imagen_cbc.ppm"
}

fig, axes = plt.subplots(1, 3, figsize=(10, 5))

for ax, (title, path) in zip(axes, image_paths.items()):
    img = Image.open(path).convert("L")  # Convertir a escala de grises
    ax.imshow(img, cmap="gray")
    ax.set_title(title)
    ax.axis("off")  # Ocultar ejes


plt.tight_layout()
plt.show()
