from fastapi import FastAPI
from .user import view as user

app = FastAPI()
app.include_router(user.router)
