import tkinter as tk
from tkinter import ttk

class Llamadas:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Llamadas")
        self.window.geometry("400x400")
        
        self.calls = [
            ("Juan", "Llamada perdida"),
            ("Pedro", "Llamada recibida"),
            ("María", "Llamada perdida")
        ]
        
        self.create_ui()

    def create_ui(self):
        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(fill="both", expand=True)

        for name, status in self.calls:
            self.listbox.insert(tk.END, f"{name}: {status}")
        
        self.call_button = ttk.Button(self.window, text="Hacer llamada", command=self.make_call)
        self.call_button.pack(pady=10)

    def make_call(self):
        self.calls.append(("Tú", "Llamada realizada"))
        self.listbox.insert(tk.END, "Tú: Llamada realizada")