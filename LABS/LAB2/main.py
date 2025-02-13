import conversions as conv 
import keys as k 
import images as img
from PIL import Image

image_path = "imas/p1.png"

# Convertir la imagen a base64
image_base64 = img.image_to_base64(image_path)

llave = "cifrados_2025"

# Descifrar la imagen
img.descifrar_imagen(image_base64, llave)


#cargar imágenes 
imagen1 = img.cargar_imagen("imas/luffy.jpg")
imagen2 = img.cargar_imagen("imas/shanks.jpeg", size=imagen1.shape[:2][::-1])

# Aplicar XOR
imagen_xor = img.aplicar_xor(imagen1, imagen2)

#convertir a imagen 
imagen_xor_pil = Image.fromarray(imagen_xor)

# Guardar la imagen
imagen_xor_pil.save("imagen_xor.png")


