from sqlalchemy import Column, Integer, String
from app.database import Base

class modelo(Base):
    __tablename__ = "banco"
    id = Column(Integer, primary_key=True)
    grupo = Column(String)
    mandante = Column(String)
    visitante = Column(String)
    estadio = Column(String)
    data = Column(String)
    status = Column(String)
