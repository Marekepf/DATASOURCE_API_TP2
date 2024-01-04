from fastapi import APIRouter
from src.services.model_service import train_and_save_model
from pydantic import BaseModel, Field
import numpy as np
from src.services import model_service
from pathlib import Path
import pandas as pd

router = APIRouter()

@router.get("/train-model")
def train_model():
    return train_and_save_model()


class PredictionRequest(BaseModel):
    sepal_length: float = Field(..., example=5.1)
    sepal_width: float = Field(..., example=3.5)
    petal_length: float = Field(..., example=1.4)
    petal_width: float = Field(..., example=0.2)


@router.post("/predict")
async def predict(request: PredictionRequest):
    # Construct the path to the model
    current_directory = Path(__file__).parent
    model_path = "C:\\Users\\Utilisateur\\Desktop\\DATA_S9\\Data_source\\TP2_API\\DATASOURCE_API_TP2\\services\\epf-flower-data-science\\models\\random_forest_model.joblib"
    
    # Load the model
    model = model_service.load_model(model_path)
    
    # Prepare the data for prediction
    data_to_predict = pd.DataFrame([[
        request.sepal_length, 
        request.sepal_width, 
        request.petal_length, 
        request.petal_width
    ]], columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])

    
    # Make prediction
    prediction = model_service.make_prediction(model, data_to_predict)
    
    # Return the prediction as JSON
    return {"prediction": prediction.tolist()}
