from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.config import API_V1_STR, BACKEND_CORS_ORIGINS

app = FastAPI(
    title="Resource Prediction API",
    openapi_url=f"{API_V1_STR}/openapi.json",
)

if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=BACKEND_CORS_ORIGINS.split(","),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=API_V1_STR)
