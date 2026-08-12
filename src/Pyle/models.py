import datetime

from sqlalchemy import (DateTime, Float, Integer, String, Text)
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column)

# Starting with ORM Annotated Declarative style

class Base(DeclarativeBase):
    pass

'''
Model for vehicle data
'''
class Vehicle(Base):
    __tablename__ = 'vehicles'

    vehicle_name: Mapped[str] = mapped_column(String(64), primary_key=True)
    vehicle_make = Mapped[str] = mapped_column(String(32), nullable=True)
    vehicle_model = Mapped[str] = mapped_column(String(32, nullable=True))
    vin: Mapped[str] = mapped_column(String(32, nullable=True))
    mileage: Mapped[float] = mapped_column(Float(precision=9, scale=1), nullable=True)

'''
Model for Record
'''
class Record(Base):
    __tablename__ = 'maintenance'

    vehicle_name: Mapped[str] = mapped_column(String(64), primary_key=True)
    date: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.now)
    technician: Mapped[str] = mapped_column(String(64), nullable=False)
    service_name: Mapped[str] = mapped_column(String(128), nullable=False)
    service_notes: Mapped[str] = mapped_column(Text, nullable=True)
    # NOTE Will likely replace this with a list of strings to document multiple parts used in one record
    replacement_part: Mapped[str] = mapped_column(Text, nullable=True)
    lifespan_miles: Mapped[int] = mapped_column(Integer, nullable=True)
    lifespan_months: Mapped[int] = mapped_column(Integer, nullable=True)