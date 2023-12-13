from fastapi import APIRouter
from src.services.model_service import train_and_save_model

router = APIRouter()

@router.get("/train-model")
def train_model():
    return train_and_save_model()
