
from sqlalchemy import create_engine, Column, String, Integer,ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

engine = create_engine('sqlite:///lib/ignition.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind= engine)
session = Session()


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key = True)
    name =Column(String())
    email = Column(String())
    contact = Column(Integer())


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer(), primary_key = True)
    make =Column(String())
    model = Column(String())
    make_year = Column(Integer())
    license_plate = Column(String())



class Rental(Base):
    __tablename__ = 'car_rentals'  

    id= Column(Integer(), primary_key=True)
    customer_id =Column(Integer(), ForeignKey("cars.id"))
    customer_id = Column(Integer(), ForeignKey("customers.id"))
    rental_date = Column(DateTime)
    price = Column(Integer())
    return_date = Column(DateTime)
    