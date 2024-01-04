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
    parameters_file = 'C:\\Users\\Utilisateur\\Desktop\\DATA_S9\\Data_source\\TP2_API\\DATASOURCE_API_TP2\\services\\epf-flower-data-science\\src\\config\\model_parameters.json'

    # Load parameters
    with open(parameters_file, 'r') as file:
        params = json.load(file)["RandomForestClassifier"]

    # Load dataset
    df = pd.read_csv('C:\\Users\\Utilisateur\\Desktop\\DATA_S9\\Data_source\\TP2_API\\DATASOURCE_API_TP2\\services\\epf-flower-data-science\\src\\data\\Iris.csv')
    
    X = df.iloc[:, 1:-1]  # Excludes the first (Id) and last (Species) columns
    y = df.iloc[:, -1]    # Selects only the last column (Species)


    # Train the model
    model = RandomForestClassifier(**params)
    model.fit(X, y)

    # Save the model
    model_save_path = current_directory / '../../models/random_forest_model.joblib'
    os.makedirs(model_save_path.parent, exist_ok=True)
    joblib.dump(model, model_save_path)

    return {"status": "Model trained and saved successfully"}



def load_model(model_path):
    # Code to load and return the model
    return joblib.load(model_path)


def make_prediction(model, input_data):
    # Assuming input_data is already in the correct format
    predictions = model.predict(input_data)
    return predictions

