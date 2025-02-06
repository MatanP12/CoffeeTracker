from sqlmodel import Field, SQLModel
from datetime import datetime
from .CoffeeType import CoffeeType

class CoffeBaseModel(SQLModel):
    type: CoffeeType
    creation_time : datetime

class Coffee(CoffeBaseModel, table=True):
    id: int | None = Field(default=None,primary_key=True)

class CoffeeView(CoffeBaseModel):
    id: int

class CoffeeCreate(CoffeBaseModel):
    pass

class CoffeeUpdate(CoffeBaseModel):
    type: CoffeeType | None = None
    creation_time: datetime | None = None