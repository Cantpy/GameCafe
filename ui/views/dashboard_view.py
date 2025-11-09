# ui/views/dashboard_view.py

from PySide6.QtWidgets import QWidget, QGridLayout
from ui.widgets.device_card import DeviceCard


class DashboardView(QWidget):
    """
    The main view that displays all the device cards in a grid.
    """

    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setSpacing(15)

    def update_view(self, devices):
        """
        This is the "slot" that receives the device list from the ViewModel's signal.
        It clears the old view and redraws it with the new data.
        """
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        columns = 5  # Let's try 5 columns for a better layout

        # --- MODIFICATION IS HERE ---
        # Replace the old QLabel with our new DeviceCard
        for index, device in enumerate(devices):
            row = index // columns
            col = index % columns

            # Create an instance of our powerful new widget
            device_card = DeviceCard(device)

            # Add it to the grid
            self.grid_layout.addWidget(device_card, row, col)
