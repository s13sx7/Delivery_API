from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import Base
from sqlalchemy import ARRAY, ForeignKey, String

class Order(Base):
    products_list: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    courier_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), default=None)
    complete: Mapped[bool] = mapped_column(default=False, nullable=False)

    customer: Mapped["User"] = relationship(
        "User", 
        foreign_keys=[customer_id],
        back_populates="customer_orders"
    )
    
    courier: Mapped["User | None"] = relationship(
        "User", 
        foreign_keys=[courier_id],
        primaryjoin="and_(User.id == Order.courier_id, User.role == 'courier')",
        back_populates="courier_orders",
        viewonly=False  
    )