from fastapi import APIRouter
from api import user_controller

def get_router():
    router = APIRouter()
    router.include_router(user_controller.router)
    return router