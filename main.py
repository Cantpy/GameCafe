import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QLocale, Qt
from ui.main_window import MainWindow
from core.database import create_db_and_tables

# --- App Constants ---
# In a real app, you might load this from a config file (e.g., config.json)
CURRENT_LANGUAGE = "fa"  # <--- CHANGE THIS between "en" and "fa" to test!

if __name__ == '__main__':
    # --- Database Setup ---
    create_db_and_tables()

    # --- Application Setup ---
    app = QApplication(sys.argv)

    # --- Internationalization (i18n) and RTL Setup ---
    translator = QTranslator()

    # Construct the path to the translation file
    # Example path: gaming_cafe_app/i18n/app_fa.qm
    i18n_path = os.path.join(os.path.dirname(__file__), 'i18n', f'app_{CURRENT_LANGUAGE}.qm')

    if os.path.exists(i18n_path):
        translator.load(i18n_path)
        QApplication.installTranslator(translator)
        print(f"Successfully loaded translation for '{CURRENT_LANGUAGE}'")
    else:
        print(f"Warning: Translation file not found for '{CURRENT_LANGUAGE}'. Using default language.")

    # Set Layout Direction based on language
    if CURRENT_LANGUAGE == 'fa':
        QApplication.setLayoutDirection(Qt.RightToLeft)
    else:
        QApplication.setLayoutDirection(Qt.LeftToRight)

    # --- Window Creation ---
    window = MainWindow()
    window.show()

    # --- Start Event Loop ---
    sys.exit(app.exec())