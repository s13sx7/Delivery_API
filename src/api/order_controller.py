from fastapi import APIRouter, Depends, HTTPException, status
from services.order_service import order_service
from api.dependencies import get_current_user
from models.user_model import User
from schemas.order_shema import SOrderCreate, SOrderTake, SOrderUpdateComplete
from exeptions.exeptions import BadProductListError

router = APIRouter(prefix="/order", tags=["order"])

@router.post("/create")
async def new_order(data: SOrderCreate, user: User= Depends(get_current_user)):
    try:
        result = await order_service.create(data, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/show_my_orders")
async def my_orders(user: User = Depends(get_current_user)):
    return await order_service.my_orders(pk=user.id, role=user.role)

@router.patch("/complite_order")
async def complite_order(data: SOrderUpdateComplete, user: User = Depends(get_current_user)):
    return await order_service.complete_order(data.id, user.role, model=data)

@router.patch("/take_order")
async def take_order(data: SOrderTake, user: User = Depends(get_current_user)):
    data.courier_id = user.id
    return await order_service.take_order(data.id, user.role, model=data)