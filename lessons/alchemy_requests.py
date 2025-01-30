import sqlite3
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Numeric
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.automap import automap_base, _declarative_base
# from datetime import datetime, timedelta
# from sqlalchemy import func
# from dotenv import load_dotenv
# import os
# load_dotenv()

# engine = create_engine(f'{os.getenv("str_read")}world')
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# Session = sessionmaker(bind=engine)


# Country = Base.classes.country
#
# with Session() as session:
#     employees = session.query(Country).having(Country.SurfaceArea > 5000000).all()
#     for a in employees:
#         print(a.Name + ':', a.SurfaceArea)




# Sqlite3






from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime, timedelta
from sqlalchemy.sql import func


Base = declarative_base()
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    orders = relationship("Order", back_populates="user")
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Numeric)
    created_at = Column(DateTime)
    user = relationship("User", back_populates="orders")
Base.metadata.create_all(engine)



user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=22)
session.add_all([user1, user2])
session.commit()


order1 = Order(user_id=user1.id, amount=100.50, created_at=datetime.now() - timedelta(days=1))
order2 = Order(user_id=user1.id, amount=200.75, created_at=datetime.now())
order3 = Order(user_id=user2.id, amount=80.99, created_at=datetime.now() - timedelta(days=2))
session.add_all([order1, order2, order3])
session.commit()


u = session.query(User).all()
for user in u:
    print(user.name)

countt = session.query(func.count(User.id)).scalar()
print(countt)


user = session.get(User, 1)
print(user.name)


