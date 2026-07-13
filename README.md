# Generador de códigos QR en Python

Script simple para generar códigos QR comunes en formato PNG a partir de una URL o texto.

Los códigos QR se generan sin imagen ni logotipo en el centro.

## Requisitos

* Python 3.10 o superior.
* Dependencias indicadas en `requirements.txt`.

## Abrir la terminal en Visual Studio Code

Dentro del proyecto, abrir:

```text
Terminal → Nueva terminal
```

Para comprobar que la terminal está ubicada en la carpeta correcta:

```powershell
dir
```

En la lista debe aparecer:

```text
generadorqr.py
```

## Instalar las dependencias

La primera vez que se utiliza el proyecto, ejecutar:

```powershell
py -m pip install -r requirements.txt
```

Si el comando `py` no funciona, probar:

```powershell
python -m pip install -r requirements.txt
```

## Generar un código QR

Formato general:

```powershell
py generadorqr.py "URL_O_TEXTO" -o "nombre-del-archivo.png"
```

Ejemplo:

```powershell
py generadorqr.py "https://example.com" -o "QR_EJEMPLO.png"
```

El archivo PNG se guarda en la carpeta actual del proyecto.

## QR de acceso para encargado de QUIRVO

Para generar el QR correspondiente al código `QV-2DEGCUZR`, ejecutar:

```powershell
py generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=QV-2DEGCUZR" -o "QR_QV-2DEGCUZR.png"
```

El archivo generado será:

```text
QR_QV-2DEGCUZR.png
```

## Generar un QR para otro código de QUIRVO

Hay que reemplazar el código en la URL y en el nombre del archivo.

Formato:

```powershell
py generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=CODIGO" -o "QR_CODIGO.png"
```

Ejemplo:

```powershell
py generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=QV-ABC12345" -o "QR_QV-ABC12345.png"
```

## Alternativa si `py` no funciona

Usar `python`:

```powershell
python generadorqr.py "https://quirvo-omega.vercel.app/login?go=encargado&codigo=QV-2DEGCUZR" -o "QR_QV-2DEGCUZR.png"
```

## Errores frecuentes

### No encuentra `generadorqr.py`

La terminal no está ubicada en la carpeta correcta.

Comprobarlo ejecutando:

```powershell
dir
```

### Falta alguna dependencia

Ejecutar:

```powershell
py -m pip install -r requirements.txt
```

O instalar las librerías directamente:

```powershell
py -m pip install qrcode pillow
```

## Notas

* Este proyecto es público y no contiene secretos.
* El programa solamente convierte una URL o texto en un código QR.
* Los permisos y la cantidad de usos del código se controlan desde la aplicación QUIRVO.
* No es necesario modificar `generadorqr.py` para generar un QR común.
