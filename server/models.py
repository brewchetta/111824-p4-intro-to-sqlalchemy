from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# the metadata here creates naming convensions in the database
# in this case it handles foreign keys
# you generally won't have to set this up
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# this sets up the database connection
db = SQLAlchemy(metadata=metadata)

class Hamburger(???):
    pass

class Deli(???):
    pass