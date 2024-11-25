import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame

class Musica:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Reproductor de Música")
        self.window.geometry("400x200")
        
        pygame.mixer.init()

        self.create_ui()

    def create_ui(self):
        self.play_button = ttk.Button(self.window, text="Cargar y Reproducir", command=self.play_music)
        self.play_button.pack(pady=20)

    def play_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3 *.wav")])
        if file_path:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()