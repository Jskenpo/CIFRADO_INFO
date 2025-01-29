import conversions as conv
import keys

def leer_archivo_txt(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return f"Error: El archivo '{ruta_archivo}' no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {e}"

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def inverso_modular(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f"No existe inverso modular para a={a} y m={m}")

def cifrar_afin(texto, a, b):
    if mcd(a, 26) != 1:
        raise ValueError("El valor de 'a' debe ser coprimo con 26.")
    
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():  # Solo cifrar letras
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            # Aplicar fórmula del cifrado afín
            cifrado = (a * x + b) % 26
            texto_cifrado += chr(cifrado + base)
        else:
            texto_cifrado += char  # Mantener caracteres no alfabéticos
    return texto_cifrado

def descifrar_afin(texto_cifrado, a, b):
    if mcd(a, 26) != 1:
        raise ValueError("El valor de 'a' debe ser coprimo con 26.")
    
    texto_descifrado = ""
    a_inv = inverso_modular(a, 26)  # Obtener el inverso modular de 'a'
    for char in texto_cifrado:
        if char.isalpha():  # Solo descifrar letras
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            # Aplicar fórmula del descifrado afín
            descifrado = (a_inv * (x - b)) % 26
            texto_descifrado += chr(descifrado + base)
        else:
            texto_descifrado += char  # Mantener caracteres no alfabéticos
    return texto_descifrado



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

texto_cifrado2 = keys.cypher_estatico(contenido)
print("texto cifrado: " + texto_cifrado2)

texto_descifrado = keys.decipher_texto(texto_cifrado, llave)
print("texto descifrado: " + texto_descifrado)


texto_cifrado = cifrar_afin(contenido, 5, 8)
print("texto cifrado: " + texto_cifrado)

texto_descifrado = descifrar_afin(texto_cifrado, 5, 8)
print("texto descifrado: " + texto_descifrado)
