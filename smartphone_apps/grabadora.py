import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import numpy as np
import wave
import tempfile

class Grabadora:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Grabadora de Voz")
        self.window.geometry("400x300")
        
        self.create_ui()

    def create_ui(self):
        self.record_button = ttk.Button(self.window, text="Grabar", command=self.record_audio)
        self.record_button.pack(pady=20)

        self.play_button = ttk.Button(self.window, text="Reproducir", command=self.play_audio)
        self.play_button.pack(pady=10)

    def record_audio(self):
        self.recording = True
        self.record_button.config(state="disabled")
        self.data = []

        with sd.InputStream(callback=self.callback):
            sd.sleep(10000)  # Graba durante 10 segundos
        self.record_button.config(state="normal")

    def callback(self, indata, frames, time, status):
        if self.recording:
            self.data.append(indata)
        else:
            raise sd.CallbackStop()

    def play_audio(self):
        if hasattr(self, 'data'):
            audio_data = np.concatenate(self.data, axis=0)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                with wave.open(tmp_file, 'wb') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)  # 16-bit depth
                    wf.setframerate(44100)
                    wf.writeframes(audio_data.tobytes())
                sd.play(audio_data, 44100)