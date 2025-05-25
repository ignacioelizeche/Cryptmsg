import os
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Cargar variables desde .env
load_dotenv()
SECRET_KEY = os.getenv("KEY")

def import_key() -> bytes:
    if not SECRET_KEY:
        raise Exception("No se encontró la variable de entorno 'KEY'.")
    key_data = SECRET_KEY.encode()
    return key_data[:32]  # AES-256: 32 bytes

def encrypt(plain_text: str) -> str:
    key = import_key()
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(plain_text.encode()) + encryptor.finalize()
    combined = iv + encrypted_data + encryptor.tag
    return base64.urlsafe_b64encode(combined).decode()

def decrypt(encrypted_text: str) -> str:
    try:
        key = import_key()
        combined = base64.urlsafe_b64decode(encrypted_text.encode())
        iv, encrypted_data, tag = combined[:12], combined[12:-16], combined[-16:]
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        return decrypted_data.decode()
    except Exception as e:
        raise Exception(f"Error en la desencriptación: {str(e)}")
