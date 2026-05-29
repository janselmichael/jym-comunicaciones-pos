#!/usr/bin/env python3
"""
Script to compile both applications to .exe format
Run this to generate the executable files
"""

import os
import subprocess
import sys

def compile_pos_app():
    """Compile POS application"""
    print("="*60)
    print("Compilando JyM Comunicaciones POS System...")
    print("="*60)
    try:
        subprocess.run([sys.executable, 'build_exe.py'], check=True)
        print("✓ POS app compilado exitosamente!")
    except Exception as e:
        print(f"✗ Error compilando POS: {e}")

def compile_todo_app():
    """Compile Todo application"""
    print("\n" + "="*60)
    print("Compilando Todo List Application...")
    print("="*60)
    try:
        subprocess.run([sys.executable, 'build_todo_exe.py'], check=True)
        print("✓ Todo app compilado exitosamente!")
    except Exception as e:
        print(f"✗ Error compilando Todo: {e}")

def main():
    print("\n🚀 COMPILADOR DE APLICACIONES")
    print("="*60)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("Instalando PyInstaller...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], check=True)
    
    # Compile applications
    compile_pos_app()
    compile_todo_app()
    
    print("\n" + "="*60)
    print("✓ COMPILACIÓN COMPLETADA!")
    print("="*60)
    print("\nTus ejecutables están listos en:")
    print("  📦 dist/JyM_Comunicaciones_POS.exe")
    print("  📦 dist/TodoList_App.exe")
    print("\n¡Puedes descargarlos directamente desde GitHub!")

if __name__ == '__main__':
    main()
