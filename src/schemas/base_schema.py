from pydantic import BaseModel
from typing import NewType

PyModel = NewType("PyModel", BaseModel)

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True