from faker import Faker 
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Car
fake = Faker()

# if __name__ == '__main__':
    
engine = create_engine('sqlite:///ignition.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Car).delete() #clears existing data
 

cars = [
    Car(
        make = fake.make(),
        model = fake.model(),
        make_year = fake.make_year(),
        license = fake.license()
    )
    for i in range(10)
]
session.add_all(cars)
session.commit()