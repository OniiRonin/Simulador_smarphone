import tkinter as tk
from tkinter import ttk
import webbrowser

class Navegador:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Navegador Web")
        self.window.geometry("500x400")
        
        self.create_ui()

    def create_ui(self):
        self.url_entry = ttk.Entry(self.window)
        self.url_entry.pack(fill="x", padx=10, pady=10)
        self.url_entry.insert(0, "https://www.google.com")

        self.go_button = ttk.Button(self.window, text="Ir", command=self.open_url)
        self.go_button.pack(pady=10)

    def open_url(self):
        url = self.url_entry.get()
        webbrowser.open(url)