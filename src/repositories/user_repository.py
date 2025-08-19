from typing import Optional
from repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from models.user_model import User
from database import db_helper
from schemas.user_schema import SUserCreate, SUserUpdate
from sqlalchemy import select
from auth.security import get_hashed_password


class UserRepository(SqlAlchemyRepository[ModelType, SUserCreate, SUserUpdate]):
    async def get_all(self) -> list[ModelType]:
        async with self._session_factory as session:
            row = await session.execute(select(self.model))
            return list(row.scalars().all())

user_repository = UserRepository(model=User, db_session=db_helper.get_db_session) # type: ignore