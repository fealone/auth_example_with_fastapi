from app.lib.database import SessionLocal, engine
from app.settings import JWKS, PRIVATE_PEM, TOKEN_EXPIRE
from app.user import crud, models

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import (
        HTTPBasic,
        HTTPBasicCredentials)

import jwt

from sqlalchemy.orm import Session


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
    user = crud.authenticate_user(db,
                                  credentials.username,
                                  credentials.password)
    if user:
        payload = {
            "exp": TOKEN_EXPIRE,
            "email": user.email,
            "user": user.name
        }
        token = jwt.encode(payload,
                           PRIVATE_PEM,
                           algorithm=JWKS["keys"][0]["alg"],
                           headers={"kid": JWKS["keys"][0]["kid"]})

        return {"access_token": token}
    else:
        raise HTTPException(
                status_code=401,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"})
