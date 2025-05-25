from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crypto_utils import encrypt, decrypt

app = FastAPI()

class CryptoRequest(BaseModel):
    key: str
    text: str

@app.post("/encrypt")
def encrypt_text(request: CryptoRequest):
    try:
        result = encrypt(request.text, request.key)
        return {"encrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/decrypt")
def decrypt_text(request: CryptoRequest):
    try:
        result = decrypt(request.text, request.key)
        return {"decrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))