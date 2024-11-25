import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class Galeria:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Galería de Imágenes")
        self.window.geometry("500x500")

        self.image_label = ttk.Label(self.window)
        self.image_label.pack(fill="both", expand=True)

        self.create_ui()

    def create_ui(self):
        self.select_button = ttk.Button(self.window, text="Seleccionar Imagen", command=self.select_image)
        self.select_button.pack(pady=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png *.jpg *.jpeg *.gif")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((400, 400))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
