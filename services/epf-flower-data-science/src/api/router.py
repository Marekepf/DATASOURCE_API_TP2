"""API Router for FastAPI."""
from fastapi import APIRouter
from src.api.routes import hello, data
from src.api.routes.model_routes import router as model_router

router = APIRouter()
router.include_router(hello.router, tags=["Hello"])
router.include_router(data.router, tags=["Data"])
router.include_router(model_router, tags=["Model"])