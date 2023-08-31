#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

# created base object
# from sqlalchemy.ext.declarative import declarative_base

#  seed.py
# initializes sessions maker for creating instances
#  needs creater_engine 
# session_maker
# session itself




