from app import app
from models import db, DeliSandwich, Pizza
from faker import Faker
from random import choice as random_choice

faker = Faker()

sandwich_names = ["Italian", "Chopped Cheese", "Bacon Egg & Cheese", "BLT", "Tasty Sandwich", "Not Tasty Sandwich", "Quality Lettuce Sandwich", "Next Sandwich", "Sandwich Sixty", 'lower case sandwich name']

if __name__ == '__main__': # ignored if used in other files
    with app.app_context():

        print("Seeding database...")

        # delete previous data
        DeliSandwich.query.delete()

        # create sandwiches
        sandwich_instances = [ DeliSandwich(
            name=sn, 
            toasted=random_choice( [True, False] ), 
            price=random_choice( range(2, 20) ), 
            ingredients="quality ingredients", 
            is_kosher=random_choice( [True, False] )) 
            for sn in sandwich_names ]

        db.session.add_all( sandwich_instances )
        db.session.commit()

        # delete previous pizzas
        Pizza.query.delete()

        for _ in range(100):
            new_pizza = Pizza( name=faker.name() )
            db.session.add( new_pizza )

        db.session.commit()

        print("Seeding complete!")
