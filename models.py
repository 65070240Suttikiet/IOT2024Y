from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import DateTime

class Student(Base):
    __tablename__ = 'students'
    
    student_id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    birth_day = Column(String, index=True)
    age = Column(Integer, index=True)
    sex = Column(String, index=True)
    
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    details = Column(String, index=True)
    short_details = Column(String, index=True)
    genre = Column(String, index=True)

class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, index=True)
    des = Column(String, index=True)
    price = Column(Integer, index=True)
    available = Column(Boolean, index=True)
    
class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    order_date = Column(DateTime, index=True)
    amount = Column(Integer, index=True)
    total_price = Column(Integer, index=True)
    notes = Column(String, index=True)