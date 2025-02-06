from collections import Counter
import itertools
import algoritmos as alg
import pandas as pd 

def cargar_frecuencia_csv(archivo):
    df = pd.read_csv(archivo)
    frecuencia = {row["Letter"].lower(): float(row["Spanish_Frequency"].strip('%')) for _, row in df.iterrows()}
    return frecuencia

def limpiar_texto(texto):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    texto = texto.lower()
    return ''.join(c for c in texto if c in alfabeto)

def calcular_metrica(texto_descifrado, frecuencia_espanol):
    frecuencia_texto = alg.analizar_frecuencia(texto_descifrado)
    return sum(abs(frecuencia_texto.get(letra, 0) - frecuencia_espanol.get(letra, 0)) for letra in frecuencia_espanol)

def fuerza_bruta_cesar(texto, k, frecuencia_espanol):
    mejores = []
    for clave in range(0, 27):
        texto_descifrado = alg.descifrar_cesar(texto, clave)
        metrica = calcular_metrica(texto_descifrado, frecuencia_espanol)
        mejores.append((clave, metrica, texto_descifrado))
    
    return sorted(mejores, key=lambda x: x[1])[:k]  

def fuerza_bruta_afin(texto, k, frecuencia_espanol):
    mejores = []
    for a in range(1, 17):
        if alg.mcd(a, 27) != 1: 
            continue
        for b in range(1, 17):
            try:
                texto_descifrado = alg.descifrar_afin(texto, a, b)
                metrica = calcular_metrica(texto_descifrado, frecuencia_espanol)
                mejores.append(((a, b), metrica, texto_descifrado))
            except ValueError:
                continue  
    
    return sorted(mejores, key=lambda x: x[1])[:k]

def fuerza_bruta_vigenere(texto, k, frecuencia_espanol):
    mejores = []
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    
    for longitud in range(1, 7):
        for combinacion in itertools.product(alfabeto, repeat=longitud):
            clave = "PA" + "".join(combinacion)[2:]  # Iniciar con "PA"
            texto_descifrado = alg.descifrar_vigenere(texto, clave)
            metrica = calcular_metrica(texto_descifrado, frecuencia_espanol)
            mejores.append((clave, metrica, texto_descifrado))
    
    return sorted(mejores, key=lambda x: x[1])[:k]




def fuerza_bruta_vigenere(texto_cifrado, k, frecuencia_espanol):
    
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    frase_objetivo = "nuevaamenazaenelhorizonte"
    mejores = []
    
    for longitud in range(2, 7):  
        if longitud == 2:
            claves_posibles = ["pa"]  
        else:
            claves_posibles = ["pa" + "".join(combinacion) for combinacion in itertools.product(alfabeto, repeat=longitud - 2)]
        
        for clave in claves_posibles:
            texto_descifrado = alg.descifrar_vigenere(texto_cifrado, clave)
            
            if frase_objetivo in texto_descifrado:
                metrica = calcular_metrica(texto_descifrado, frecuencia_espanol)
                mejores.append((clave, metrica, texto_descifrado))

    return sorted(mejores, key=lambda x: x[1])[:k]
