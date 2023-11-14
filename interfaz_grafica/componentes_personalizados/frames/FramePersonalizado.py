import tkinter as tk
from PIL import Image, ImageTk

class FramePersonalizado(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.lista_componentes = []
        self.config(width=693, height=558, bg="#6053AF")

        imagen_original = Image.open('../imagenes/Contenedor programas.png')
        self.imagen_redimensionada = self.redimensionar_imagen(imagen_original, 693, 558)
        etiqueta_imagen = tk.Label(self, image=self.imagen_redimensionada, bg="#6053AF")
        etiqueta_imagen.place(x=0, y=0)

        self.etiquetaTitulo = tk.Label(self, text=".....", font=("Inter", 25, "bold"), bg="#FFFFFF", fg="#4E458E")
        self.etiquetaTitulo.place(x=58, y=26)

        self.subframe = tk.Frame(self, width=680, height=458, bg="#D39E9E")
        self.subframe.place(x=6, y=83)

        self.canvas = tk.Canvas(self.subframe, bg="#FFFFFF", width=663, height=458)
        self.canvas.pack(side="left", fill="both", expand=True)  # Usar pack para el canvas

        self.scrollbar_y = tk.Scrollbar(self.subframe, orient="vertical", command=self.canvas.yview)
        self.scrollbar_y.pack(side="right", fill="y")

        self.scrollbar_y.focus()

        self.canvas.config(yscrollcommand=self.scrollbar_y.set)

    def redimensionar_imagen(self, imagen, nuevo_ancho, nuevo_alto):
        imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
        return ImageTk.PhotoImage(imagen_redimensionada)

    def editar_titulo(self, texto):
        self.etiquetaTitulo.config(text=f"{texto}")

    def agregar_componente(self, componente, x, y):
        self.canvas.create_window((x, y), window=componente)

        # Ajustar el tamaño del canvas según el componente agregado
        bbox = self.canvas.bbox("all")  # Obtener las dimensiones de todos los elementos en el canvas

        # Configurar el área de desplazamiento del canvas
        self.canvas.config(scrollregion=(0, 0, bbox[2], bbox[3]))

        # Ajustar el tamaño del canvas y el rango del scrollbar
        self.canvas.update_idletasks()
        bbox = self.canvas.bbox("all")  # Obtener las nuevas dimensiones de todos los elementos en el canvas

        # Configurar el área de desplazamiento del canvas después de la actualización
        self.canvas.config(scrollregion=(0, 0, bbox[2], bbox[3]))

        # Ajustar el rango del scrollbar después de la actualización
        scrollbar_position = bbox[3]  # Nueva posición del último componente en relación con el canvas
        self.scrollbar_y.set(0, scrollbar_position)  # Establecer el rango del scrollbar

        # Forzar a Tkinter a redibujar los widgets cada vez que se hace scroll
        self.canvas.bind("<Configure>", lambda e: self.canvas.update_idletasks())

    def agregar_lista_componentes(self, lista_componentes):
        x_canvas = 330 - self.canvas.winfo_x()
        y_canvas = 100 - self.canvas.winfo_y()
        separacion_vertical = 200

        for i, componente in enumerate(lista_componentes):
            self.agregar_componente(componente, x_canvas, y_canvas + i * separacion_vertical)
