from typing import Annotated
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from ...models.db import engine, get_db
from ...models.user import (
    schemas as userSchema, 
    crud as userCrud, 
    models as userModel
)
from ...models.token import (
    schemas as tokenSchema,
    crud as tokenCrud
)
from ...modules import validation as valid

import re


userModel.Base.metadata.create_all(bind=engine)


router = APIRouter()


@router.post("/login", response_model=tokenSchema.Token, status_code=201)
def login(
    data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    email = data.username
    password = data.password
    try:
        valid.validate_email(email)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email!"
        )
    user = userCrud.authenticate_user(db=db, email=email, password=password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=tokenCrud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = tokenCrud.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}