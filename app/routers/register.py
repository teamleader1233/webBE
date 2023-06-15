from fastapi import APIRouter
from fastapi import HTTPException

from ..param.auth import UserParam, LoginParam
from ..service.user import (
    validate_email,
    validate_password,
    validate_username,
    get_user_from_credentials,
)
from ..service.token import get_verify_token, get_user_from_token
from ..model.user import User
from ..main import db

import re
from hashlib import sha512
from uuid import uuid4


router = APIRouter(
    prefix="/auth"
)


@router.post("/register", status_code=201)
async def register(user: UserParam):
    try:
        validate_username(user.first_name)
        validate_username(user.last_name)
        validate_email(user.email)
        validate_password(user.password)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={"status": 0, "detail": str(e)},
        )
    return {'status': 1}
    """
    password = sha512(user.password.encode('utf-8')).hexdigest()
    uuid = uuid4()
    session_uuid = uuid4()
    db.insert(
        "INSERT INTO User (uuid, first_name, last_name, email, password, is_verified, is_active) VALUES (%s, %s, %s, %s, %s, %s);",
        (uuid, user.first_name, user.last_name, user.email, user.password, user.is_verified, user.is_active)
    )
    """
    
    
    
@router.post("/login", status_code=200)
async def login(user: LoginParam):
    """
    user = get_user_from_credentials(user.email, user.password)

    if not user:
        raise HTTPException(
            status_code=403,
            detail="Email hoặc mật khẩu không đúng"
        )
    
    if not user.is_verified:
        raise HTTPException(
            status_code=403,
            detail="Vui lòng xác nhận tài khoản bằng đường link được gửi qua email"
        )
    """
    if user.email == "sample" and user.password == "password":
        return {"status": 1}
    elif user.email == "unverified" and user.password == "password":
        raise HTTPException(
            status_code=403,
            detail="Vui lòng xác nhận tài khoản bằng đường link được gửi qua email"
        )
    else:
        raise HTTPException(
            status_code=403,
            detail="Email hoặc mật khẩu không đúng"
        )


@router.get('/verify', status_code=200)
async def verify(token: str):
    if not token:
        raise HTTPException(status_code=403, content={"status": 0, "detail": "Mã xác nhận không hợp lệ"})

    #user = get_user_from_token(token)
    # user.verify()
    # verify_user(user.uuid)
    # save_user(user)
    # db.insert("UPDATE User SET is_verified=%s WHERE uuid=%s;", (True, uuid))
    return {"status": 1}


"""
ID (BigINT) |
SECRET_KEY  | => ENCRYPTED_1     | =>ENCRYPTED_2 (USER_TOKEN)
                 USER_SECRET_KEY | 
                        |  ENCRYPT WITH SYSTEM_KEY (CONSTANT)
                        V
                 STORE IN COOKIE
"""