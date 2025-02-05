from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func


Base = declarative_base()
engine = create_engine('sqlite:///memory')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship('Address', back_populates='user')



class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String)
    user = relationship('User', back_populates='addresses')


Base.metadata.create_all(engine)




with Session() as session:
    user1 = User(name='Charlie', age=22)
    user2 = User(name='Jasdn', age=12)
    user3 = User(name='Alice', age=30)
    user4 = User(name='Bob', age=25)
    user5 = User(name='Eve', age=28)
    user6 = User(name='Mallory', age=35)
    user7 = User(name='Oscar', age=19)
    user8 = User(name='Trent', age=40)
    session.add_all([user1, user2, user3, user4, user5, user6, user7, user8])
    session.commit()

    # user = session.query(User).filter(User.name == 'Charlie').first()
    #
    # session.delete(user)
    # session.commit()


    # exist = session.query(session.query(User).filter(User.name == 'Charlie').exists())
    # if exist:
    #     print('exist')
    #
    # avg = session.query(func.avg(User.age)).scalar()
    # print(avg)

    # maxmin = session.query(func.max(User.age), func.min(User.age)).first()
    # max_age, min_age = maxmin
    # print(max_age)
    # print(min_age)

    # group = session.query(User.age, func.count(User.id)).group_by(User.age).having(func.count(User.id) > 1).all()
    # for age, count in group:
    #     print(age, count)

    avg = session.query(func.avg(User.age).label('avg')).subquery()
    query = session.query(User).filter(User.age > avg.c.avg).all()

    # for user in query:
        # print(user.age)


    auery = session.query(User.name, Address.description).join(User.addresses).all()
    for user in auery:
        print(user.age)











