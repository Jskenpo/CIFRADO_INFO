from collections import Counter 

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
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    
    if mcd(a, 27) != 1:
        raise ValueError("El valor de 'a' debe ser coprimo con 27.")
    
    texto_descifrado = ""
    a_inv = inverso_modular(a, 27)  # Obtener el inverso modular de 'a'
    
    for char in texto_cifrado:
        if char in alfabeto:  # Solo descifrar letras en español
            x = alfabeto.index(char)
            descifrado = (a_inv * (x - b)) % 27
            texto_descifrado += alfabeto[descifrado]
        else:
            texto_descifrado += char  # Mantener caracteres no alfabéticos
    
    return texto_descifrado



def cifrar_cesar(text: str, shift: int) -> str:
    shift = shift % 26
    encrypted = ""
    
    for char in text:
        if 'a' <= char <= 'z':
            encrypted += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted += char
    
    return encrypted

def descifrar_cesar(texto_cifrado, k):
    return cifrar_cesar(texto_cifrado, -k)  # Simplemente usamos la misma función con -k


def cifrar_vigenere(texto, clave):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    clave_extendida = (clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]).lower()
    texto_cifrado = ""

    for i in range(len(texto)):
        if texto[i] in alfabeto:  # Solo cifrar letras del alfabeto español
            desplazamiento = alfabeto.index(clave_extendida[i])  # Índice de la clave en el alfabeto
            nueva_letra = alfabeto[(alfabeto.index(texto[i]) + desplazamiento) % 27]
            texto_cifrado += nueva_letra
        else:
            texto_cifrado += texto[i]  # Mantener caracteres no alfabéticos

    return texto_cifrado

def descifrar_vigenere(texto_cifrado, clave):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    clave_extendida = (clave * (len(texto_cifrado) // len(clave)) + clave[:len(texto_cifrado) % len(clave)]).lower()
    texto_descifrado = ""

    for i in range(len(texto_cifrado)):
        if texto_cifrado[i] in alfabeto:  # Solo descifrar letras del alfabeto español
            desplazamiento = alfabeto.index(clave_extendida[i])  # Índice de la clave en el alfabeto
            nueva_letra = alfabeto[(alfabeto.index(texto_cifrado[i]) - desplazamiento) % 27]
            texto_descifrado += nueva_letra
        else:
            texto_descifrado += texto_cifrado[i]  # Mantener caracteres no alfabéticos

    return texto_descifrado


def analizar_frecuencia(texto):
    texto = texto.lower()  
    texto = ''.join([c for c in texto if c.isalpha()]) 
    
    total_letras = len(texto) 
    conteo = Counter(texto)  
    
    frecuencia_porcentaje = {letra: (conteo[letra] / total_letras) * 100 for letra in conteo}
    frecuencia_ordenada = dict(sorted(frecuencia_porcentaje.items(), key=lambda x: x[1], reverse=True))
    
    return frecuencia_ordenada