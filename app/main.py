from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

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


client = TestClient(app)

def test_register():
    response = client.post(
        url='/api/auth/register',
        json={
            'first_name': 'SVN',
            'last_name': 'logistic',
            'email': 'svn@gmail.com',
            'password': 'Svn2023!'
        }
    )
    assert response.status_code == 201
    assert any(key in response.json().keys() for key in ['email', 'uuid', 'is_active', 'is_verified'])

def test_login():
    response = client.post(
        url='/api/auth/login',
        json={
            'username': 'svn@gmail.com',
            'password': 'Svn2023!'
        }
    )
    assert response.status_code == 201
    assert any(key in response.json().keys() for key in ['access_token', 'token_type'])