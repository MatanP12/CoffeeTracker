from .CoffeeModel import Coffee,CoffeeCreate, CoffeeView, CoffeeUpdate ,SQLModel
from sqlmodel import create_engine
import os
sql_connection_string = os.environ.get("DATABASE_CONNECTION_STRING","sqlite:///coffee.db") 

engine = create_engine(sql_connection_string, echo=True)

SQLModel.metadata.create_all(engine)
