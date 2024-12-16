from get_organization_value import get_organization_value
from get_organization_last_payment import get_organization_last_payment
from update_organization_data import update_organization_data
from insert_prediction_result import insert_prediction_result_if_not_exists
from get_list_organization_codes import get_list_organization_code
import joblib

def predict_organization_rate(organization_code: str, limit: int):
    organization_value = get_organization_value(organization_code, limit)
    organization_last_payment = get_organization_last_payment(
        organization_code, limit)

    if organization_value == None:
        return f"{organization_code} organization is not found in database"

    data = joblib.load('model/model_knn_and_encoder.pkl')
    le = data["encoder"]
    model = data["model"]
    pred = model.predict([[organization_value]])
    inverse_pred = le.inverse_transform(pred)[0]

    result_update_organization_data = update_organization_data(
        {"rate": inverse_pred}, organization_code)

    if result_update_organization_data:
        return insert_prediction_result_if_not_exists({"organization_code": organization_code, "rate": organization_value,
                                               "rate_value": inverse_pred, "last_payment": organization_last_payment}, organization_code)
    
    return "Failed Update Organization Data"

def predict_all_organization_rate(limit: int):
    list_organization_code = get_list_organization_code()
    
    for organization_code in list_organization_code:
        predict_organization_rate(organization_code, limit)
    
    return "Success"
    
    
