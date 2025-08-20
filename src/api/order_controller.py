from fastapi import APIRouter, Depends, HTTPException, status
from services.order_service import order_service
from api.dependencies import get_current_user
from schemas.order_shema import SOrderCreate
from exeptions.exeptions import BadProductListError

router = APIRouter(prefix="/order", tags=["order"])

#!!!!Подумать как всё это запихать в сервис
@router.post("/create")
async def new_order(data: SOrderCreate, user = Depends(get_current_user)):
    try:
        result = await order_service.create(data, user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.post("/show_my_orders")
async def my_orders(user = Depends(get_current_user)):
    return await order_service.my_orders(pk=user.id, role=user.role)