import tkinter as tk

from tkinter import filedialog, messagebox

 

class EditorNotas(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Editor de Notas")

        self.geometry("600x400")

        self.filepath = None
        self.cambios = False

        # Crear área de texto
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # Detectar cambios en el texto
        self.text_area.bind("<<Modified>>", self.on_modified)
        
        # Interceptar el evento de cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.al_cerrar)

        # Crear menú
        self.crear_menu()

    def on_modified(self, event=None):
        if self.text_area.edit_modified():
            self.cambios = True

   

    def crear_menu(self):

        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)

        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_command(label="Guardar como...", command=self.guardar_como)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.al_cerrar)
        menubar.add_cascade(label="Archivo", menu=filemenu)

        self.config(menu=menubar)

   

    def abrir_archivo(self):

        filepath = filedialog.askopenfilename(

            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")]

        )

        if not filepath:

            return

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
            
            self.filepath = filepath
            self.cambios = False
            self.text_area.edit_modified(False)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

    def guardar_archivo(self):
        if not self.filepath:
            return self.guardar_como()
            
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(self.filepath, "w", encoding="utf-8") as file:
                file.write(contenido)
            self.cambios = False
            self.text_area.edit_modified(False)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")
            return False

    def guardar_como(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")]
        )
        if not filepath:
            return False
            
        self.filepath = filepath
        return self.guardar_archivo()

    def al_cerrar(self):
        if self.cambios:
            respuesta = messagebox.askyesnocancel("Salir", "¿Desea guardar cambios antes de salir?")
            if respuesta: # Yes
                if self.guardar_archivo():
                    self.destroy()
            elif respuesta is False: # No
                self.destroy()
            # If None (Cancel), we do nothing and keep the window open
        else:
            self.destroy()

 

if __name__ == "__main__":

    app = EditorNotas()

    app.mainloop()