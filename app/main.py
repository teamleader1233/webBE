from fastapi import FastAPI, Depends

from .routers.auth import register, login
from .dependencies import get_query_token, get_token_header
from .models.db import db, engine
from .models.user import models as userModel


app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(
    register.router,
    prefix='/auth'
)
app.include_router(
    login.router,
    prefix='/auth'
)


# @app.on_event("startup")
# async def startup():
#     userModel.User.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {'msg': 'Welcome to SVN'}