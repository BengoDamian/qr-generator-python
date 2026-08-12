@echo off
chcp 65001 >nul
cd /d "%~dp0"

python qr_facil.py
if errorlevel 1 (
  py qr_facil.py
)

if errorlevel 1 (
  echo.
  echo No se encontro Python instalado.
  echo Descargalo gratis desde: https://www.python.org/downloads/
  echo Al instalarlo, marca la casilla "Add Python to PATH".
  echo.
  pause
)