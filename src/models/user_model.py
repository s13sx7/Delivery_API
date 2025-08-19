from models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from pydantic import EmailStr
class User(Base):
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[EmailStr] = mapped_column(String(255), nullable=False, unique=True)

    hashed_password: Mapped[str] = mapped_column(nullable=False) 