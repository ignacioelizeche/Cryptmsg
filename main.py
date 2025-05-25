from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

app = FastAPI()

# Función para importar clave desde una cadena de texto
def import_key(key_string: str) -> bytes:
    key_data = key_string.encode()
    return key_data[:32]  # Asegurar que tenga 32 bytes (AES-256)

# Función de cifrado
def encrypt(plain_text: str, key_string: str) -> str:
    key = import_key(key_string)
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(plain_text.encode()) + encryptor.finalize()
    combined = iv + encrypted_data + encryptor.tag
    return base64.urlsafe_b64encode(combined).decode()

# Función de descifrado
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
        raise HTTPException(status_code=400, detail=f"Error en la desencriptación: {str(e)}")

# Esquema de solicitud para cifrado/descifrado
class CryptoRequest(BaseModel):
    key: str
    text: str

# Endpoint para cifrar
@app.post("/encrypt")
def encrypt_text(request: CryptoRequest):
    if not request.key or not request.text:
        raise HTTPException(status_code=400, detail="Se requiere una clave y un texto")
    encrypted = encrypt(request.text, request.key)
    return {"encrypted_text": encrypted}

# Endpoint para descifrar
@app.post("/decrypt")
def decrypt_text(request: CryptoRequest):
    if not request.key or not request.text:
        raise HTTPException(status_code=400, detail="Se requiere una clave y un texto cifrado")
    decrypted = decrypt(request.text, request.key)
    return {"decrypted_text": decrypted}

