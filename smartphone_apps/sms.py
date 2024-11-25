import tkinter as tk
from tkinter import ttk

class SMS:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("SMS")
        self.window.geometry("400x400")
        
        self.messages = [
            ("Juan", "Hola! ¿Cómo estás?"),
            ("Pedro", "Vamos a salir hoy"),
            ("María", "Te llamo en un momento")
        ]
        
        self.create_ui()
        
    def create_ui(self):
        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(fill="both", expand=True)
        
        for sender, msg in self.messages:
            self.listbox.insert(tk.END, f"{sender}: {msg}")
        
        self.entry = ttk.Entry(self.window)
        self.entry.pack(fill="x", padx=10, pady=10)
        
        self.send_button = ttk.Button(self.window, text="Enviar", command=self.send_message)
        self.send_button.pack(pady=10)
    
    def send_message(self):
        message = self.entry.get()
        if message:
            self.messages.append(("Tú", message))
            self.listbox.insert(tk.END, f"Tú: {message}")
            self.entry.delete(0, tk.END)