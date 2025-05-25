from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crypto_utils import encrypt, decrypt

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/encrypt")
def encrypt_text(request: TextRequest):
    try:
        result = encrypt(request.text)
        return {"encrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/decrypt")
def decrypt_text(request: TextRequest):
    try:
        result = decrypt(request.text)
        return {"decrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
