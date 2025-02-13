import conversions as conv 
import keys as k 
import images as img

image_path = "imas/p1.png"

# Convertir la imagen a base64
image_base64 = img.image_to_base64(image_path)

llave = "cifrados_2025"

# Descifrar la imagen
img.descifrar_imagen(image_base64, llave)

