from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Customer, Car, Rental

engine = create_engine('sqlite:///lib/ignition.db')
# Base.metadata.create_all(engine)

Session = sessionmaker(bind= engine)
session = Session()

# customer model
def create_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email:")
    contact = int(input("Enter customer contact:"))

    customer = Customer(name= name, email= email, contact= contact)
    session.add(customer)
    session.commit()

    print(name, "added successfully!")

def fetch_customers():
    customers = session.query(Customer).all()
    for customer in customers: 
        print(f"Name: {customer.name}, Email: {customer.email},Contact: {customer.contact}") 

def fetch_customer_by_id():
    customer_id = input("Enter customer id:") 
    customer = session.query(Customer).get(customer_id)
    if customer:
        print(f"Name: {customer.name} Email: {customer.email} Contact:{customer.contact}")
    else:
        print("Customer not found!")  

def update_customer():
    customer_id = input("Enter customer id:") 
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        name = input("Enter new customer name: ")
        email = input("Enter new email address: ")
        contact = input("Enter new customer contact: ")
        customer.name = name
        customer.email = email
        customer.contact = contact
        session.commit()
        print("Customer updated successfully!")
    else:
        print("Customer not found!")  

def delete_customer():
    customer_id = input("Enter customer id: ")
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
        print("Customer deleted succesfully")
    else:
        print("Customer not found!")    
        
#car model
def create_car():
    make = input("Enter car make: ")
    model = input("Enter car model:")
    make_year = int(input("Enter car make year:"))
    license_plate = input("Enter license number:")

    car = Car(make= make, model= model, make_year= make_year, license_plate =license_plate )
    session.add(car)
    session.commit()

    print(make, "added successfully!")

def fetch_cars():
    cars = session.query(Car).all()
    for car in cars: 
        print(f"Make: {car.make}, Model: {car.model},Year: {car.make_year}, Plate: {car.license_plate}") 

def fetch_car_by_id():
    car_id = input("Enter car id:") 
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        print(f"Make: {car.make} Model: {car.model} Year:{car.make_year} Plate: {car.license_plate}")
    else:
        print("Car not found!")  

def update_car():
    car_id = input("Enter car id:") 
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        make = input("Enter new car make: ")
        model = input("Enter new car model: ")
        make_year = input("Enter new make year: ")
        license_plate = input("Enter new plate: ")
        car.make = make
        car.model = model
        car.make_year = make_year
        car.license_plate =license_plate
        session.commit()
        print("Car updated successfully!")
    else:
        print("Car not found!")  

def delete_car():
    car_id = input("Enter car id")
    car = session.query(Car).get(car_id)
    if car:
        session.delete(car)
        session.commit()
        print("Car deleted succesfully")
    else:
        print("Car not found!")

#rental model
def create_car_rental():
    car_id = input("Enter car id: ")
    customer_id= input("Enter customer Id:")
    price = int(input("Enter Amount:"))
    hire_date = input("Enter hire date(YYYY/MM/DD) or none :")
    date_return = input("Enter return date(YYYY/MM/DD) or none :")
    rental_date = datetime.strptime(hire_date, "%Y/%m/%d") if hire_date else None
    return_date= datetime.strptime(date_return, "%Y/%m/%d") if date_return else None
    
    car = session.query(Car).filter_by(id= car_id).first()
    customer = session.query(Customer).filter_by(id= customer_id).first()
    if car and customer:
        car_rental = Rental(car_id= car_id,customer_id=customer_id, price=price, rental_date= rental_date, return_date= return_date)
        session.add(car_rental)
        session.commit()
        print(f"Car id {car.id},{car.license_plate} has been hired by customer id: {customer.id}")
    else:
        print("Car or customer not found")    
  

def fetch_car_rentals():
    car_rentals = session.query(Rental).all()
    for car_rental in car_rentals: 
        print(f"Price: {car_rental.price}, car: {car_rental.car.make}, Customer: {car_rental.customer.name} Hire-date: {car_rental.rental_date}, Return: {car_rental.return_date}") 

def fetch_car_rental_by_id():
    car_rental_id = input("Enter rental id:") 
    car_rental = session.query(Rental).filter_by(id=car_rental_id).first()
    if car_rental:
        print(f"Price: {car_rental.price}, car: {car_rental.car.make}, Customer: {car_rental.customer.name} Hire-date: {car_rental.rental_date}, Return: {car_rental.return_date}") 
    else:
        print("Car not hired!")  

def update_car_rental():
    car_rental_id = input("Enter car rental id:") 
    car_rental = session.query(Rental).filter_by(id=car_rental_id).first()
    if car_rental:
        car_id = input("Enter new car rental id: ")
        customer_id= input("Enter customer  Id:")
        price = int(input("Enter new amount:"))
        hire_date = input("Enter hire date(YYYY/MM/DD) or none :")
        date_return = input("Enter return date(YYYY/MM/DD) or none :")
        rental_date = datetime.strptime(hire_date, "%Y/%m/%d") if hire_date else None
        return_date= datetime.strptime(date_return, "%Y/%m/%d") if date_return else None
    
        car_rental.car_id= car_id
        car_rental.customer_id = customer_id
        car_rental.price = price
        car_rental.rental_date= rental_date
        car_rental.return_date = return_date
        session.commit()
        print("Car rented updated successfully!")
    else:
        print("Car not found!")  

def delete_car_rental():
    car_rental_id = input("Enter rental id:")
    car_rental = session.query(Rental).get(car_rental_id)
    if car_rental:
        session.delete(car_rental)
        session.commit()
        print("Car hired deleted succesfully")
    else:
        print("Car not hired!")

