import random

# Convierte el texto hexadecimal a bytes una sola vez
ciphertext = bytes.fromhex("a77742694e4801874d3d6938d295db291f6c0a33c94b458c124923ee10aac384e91d55df39")
length = len(ciphertext)

# Prueba de todas las semillas posibles hasta 100000
for seed in range(100000):
    random.seed(seed)
    keystream = bytearray(random.randint(0, 255) for _ in range(length))
    
    # XOR entre ciphertext y keystream
    plaintext = bytearray(c ^ k for c, k in zip(ciphertext, keystream))
    
    # Verifica si el texto comienza con "FLAG_"
    if plaintext.startswith(b"FLAG_"):
        print(f"Semilla encontrada: {seed}")
        print(f"Texto descifrado: {plaintext.decode()}")
        break
