from pydantic import BaseModel, EmailStr

class SUserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class SUserUpdate(SUserCreate):
    pass

class SUserAuth(BaseModel):
    email: EmailStr
    password: str


