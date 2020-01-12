from fastapi import Depends
from fastapi import APIRouter
from app.lib.authenticate import authenticate_user

router = APIRouter()


@router.get("/user/helloworld", tags=["user"])
async def get_helloworld(is_auth: bool = Depends(authenticate_user)):
    return "HelloWorld"
