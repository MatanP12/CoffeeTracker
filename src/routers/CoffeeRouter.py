from fastapi import APIRouter, HTTPException
from src.models import Coffee, CoffeeCreate, CoffeeUpdate, CoffeeView,engine
from sqlmodel import Session, select
import logging

router = APIRouter(prefix="/coffee")

# Create a logger for coffee creation
coffee_logger = logging.getLogger("coffee_creation")
coffee_logger.setLevel(logging.INFO)
coffee_handler = logging.FileHandler("logs/coffee_creation.log")  # Log file for coffee creation
coffee_handler.setFormatter(logging.Formatter('%(message)s'))
coffee_logger.addHandler(coffee_handler)

@router.get(path="/", response_model=list[CoffeeView])
async def get_coffes() -> list[CoffeeView]:
    with Session(engine) as session:
        logging.info("Fetching all coffee entries.")
        statement = select(Coffee)
        coffees = session.exec(statement)
        return coffees.all()

@router.post(path="/", response_model=CoffeeView)
async def create_coffee(coffee: CoffeeCreate):
    logging.info("Creating a new coffee entry.")
    with Session(engine) as session:
        new_coffee: Coffee = Coffee.model_validate(coffee)
        session.add(new_coffee)
        session.commit()
        session.refresh(new_coffee)
        coffee_logger.info(f"[{new_coffee.type.value}] [{new_coffee.creation_time.date().strftime('%d-%m-%Y')}] [{new_coffee.creation_time.time().strftime('%H:%M')}]")
        logging.info(f'Created new coffee with ID: {new_coffee.id}')
        return new_coffee

@router.put("/{coffee_id}", response_model=CoffeeView)
async def update_coffee(coffee_id:int, coffee: CoffeeUpdate):
    with Session(engine) as session:
        coffee_db = session.get(Coffee, coffee_id)
        if not coffee_db:
            logging.error(f"No coffee found with ID: {coffee_id}")
            raise HTTPException(status_code=404, detail=f"No coffee with id {coffee_id}")
        coffee_data = coffee.model_dump(exclude_unset=True)
        coffee_db.sqlmodel_update(coffee_data)
        session.add(coffee_db)
        session.commit()
        session.refresh(coffee_db)
        logging.info(f"Coffee updated with ID: {coffee_id}")
        return coffee_db

@router.delete(path="/{coffee_id}", response_model=CoffeeView)
def delete_coffee(coffee_id:int):
    logging.info(f"Deleting coffee entry with ID: {coffee_id}")
    with Session(engine) as session:
        coffee_db = session.get(Coffee, coffee_id)
        if not coffee_db:
            logging.error(f"No coffee found with ID: {coffee_id}")
            raise HTTPException(status_code=404, detail=f"No coffee with id {coffee_id}")
        session.delete(coffee_db)
        session.commit()
        logging.info(f"Coffee deleted with ID: {coffee_id}")
        return coffee_db