from sqlalchemy import VARCHAR, Column, Integer

from .database import Base


class ProductTable(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(VARCHAR(50))
    name = Column(VARCHAR(50))
    address = Column(VARCHAR(50))
    result = Column(VARCHAR(50))


class TempTable(Base):
    __tablename__ = "temp"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(VARCHAR(50))
    name = Column(VARCHAR(50))
    address = Column(VARCHAR(50))
    result = Column(VARCHAR(50))
