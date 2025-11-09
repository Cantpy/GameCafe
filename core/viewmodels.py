# core/viewmodels.py

"""
Defines the ViewModel classes for the gaming cafe management application.
These classes manage the state and business logic, acting as an intermediary
between the Views (UI) and the Models (data).
"""

from PySide6.QtCore import QObject, Signal
from core.database import SessionLocal
from core.models import Device


class DashboardViewModel(QObject):
    """
    Manages the state and business logic for the main dashboard.
    """
    # Signal that emits the list of devices whenever it's updated.
    # The UI (View) will connect a function to this signal.
    devices_changed = Signal(list)

    def __init__(self):
        super().__init__()
        self._devices = []

    def load_devices(self):
        """
        Loads all devices from the database and emits the devices_changed signal.
        """
        db = SessionLocal()
        try:
            # Query the database for all devices, order them by name
            self._devices = db.query(Device).order_by(Device.name).all()
            # Emit the signal with the fresh list of devices
            self.devices_changed.emit(self._devices)
        finally:
            db.close()
