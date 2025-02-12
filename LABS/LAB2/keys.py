import conversions as conv
import random as r

def xor_binario(binario1, binario2):

    #imprimir paso a paso la operacion xor
    print("Operacion XOR: ")
    for bit1, bit2 in zip(binario1, binario2):
        print(f"{bit1} XOR {bit2} = {int(bit1) ^ int(bit2)}")


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
    
    #si la llave es mas grande que el texto, se corta
    if len(llave) > len(texto):
        llave = llave[:len(texto)]

    llave = llave * (len(texto) // len(llave)) + llave[:len(texto) % len(llave)]

    print ("Llave: ")
    print(llave + "\n")

    print ("Texto a binario : ")
    texto_binario = conv.texto_a_binario(texto)

    print ("\nLlave a binario : ")
    llave_binario = conv.texto_a_binario(llave)

    print ("\nTexto cifrado con XOR: ")
    texto_cifrado = xor_binario(texto_binario, llave_binario)

    print ("\nTexto cifrado: ")
    print(texto_cifrado + "\n")

    print ("Texto cifrado a ascii: ")
    return conv.binario_a_texto(texto_cifrado)