import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class GestorArchivos:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Gestor de Archivos")
        self.window.geometry("400x400")
        
        self.create_ui()

    def create_ui(self):
        self.open_button = ttk.Button(self.window, text="Abrir archivo", command=self.open_file)
        self.open_button.pack(pady=20)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print(f"Abriendo archivo: {file_path}")
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)