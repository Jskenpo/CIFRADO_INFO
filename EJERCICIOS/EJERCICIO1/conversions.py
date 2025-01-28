def texto_a_binario(texto):
    return ' '.join(format(ord(char), '08b') for char in texto)

def base64_a_binario(base64_texto):
    tabla_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    padding = base64_texto.count('=')
    
    base64_texto = base64_texto.rstrip('=')
    
    bits = ''.join(format(tabla_base64.index(char), '06b') for char in base64_texto)
    
    if padding:
        bits = bits[:-(padding * 2)]  
        
    bloques_binarios = ' '.join(bits[i:i+8] for i in range(0, len(bits), 8))
    
    return bloques_binarios

