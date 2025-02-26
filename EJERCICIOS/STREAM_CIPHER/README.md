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
Luego, abre `notebook.ipynb` en Jupyter y sigue las instrucciones dentro del notebook.  

## 🛠 Pruebas  

El notebook incluye pruebas unitarias para verificar el correcto funcionamiento del cifrado y descifrado. También puedes ejecutarlas manualmente con:  
```bash
python -m unittest notebook.ipynb
```  
