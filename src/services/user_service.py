from auth.security import get_hashed_password
from services.base_service import BaseServise
from models.user_model import User
from repositories.sqlalchemy_repository import ModelType
from repositories.user_repository import user_repository
from schemas.user_schema import SUserUpdate, SUserCreate, SUserAuth
from pydantic import EmailStr
from auth.security import verify_password
from typing import Optional
from exeptions.exeptions import EmailNotExistError, EmailExistError
class UserService(BaseServise):
    async def create(self, model: SUserCreate) -> User:
        if await self.repository.get_single(email=model.email):
            raise EmailExistError
        user_data = model.model_dump(exclude={"password"})
        user_data["hashed_password"] = get_hashed_password(model.password)
        return await self.repository.create(data = user_data)
    
    async def authenticate(self, data: SUserAuth) -> bool:
        user: Optional[User] = await self.repository.get_single(email = data.email)
        if not user:
            raise EmailNotExistError
        return verify_password(data.password, user.hashed_password)

        
user_service = UserService(repository=user_repository)