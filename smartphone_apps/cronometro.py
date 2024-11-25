import tkinter as tk
from tkinter import ttk

class Cronometro:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Cronómetro")
        self.window.geometry("300x200")
        
        self.time = 0
        self.running = False
        self.create_ui()

    def create_ui(self):
        self.label = ttk.Label(self.window, text="00:00", font=("Helvetica", 30))
        self.label.pack(pady=20)

        self.start_button = ttk.Button(self.window, text="Iniciar", command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.pause_button = ttk.Button(self.window, text="Pausar", command=self.pause)
        self.pause_button.pack(side="left", padx=10)

        self.reset_button = ttk.Button(self.window, text="Reiniciar", command=self.reset)
        self.reset_button.pack(side="left", padx=10)

    def update_time(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            self.label.config(text=f"{minutes:02}:{seconds:02}")
            self.window.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00")