from .CoffeeModel import Coffee, CoffeeView, SQLModel
from sqlmodel import create_engine

sqllite_db_name = "coffee.db"
sqlite_url = f"sqlite:///{sqllite_db_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

__all__ = ["engine", "Coffe", "CoffeeView"]