from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

SQLALCHEMY_DATABASE_URL = Config.DB_STRING

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
