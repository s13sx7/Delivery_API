from repositories.sqlalchemy_repository import ModelType
from schemas.order_shema import SOrderCreate
from .base_service import BaseServise
from repositories.order_repository import order_repository

class OrderServise(BaseServise):
    async def create(self, model: SOrderCreate, cust_id) -> ModelType:
        order_data = model.model_dump()
        order_data["customer_id"] = cust_id
        return await self.repository.create(data =order_data)
    
    async def my_orders(self, pk: int, role: str):
        if role == "customer":
            return await self.repository.get_all_by_filter(customer_id=pk)
        elif role == "courier":
            return await self.repository.get_all_by_filter(courier_id=pk)
        else:
            return []
        

order_service = OrderServise(repository=order_repository)