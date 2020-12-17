from app.lib.authenticate import authenticate_user

from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("/user/_authenticate", tags=["user"])
async def authenticate(token: bool = Depends(authenticate_user)):
    return token
