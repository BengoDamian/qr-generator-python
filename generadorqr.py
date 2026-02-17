# generar_qr_link.py
# Instalar: pip install qrcode[pil]

import argparse
from urllib.parse import urlparse
import qrcode

def nombre_archivo_desde_link(link: str) -> str:
    p = urlparse(link)
    host = p.netloc.replace("www.", "").replace(":", "_")
    if not host:
        return "qr_link.png"
    return f"qr_{host}.png"

def generar_qr(link: str, output: str | None = None):
    if not link.startswith(("http://", "https://")):
        raise ValueError("El link debe empezar con http:// o https://")

    if output is None:
        output = nombre_archivo_desde_link(link)

    img = qrcode.make(link)
    img.save(output)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar QR desde un link")
    parser.add_argument("link", help="Ej: https://ercas.com.ar")
    parser.add_argument("-o", "--output", help="Archivo de salida (opcional)")
    args = parser.parse_args()

    archivo = generar_qr(args.link, args.output)
    print(f"✅ QR generado: {archivo}")
