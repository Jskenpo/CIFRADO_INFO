import time
import tracemalloc
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import ChaCha20

def chacha20_encrypt(plaintext, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def chacha20_decrypt(ciphertext, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def aes_encrypt(plaintext, key, mode, iv=None):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == AES.MODE_CBC:
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("Modo no soportado")
    
    # Asegurar que el texto es múltiplo de 16 (PKCS7 padding)
    padding_length = 16 - len(plaintext) % 16
    padded_text = plaintext + bytes([padding_length] * padding_length)

    return cipher.encrypt(padded_text)

def aes_decrypt(ciphertext, key, mode, iv=None):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == AES.MODE_CBC:
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("Modo no soportado")
    
    decrypted_text = cipher.decrypt(ciphertext)
    padding_length = decrypted_text[-1]
    return decrypted_text[:-padding_length]

# Mensaje de prueba (1MB de datos)
plaintext = get_random_bytes(1024 * 1024)  # 1MB de datos aleatorios


key_aes = get_random_bytes(16)  # AES-128
key_chacha = get_random_bytes(32)  # ChaCha20 usa 256 bits
iv = get_random_bytes(16)  # IV para AES-CBC
nonce = get_random_bytes(8)  # Nonce para ChaCha20


def measure_performance(encrypt_func, decrypt_func, *args):
    tracemalloc.start()
    start_time = time.time()
    encrypted = encrypt_func(*args)
    encrypt_time = time.time() - start_time

    start_time = time.time()
    decrypted = decrypt_func(encrypted, *args[1:])
    decrypt_time = time.time() - start_time

    mem_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    return encrypt_time, decrypt_time, mem_used


chacha_encrypt_time, chacha_decrypt_time, chacha_mem = measure_performance(chacha20_encrypt, chacha20_decrypt, plaintext, key_chacha, nonce)
aes_ecb_encrypt_time, aes_ecb_decrypt_time, aes_ecb_mem = measure_performance(aes_encrypt, aes_decrypt, plaintext, key_aes, AES.MODE_ECB)
aes_cbc_encrypt_time, aes_cbc_decrypt_time, aes_cbc_mem = measure_performance(aes_encrypt, aes_decrypt, plaintext, key_aes, AES.MODE_CBC, iv)


print("\nRendimiento de cifrado y descifrado (1MB de datos):")
print(f"ChaCha20   - Cifrado: {chacha_encrypt_time:.5f}s | Descifrado: {chacha_decrypt_time:.5f}s | Memoria: {chacha_mem / 1024:.2f} KB")
print(f"AES-ECB    - Cifrado: {aes_ecb_encrypt_time:.5f}s | Descifrado: {aes_ecb_decrypt_time:.5f}s | Memoria: {aes_ecb_mem / 1024:.2f} KB")
print(f"AES-CBC    - Cifrado: {aes_cbc_encrypt_time:.5f}s | Descifrado: {aes_cbc_decrypt_time:.5f}s | Memoria: {aes_cbc_mem / 1024:.2f} KB")
