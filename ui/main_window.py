from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        # Call the constructor of the parent class (QMainWindow)
        super().__init__()

        # --- Window Properties ---
        self.setWindowTitle("Gaming Cafe Manager")
        self.setGeometry(100, 100, 1200, 800)  # (x, y, width, height)

        # --- Central Widget and Layout ---
        # QMainWindow has a special area for the main content called the "central widget".
        # We'll create a generic QWidget to act as this container.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # A layout manager is essential for arranging widgets.
        # QVBoxLayout arranges widgets vertically.
        layout = QVBoxLayout(central_widget)

        # --- Placeholder Content ---
        # Let's add a simple label to show that our window is working.
        # We will replace this later with our actual dashboard.
        welcome_label = QLabel("Welcome to the Gaming Cafe Manager! Dashboard coming soon...")
        welcome_label.setStyleSheet("font-size: 24px; text-align: center; color: #333;")

        layout.addWidget(welcome_label)
