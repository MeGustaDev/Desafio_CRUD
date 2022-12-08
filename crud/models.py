from sqlalchemy import Column, Integer, String
from database import Base

#Classes do do sqlAlchemy: Column, Inteber, String

class Cliente(Base):
    __tablename__ = "cliente"

    id: int = Column(Integer, primary_key="True", index=True)
    nome: str = Column(String(100))