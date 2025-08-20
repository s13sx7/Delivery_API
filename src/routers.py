from fastapi import APIRouter
from api import user_controller, order_controller

def get_router():
    router = APIRouter()
    router.include_router(user_controller.router)
    router.include_router(order_controller.router)
    return router