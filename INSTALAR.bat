@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================
echo    INSTALADOR DE DEPENDENCIAS - GENERADOR QR
echo ============================================
echo.
echo Este paso se hace UNA SOLA VEZ.
echo Instala lo que Python necesita para generar los QR.
echo.

REM Detectar Python (primero "python", luego "py")
set "PY=python"
python --version >nul 2>&1
if errorlevel 1 (
  set "PY=py"
  py --version >nul 2>&1
  if errorlevel 1 goto sin_python
)

echo Usando: %PY%
echo.
echo Instalando dependencias...
echo.
%PY% -m pip install --upgrade pip
%PY% -m pip install -r requirements.txt

if errorlevel 1 (
  echo.
  echo Hubo un problema al instalar. Revisa tu conexion a internet.
  echo.
  pause
  exit /b 1
)

echo.
echo ============================================
echo    LISTO! Ya podes usar GENERAR_QR.bat
echo ============================================
echo.
pause
exit /b 0

:sin_python
echo.
echo No se encontro Python en esta computadora.
echo.
echo 1) Descargalo gratis desde: https://www.python.org/downloads/
echo 2) Al instalarlo, MARCA la casilla "Add Python to PATH".
echo 3) Volve a ejecutar este INSTALAR.bat.
echo.
pause
exit /b 1
