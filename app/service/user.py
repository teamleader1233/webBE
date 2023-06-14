import re
import random
import string
from hashlib import sha512
from uuid import uuid4

from ..param.auth import UserParam
from ..model.user import User
from ..model.token import Token
from ..database import Database


EMAIL_REGEX = "^[A-Za-z0-9!#$%&'*+-\/=?^_`{|}~]+@[a-z0-9.]+$"
INVALID_NAME_CHARACTERS = ("'", '"', "<", ">")


def get_user_from_uuid(uuid: str, db: Database):
    attrs = db.fetch("SELECT * FROM User WHERE uuid=%s;", (uuid,))
    if not attrs:
        return None
    
    return User(*attrs)


def get_user_from_email(email: str, db: Database):
    attrs = db.fetch("SELECT * FROM User WHERE email=%s;", (email,))
    if not attrs:
        return None

    return User(*attrs)


def get_user_from_token(uuid: str):
    assert isinstance(uuid, str)
    return get_user_from_uuid(uuid)


def get_user_from_credentials(email: str, password: str, db: Database):
    attrs = db.fetch("SELECT * FROM User WHERE email=%s AND password=%s;", (email, password))
    if not attrs:
        return None
    return User(*attrs)


def create_user(user: UserParam, db: Database):
    password = sha512(user.password.encode('utf-8')).hexdigest()
    uuid = uuid4()
    user = User(uuid=uuid, email=user.email, password=user.password)

    db.insert(
        "INSERT INTO User (email, password, uuid, name, is_verified, is_active) VALUES (%s, %s, %s, %s, %s, %s);",
        (user.email, user.password, user.uuid, user.name, user.is_verified, user.is_active)
    )


def verify_user(uuid: str, db: Database):
    assert isinstance(uuid, str)
    db.insert("UPDATE User SET is_verified=%s WHERE uuid=%s;", (True, uuid))
    

def validate_username(username: str):
    assert isinstance(username, str)
    if any(char in username for char in INVALID_NAME_CHARACTERS):
        raise Exception("Tên không được chứa kí không hợp lệ")
    

def validate_email(email: str, db: Database):
    assert isinstance(email, str)
    assert isinstance(db, Database)
    
    if re.search(EMAIL_REGEX, email):
        raise Exception("Email không hợp lệ")

    if db.get_user_from_email(email):
        raise Exception("Email đã được đăng ký")


def validate_password(password: str):
    assert isinstance(password, str)
    if len(password) < 8:
        raise Exception("Mật khẩu phải chứa từ 8 kí tự trở lên")

    if (
        not any(char in password for char in string.ascii_lowercase)
        or not any(char in password for char in string.ascii_uppercase)
        or not any(char in password for char in string.digits)
        or not any(char in password for char in string.punctuation)
        ):
        raise Exception("Mật khẩu không hợp lệ")