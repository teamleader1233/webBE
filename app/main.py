from fastapi import FastAPI, Depends

from .routers.auth import register, login
from .dependencies import get_query_token, get_token_header


app = FastAPI()
#dependencies=[Depends(get_query_token)]


app.include_router(
    register.router,
    prefix='/api'
)
app.include_router(
    login.router,
    prefix='/api'
)


@app.get("/")
async def root():
    return {'msg': 'Welcome to SVN'}