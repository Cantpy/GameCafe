from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
# We need QCoreApplication for the tr function context if not in a QObject
from PySide6.QtCore import QCoreApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(QCoreApplication.translate("MainWindow", "Gaming Cafe Manager"))
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # We now use self.tr() for the label text
        # The first argument is the source text, the second is a disambiguation comment for translators
        welcome_label = QLabel(self.tr("Welcome to the Gaming Cafe Manager! Dashboard coming soon..."))
        welcome_label.setStyleSheet("font-size: 24px; text-align: center; color: #333;")

        layout.addWidget(welcome_label)

    # We need a method to re-translate the UI when the language changes
    def retranslate_ui(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", "Gaming Cafe Manager"))
        # Any other widgets that need text updates would go here
        # For example: self.welcome_label.setText(self.tr("..."))
