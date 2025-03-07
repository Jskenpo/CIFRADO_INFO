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
contenido = "SV OHU JVUZLNBPKV, OHU LUJVUAYHKV BUH MSHN WHYH LS ZPNBPLUAL KLZHMPV MSHN{JYFWAV_HUHSFZPZ}"

# Cargar frecuencia desde archivo CSV
frecuencia_espanol = bf.cargar_frecuencia_csv("en_freq.csv")

# Analizar frecuencia del texto original
analisis = alg.analizar_frecuencia(contenido)



print("\nFrecuencia del texto cifrado:")
for letra, porcentaje in analisis.items():
    print(f"Letra '{letra}': {porcentaje:.2f}%")

# Limpiar el texto cifrado
texto_cifrado = bf.limpiar_texto(contenido)

# Ejecutar fuerza bruta
mejores_cesar = bf.fuerza_bruta_cesar(texto_cifrado, 3, frecuencia_espanol)
# Mostrar resultados
print("\n Top 3 claves César:")
for clave, metrica, descifrado in mejores_cesar:
    print(f"Clave {clave}: {descifrado} (Métrica: {metrica:.2f})")


