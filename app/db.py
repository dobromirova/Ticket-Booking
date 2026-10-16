from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Database URL
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg://postgres:pass@localhost:5433/pytickets"
)

# Create database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
class Base(DeclarativeBase):
    pass


# Dependency for database sessions (e.g., FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()