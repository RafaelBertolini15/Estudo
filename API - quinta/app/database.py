from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BANCO_URL = "sqlite:///./banco.db"

engine = create_engine(BANCO_URL)
sessaoLocal = sessionmaker(bind=engine)
Base = declarative_base()