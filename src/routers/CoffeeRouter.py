from fastapi import APIRouter, HTTPException
from src.models import Coffee, CoffeeCreate, CoffeeUpdate, CoffeeView,engine
from sqlmodel import Session, select
router = APIRouter(prefix="/coffee")

@router.get(path="/", response_model=list[CoffeeView])
async def get_coffes() -> list[CoffeeView]:
    with Session(engine) as session:
        statement = select(Coffee)
        coffees = session.exec(statement)
        return coffees.all()

@router.post(path="/", response_model=CoffeeView)
async def create_coffee(coffee: CoffeeCreate):
    with Session(engine) as session:
        new_coffee = Coffee.model_validate(coffee)
        session.add(new_coffee)
        session.commit()
        session.refresh(new_coffee)
        return new_coffee

@router.put("/{coffee_id}", response_model=CoffeeView)
async def update_coffee(coffee_id:int, coffee: CoffeeUpdate):
    with Session(engine) as session:
        coffee_db = session.get(Coffee, coffee_id)
        if not coffee_db:
            raise HTTPException(status_code=404, detail=f"No coffee with id {coffee_id}")
        coffee_data = coffee.model_dump(exclude_unset=True)
        coffee_db.sqlmodel_update(coffee_data)
        session.add(coffee_db)
        session.commit()
        session.refresh(coffee_db)
        return coffee_db

@router.delete(path="/{coffee_id}", response_model=CoffeeView)
def delete_coffee(coffee_id:int):
    with Session(engine) as session:
        coffee_db = session.get(Coffee, coffee_id)
        if not coffee_db:
            raise HTTPException(status_code=404, detail=f"No coffee with id {coffee_id}")
        session.delete(coffee_db)
        session.commit()
        return coffee_db