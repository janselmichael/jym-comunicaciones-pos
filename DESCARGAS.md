# 📥 GUÍA PARA DESCARGAR LOS EJECUTABLES

## 🚀 Opción 1: Descargar desde GitHub (RECOMENDADO)

### Pasos:

1. **Ve a tu repositorio:**
   ```
   https://github.com/janselmichael/jym-comunicaciones-pos
   ```

2. **Busca la carpeta `dist/`** en el repositorio

3. **Haz clic en los archivos:**
   - `JyM_Comunicaciones_POS.exe` - Sistema POS
   - `TodoList_App.exe` - Aplicación de tareas

4. **Haz clic en el botón "Download"** (ícono de descarga)

---

## 🔧 Opción 2: Compilar los Ejecutables Tú Mismo (Si no están en dist/)

Si los archivos .exe no están en la carpeta `dist/`, puedes compilarlos:

### Requisitos previos:
- Tener Python instalado (3.7+)
- Conexión a Internet

### Pasos:

1. **Descarga todo el repositorio:**
   ```bash
   git clone https://github.com/janselmichael/jym-comunicaciones-pos.git
   cd jym-comunicaciones-pos
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   pip install PyInstaller
   ```

3. **Ejecuta el compilador:**
   ```bash
   python compile_all.py
   ```

4. **Espera a que termine** (puede tomar 2-3 minutos)

5. **Los ejecutables estarán en:**
   ```
   ./dist/JyM_Comunicaciones_POS.exe
   ./dist/TodoList_App.exe
   ```

---

## 📦 Links Directos de Descarga

### POS System:
```
https://github.com/janselmichael/jym-comunicaciones-pos/releases
```

### Todo List App:
```
https://github.com/janselmichael/jym-comunicaciones-pos/releases
```

---

## ✅ Verificar que están completos

Después de descargar, verifica que los archivos sean:
- **JyM_Comunicaciones_POS.exe** - ~50-80 MB
- **TodoList_App.exe** - ~30-50 MB

---

## 🎯 Instalar y Usar

### Windows:
1. **Haz doble clic** en el .exe
2. **Acepta los permisos** si aparece un diálogo
3. **¡Listo! La aplicación se abrirá**

### Primera vez:
- **POS**: Ingresa el nombre de tu negocio
- **Todo**: Empieza a agregar tareas

---

## 🆘 Si no encuentras los .exe

### Alternativa rápida:

Ejecuta directamente desde Python:

```bash
# Para POS
python main.py

# Para Todo List
python todo_app.py
```

---

## 📞 Problemas Comunes

**P: El antivirus bloquea el .exe**
R: Es normal con archivos nuevos. Haz clic en "Permitir" o agrega a excepciones.

**P: No encuentro la carpeta dist/**
R: Ejecuta `python compile_all.py` para crearla.

**P: Me aparece error de librería**
R: Ejecuta: `pip install -r requirements.txt`

---

## 📝 Resumen

Los ejecutables están en tu GitHub en la carpeta `dist/`:

👉 **https://github.com/janselmichael/jym-comunicaciones-pos/tree/main/dist**

O compila localmente con:
```bash
python compile_all.py
```

¡Listo para usar! 🚀
