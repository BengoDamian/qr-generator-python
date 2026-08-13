# Generador de códigos QR en Python

Convierte cualquier link (o texto) en un código QR en formato PNG.

Los códigos QR se generan **limpios**: solo el código, sin logotipo ni imagen en el centro.

---

## ✅ Modo fácil (recomendado, sin usar la terminal)

Pensado para cualquier persona, aunque no sepa programar. Son **3 archivos** con doble clic:

### 1) Instalar (una sola vez)

Doble clic en **`INSTALAR.bat`**

* Instala automáticamente todo lo que Python necesita.
* Si no tenés Python, te avisa y te da el link para descargarlo.
* Esto se hace **una única vez** en la computadora.

### 2) Generar un QR

Doble clic en **`GENERAR_QR.bat`**

1. Se abre una ventana que dice: *"Pega el link y presiona Enter"*.
2. Pegás el link (ejemplo: `quirvo-omega.vercel.app/setup`) y apretás **Enter**.
3. El QR se genera y **se abre solo** en pantalla.
4. El archivo `.png` queda guardado en esta misma carpeta.

> No hace falta escribir `https://` — si lo omitís, se agrega solo.

### Requisito único

Tener **Python instalado** (es gratis, se instala una sola vez):

* Descarga: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Importante: al instalar, marcar la casilla **"Add Python to PATH"**.

---

## 🛠️ Modo avanzado (por terminal)

Para quien prefiere la línea de comandos.

### Requisitos

* Python 3.10 o superior.
* Dependencias indicadas en `requirements.txt`.

### Abrir la terminal en Visual Studio Code

Dentro del proyecto, abrir:

```text
Terminal → Nueva terminal
```

Para comprobar que la terminal está en la carpeta correcta:

```powershell
dir
```

En la lista debe aparecer `generadorqr.py`.

### Instalar las dependencias

La primera vez que se utiliza el proyecto, ejecutar:

```powershell
py -m pip install -r requirements.txt
```

Si el comando `py` no funciona, probar:

```powershell
python -m pip install -r requirements.txt
```

### Generar un código QR

Formato general:

```powershell
py generadorqr.py "URL_O_TEXTO" -o "nombre-del-archivo.png"
```

Ejemplo:

```powershell
py generadorqr.py "https://example.com" -o "QR_EJEMPLO.png"
```

El archivo PNG se guarda en la carpeta actual del proyecto.

---

## QR de acceso para encargado de QUIRVO

Para generar el QR correspondiente al código `QV-2DEGCUZR`, ejecutar:

```powershell
py generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=QV-2DEGCUZR" -o "QR_QV-2DEGCUZR.png"
```

El archivo generado será `QR_QV-2DEGCUZR.png`.

### Generar un QR para otro código de QUIRVO

Reemplazar el código en la URL y en el nombre del archivo.

```powershell
py generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=CODIGO" -o "QR_CODIGO.png"
```

Ejemplo:

```powershell
py generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=QV-ABC12345" -o "QR_QV-ABC12345.png"
```

Alternativa si `py` no funciona, usar `python`:

```powershell
python generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=QV-2DEGCUZR" -o "QR_QV-2DEGCUZR.png"
```

---

## Errores frecuentes

### No encuentra `generadorqr.py`

La terminal no está ubicada en la carpeta correcta. Comprobarlo con:

```powershell
dir
```

### Falta alguna dependencia

Ejecutar el instalador **`INSTALAR.bat`**, o bien:

```powershell
py -m pip install -r requirements.txt
```

O instalar las librerías directamente:

```powershell
py -m pip install qrcode pillow
```

### "No se encontró Python"

Instalar Python desde [https://www.python.org/downloads/](https://www.python.org/downloads/) y marcar **"Add Python to PATH"** durante la instalación.

---

## Archivos del proyecto

| Archivo | Para qué sirve |
|---|---|
| `INSTALAR.bat` | Instala las dependencias (doble clic, una sola vez). |
| `GENERAR_QR.bat` | Genera un QR pegando el link (doble clic). |
| `qr_facil.py` | Script interactivo que usa el `.bat` de arriba. |
| `generadorqr.py` | Script por línea de comandos (modo avanzado). |
| `requirements.txt` | Lista de dependencias de Python. |

---

## Notas

* Este proyecto es público y no contiene secretos.
* El programa solamente convierte una URL o texto en un código QR.
* Los permisos y la cantidad de usos del código se controlan desde la aplicación QUIRVO.
* No es necesario modificar `generadorqr.py` para generar un QR común.
