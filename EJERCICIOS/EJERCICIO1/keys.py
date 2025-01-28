import random as r 
import conversions as conv

def xor_binario(binario1, binario2):
    return ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(binario1, binario2))

def generar_llave_ascii(longitud):
    
    # Conjunto de caracteres imprimibles ASCII (códigos del 32 al 126)
    caracteres_ascii = [chr(i) for i in range(32, 127)]
    
    # Generar una llave aleatoria seleccionando caracteres al azar
    llave = ''.join(r.choice(caracteres_ascii) for _ in range(int(longitud)))
    return llave

def cypher_dinamico(texto):
    llave = generar_llave_ascii(len(texto))
    llave_binario = conv.texto_a_binario(llave)
    texto_binario = conv.texto_a_binario(texto)
    
    # Asegurar que la llave sea del mismo tamaño que el texto
    llave_binario = llave_binario * (len(texto_binario) // len(llave_binario)) + llave_binario[:len(texto_binario) % len(llave_binario)]
    
    texto_cifrado = xor_binario(texto_binario, llave_binario)
    
    return conv.binario_a_texto(texto_cifrado)

def cypher_estatico(texto):
    llave=input("Ingrese la llave: ")

    # Asegurar que la llave sea del mismo tamaño que el texto
    llave = llave * (len(texto) // len(llave)) + llave[:len(texto) % len(llave)]
    print(llave)
    texto_binario = conv.texto_a_binario(texto)
    llave_binario = conv.texto_a_binario(llave)

    texto_cifrado = xor_binario(texto_binario, llave_binario)

    return conv.binario_a_texto(texto_cifrado)

def decipher_texto(texto_cifrado, llave):
    
    # Asegurar que la llave sea del mismo tamaño que el texto cifrado
    llave = llave * (len(texto_cifrado) // len(llave)) + llave[:len(texto_cifrado) % len(llave)]
    
    # Convertir el texto cifrado y la llave a binario
    texto_binario = conv.texto_a_binario(texto_cifrado)
    llave_binario = conv.texto_a_binario(llave)
    
    # Realizar la operación XOR inversa (es lo mismo que el cifrado en XOR)
    texto_descifrado_binario = xor_binario(texto_binario, llave_binario)
    
    # Convertir el binario descifrado a texto
    texto_descifrado = conv.binario_a_texto(texto_descifrado_binario)
    
    return texto_descifrado
