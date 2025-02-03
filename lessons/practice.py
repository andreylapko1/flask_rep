from pydantic import BaseModel, field_validator, ValidationError, EmailStr, Field
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey,Text


class Event(BaseModel):
    title: str
    date: datetime
    location: str

    @field_validator('date')
    def data_validation(cls, value):
        if value < datetime.now():
            raise ValidationError('Date must be in the future')
        return value


a = Event(title='Birthday', date='2025-10-05', location='Chicago')
print(a)


class UserProfile(BaseModel):
    username: str = Field(..., title='Username')
    password: str = Field(..., min_length=8, description='Email min length 8')
    email: EmailStr = Field(..., title='Email')



user = UserProfile(
    username='username',
    password='password',
    email='email@gmail.com',
)
print(user)




Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

user_alchemy = User(name='Andrey', age=99)
print(user_alchemy)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship('User1', back_populates='post')
    title = Column(Text, nullable=False)
















