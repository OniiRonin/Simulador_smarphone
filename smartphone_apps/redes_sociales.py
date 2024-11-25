import tkinter as tk
from tkinter import ttk
import webbrowser

class RedesSociales:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Redes Sociales")
        self.window.geometry("400x400")
        
        self.create_ui()

    def create_ui(self):
        self.fb_button = ttk.Button(self.window, text="Facebook", command=lambda: self.open_platform("https://www.facebook.com"))
        self.fb_button.pack(pady=10)

        self.tw_button = ttk.Button(self.window, text="Twitter", command=lambda: self.open_platform("https://www.twitter.com"))
        self.tw_button.pack(pady=10)

        self.insta_button = ttk.Button(self.window, text="Instagram", command=lambda: self.open_platform("https://www.instagram.com"))
        self.insta_button.pack(pady=10)

    def open_platform(self, url):
        webbrowser.open(url)