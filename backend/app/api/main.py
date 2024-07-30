from app.api.routes import inference
from fastapi import APIRouter

api_router = APIRouter()

api_router.get("/", tags=["root"])(lambda: {"message": "Hello from root"})
api_router.include_router(inference.router, prefix="/inference", tags=["inference"])
