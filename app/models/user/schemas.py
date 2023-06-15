from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    first_name: str
    last_name: str
    password: str


class UserLogin(UserBase):
    password: str


class User(UserBase):
    uuid: str
    is_active: bool = True
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str