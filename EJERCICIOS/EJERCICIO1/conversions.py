tabla_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def texto_a_binario(texto):
    return ''.join(format(ord(char), '08b') for char in texto)

def base64_a_binario(base64_texto):
    
    padding = base64_texto.count('=')
    
    base64_texto = base64_texto.rstrip('=')
    
    bits = ''.join(format(tabla_base64.index(char), '06b') for char in base64_texto)
    
    if padding:
        bits = bits[:-(padding * 2)]  
        
    bloques_binarios = ''.join(bits[i:i+8] for i in range(0, len(bits), 8))
    
    return bloques_binarios

def binario_a_base64(binario):

    longitud_original = len(binario)
    
    # Asegurar que el número total de bits sea múltiplo de 6
    while len(binario) % 6 != 0:
        binario += '0'  # Agregar ceros al final para completar bloques de 6 bits

    bloques = [binario[i:i+6] for i in range(0, len(binario), 6)]
    
    caracteres_base64 = ''.join(tabla_base64[int(bloque, 2)] for bloque in bloques)
    
    # Agregar relleno '=' si el número de bits originales no era múltiplo de 24
    bits_restantes = longitud_original % 24
    if bits_restantes == 8:  # Faltan 16 bits (1 byte en los datos originales)
        caracteres_base64 += '=='
    elif bits_restantes == 16:  # Faltan 8 bits (2 bytes en los datos originales)
        caracteres_base64 += '='
    
    return caracteres_base64

def binario_a_texto(binario):
    return ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))

def base64_a_ascii(base64_texto):
    # Tabla Base64 estándar
    tabla_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Eliminar caracteres de relleno ('=')
    base64_texto = base64_texto.rstrip('=')
    
    # Convertir cada carácter Base64 a su valor decimal
    valores_decimales = [tabla_base64.index(c) for c in base64_texto]
    
    # Convertir a binario de 6 bits y unirlos en una sola cadena
    binario = ''.join(f"{valor:06b}" for valor in valores_decimales)
    
    # Dividir la cadena binaria en bloques de 8 bits
    bloques_bytes = [binario[i:i+8] for i in range(0, len(binario), 8)]
    
    # Convertir cada bloque de 8 bits a su carácter ASCII
    ascii_texto = ''.join(chr(int(bloque, 2)) for bloque in bloques_bytes)
    
    return ascii_texto



