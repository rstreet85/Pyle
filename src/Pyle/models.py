from sqlalchemy import Text
from sqlalchemy.orm import (declarative_base, relationship)

'''
Model for vehicle data
'''
Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'
    