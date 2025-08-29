# main.py - Entry point pulito

#!/usr/bin/env python3
'''
STL Splitter Pro v1.0
Entry point dell'applicazione
'''

import sys
import os

# Aggiungi src al path per import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import STLSplitterProApp

def main():
    '''Avvia l'applicazione'''
    try:
        app = STLSplitterProApp()
        app.run()
    except Exception as e:
        print(f"Errore critico nell'avvio: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()