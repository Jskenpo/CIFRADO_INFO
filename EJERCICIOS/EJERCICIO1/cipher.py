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
print(contenido_binario)
