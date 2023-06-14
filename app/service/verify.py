from datetime import datetime, timedelta
from ..config import settings
from ..model.token import Token
from ..service.token import generate_token, save_token, secret_exists
import secrets


TOKEN_TYPE = "verify_email"


def send_verify(uuid: str, email: str):
    assert isinstance(uuid, str)
    assert isinstance(email, str)
    token = generate_token(uuid, email, TOKEN_TYPE)
    link = create_link(token)


def create_link(token):
    return f"https://{settings.domain}/verify?token={token}"