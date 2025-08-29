# src/app.py - Classe principale dell'applicazione

import tkinter as tk
from ui.main_window import MainWindow
from core.project_manager import ProjectManager
from io.settings_io import SettingsManager
from config import APP_CONFIG
import logging

class STLSplitterProApp:
    '''Classe principale dell'applicazione STL Splitter Pro'''

    def __init__(self):
        self.setup_logging()
        self.settings_manager = SettingsManager()
        self.project_manager = ProjectManager()

        # Crea finestra principale
        self.root = tk.Tk()
        self.main_window = MainWindow(
            self.root,
            self.settings_manager,
            self.project_manager
        )

    def setup_logging(self):
        '''Configura il sistema di logging'''
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('stl_splitter.log'),
                logging.StreamHandler()
            ]
        )

    def run(self):
        '''Avvia l'applicazione'''
        logging.info("Avvio STL Splitter Pro v1.0")

        # Carica impostazioni
        self.settings_manager.load_settings()

        # Avvia GUI
        self.main_window.setup_window()
        self.root.mainloop()

        # Salva impostazioni prima di chiudere
        self.settings_manager.save_settings()
        logging.info("Applicazione chiusa")