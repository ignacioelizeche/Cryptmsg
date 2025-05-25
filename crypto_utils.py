from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

def import_key(key_string: str) -> bytes:
    key_data = key_string.encode()
    return key_data[:32]  # Asegura 32 bytes (AES-256)

def encrypt(plain_text: str, key_string: str) -> str:
    key = import_key(key_string)
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(plain_text.encode()) + encryptor.finalize()
    combined = iv + encrypted_data + encryptor.tag
    return base64.urlsafe_b64encode(combined).decode()

def decrypt(encrypted_text: str, key_string: str) -> str:
    try:
        key = import_key(key_string)
        combined = base64.urlsafe_b64decode(encrypted_text.encode())
        iv, encrypted_data, tag = combined[:12], combined[12:-16], combined[-16:]
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        return decrypted_data.decode()
    except Exception as e:
        raise Exception(f"Error en la desencriptación: {str(e)}")