from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base  # Import the Base from our database.py file


class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)
    hourly_rate = Column(Float, nullable=False)
    status = Column(String, default='Available')

    sessions = relationship("Session", back_populates="device")


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, index=True)
    join_date = Column(DateTime(timezone=True), server_default=func.now())
    loyalty_points = Column(Integer, default=0)

    sessions = relationship("Session", back_populates="customer")


class CafeteriaItem(Base):
    __tablename__ = 'cafeteria_items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)


class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    session_cost = Column(Float, nullable=True)
    total_cost = Column(Float, nullable=True)
    payment_status = Column(String, default='Unpaid')

    device = relationship("Device", back_populates="sessions")
    customer = relationship("Customer", back_populates="sessions")
    orders = relationship("SessionOrder", back_populates="session")


class SessionOrder(Base):
    __tablename__ = 'session_orders'
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('sessions.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('cafeteria_items.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    order_time = Column(DateTime(timezone=True), server_default=func.now())
    price_per_item = Column(Float, nullable=False)

    session = relationship("Session", back_populates="orders")
    item = relationship("CafeteriaItem")
