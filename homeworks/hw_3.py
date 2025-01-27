
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///hw_3.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(5,2), nullable=False),
    in_stock = Column(Boolean, nullable=False, default=True),
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

class Category(Base):
    __tablename__ = 'category',
    id = Column(Integer, primary_key=True, nullable=False),
    name = Column(String(100), nullable=False),
    description = Column(String(255), nullable=False)