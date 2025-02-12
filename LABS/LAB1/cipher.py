import algoritmos as alg
import bruteforce as bf
import matplotlib.pyplot as plt


def leer_archivo_txt(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        return f"Error: El archivo '{ruta_archivo}' no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {e}"

# Ruta del archivo cifrado
ruta = "Cifrados/afines.txt"
contenido = leer_archivo_txt(ruta)

# Cargar frecuencia desde archivo CSV
frecuencia_espanol = bf.cargar_frecuencia_csv("sp_frequencies.csv")

# Analizar frecuencia del texto original
analisis = alg.analizar_frecuencia(contenido)

# Graficar frecuencia del texto analizado
plt.figure(figsize=(10, 5))
plt.bar(analisis.keys(), analisis.values(), color="orange", alpha=0.7)

plt.xlabel("Letras")
plt.ylabel("Frecuencia (%)")
plt.title("Frecuencia de Letras en el Texto Analizado")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()



print("\nFrecuencia del texto cifrado:")
for letra, porcentaje in analisis.items():
    print(f"Letra '{letra}': {porcentaje:.2f}%")

# Limpiar el texto cifrado
texto_cifrado = bf.limpiar_texto(contenido)
'''
# Ejecutar fuerza bruta
mejores_cesar = bf.fuerza_bruta_cesar(texto_cifrado, 3, frecuencia_espanol)
# Mostrar resultados
print("\n Top 3 claves César:")
for clave, metrica, descifrado in mejores_cesar:
    print(f"Clave {clave}: {descifrado} (Métrica: {metrica:.2f})")
'''

# Ejecutar fuerza bruta
mejores_afin = bf.fuerza_bruta_afin(texto_cifrado, 3, frecuencia_espanol)
# Mostrar resultados
print("\n Top 3 claves Afín:")
for clave, metrica, descifrado in mejores_afin:
    print(f"Clave {clave}: {descifrado} (Métrica: {metrica:.2f})")
'''

# Ejecutar fuerza bruta
mejores_vigenere = bf.fuerza_bruta_vigenere(texto_cifrado, 3, frecuencia_espanol)
# Mostrar resultados
print("\n Top 3 claves Vigenère:")
for clave, metrica, descifrado in mejores_vigenere:
    print(f"Clave {clave}: {descifrado} (Métrica: {metrica:.2f})")

    '''