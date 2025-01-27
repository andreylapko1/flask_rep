from sqlalchemy import create_engine

from sqlalchemy import Table, Column, Integer, String,create_engine
from sqlalchemy.orm import registry


engine = create_engine('sqlite:///:memory:')
Register = registry()

user_table = Table('users', Register.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String),
                   Column('age', Integer))


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age



Register.map_imperatively(User, user_table)

Register.create_all(engine)
