from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi.security import (
        HTTPBasic,
        HTTPBasicCredentials)

from app.user import crud, models
from app.lib.database import SessionLocal, engine

router = APIRouter()

security = HTTPBasic()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def authenticate_user(
        db: Session = Depends(get_db),
        credentials: HTTPBasicCredentials = Depends(security)):
    if crud.authenticate_user(db,
                              credentials.username,
                              credentials.password):
        return True
    else:
        raise HTTPException(
                status_code=401,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"})
