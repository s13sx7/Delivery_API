from datetime import timedelta
from fastapi import APIRouter, Response, Depends
from services.user_service import user_service
from schemas.user_schema import SUserAuth, SUserCreate
from auth.security import create_access_token
from exeptions.exeptions import InvalidPasswordError
from api.dependencies import get_current_user
router = APIRouter(prefix="/user", tags=["user"])

@router.post("/login")
async def login(data: SUserAuth, response: Response):
    if not await user_service.authenticate(data=data):
        raise InvalidPasswordError
    token = create_access_token({"sub": data.email})
    response.set_cookie(key="access_token",
                        httponly=True,
                        secure=True,
                        value=token,
                        max_age=int(timedelta(minutes=60).total_seconds()))
    return {"message: login complite"}

@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token",
                        httponly=True,
                        secure=True,
                        )
    return {"message": "logout complete"}

@router.post("/create")
async def create_new_user(data: SUserCreate):
    return await user_service.create(data)

@router.get("/me")
async def get_me(user = Depends(get_current_user)):
    return await user_service.get(email=user.email)