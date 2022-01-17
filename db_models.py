from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, Column, Integer, \
    String, ForeignKey, JSON, Float


"""----------table definition---------"""


class users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    city = Column(String(50), nullable= False )

    def __init__(self, full_name,email,city):
        self.full_name = full_name
        self.email = email
        self.city = city
