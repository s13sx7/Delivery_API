from pydantic import BaseModel, field_validator, ValidationError

class SOrderCreate(BaseModel):
    products_list: list
    class Config:
        from_attributes = True

    @field_validator("products_list")
    @classmethod
    def validate_products_list(cls, v: list):
        if len(v) == 0:
            raise ValueError("Product list cannot be empty")
        if any(isinstance(item, int) for item in v):
            raise ValueError("Bad list")
            
        return v
        




class SOrderUpdate(SOrderCreate):
    ...

