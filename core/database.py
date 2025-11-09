import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the path for the database file
DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'gaming_cafe.db')
DATABASE_URL = f"sqlite:///{DB_FILE}"

# The Engine is the core interface to the database.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# A SessionLocal class is a factory for creating new database sessions.
# A session is like a temporary "workspace" for all your database interactions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is a special class that all of our ORM model classes will inherit from.
# SQLAlchemy uses it to map our classes to the database tables.
Base = declarative_base()

def create_db_and_tables():
    """
    Creates the database file and all tables defined by classes inheriting from Base.
    """
    # This command connects to the database and creates all tables.
    # It checks for the existence of tables first, so it's safe to run multiple times.
    Base.metadata.create_all(bind=engine)
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_db_and_tables()
