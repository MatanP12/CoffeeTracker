from fastapi import APIRouter
from src.models import Coffee, CoffeeCreate, CoffeeView,engine
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