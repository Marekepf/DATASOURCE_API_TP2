import requests
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_iris_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('uciml/iris', path='src/data', unzip=True)

    return {"status": "Dataset downloaded successfully"}

# def download_iris_dataset():
#     dataset_url = "https://www.kaggle.com/datasets/uciml/iris"
#     response = requests.get(dataset_url)
    
#     if response.status_code == 200:
#         os.makedirs('src/data', exist_ok=True)
#         with open('src/data/iris.csv', 'wb') as file:
#             file.write(response.content)
#         return {"status": "Dataset downloaded successfully"}
#     else:
#         return {"status": "Failed to download the dataset"}
