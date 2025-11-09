# ui/widgets/device_card.py

from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from core.models import Device

# Define a color mapping for different device statuses.
# This makes it easy to change the color scheme later.
STATUS_COLORS = {
    "Available": "#4CAF50",  # Green
    "In Use": "#FF9800",  # Orange
    "Needs Attention": "#F44336",  # Red
    "Reserved": "#2196F3",  # Blue
    "default": "#BDBDBD"  # Gray for any other status
}


class DeviceCard(QFrame):
    """
    A custom widget that displays information about a single device.
    It's a QFrame, which allows it to have a border and background color.
    """

    def __init__(self, device: Device):
        super().__init__()
        self.device = device

        # --- Widget Properties ---
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setMinimumHeight(120)

        # --- Layout ---
        # A vertical layout is perfect for stacking info in the card.
        layout = QVBoxLayout(self)

        # --- Widgets to display info ---
        self.name_label = QLabel(f"<b>{self.device.name}</b>")
        self.name_label.setStyleSheet("font-size: 16px;")

        self.type_label = QLabel(f"{self.tr('Type')}: {self.device.type}")
        self.status_label = QLabel(f"{self.tr('Status')}: {self.device.status}")

        # In the future, we will add a timer and cost label here.

        # --- Add widgets to the layout ---
        layout.addWidget(self.name_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.type_label)
        layout.addWidget(self.status_label)

        # --- Apply Initial Style ---
        self._update_style()

    def _update_style(self):
        """
        Sets the background color of the card based on the device status.
        """
        status = self.device.status
        color = STATUS_COLORS.get(status, STATUS_COLORS["default"])

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border: 1px solid #777;
                border-radius: 8px;
                color: white;
            }}
            QLabel {{
                background-color: transparent; /* Labels should not have their own background */
                border: none;
                font-size: 14px;
                padding: 2px;
            }}
        """)
