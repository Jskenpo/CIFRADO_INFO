from Crypto.Cipher import ChaCha20

def generate_key_nonce(user_id):
    key = (user_id.encode() * 32)[:32]
    nonce = (user_id.encode() * 8)[:8]
    return key, nonce

def chacha20_decrypt(ciphertext_hex, user_id):
    key, nonce = generate_key_nonce(user_id)
    ciphertext = bytes.fromhex(ciphertext_hex)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode(errors="ignore")  


ciphertext = "4ff81a93941b29fe7f5fa5902b7bde49824f5e972fb5cda7318c59b9252101470a9e3ad419"
user_id = "21153"

mensaje = chacha20_decrypt(ciphertext, user_id)
print("Texto descifrado:", mensaje)
