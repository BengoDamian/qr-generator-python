# qr_facil.py
# Version simple e interactiva: pide el link y genera el QR.

import os
import sys
import subprocess


def asegurar_qrcode():
    """Instala qrcode[pil] automaticamente si no esta disponible."""
    try:
        import qrcode  # noqa: F401
        return
    except ImportError:
        print("Instalando lo necesario por unica vez, espera unos segundos...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "qrcode[pil]"],
            check=True,
        )


def nombre_desde_link(link: str) -> str:
    limpio = link.split("//")[-1]
    limpio = limpio.replace("www.", "")
    for c in '\\/:*?"<>|':
        limpio = limpio.replace(c, "_")
    limpio = limpio.strip("_")
    if not limpio:
        limpio = "link"
    return f"qr_{limpio}.png"


def main():
    asegurar_qrcode()
    import qrcode

    print("=" * 40)
    print("   GENERADOR DE QR")
    print("=" * 40)
    link = input("\nPega el link y presiona Enter:\n> ").strip()

    if not link:
        print("\nNo escribiste ningun link.")
        input("\nPresiona Enter para cerrar...")
        return

    if not link.startswith(("http://", "https://")):
        link = "https://" + link

    salida = nombre_desde_link(link)
    img = qrcode.make(link)
    img.save(salida)

    ruta = os.path.abspath(salida)
    print(f"\nListo! QR generado para:\n  {link}")
    print(f"\nArchivo guardado en:\n  {ruta}")

    # Abrir la imagen automaticamente (Windows)
    try:
        os.startfile(ruta)
    except Exception:
        pass

    input("\nPresiona Enter para cerrar...")


if __name__ == "__main__":
    main()