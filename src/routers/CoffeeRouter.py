from fastapi import APIRouter
from src.models import Coffee, CoffeeView, engine
from sqlmodel import Session
router = APIRouter(prefix="/coffee")

@router.get("/")
async def get_coffes():
    with Session(engine) as session:
        