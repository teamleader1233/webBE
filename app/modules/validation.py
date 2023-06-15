from sqlalchemy.orm import Session

from ..models.user import crud

import re


INVALID_NAME_CHARACTERS = ("'", '"', "<", ">")
EMAIL_REGEX = "^[A-Za-z0-9!#$%&'*+-\/=?^_`{|}~]+@[a-z0-9.]+$"


def validate_name(name: str):
    assert name is str, "Non-string value found!"
    if any(char in name for char in INVALID_NAME_CHARACTERS):
        raise ValueError("Invalid character(s) found!")
    

def validate_email(email: str, db: Session):
    assert email is str, "Non-string value found!"
    assert db is Session, "Not a database!"
    
    if re.search(EMAIL_REGEX, email):
        raise ValueError("Not an email!")

    if crud.get_user_by_email(db, email) is not None:
        raise ValueError("Email has already been used!")
    

def validate_password(password: str):
    assert isinstance(password, str)
    if len(password) < 8:
        raise Exception("Password must be at least 8 characters!")

    uppercase, lowercase, special_char, digit = False, False, False, False

    for char in password:
        if char.isupper():
            uppercase = True
        if char.islower():
            lowercase = True
        if not char.isalnum():
            special_char = True
        if char.isdigit():
            digit = True

    msg = "Password must contains at least one {} character!"
    
    if not uppercase:
        raise ValueError(msg.format("uppercase"))
    if not lowercase:
        raise ValueError(msg.format("lowercase"))
    if not special_char:
        raise ValueError(msg.format("special"))
    if not digit:
        raise ValueError(msg.format("digit"))