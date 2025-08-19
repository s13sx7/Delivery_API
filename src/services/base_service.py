from repositories.base_repository import AbstractRepository
from schemas.base_schema import PyModel
from repositories.sqlalchemy_repository import ModelType


class BaseServise:

    def __init__(self, repository: AbstractRepository) -> None:
        self.repository = repository

    async def create(self, model: PyModel) -> ModelType:
        return await self.repository.create(data = model.model_dump())
    
    async def update(self, pk: int, model: PyModel) -> ModelType:
        return await self.repository.update(data = model.model_dump(), id = pk)
    
    async def delete(self, pk: int) -> None:
        await self.repository.delete(id = pk)

    async def get(self, **kwargs) -> ModelType:
        return await self.repository.get_single(**kwargs)