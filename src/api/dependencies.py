from fastapi import Request, HTTPException
from auth.security import decode_token
from services.user_service import user_service
from models.user_model import User
from exeptions.exeptions import InvalidTokenError

async def get_current_user(request: Request) -> User:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail=" not authenticate")
    payload:dict = decode_token(token)
    if not payload:
        raise InvalidTokenError
    return await user_service.get(email = payload["sub"])