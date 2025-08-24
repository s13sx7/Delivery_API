from enum import Enum
from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from pydantic import EmailStr
from sqlalchemy import Enum as SqlEnum
class Role(str, Enum):
    CUSTOMER = "customer"
    COURIER = "courier"

class User(Base):
    
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[EmailStr] = mapped_column(String(255), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[Role] = mapped_column(SqlEnum(Role), nullable=False, default=Role.CUSTOMER)
    
    customer_orders: Mapped[list["Order"]] = relationship(
        "Order", 
        foreign_keys="[Order.customer_id]",
        back_populates="customer"
    )
    
    courier_orders: Mapped[list["Order"]] = relationship(
        "Order", 
        foreign_keys="[Order.courier_id]",
        back_populates="courier"
    )