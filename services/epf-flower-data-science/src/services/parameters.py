import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin
cred = credentials.Certificate('C:\\Users\\Utilisateur\\Desktop\\DATA_S9\\Data_source\\TP2_API\\DATASOURCE_API_TP2\\services\\epf-flower-data-science\\src\\config\\tpapiboudeville-firebase-adminsdk-kms1s-7e4cfffa4f.json')
firebase_admin.initialize_app(cred)

def get_firestore_parameters():
    db = firestore.client()
    parameters_collection = db.collection('parameters')

    # Fetching parameters
    n_estimators_doc = parameters_collection.document('n_estimators').get()
    criterion_doc = parameters_collection.document('criterion').get()

    n_estimators = n_estimators_doc.to_dict() if n_estimators_doc.exists else None
    criterion = criterion_doc.to_dict() if criterion_doc.exists else None

    # Check if the documents exist and have the 'value' key
    n_estimators_value = n_estimators.get('value', None) if n_estimators else None
    criterion_value = criterion.get('value', None) if criterion else None

    return {
        'n_estimators': n_estimators_value,
        'criterion': criterion_value
    }

def add_or_update_parameter(parameter_name: str, value: int):
    db = firestore.client()
    parameters_collection = db.collection('parameters')
    parameters_collection.document(parameter_name).set({'value': value})
    return {"message": f"Parameter '{parameter_name}' updated/added successfully."}
