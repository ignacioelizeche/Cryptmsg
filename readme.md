
# API de Cifrado y Descifrado AES-GCM con FastAPI

Esta API permite cifrar y descifrar textos usando el algoritmo AES en modo GCM (Galois/Counter Mode) con claves de hasta 256 bits. Está desarrollada con FastAPI, lo que proporciona alto rendimiento, documentación automática y validación de datos.

---

## ⚙️ Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- `pip` (el instalador de paquetes de Python)
- Acceso a la terminal (Linux/Mac) o consola (Windows)

---

## 🚀 Instalación paso a paso

### 1. Verificar instalación de Python y pip

```bash
python3 --version
pip3 --version
````

Si no están instalados:

* **Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

* **MacOS (usando Homebrew):**

```bash
brew install python
```

* **Windows:**

Descargar desde: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Asegúrate de marcar la opción `Add Python to PATH` durante la instalación.

---

### 2. Crear y activar un entorno virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```

---

### 3. Clonar el repositorio o copiar los archivos

```bash
git clone https://github.com/tu-usuario/encrypt-api.git
cd encrypt-api
```

> Si no usas Git, simplemente crea una carpeta y copia los archivos `main.py`, `crypto_utils.py`, `requirements.txt` y este `README.md`.

---

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

### 5. Ejecutar el servidor

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📦 Estructura del Proyecto

```
encrypt_api/
├── main.py             # Archivo principal de FastAPI
├── crypto_utils.py     # Funciones de cifrado y descifrado
├── requirements.txt    # Lista de dependencias
└── README.md           # Documentación del proyecto
```

---

## 🛠️ Endpoints

### 🔐 POST `/encrypt`

Cifra un texto usando una clave.

#### Request:

```json
{
  "key": "mi_clave_secreta",
  "text": "Hola mundo"
}
```

#### Response:

```json
{
  "encrypted_text": "texto_cifrado_base64"
}
```

---

### 🔓 POST `/decrypt`

Descifra un texto previamente cifrado.

#### Request:

```json
{
  "key": "mi_clave_secreta",
  "text": "texto_cifrado_base64"
}
```

#### Response:

```json
{
  "decrypted_text": "Hola mundo"
}
```

---

## 🔐 Detalles Técnicos

* Se utiliza AES-256 en modo GCM (autenticado).
* IV aleatorio de 12 bytes para cada cifrado.
* El resultado incluye IV + datos cifrados + etiqueta GCM (`tag`), codificados en Base64.

---

## 🧾 Licencia

Este proyecto está bajo licencia MIT.

---

## 📚 Referencias

* Duy, H. (n.d.). *FastAPI documentation*. [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
* The Python Cryptographic Authority. (n.d.). *Cryptography documentation*. [https://cryptography.io/en/latest/](https://cryptography.io/en/latest/)

```

