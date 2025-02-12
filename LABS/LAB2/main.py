import conversions as conv 

texto = 'Hola, mundo!'
print(f'Texto original: {texto}')

#----------------CONVERTIR TEXTO A BINARIO----------------
print('----------------CONVERTIR TEXTO A BINARIO----------------')
binario = conv.texto_a_binario(texto)
print(f'Texto en binario: {binario}\n')

#----------------CONVERTIR BINARIO A ASCII----------------
print('----------------CONVERTIR BINARIO A ASCII----------------')
texto = conv.binario_a_texto(binario)
print(f'Texto en ASCII: {texto}\n')

#----------------CONVERTIR TEXTO A BASE64----------------
print('----------------CONVERTIR TEXTO A BASE64----------------')
base64 = conv.texto_a_base64(texto)
print(f'Texto en Base64: {base64}\n')

#----------------CONVERTIR BASE64 A ASCII----------------
print('----------------CONVERTIR BASE64 A ASCII----------------')
texto = conv.base64_a_ascii(base64)
print(f'Texto en ASCII: {texto}\n')