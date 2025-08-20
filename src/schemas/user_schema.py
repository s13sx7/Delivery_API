from pydantic import BaseModel, EmailStr
from models.user_model import Role

class SUserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class SUserUpdate(SUserCreate):
    pass

class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserCourierUpdate(BaseModel):
    role: Role = Role.COURIER

class SUserCustomerUpdate(BaseModel):
   role: Role = Role.CUSTOMER