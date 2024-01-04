from fastapi import APIRouter
from src.api.routes import hello, data, model_routes, parameters

router = APIRouter()
router.include_router(hello.router, tags=["Hello"])
router.include_router(data.router, tags=["Data"])
router.include_router(model_routes.router, tags=["Model"])
router.include_router(parameters.router, tags=["Parameters"])