from fastapi import APIRouter, HTTPException
from src.models import Coffee, CoffeeCreate, CoffeeUpdate, CoffeeView,engine
from sqlmodel import Session, select
from src.loggers import coffee_logger, program_logger
router = APIRouter(prefix="/coffee")


@router.get(path="/", response_model=list[CoffeeView])
async def get_coffes() -> list[CoffeeView]:
    with Session(engine) as session:
        program_logger.info("Fetching all coffee entries.")
        statement = select(Coffee)
        coffees = session.exec(statement)
        return coffees.all()

@router.post(path="/", response_model=CoffeeView)
async def create_coffee(coffee: CoffeeCreate):
    program_logger.info("Creating a new coffee entry.")
    with Session(engine) as session:
        new_coffee: Coffee = Coffee.model_validate(coffee)
        session.add(new_coffee)
        session.commit()
        session.refresh(new_coffee)
        coffee_logger.info(f"{new_coffee.type.value}")
        program_logger.info(f'Created new coffee with ID: {new_coffee.id}')
        return new_coffee

@router.put("/{coffee_id}", response_model=CoffeeView)
async def update_coffee(coffee_id:int, coffee: CoffeeUpdate):
    program_logger.info(f"Updating Coffee with ID: {coffee_id}")
    with Session(engine) as session:
        coffee_db = session.get(Coffee, coffee_id)
        if not coffee_db:
            program_logger.error(f"No coffee found with ID: {coffee_id}")
            raise HTTPException(status_code=404, detail=f"No coffee with id {coffee_id}")
        coffee_data = coffee.model_dump(exclude_unset=True)
        coffee_db.sqlmodel_update(coffee_data)
        session.add(coffee_db)
        session.commit()
        session.refresh(coffee_db)
        program_logger.info(f"Coffee updated with ID: {coffee_id}")
        return coffee_db

@router.delete(path="/{coffee_id}", response_model=CoffeeView)
def delete_coffee(coffee_id:int):
    program_logger.info(f"Deleting coffee entry with ID: {coffee_id}")
    with Session(engine) as session:
        coffee_db = session.get(Coffee, coffee_id)
        if not coffee_db:
            program_logger.error(f"No coffee found with ID: {coffee_id}")
            raise HTTPException(status_code=404, detail=f"No coffee with id {coffee_id}")
        session.delete(coffee_db)
        session.commit()
        program_logger.info(f"Coffee deleted with ID: {coffee_id}")
        return coffee_db