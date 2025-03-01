import conversions as conv
import keys
import algoritmos as alg

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
print("texto abinario: " + contenido_binario)

contenido_base64 = conv.binario_a_base64(contenido_binario)
print("texto a base64: " + contenido_base64)

contenido_binario = conv.base64_a_binario(contenido_base64)
print("base64 a binario: " + contenido_binario)

contenido = conv.binario_a_texto(contenido_binario)
print("binario a texto: " + contenido)

contenido = conv.base64_a_ascii(contenido_base64)
print("base64 a ascii: " + contenido)

llave = keys.generar_llave_ascii(15)
print("llave: " + llave)

texto_cifrado = keys.cypher_dinamico(contenido)
print("texto cifrado: " + texto_cifrado)

#texto_cifrado2 = keys.cypher_estatico(contenido)
#print("texto cifrado: " + texto_cifrado2)

texto_descifrado = keys.decipher_texto(texto_cifrado, llave)
print("texto descifrado: " + texto_descifrado)


texto_cifrado = alg.cifrar_afin(contenido, 5, 8)
print("texto cifrado afin: " + texto_cifrado)

texto_descifrado = alg.descifrar_afin(texto_cifrado, 5, 8)
print("texto descifrado afin: " + texto_descifrado)

texto_cifrado = alg.cifrar_cesar(contenido, 5)
print("texto cifrado cesar: " + texto_cifrado)

texto_descifrado = alg.descifrar_cesar(texto_cifrado, 5)
print("texto descifrado cesar: " + texto_descifrado)

texto_cifrado = alg.cifrar_vigenere(contenido)
print("texto cifrado vigenere: " + texto_cifrado)

texto_descifrado = alg.descifrar_vigenere(texto_cifrado)
print("texto descifrado vigenere: " + texto_descifrado)
