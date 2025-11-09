import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from core.database import create_db_and_tables

if __name__ == '__main__':
    # --- Application Setup ---

    # 1. Create the database and tables if they don't exist
    # This is the perfect place to ensure our database is ready.
    create_db_and_tables()

    # 2. Create the QApplication instance
    # Every PySide6 application needs one (and only one) QApplication object.
    # It manages the application's main event loop and resources.
    app = QApplication(sys.argv)

    # 3. Create and show our main window
    window = MainWindow()
    window.show()

    # 4. Start the application's event loop
    # This line is crucial. It starts the event loop, which listens for
    # user interactions (like clicks and key presses) and keeps the
    # application running until the user closes it.
    sys.exit(app.exec())
