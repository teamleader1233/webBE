from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class VerifyToken(Token):
    token_type = 'verify'


class AuthToken(Token):
    token_type = 'auth'