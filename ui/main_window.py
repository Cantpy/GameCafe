# ui/main_window.py

from PySide6.QtWidgets import QMainWindow
from ui.views.dashboard_view import DashboardView
from core.viewmodels import DashboardViewModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.tr("Gaming Cafe Manager"))
        self.setGeometry(100, 100, 1200, 800)

        # 1. Create instances of the ViewModel and the View
        self.view_model = DashboardViewModel()
        self.dashboard_view = DashboardView()

        # 2. Set the dashboard_view as the central widget
        # QMainWindow requires a single central widget, so we set our view directly.
        self.setCentralWidget(self.dashboard_view)

        # 3. Connect the ViewModel's signal to the View's slot (The MVVM Magic)
        # When the view_model emits 'devices_changed', the dashboard_view's
        # 'update_view' method will be called automatically with the new data.
        self.view_model.devices_changed.connect(self.dashboard_view.update_view)

        # 4. Trigger the initial data load
        self.view_model.load_devices()

    # The retranslate method might be needed later for dynamic language switching
    def retranslate_ui(self):
        self.setWindowTitle(self.tr("Gaming Cafe Manager"))
        # In a more complex app, you would tell the view to re-translate its widgets
