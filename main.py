import tkinter as tk
from tkinter import ttk
from smartphone_apps.calculadora import Calculadora
from smartphone_apps.sms import SMS
from smartphone_apps.llamadas import Llamadas
from smartphone_apps.contactos import Contactos
from smartphone_apps.camara import Camara
from smartphone_apps.cronometro import Cronometro
from smartphone_apps.musica import Musica
from smartphone_apps.navegador import Navegador
from smartphone_apps.galeria import Galeria
from smartphone_apps.gestor_archivos import GestorArchivos
from smartphone_apps.redes_sociales import RedesSociales
from smartphone_apps.grabadora import Grabadora

class SmartphoneSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Smartphone")
        self.root.geometry("400x600")
        
        # Botones para abrir aplicaciones
        self.create_main_menu()

    def create_main_menu(self):
        # Botones de las aplicaciones
        ttk.Button(self.root, text="Calculadora", width=20, command=self.open_calculadora).pack(pady=10)
        ttk.Button(self.root, text="SMS", width=20, command=self.open_sms).pack(pady=10)
        ttk.Button(self.root, text="Llamadas", width=20, command=self.open_llamadas).pack(pady=10)
        ttk.Button(self.root, text="Contactos", width=20, command=self.open_contactos).pack(pady=10)
        ttk.Button(self.root, text="Cámara", width=20, command=self.open_camara).pack(pady=10)
        ttk.Button(self.root, text="Cronómetro", width=20, command=self.open_cronometro).pack(pady=10)
        ttk.Button(self.root, text="Música", width=20, command=self.open_musica).pack(pady=10)
        ttk.Button(self.root, text="Navegador", width=20, command=self.open_navegador).pack(pady=10)
        ttk.Button(self.root, text="Galería", width=20, command=self.open_galeria).pack(pady=10)
        ttk.Button(self.root, text="Gestor de Archivos", width=20, command=self.open_gestor_archivos).pack(pady=10)
        ttk.Button(self.root, text="Redes Sociales", width=20, command=self.open_redes_sociales).pack(pady=10)
        ttk.Button(self.root, text="Grabadora", width=20, command=self.open_grabadora).pack(pady=10)

    def open_calculadora(self):
        Calculadora(self.root)

    def open_sms(self):
    
        SMS(self.root)

    def open_llamadas(self):
        Llamadas(self.root)

    def open_contactos(self):
        Contactos(self.root)

    def open_camara(self):
        Camara(self.root)

    def open_cronometro(self):
        Cronometro(self.root)

    def open_musica(self):
        Musica(self.root)

    def open_navegador(self):
        Navegador(self.root)

    def open_galeria(self):
        Galeria(self.root)

    def open_gestor_archivos(self):
        GestorArchivos(self.root)

    def open_redes_sociales(self):
        RedesSociales(self.root)

    def open_grabadora(self):
        Grabadora(self.root)

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartphoneSimulator(root)
    root.mainloop()