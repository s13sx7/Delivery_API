from datetime import datetime, timedelta
from typing import Union
from passlib.context import CryptContext
from jose import jwt, JWTError
from config import settings
from exeptions.exeptions import InvalidTokenError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(pwd: str) -> str:
    return pwd_context.hash(pwd)

def verify_password(plain_wd: str, hash_pwd: str) -> bool:
    return pwd_context.verify(plain_wd,hash_pwd)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECKRET_KEY, 
                      algorithm=settings.ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECKRET_KEY,
                             settings.ALGORITHM)
        return payload
    except JWTError as e:
        raise InvalidTokenError