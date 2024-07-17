from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    student_id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    birth_day = Column(String, index=True)
    age = Column(Integer, index=True)
    sex = Column(String, index=True)
    
