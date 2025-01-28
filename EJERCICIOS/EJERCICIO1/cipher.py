import conversions as conv

def leer_archivo_txt(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return f"Error: El archivo '{ruta_archivo}' no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {e}"

ruta = "text.txt"  
contenido = leer_archivo_txt(ruta)
print(contenido)

contenido_binario = conv.texto_a_binario(contenido)
print("texto abinario " + contenido_binario)

contenido_base64 = conv.binario_a_base64(contenido_binario)
print("texto a base64 " + contenido_base64)

contenido_binario = conv.base64_a_binario(contenido_base64)
print("base64 a binario " + contenido_binario)
