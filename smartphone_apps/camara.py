import tkinter as tk
from tkinter import ttk

class Camara:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Cámara")
        self.window.geometry("400x400")
        
        self.create_ui()

    def create_ui(self):
        self.capture_button = ttk.Button(self.window, text="Capturar Foto", command=self.capture)
        self.capture_button.pack(pady=10)

    def capture(self):
        # Aquí iría la lógica para capturar una foto. Actualmente es solo un simulacro.
        print("Foto capturada.")