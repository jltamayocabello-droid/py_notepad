import tkinter as tk
from tkinter import filedialog, messagebox

class EditorNotas(tk.Tk):
    """
    Clase principal que representa la ventana del editor de notas.
    Hereda de tk.Tk para crear la ventana principal de la aplicación.
    """
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.title("Editor de Notas")
        self.geometry("600x400")

        # Variables de estado
        self.filepath = None # Almacena la ruta del archivo actual
        self.cambios = False # Indica si hay cambios sin guardar

        # Crear área de texto principal
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # Detectar cambios en el texto para actualizar el estado 'cambios'
        self.text_area.bind("<<Modified>>", self.on_modified)
        
        # Interceptar el evento de cierre de ventana para advertir sobre cambios no guardados
        self.protocol("WM_DELETE_WINDOW", self.al_cerrar)

        # Inicializar y configurar el menú de la aplicación
        self.crear_menu()

    def on_modified(self, event=None):
        """Maneja el evento cuando el texto es modificado."""
        if self.text_area.edit_modified():
            self.cambios = True

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
        editmenu.add_command(label="Cortar", command=self.cortar)
        editmenu.add_command(label="Copiar", command=self.copiar)
        editmenu.add_command(label="Pegar", command=self.pegar)
        menubar.add_cascade(label="Editar", menu=editmenu)

        # Asignar el menú a la ventana
        self.config(menu=menubar)

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
            self.text_area.edit_modified(False)
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