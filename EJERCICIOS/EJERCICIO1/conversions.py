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



