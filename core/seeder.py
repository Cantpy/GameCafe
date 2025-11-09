# core/seeder.py

"""
Seeds the database with initial data for devices if the database is empty.
"""

from core.database import SessionLocal
from core.models import Device


def seed_initial_data():
    """Adds some initial devices to the database if it's empty."""
    db = SessionLocal()

    # Check if there are any devices already
    if db.query(Device).count() == 0:
        print("Database is empty. Seeding initial device data...")

        # Sample Data
        devices_to_add = [
            Device(name="کامپیوتر ۱", type="کامپیوتر آنلاین", hourly_rate=50000),
            Device(name="کامپیوتر ۲", type="کامپیوتر آنلاین", hourly_rate=50000),
            Device(name="کامپیوتر ۳", type="کامپیوتر آفلاین", hourly_rate=35000, status="در حال استفاده"),
            Device(name="کامپیوتر ۴", type="کامپیوتر آفلاین", hourly_rate=35000),
            Device(name="پلی استیشن - تلویزیون ۱", type="کنسول", hourly_rate=80000),
            Device(name="ایکس باکس - تلویزیون ۲", type="کنسول", hourly_rate=70000),
            Device(name="اسنوکر", type="بازی میزی", hourly_rate=100000, status="نیازمند توجه"),
            Device(name="پینگ پنگ", type="بازی میزی", hourly_rate=50000),
        ]

        db.add_all(devices_to_add)
        db.commit()
        print("Initial data seeded.")
    else:
        print("Database already contains data. Skipping seed.")

    db.close()
