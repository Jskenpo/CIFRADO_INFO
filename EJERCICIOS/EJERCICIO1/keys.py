import random as r 

def xor_binario(binario1, binario2):
    return ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(binario1, binario2))

def generar_llave_ascii():
    longitud = input ("Ingrese la longitud de la llave: ")
    # Conjunto de caracteres imprimibles ASCII (códigos del 32 al 126)
    caracteres_ascii = [chr(i) for i in range(32, 127)]
    
    # Generar una llave aleatoria seleccionando caracteres al azar
    llave = ''.join(r.choice(caracteres_ascii) for _ in range(int(longitud)))
    return llave