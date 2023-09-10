import sys
from rich import print as printC
from rich.console import Console
console = Console()


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Symmetric Encryption
# Cipher object
# Algorithm = AES256 (Cipher Algorithm)
# Mode = CBC (Cipher Block Chaining)

# Encrypt New Site Entry
def EncryptAES256(data_bytes: bytes, key: bytes, iv: bytes) -> bytes:
    try:
        cipher = Cipher(algorithms.AES256(key), modes.CBC(iv))

        # Padding data_bytes
        padder = padding.PKCS7(cipher.algorithm.key_size).padder()
        padded_bytes = padder.update(data_bytes) + padder.finalize()

        # AES256 Encryption
        encryptor = cipher.encryptor()
        cipherText = encryptor.update(padded_bytes) + encryptor.finalize()

        return cipherText
    
    except Exception as e:
        console.print_exception()
        sys.exit(0)



# Decrypt Site Entry
def DecryptAES256(cipherText: bytes, key: bytes, iv: bytes) -> bytes:
    try:
        cipher = Cipher(algorithms.AES256(key), modes.CBC(iv))

        # AES256 Decryption
        decryptor = cipher.decryptor()
        cipherText = decryptor.update(cipherText) + decryptor.finalize()

        # Unpadding data_bytes
        unpadder = padding.PKCS7(cipher.algorithm.key_size).unpadder()
        data_bytes = unpadder.update(cipherText) + unpadder.finalize()

        return data_bytes
    
    except Exception as e:
        console.print_exception()
        sys.exit(0)
