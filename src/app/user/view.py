from app.lib.authenticate import authenticate_user
from app.lib.authorize import authorize_user

from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("/user/_authenticate", tags=["user"])
async def authenticate(token: str = Depends(authenticate_user)):
    return token


@router.get("/user", tags=["user"])
async def authorize(user: bool = Depends(authorize_user)):
    return user
