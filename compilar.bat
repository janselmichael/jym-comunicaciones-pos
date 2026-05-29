@echo off
REM Instalador automático para compilar los ejecutables
REM No requiere Python instalado previamente

echo.
echo ==========================================
echo   COMPILADOR DE APLICACIONES JYM
echo ==========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado
    echo.
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Asegúrate de marcar "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Instalar PyInstaller
echo Instalando PyInstaller...
pip install PyInstaller -q
echo [OK] PyInstaller instalado

REM Compilar POS
echo.
echo ==========================================
echo Compilando: JyM Comunicaciones POS
echo ==========================================
python build_exe.py

REM Compilar TODO App
echo.
echo ==========================================
echo Compilando: Todo List Application
echo ==========================================
python build_todo_exe.py

echo.
echo ==========================================
echo [OK] COMPILACION COMPLETADA!
echo ==========================================
echo.
echo Los ejecutables están en la carpeta: dist/
echo.
echo  - JyM_Comunicaciones_POS.exe
echo  - TodoList_App.exe
echo.
echo Puedes ejecutarlos directamente haciendo doble clic
echo.
pause
