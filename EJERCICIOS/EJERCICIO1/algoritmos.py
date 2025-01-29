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
    return cifrar_cesar(texto_cifrado, -k)  # Simplemente usamos la misma función con -k
