from fastapi import FastAPI
from .database import Database
from .routers import auth


app = FastAPI()


db = Database()


app.include_router(auth.router)