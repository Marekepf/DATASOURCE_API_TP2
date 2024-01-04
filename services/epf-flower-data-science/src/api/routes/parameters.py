from fastapi import APIRouter
from src.services.parameters import get_firestore_parameters
from src.services.parameters import add_or_update_parameter
from pydantic import BaseModel

class Parameter(BaseModel):
    value: int


router = APIRouter()

@router.get("/get-parameters")
async def get_parameters():
    return get_firestore_parameters()


@router.post("/update-parameter/{parameter_name}")
async def update_parameter(parameter_name: str, parameter: Parameter):
    return add_or_update_parameter(parameter_name, parameter.value)

@router.post("/add-parameter/{parameter_name}")
async def add_parameter(parameter_name: str, parameter: Parameter):
    return add_or_update_parameter(parameter_name, parameter.value)
