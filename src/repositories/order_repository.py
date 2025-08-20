from sqlalchemy import select
from repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from models.order_model import Order
from database import db_helper
from schemas.order_shema import SOrderCreate, SOrderUpdate

class  OrderRepository(SqlAlchemyRepository[ModelType, SOrderCreate, SOrderUpdate]):

    async def get_all_by_filter(self, **filters) -> list[ModelType]:
        async with self._session_factory() as session:
            query = select(self.model).filter_by(**filters)
            row = await session.execute(query)
            return list(row.scalars().all())
order_repository = OrderRepository(model=Order, db_session=db_helper.get_db_session)