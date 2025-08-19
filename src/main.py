import uvicorn
from fastapi import FastAPI
from services.user_service import user_service
from schemas.user_schema import SUserCreate
from routers import get_router

def get_application() -> FastAPI:
    application = FastAPI(title="delivery")
    return application

app = get_application()

app.include_router(get_router())


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)