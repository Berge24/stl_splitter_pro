# src/config.py - Configurazioni centrali

import os
from pathlib import Path

# Configurazioni applicazione
APP_CONFIG = {
    'name': 'STL Splitter Pro',
    'version': '1.0.0',
    'author': 'STL Splitter Pro Team',
    'description': 'Professional STL 3D Model Splitter for 3D Printing',
    'window_size': '1200x800',
    'min_window_size': (1000, 700),
}

# Percorsi
BASE_DIR = Path(__file__).parent.parent
ASSETS_DIR = BASE_DIR / 'assets'
ICONS_DIR = ASSETS_DIR / 'icons'
THEMES_DIR = ASSETS_DIR / 'themes'
DOCS_DIR = BASE_DIR / 'docs'

# Impostazioni default
DEFAULT_SETTINGS = {
    'theme': 'light',
    'language': 'it',
    'default_printer': 'Ender 3',
    'auto_save': True,
    'safety_margin': 2.0,
    'overlap': 0.5,
    'recent_files_limit': 10,
    'log_level': 'INFO'
}

# Profili stampanti
PRINTER_PROFILES = {
    'Ender 3': {'x': 220, 'y': 220, 'z': 250},
    'Ender 3 Pro': {'x': 220, 'y': 220, 'z': 250},
    'Ender 3 V2': {'x': 220, 'y': 220, 'z': 250},
    'Prusa i3 MK3': {'x': 250, 'y': 210, 'z': 200},
    'Prusa i3 MK3S': {'x': 250, 'y': 210, 'z': 200},
    'Artillery Sidewinder X1': {'x': 300, 'y': 300, 'z': 400},
    'Artillery Sidewinder X2': {'x': 300, 'y': 300, 'z': 400},
    'Bambu Lab X1': {'x': 256, 'y': 256, 'z': 256},
    'Bambu Lab A1': {'x': 256, 'y': 256, 'z': 256},
    'Anycubic Kobra': {'x': 220, 'y': 220, 'z': 250},
    'Anycubic Kobra 2': {'x': 220, 'y': 220, 'z': 250},
    'Custom': {'x': 200, 'y': 200, 'z': 200}
}

# Costanti algoritmi
ALGORITHM_CONFIG = {
    'min_part_volume_ratio': 0.05,  # 5% del volume totale
    'max_faces_per_part': 50000,    # Massimo facce per parte
    'overlap_tolerance': 0.1,        # Tolleranza sovrapposizione
    'mesh_repair_enabled': True,     # Auto-repair mesh
}

# Formati file supportati
SUPPORTED_FORMATS = {
    'input': ['.stl'],
    'output': ['.stl'],
    'project': ['.ssp']  # STL Splitter Pro project
}