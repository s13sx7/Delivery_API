from typing import Union
from repositories.sqlalchemy_repository import ModelType
from schemas.order_shema import SOrderCreate, SOrderUpdateComplete, SOrderUpdate, SOrderTake
from .base_service import BaseServise
from models.user_model import User, Role
from repositories.order_repository import order_repository
from exeptions.exeptions import BadRUserRole

class OrderServise(BaseServise):
    async def create(self, model: SOrderCreate, user: User) -> ModelType:
        try:
            if user.role != Role.CUSTOMER:
                raise BadRUserRole
            order_data = model.model_dump()
            order_data["customer_id"] = user.id
            return await self.repository.create(data =order_data)
        except BadRUserRole:
            raise 

    async def my_orders(self, pk: int, role: str):
        if role == "customer":
            return await self.repository.get_all_by_filter(customer_id=pk)
        elif role == "courier":
            return await self.repository.get_all_by_filter(courier_id=pk)
        else:
            return []
        
    async def complete_order(self, pk: int, model: Union[SOrderUpdateComplete, SOrderUpdate]) -> ModelType:
        return await self.repository.update(data = model.model_dump(), id = pk)

    async def take_order(self, pk: int, model: Union[SOrderTake, SOrderUpdate]) -> ModelType:
        return await self.repository.update(data = model.model_dump(), id = pk)

order_service = OrderServise(repository=order_repository)