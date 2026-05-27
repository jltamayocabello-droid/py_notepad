# Aplicación de Escritorio con Interfaz Gráfica (Tkinter)

---

Curso: **Cursor con Python: desarrollo inteligente con IA** — Santander Open Academy

Proyecto de aplicación de escritorio con GUI (interfaz gráfica) desarrollado con Python, utilizando `Tkinter`, la biblioteca gráfica estándar de Python. Este script ejecuta una pequeña aplicación de bloc de notas (notepad) simplificado: una ventana con un área de texto multi-línea que permite escribir notas, con opciones avanzadas como abrir un archivo de texto existente, guardar lo escrito a un archivo, cambiar el formato de la fuente y mostrar números de línea. El proyecto forma parte del itinerario formativo del curso y pone en práctica la creación de interfaces gráficas.

## 🎯 Objetivos del Proyecto
Desarrollar un editor de texto funcional y visualmente accesible que permita a los usuarios gestionar sus notas y archivos de texto de manera sencilla.
El script realiza lo siguiente:
- ✅ **Gestión de archivos:** Permite abrir archivos de texto `.txt` y otros, guardar los cambios y usar la opción "Guardar como..." para crear nuevos archivos.
- ✅ **Edición de texto:** Área de texto multi-línea con funciones de deshacer, cortar, copiar y pegar.
- ✅ **Numeración de líneas:** Canvas lateral que dibuja dinámicamente los números de línea correspondientes al texto, facilitando la ubicación en documentos largos.
- ✅ **Personalización de formato:** Menú desplegable para cambiar la familia tipográfica (Consolas, Arial, Courier New, etc.) y el tamaño de la letra.
- ✅ **Validación de cierre:** Advierte al usuario si intenta cerrar la aplicación habiendo cambios sin guardar en el texto.

## 🛠️ Stack Tecnológico
- **Python 3:** Lenguaje base para el script de la aplicación.
- **Tkinter:** Biblioteca principal y estándar de Python para la creación de la interfaz gráfica de usuario (GUI).
- **Git / GitHub:** Control de versiones y publicación del código.

## 📂 Estructura del Proyecto
```text
notas/
├── notas.py             # Script principal con la lógica de la interfaz y editor de texto
└── README.md            # Documentación del proyecto
```

## 🚀 Instalación y Ejecución Local
Para ejecutar el bloc de notas en tu entorno local:

### 1. Clonar el repositorio:
```bash
git clone https://github.com/jltamayocabello-droid/py_notepad.git
cd py_notepad
```

### 2. Ejecutar el script:
No se requieren dependencias externas complejas, ya que `Tkinter` viene incluido por defecto en las instalaciones estándar de Python. Solo asegúrate de tener Python instalado.

```bash
python notas.py
```

### 3. Resultados:
- Se abrirá una ventana gráfica titulada "Editor de Notas" de 800x600.
- Podrás empezar a escribir, utilizar los menús superiores para guardar tus archivos (`Archivo -> Guardar`) y personalizar el tipo de letra (`Formato -> Fuente`).

## 🔗 Repositorio GitHub
[https://github.com/jltamayocabello-droid/py_notepad](https://github.com/jltamayocabello-droid/py_notepad)

## ✒️ Autor
Jorge Tamayo Cabello

Desarrollador Front-End

## 📄 Licencia
Este proyecto es parte de un trabajo formativo del curso "Cursor con Python: desarrollo inteligente con IA" de Santander Open Academy y está disponible con fines educativos.
