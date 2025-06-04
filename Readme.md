## Ignition-hub
A CLI application built with python and sqlalchremy ORM that allows users to manage a car hire database i.e manage customers, cars, and rentals in a car hire business using a simple terminal interface.

# Structure
ignition hub
  |
  |__
    lib
      |
      |
      |___
         cli.py
         ignition.db
         main.py
         models.py
         seed.py

# Feature
.Customer managment
    .Create new customers
    .View all customers
    .View a particular customer by Id
    .Update customer details
    .Delete a customer from db
.Car managment
    .Add new cars
    .View all cars
    .Update car information
    .Delete cars
.Car rental managment
    .Add a new hire(links a customer and a car)
    .View all rentals
    .Update rental information
    .Delete rental upon return of vehicle

# Technologies used
 Python
 SQLAlchemy ORM
 Alembic migrations
 Datetime module (for handling rental and return dates)

# Database models
Customer:
   Fields:id, name, email, contact
   Relationship: many to many with cars, one to many with rentals
Car:  
   Fields:id, make, model, make-year, license-plate
   Relationship: many to many with customers, one to many with rentals
Car-rental:
   Fields:id, car_id, customer_id, rental_date, return_date, price
   Relationship: join table, belongs to both customer and car

# How to run   
cd Ignition-hub
set up virtual environment: pipenv install, pipenv shell
Install dependencies: pip install sqlalchemy, pip install faker
Initialize database  and  create it :alembic revision --autogenerate -m "create db", alembic upgrade head
Run application: python lib/cli.py


