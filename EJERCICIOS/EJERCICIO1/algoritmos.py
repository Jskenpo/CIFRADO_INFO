
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


def cifrar_cesar(texto, k):
    texto_cifrado = ""
    
    for char in texto:
        if char.isalpha():  # Solo ciframos letras
            base = ord('A') if char.isupper() else ord('a')  # Detectar mayúsculas o minúsculas
            nueva_pos = (ord(char) - base + k) % 26  # Aplicar la fórmula del cifrado
            texto_cifrado += chr(nueva_pos + base)  # Convertir de nuevo a carácter
        else:
            texto_cifrado += char  # Mantener caracteres especiales sin cifrar
    
    return texto_cifrado

def descifrar_cesar(texto_cifrado, k):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    descifrado = ""

    for letra in texto_cifrado:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) - k) % 26
            descifrado += alfabeto[indice]
        else:
            descifrado += letra  # Mantiene caracteres que no son letras

    return descifrado
def cifrar_vigenere(texto):
    clave = input("Ingrese la clave: ")
    clave_extendida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]
    texto_cifrado = ""
    for i in range(len(texto)):
        if texto[i].isalpha():  # Solo ciframos letras
            base = ord('A') if texto[i].isupper() else ord('a')
            desplazamiento = ord(clave_extendida[i].upper()) - ord('A')  # Convertir clave a número
            nueva_letra = chr((ord(texto[i]) - base + desplazamiento) % 26 + base)
            texto_cifrado += nueva_letra
        else:
            texto_cifrado += texto[i]  # No ciframos espacios o caracteres especiales
    
    return texto_cifrado

def descifrar_vigenere(texto_cifrado):
    clave = input("Ingrese la clave: ")
    clave_extendida = clave * (len(texto_cifrado) // len(clave)) + clave[:len(texto_cifrado) % len(clave)]
    texto_descifrado = ""
    for i in range(len(texto_cifrado)):
        if texto_cifrado[i].isalpha():  # Solo desciframos letras
            base = ord('A') if texto_cifrado[i].isupper() else ord('a')
            desplazamiento = ord(clave_extendida[i].upper()) - ord('A')
            nueva_letra = chr((ord(texto_cifrado[i]) - base - desplazamiento) % 26 + base)
            texto_descifrado += nueva_letra
        else:
            texto_descifrado += texto_cifrado[i]
    
    return texto_descifrado
