def xor_decrypt_hex(hex_string: str, key: str) -> str:
    """
    Descifra un texto cifrado con XOR usando una clave, donde el texto está en hexadecimal.
    """
    ciphertext = bytes.fromhex(hex_string)
    key_bytes = key.encode()

    decrypted = bytearray()
    for i in range(len(ciphertext)):
        decrypted.append(ciphertext[i] ^ key_bytes[i % len(key_bytes)])

    try:
        return decrypted.decode("utf-8")
    except UnicodeDecodeError:
        # Si no se puede decodificar, lo mostramos como bytes
        return str(decrypted)


texto_hex = "747d70726c5709000d0a03555456500708550d510053045601540550020a03530750035652"
clave = "21153"

texto_descifrado = xor_decrypt_hex(texto_hex, clave)
print("Texto descifrado:\n", texto_descifrado)
