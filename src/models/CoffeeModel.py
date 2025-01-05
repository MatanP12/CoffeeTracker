from sqlmodel import Field, SQLModel
from datetime import datetime

class CoffeBaseModel(SQLModel):
    type: str
    creation_time : datetime = datetime.now()

class Coffee(CoffeBaseModel, table=True):
    id: int | None = Field(default=None,primary_key=True)

class CoffeeView(CoffeBaseModel):
    id: int

class CoffeeCreate(CoffeBaseModel):
    pass

class CoffeeUpdate(CoffeBaseModel):
    type: str | None = None
    creation_time: datetime | None = None