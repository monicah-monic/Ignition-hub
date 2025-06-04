from faker import Faker 
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Car, Base

fake = Faker()


engine = create_engine('sqlite:///lib/ignition.db')
Session = sessionmaker(bind=engine)
session = Session()


session.query(Car).delete()

car_makes =['Toyota', 'Honda','Hyundai', 'Mitsubishi', 'Subaru', 'Mercedes', 'Mazda', 'Volkswagen']
car_models = ['Fit', 'Vitz', 'Outlander', 'Forester', 'GLE', 'Pajero', 'V8', 'Mark-x', 'Harrier','Touareg']



cars = [
    Car(
        make=random.choice(car_makes),
        model=random.choice(car_models),    
        make_year=random.randint(2010, 2024),
        license_plate=fake.license_plate() 
    )
    for _ in range(10)
]


session.add_all(cars)
session.commit()

