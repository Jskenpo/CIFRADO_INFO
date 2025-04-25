from Crypto.Cipher import ARC4

def rc4_decrypt(cipher_hex, key):
    ciphertext = bytes.fromhex(cipher_hex)
    cipher = ARC4.new(key.encode())
    plaintext = cipher.decrypt(ciphertext)
    try:
        return plaintext.decode("utf-8")
    except UnicodeDecodeError:
        return plaintext

cipher_hex = "87158c3af198fe8f7ef2e302251772f396de084b30830634389d54d6530f8ef099e695f536"
key = "21153"  

print(rc4_decrypt(cipher_hex, key))
