
---

### 📄 `README.md`

````markdown
# API de Cifrado y Descifrado AES-GCM con FastAPI

Esta API permite cifrar y descifrar textos utilizando el algoritmo AES en modo GCM (Galois/Counter Mode) con claves de hasta 256 bits. Está desarrollada con FastAPI, ofreciendo alto rendimiento, documentación automática y validación de datos.

---

## 🚀 Instalación

1. **Clonar el repositorio o copiar los archivos** del proyecto.

2. **Instalar las dependencias** necesarias:

```bash
pip install -r requirements.txt
````

3. **Ejecutar el servidor**:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

> Asegúrate de que el archivo se llame `main.py`, o ajusta el nombre en el comando anterior.

---

## 🛠️ Endpoints

### 🔐 `POST /encrypt`

Cifra un texto plano usando una clave.

* **Request JSON:**

```json
{
  "key": "mi_clave_secreta",
  "text": "Hola mundo"
}
```

* **Response JSON:**

```json
{
  "encrypted_text": "texto_cifrado_base64"
}
```

---

### 🔓 `POST /decrypt`

Descifra un texto previamente cifrado con la misma clave.

* **Request JSON:**

```json
{
  "key": "mi_clave_secreta",
  "text": "texto_cifrado_base64"
}
```

* **Response JSON:**

```json
{
  "decrypted_text": "Hola mundo"
}
```

---

## 🧠 Detalles Técnicos

* Utiliza **AES-256 en modo GCM**, que garantiza confidencialidad e integridad de los datos.
* Se genera un IV aleatorio de 12 bytes para cada operación de cifrado.
* El resultado cifrado contiene: `IV + datos cifrados + etiqueta de autenticación (tag)`, todo codificado en base64.

---

## 🧾 Licencia

Este proyecto está bajo la Licencia MIT.

---

## 📚 Referencias

* Duy, H. (n.d.). *FastAPI documentation*. [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
* The Python Cryptographic Authority. (n.d.). *Cryptography documentation*. [https://cryptography.io/en/latest/](https://cryptography.io/en/latest/)

```

---
```
