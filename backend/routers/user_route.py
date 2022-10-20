from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import get_db

router = APIRouter()


@router.get("/all")
def get_all_users(db:Session = Depends(get_db)):
    return {'message':'Hello world!!'}