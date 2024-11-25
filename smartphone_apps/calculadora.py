import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Calculadora")
        self.window.geometry("300x400")
        
        self.result_var = tk.StringVar()
        
        entry = ttk.Entry(self.window, textvariable=self.result_var, font=("Helvetica", 20), justify="right")
        entry.pack(fill="both", padx=10, pady=10)
        
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]
        
        for (text, row, col) in buttons:
            ttk.Button(self.window, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        for i in range(5):
            self.window.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.window.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                expression = self.result_var.get()
                self.result_var.set(eval(expression))
            except Exception:
                self.result_var.set("Error")
        else:
            self.result_var.set(self.result_var.get() + char)