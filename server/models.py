from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# the metadata here creates foreign key naming conventions in the database
# you generally won't have to set this up
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# this sets up the database connection
db = SQLAlchemy(metadata=metadata)

# this will eventually become our Deli model
class DeliSandwich(db.Model):
    
    __tablename__ = "deli_sandwiches_table"

    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String )
    toasted = db.Column( db.Boolean )
    ingredients = db.Column( db.String )
    price = db.Column( db.Float )
    is_kosher = db.Column( db.Boolean )


class Pizza(db.Model):

    __tablename__ = "pizzas_table"

    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String )
    size_in_inches = db.Column( db.Integer )
    crust = db.Column( db.String )
    meta_pizza = db.Column( db.Boolean )