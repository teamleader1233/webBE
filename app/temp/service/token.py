from datetime import datetime, timedelta
import secrets
import jwt
from user import get_user_from_uuid
from ..config import settings
from ..database import Database
from ..model.token import Token


def generate_token(uuid: str, session_uuid: str, token_type: str, db: Database):
    expiry_date = datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    payload = {
        "uuid": uuid, 
        "suuid": session_uuid,
        "exp": expiry_date,
        "type": token_type,
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.SECURITY_ALGORITHM)


def get_user_from_token(token_type: str, token: str):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
    uuid = payload.get("uuid")
    session_uuid = payload.get("suuid")
    expiry_date = payload.get("exp")
    token_type_ = payload.get("type")

    if not all(uuid, session_uuid, expiry_date, token_type) or token_type != token_type_:
        raise Exception("Mã không hợp lệ")
    elif datetime.utcnow() > expiry_date:
        raise Exception("Mã đã hết hạn")

    user = get_user_from_uuid(uuid)
    if user.session_uuid != session_uuid:
        raise Exception("Mã đã bị vô hiệu hóa")
    
    return user
