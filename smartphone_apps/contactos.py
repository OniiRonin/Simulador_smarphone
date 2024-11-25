import tkinter as tk
from tkinter import ttk

class Contactos:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Contactos")
        self.window.geometry("400x400")
        
        self.contacts = [("Juan", "123456789"), ("María", "987654321")]
        self.create_ui()

    def create_ui(self):
        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(fill="both", expand=True)

        for name, phone in self.contacts:
            self.listbox.insert(tk.END, f"{name}: {phone}")
        
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.pack(fill="x", padx=10, pady=10)
        self.phone_entry = ttk.Entry(self.window)
        self.phone_entry.pack(fill="x", padx=10, pady=10)
        
        self.add_button = ttk.Button(self.window, text="Agregar Contacto", command=self.add_contact)
        self.add_button.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append((name, phone))
            self.listbox.insert(tk.END, f"{name}: {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)