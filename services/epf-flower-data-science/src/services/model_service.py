import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import json
from pathlib import Path

def train_and_save_model():
    # Path to the current script
    current_directory = Path(__file__).parent

    # Path to the model parameters file
    parameters_file = current_directory / '../../config/model_parameters.json'

    # Load parameters
    with open(parameters_file, 'r') as file:
        params = json.load(file)["RandomForestClassifier"]

    # Load dataset
    df = pd.read_csv(current_directory / '../../data/Iris.csv')
    
    # Assume the last column is the target and the rest are features
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Train the model
    model = RandomForestClassifier(**params)
    model.fit(X, y)

    # Save the model
    model_save_path = current_directory / '../../models/random_forest_model.joblib'
    os.makedirs(model_save_path.parent, exist_ok=True)
    joblib.dump(model, model_save_path)

    return {"status": "Model trained and saved successfully"}
