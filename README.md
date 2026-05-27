# Aplicación de Escritorio con Interfaz Gráfica (Tkinter)

---

![Estado del Proyecto](https://img.shields.io/badge/Estado-Completado-success)
![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Tkinter-blue)
![UI](https://img.shields.io/badge/UI-Dark%20Mode%20%7C%20Minimalist-6f42c1)

**Curso:** [Cursor con Python: desarrollo inteligente con IA](https://www.santanderopenacademy.com/) — **Santander Open Academy**

**App bloc de notas:** aplicación de escritorio moderna con interfaz gráfica (GUI) desarrollada en Python usando la biblioteca estándar **Tkinter**. El proyecto forma parte del itinerario formativo del curso y pone en práctica la creación de interfaces de usuario locales, la manipulación de flujos de archivos (I/O) y el control dinámico de eventos en tiempo real.

Desarrollar un bloc de notas simplificado que sea responsivo, intuitivo y estéticamente agradable. La aplicación proporciona una ventana interactiva de edición de notas con herramientas avanzadas para la gestión de archivos y personalización de lectura.

La aplicación permite:
* ✅ Abrir archivos de texto plano `.txt` y cargarlos en el editor.
* ✅ Guardar directamente en el archivo abierto o utilizar la opción "Guardar como..." para almacenar notas nuevas.
* ✅ Edición ágil de texto con soporte nativo de deshacer (`undo`), copiar, cortar y pegar.
* ✅ Numeración dinámica de líneas que se redibuja en tiempo real durante la edición y el scroll.
* ✅ Personalización de la tipografía (fuentes y tamaños) mediante menús intuitivos de formato.
* ✅ Interfaz moderna optimizada en **modo oscuro** para reducir la fatiga visual.
* ✅ Sistema inteligente de advertencia al cerrar la ventana si existen cambios pendientes de guardar.

---

Este proyecto cumple con todos los objetivos pedagógicos y técnicos del módulo formativo:
* ✅ **Biblioteca Gráfica Estándar**: Uso avanzado del paquete `tkinter` e interacción de clases integradas (`tk.Tk`, `tk.Canvas`, `tk.Text`, etc.).
* ✅ **Programación Orientada a Objetos**: Lógica estructurada en la clase principal `EditorNotas` y componente especializado `LineNumbers`.
* ✅ **Dibujo y Canvas Dinámico**: Manipulación de coordenadas en `tk.Canvas` para la actualización dinámica de números alineados.
* ✅ **Control de Eventos y Bindings**: Vinculación de teclas, scroll y cambios estructurales (`<KeyRelease>`, `<MouseWheel>`, `<<Modified>>`).
* ✅ **Gestión del Sistema de Archivos**: Uso de `filedialog` y manejo robusto de flujos I/O (lectura y escritura codificada en `utf-8`).
* ✅ **Manejo de Diálogos**: Mensajes de confirmación (`messagebox.askyesnocancel`) y alertas de error en tiempo de ejecución.
* ✅ **Diseño UI en Modo Oscuro**: Integración manual de paleta cromática estilo "VS Code" con bordes planos y alto contraste.

---

### 1. Stack Tecnológico
* **Python 3**: Lenguaje base para el backend y frontend local.
* **Tkinter**: Biblioteca oficial y nativa de Python para interfaces de usuario (GUI).
* **Git / GitHub**: Control de versiones y publicación del código.

### 2. Estructura del Proyecto
```text
notas/
├── notas.py             # Script principal con la lógica de GUI, eventos y negocio
└── README.md            # Documentación detallada del proyecto
```

### 3. Modelo de Datos y Flujo de Eventos
La interacción del usuario con la interfaz gráfica se maneja a través de variables de estado y la propagación de eventos sobre los widgets clave:

| Variable / Estado | Tipo | Propósito |
|-------------------|------|-----------|
| `filepath`        | str / None | Ruta del archivo de texto abierto actualmente en disco. |
| `cambios`         | bool | Bandera para controlar si hay modificaciones pendientes sin guardar. |
| `current_font_family` | StringVar | Almacena y sincroniza el nombre de la tipografía seleccionada. |
| `current_font_size` | IntVar | Almacena y sincroniza el tamaño de la tipografía en píxeles. |

**Flujo de Redibujado de Números (`LineNumbers`):**
```python
def redraw(self, *args):
    """Calcula la posición exacta de las líneas visibles y dibuja los números correspondientes."""
```

### 4. Menú y Funciones de la Aplicación
| Categoría | Opción | Función Asociada | Descripción |
|-----------|--------|------------------|-------------|
| **Archivo** | Abrir | `abrir_archivo` | Lanza cuadro de diálogo para cargar contenido desde el almacenamiento local. |
| **Archivo** | Guardar | `guardar_archivo` | Guarda el contenido actual en el archivo activo; si es nuevo, abre diálogo de guardado. |
| **Archivo** | Guardar como | `guardar_como` | Guarda el texto forzando la especificación de un nuevo nombre y ruta. |
| **Editar** | Deshacer / Cortar / Copiar / Pegar | `deshacer` / `event_generate` | Ejecuta operaciones clásicas del portapapeles y de historial del editor. |
| **Formato** | Fuente | `actualizar_fuente` | Cambia dinámicamente la familia de la tipografía a la seleccionada (Consolas, Arial, etc.). |
| **Formato** | Tamaño | `actualizar_fuente` | Ajusta instantáneamente la escala de fuente del editor y los números. |

### 5. Paleta de Colores — Modo Oscuro
El editor ha sido estilizado para garantizar legibilidad mediante un esquema oscuro de baja fatiga visual:

| Elemento | Color (Hex) | Propósito |
|----------|-------------|-----------|
| Fondo del Editor / Ventana | `#1e1e1e` | Fondo principal oscuro, idéntico a las áreas de trabajo de editores profesionales. |
| Fondo del Canvas (Líneas) | `#252526` | Panel de números lateral ligeramente más claro para ofrecer separación visual y contraste. |
| Números de Línea | `#858585` | Color gris mate neutro para la numeración, evitando distracciones al programar o escribir. |
| Texto del Editor | `#d4d4d4` | Color del texto principal, un tono gris claro suave ideal para lectura prolongada. |
| Cursor de Texto | `white` | Cursor blanco de alta visibilidad para localizar el foco inmediatamente. |
| Selección de Texto | `#264f78` | Azul oscuro vibrante para marcar la selección de bloques de texto. |

---

### 6. Decisiones de Diseño y Justificaciones

#### Implementación de Numeración con Canvas
**Decisión:** Crear una clase especializada `LineNumbers` heredando de `tk.Canvas` para dibujar los números de línea, en lugar de usar otro widget de texto.

**Justificación:**
* **Precisión**: Permite calcular con exactitud la coordenada vertical `y` de cada línea visible gracias al método `dlineinfo()`.
* **Rendimiento**: Redibuja de manera fluida y exclusiva las líneas visibles en pantalla, optimizando el consumo de recursos en archivos extensos.
* **Separación de Responsabilidades**: El canvas se encarga solo de la representación gráfica del número de línea y se acopla de manera no intrusiva al control de texto principal.

#### Eventos Multi-Enlace (Multi-bindings) para actualización
**Decisión:** Vincular el redibujado de la numeración a eventos como `<KeyRelease>`, `<MouseWheel>`, `<Button-1>` y `<Configure>`.

**Justificación:**
* **Sincronización total**: Asegura que los números se actualicen inmediatamente sin importar si el usuario escribe, hace scroll, hace clic para mover el cursor o redimensiona la ventana de la aplicación.

#### Gestión del Estado Modificado (Modified)
**Decisión:** Utilizar el evento interno `<<Modified>>` del control `tk.Text` con un reinicio manual de la bandera.

**Justificación:**
* **Eficiencia**: Evita tener que evaluar de forma manual cada pulsación de tecla para determinar si ha cambiado el contenido, utilizando el mecanismo nativo optimizado de Tkinter y permitiendo advertir al usuario con fiabilidad antes de cerrar el editor con cambios sin guardar.

#### Interfaz Libre de Bordes (Flat Relief)
**Decisión:** Configurar el widget de edición de texto principal con `relief=tk.FLAT` y bordes limpios en toda la aplicación.

**Justificación:**
* **Estética moderna**: Elimina los biseles y relieves tridimensionales clásicos de las aplicaciones antiguas de los 90, adaptando el bloc de notas a los estándares actuales de diseño plano (*flat UI*).

---

## 🚀 Instalación y Ejecución Local

Para ejecutar esta aplicación en tu entorno local:

### 1. Clonar el repositorio:
```bash
git clone https://github.com/jltamayocabello-droid/py_notepad.git
cd py_notepad
```

### 2. Ejecución directa:
No necesitas instalar entornos virtuales ni requerimientos de terceros (¡cero librerías externas!), dado que `Tkinter` viene preinstalado con la distribución oficial de Python.

Ejecuta el script principal desde tu terminal:
```bash
python notas.py
```

### 3. Operación de la aplicación:
1. **Escribir notas**: Haz clic directamente sobre la zona oscura y comienza a teclear.
2. **Personalizar**: Dirígete al menú superior `Formato` para cambiar la fuente y el tamaño de letra.
3. **Manejar Archivos**: Usa `Archivo -> Abrir` para importar texto externo, o `Archivo -> Guardar` para persistir tu progreso actual.

---

## 🧪 Testing Manual
Para validar el correcto comportamiento de todas las utilidades de la aplicación, puedes realizar las siguientes comprobaciones:
1. **Verificar numeración al escribir**: Presiona la tecla `Enter` repetidamente; la numeración lateral debe crecer de forma secuencial (1, 2, 3, etc.).
2. **Validar scroll vertical**: Carga un texto largo. Al desplazar la vista con la rueda del ratón o la barra lateral, la numeración de líneas debe actualizarse y mantenerse perfectamente sincronizada con la línea visible de texto.
3. **Comprobación de fuentes**: Ve al menú `Formato -> Fuente` y cambia el valor a *Arial*. Verifica que tanto el texto del bloc como los números de línea cambien su estilo tipográfico. Haz lo mismo con el menú de `Tamaño` para validar el escalado.
4. **Validación de seguridad al cerrar**: Escribe cualquier carácter en la pantalla e intenta cerrar directamente el programa desde la "X" superior de la ventana. Deberá emerger un diálogo de advertencia preguntándote si deseas salvar los cambios pendientes.
5. **Apertura y guardado de archivos**: Abre un archivo `.txt`, realiza una edición, haz clic en `Guardar` y cierra la aplicación. Vuelve a abrir el archivo para cerciorarte de que la edición persistió de forma íntegra.

---

## 📚 Recursos y Referencias
* [Documentación Oficial de Python 3 - Tkinter](https://docs.python.org/es/3/library/tkinter.html)
* [Tkinter Gui Application Development Reference](https://tkdocs.com/)
* [ActiveState Tkinter Reference Manual](https://www.activestate.com/resources/quick-reads/how-to-use-tkinter-in-python-guide/)

---

## ✒️ Autor
**Jorge Tamayo Cabello**

_Desarrollador Front-End_

---

## 📄 Licencia
Este proyecto es parte de un trabajo formativo del curso **"Cursor con Python: desarrollo inteligente con IA"** de **Santander Open Academy** y está disponible con fines educativos.

---

## 🙏 Agradecimientos
* **Santander Open Academy** por la excelente oportunidad de formación técnica en automatización y desarrollo práctico.
* **Comunidad Python y Tkinter** por proveer abundante documentación del ecosistema de desarrollo de escritorio.
