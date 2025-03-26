# 🔐 Keystream Cipher - XOR Encryption  

Este proyecto implementa un esquema de cifrado y descifrado basado en XOR utilizando un keystream generado con un PRNG. También incluye pruebas unitarias para verificar su correcto funcionamiento y un análisis de seguridad del keystream.  

## 📜 Requisitos  

Antes de ejecutar el notebook, asegúrate de tener instalado:  

- **Python** (>=3.8)  
- **Jupyter Notebook**  
- **NumPy** (para generación de números aleatorios)  
- **Unittest** (para pruebas unitarias)  

## 🚀 Instalación   

1. **Crea un entorno virtual (opcional, pero recomendado):**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # En macOS/Linux
   venv\Scripts\activate     # En Windows
   ```  

2. **Instala las dependencias manualmente:**  
   ```bash
   pip install jupyter numpy
   ```  

## ▶️ Uso  

Para ejecutar el notebook, usa el siguiente comando:  
```bash
jupyter notebook
```  
Luego, abre `ST_ejercicio.ipynb` en Jupyter y sigue las instrucciones dentro del notebook.  

## 🛠 Pruebas  

El notebook incluye pruebas unitarias para verificar el correcto funcionamiento del cifrado y descifrado. También puedes ejecutarlas manualmente con:  
```bash
python -m unittest ST_ejercicio.ipynb
```  

## Preguntas

### ¿Qué sucede cuando cambias la clave utilizada para generar el keystream?

Cuando se cambia la clave en un stream cipher, el keystream generado será completamente diferente. Dado que estos cifrados son deterministas, el keystream depende de la clave y, en muchos casos, de un vector de inicialización.

### ¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?

Si el mismo keystream se usa en dos mensajes distintos, un atacante puede explotar esta debilidad para extraer información de los mensajes cifrados. Esto se debe a que la operación XOR entre dos mensajes cifrados con el mismo keystream elimina la clave, revelando la combinación de los dos mensajes originales.

### ¿Cómo afecta la longitud del keystream a la seguridad del cifrado?

La seguridad del cifrado depende de que el keystream sea al menos tan largo como el mensaje que se está cifrando. Si el keystream es suficientemente largo y aleatorio, garantiza que cada bit del mensaje tenga una transformación segura y evita que un atacante pueda predecir partes del mensaje cifrado. Sin embargo, si el keystream es más corto que el mensaje y se repite, se introduce un patrón cíclico que puede ser explotado mediante análisis estadístico y ataques de frecuencia.

### ¿Qué consideraciones debes tener al generar un keystream en un entorno real?

En un entorno real, es importante garantizar la unicidad del keystream para cada mensaje cifrado. Para ello, se recomienda el uso de claves y nonces únicos, ya que en muchos stream ciphers modernos, como ChaCha20, el nonce ayuda a garantizar que el keystream generado no se repita incluso si se reutiliza la misma clave. Además, la calidad del generador de números aleatorios es crucial, ya que un keystream predecible puede comprometer la seguridad del cifrado. También es importante evitar el uso de algoritmos obsoletos como RC4, que han demostrado ser vulnerables, y optar por alternativas más seguras como ChaCha20-Poly1305.