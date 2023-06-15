from sqlalchemy.orm import Session
from sqlalchemy import select, insert

from passlib.context import CryptContext
from uuid import uuid4

from . import models, schemas


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_uuid(db: Session, user_uuid: int):
    query = select(models.User).where(models.User.uuid == user_uuid)
    return db.execute(query).first()


def get_user_by_email(db: Session, email: str):
    query = select(models.User).where(models.User.email == email)
    return db.execute(query).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    uuid = uuid4()
    query = insert(models.User).values(
        first_name = user.first_name,
        last_name = user.last_name,
        email=user.email, 
        hashed_password=hashed_password,
        uuid=uuid
    )
    db.execute(query)
    db.commit()
    return schemas.User(
        email=user.email,
        uuid=uuid
    )


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user is None or not pwd_context.verify(password, user.hashed_password):
        return False
    return user[0]