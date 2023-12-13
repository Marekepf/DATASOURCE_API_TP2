from fastapi import APIRouter
from src.services.data import download_iris_dataset

router = APIRouter()

@router.get("/download-iris")
def download_iris():
    return download_iris_dataset()
