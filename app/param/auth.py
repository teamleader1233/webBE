from pydantic import BaseModel


class UserParam(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class LoginParam(BaseModel):
    email: str
    password: str