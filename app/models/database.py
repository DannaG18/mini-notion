import logging
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=False 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@contextmanager
def get_db() -> Generator[Session, None, None]:
    """
    Provide a transactional scope around a series of operations.
    
    Yields a database session and handles committing or rolling back 
    the transaction as appropriate.
    
    Raises:
        Exception: If an error occurs during the database transaction
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Database transaction error: {e}")
        raise
    finally:
        db.close()

def init_db() -> None:
    """
    Initialize the database by creating all tables defined in the models.
    """
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise