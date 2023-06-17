from fastapi import APIRouter, HTTPException, Depends, status

from sqlalchemy.orm import Session

from ...models.db import get_db, engine
from ...models.user import (
    schemas as userSchema, 
    crud as userCrud, 
    models as userModel
)
from ...modules import validation as valid

import re


userModel.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix='/auth'
)


@router.post("/register", response_model=userSchema.User, status_code=201)
def register(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    try:
        valid.validate_name(user.first_name)
        valid.validate_name(user.last_name)
        valid.validate_email(user.email)
        valid.validate_password(user.password)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"status": 0, "detail": str(e)},
        )
    return userCrud.create_user(db=db, user=user)