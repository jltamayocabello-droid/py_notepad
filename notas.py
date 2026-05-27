import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkfont

class LineNumbers(tk.Canvas):
    """
    Widget Canvas personalizado para dibujar los números de línea.
    """
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None
        self.font = None

    def attach(self, text_widget, font):
        """Asocia el área de texto y la fuente para poder calcular la posición de las líneas."""
        self.textwidget = text_widget
        self.font = font
        
    def redraw(self, *args):
        """Redibuja los números de línea basándose en las líneas visibles en el Text."""
        self.delete("all")

        # Obtener el índice de la primera línea visible
        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            # Dibujar el número de línea alineado a la derecha
            self.create_text(35, y, anchor="ne", text=linenum, font=self.font, fill="#606366")
            i = self.textwidget.index("%s+1line" % i)

class EditorNotas(tk.Tk):
    """
    Clase principal que representa la ventana del editor de notas.
    Hereda de tk.Tk para crear la ventana principal de la aplicación.
    """
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.title("Editor de Notas")
        self.geometry("800x600")

        # Variables de estado
        self.filepath = None # Almacena la ruta del archivo actual
        self.cambios = False # Indica si hay cambios sin guardar

        # Configuración de fuente por defecto
        self.current_font_family = tk.StringVar(value="Consolas")
        self.current_font_size = tk.IntVar(value=12)
        self.editor_font = tkfont.Font(family=self.current_font_family.get(), size=self.current_font_size.get())

        # Frame principal para contener el área de texto, números de línea y scrollbars
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Scrollbars (Vertical y Horizontal)
        self.v_scroll = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL)
        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.h_scroll = tk.Scrollbar(self.main_frame, orient=tk.HORIZONTAL)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        # Canvas para números de línea
        self.line_numbers = LineNumbers(self.main_frame, width=40, bg="#f0f0f0", highlightthickness=0)
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Crear área de texto principal
        # wrap="none" permite usar la barra de desplazamiento horizontal
        self.text_area = tk.Text(self.main_frame, wrap="none", font=self.editor_font,
                                 yscrollcommand=self.sync_vscroll, xscrollcommand=self.h_scroll.set,
                                 undo=True)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # Configurar comandos de scroll
        self.v_scroll.config(command=self.text_area.yview)
        self.h_scroll.config(command=self.text_area.xview)
        
        # Conectar el widget de números de línea con el Text
        self.line_numbers.attach(self.text_area, self.editor_font)
        
        # Eventos para actualizar la numeración de líneas
        self.text_area.bind("<KeyRelease>", self.actualizar_numeros)
        self.text_area.bind("<MouseWheel>", self.actualizar_numeros)
        self.text_area.bind("<Button-1>", self.actualizar_numeros)
        self.text_area.bind("<Configure>", self.actualizar_numeros)
        
        # Detectar cambios en el texto para actualizar el estado 'cambios'
        self.text_area.bind("<<Modified>>", self.on_modified)
        
        # Interceptar el evento de cierre de ventana para advertir sobre cambios no guardados
        self.protocol("WM_DELETE_WINDOW", self.al_cerrar)

        # Inicializar y configurar el menú de la aplicación
        self.crear_menu()
        
        # Dibujo inicial de los números de línea
        self.after(100, self.actualizar_numeros)

    def sync_vscroll(self, *args):
        """Sincroniza el scroll vertical y actualiza los números de línea."""
        self.v_scroll.set(*args)
        self.actualizar_numeros()

    def actualizar_numeros(self, event=None):
        """Llama a la función de redibujado de los números de línea."""
        self.line_numbers.redraw()

    def on_modified(self, event=None):
        """Maneja el evento cuando el texto es modificado."""
        if self.text_area.edit_modified():
            self.cambios = True
        # Actualizamos también los números de línea en caso de cambios masivos
        self.actualizar_numeros()
        # Se requiere resetear la bandera modified para que vuelva a dispararse el evento en el futuro
        self.text_area.edit_modified(False)

    def actualizar_fuente(self, *args):
        """Aplica la nueva fuente seleccionada tanto al Text como a los números de línea."""
        self.editor_font.configure(family=self.current_font_family.get(), size=self.current_font_size.get())
        self.line_numbers.font = self.editor_font
        self.actualizar_numeros()

    def crear_menu(self):
        """Crea y configura la barra de menú superior."""
        menubar = tk.Menu(self)

        # Menú Archivo
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_command(label="Guardar como...", command=self.guardar_como)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.al_cerrar)
        menubar.add_cascade(label="Archivo", menu=filemenu)

        # Menú Editar
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Deshacer", command=self.deshacer)
        editmenu.add_separator()
        editmenu.add_command(label="Cortar", command=self.cortar)
        editmenu.add_command(label="Copiar", command=self.copiar)
        editmenu.add_command(label="Pegar", command=self.pegar)
        menubar.add_cascade(label="Editar", menu=editmenu)
        
        # Menú Formato
        formatmenu = tk.Menu(menubar, tearoff=0)
        
        # Submenú Fuente
        fontmenu = tk.Menu(formatmenu, tearoff=0)
        fuentes_basicas = ["Consolas", "Arial", "Courier New", "Times New Roman", "Verdana"]
        for fuente in fuentes_basicas:
            fontmenu.add_radiobutton(label=fuente, variable=self.current_font_family, 
                                     value=fuente, command=self.actualizar_fuente)
        formatmenu.add_cascade(label="Fuente", menu=fontmenu)
        
        # Submenú Tamaño de Fuente
        sizemenu = tk.Menu(formatmenu, tearoff=0)
        tamanos = [10, 12, 14, 16, 18, 20, 24]
        for tamano in tamanos:
            sizemenu.add_radiobutton(label=str(tamano), variable=self.current_font_size, 
                                     value=tamano, command=self.actualizar_fuente)
        formatmenu.add_cascade(label="Tamaño", menu=sizemenu)

        menubar.add_cascade(label="Formato", menu=formatmenu)

        # Asignar el menú a la ventana
        self.config(menu=menubar)

    def deshacer(self):
        """Ejecuta la acción de deshacer en el área de texto."""
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass

    def cortar(self):
        """Ejecuta la acción de cortar en el área de texto."""
        self.text_area.event_generate("<<Cut>>")

    def copiar(self):
        """Ejecuta la acción de copiar en el área de texto."""
        self.text_area.event_generate("<<Copy>>")

    def pegar(self):
        """Ejecuta la acción de pegar en el área de texto."""
        self.text_area.event_generate("<<Paste>>")

    def abrir_archivo(self):
        """Abre un cuadro de diálogo para seleccionar y cargar un archivo de texto."""
        filepath = filedialog.askopenfilename(
            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")]
        )

        if not filepath:
            return

        try:
            # Leer el contenido del archivo
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()
            
            # Limpiar el área de texto e insertar el nuevo contenido
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
            
            # Actualizar estado
            self.filepath = filepath
            self.cambios = False
            self.text_area.edit_modified(False)
            self.actualizar_numeros()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

    def guardar_archivo(self):
        """Guarda el contenido actual en el archivo abierto. Si es nuevo, llama a guardar_como."""
        if not self.filepath:
            return self.guardar_como()
            
        try:
            # Obtener el contenido del área de texto
            contenido = self.text_area.get(1.0, tk.END)
            # Guardar el contenido en el archivo
            with open(self.filepath, "w", encoding="utf-8") as file:
                file.write(contenido)
            
            # Restablecer estado de cambios
            self.cambios = False
            return True
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")
            return False

    def guardar_como(self):
        """Abre un cuadro de diálogo para guardar el contenido como un nuevo archivo."""
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")]
        )
        if not filepath:
            return False
            
        self.filepath = filepath
        return self.guardar_archivo()

    def al_cerrar(self):
        """Verifica si hay cambios sin guardar antes de cerrar la aplicación."""
        if self.cambios:
            respuesta = messagebox.askyesnocancel("Salir", "¿Desea guardar cambios antes de salir?")
            if respuesta: # Sí, guardar y salir
                if self.guardar_archivo():
                    self.destroy()
            elif respuesta is False: # No, salir sin guardar
                self.destroy()
            # Si es None (Cancelar), no hacemos nada y mantenemos la ventana abierta
        else:
            # No hay cambios, cerrar directamente
            self.destroy()

if __name__ == "__main__":
    # Iniciar la aplicación
    app = EditorNotas()
    app.mainloop()