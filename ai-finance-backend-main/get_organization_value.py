from core.calculate_value import calculate_value
from fetch_invoices_data import fetch_invoices_data
from datetime import datetime
import pandas as pd
    
def get_organization_value(organization_code: str, limit: int):
    invoices_data = fetch_invoices_data(organization_code, limit)
    
    if invoices_data == None:
        return None
    
    df_invoices_data = pd.DataFrame(invoices_data)
    organization_value = 0
    totalWeight = 0
    weight = 1;
    data = []

    for row in df_invoices_data.itertuples():
        due_date = datetime.strptime(row.due_date, "%Y-%m-%d").date()
        payment_date = datetime.strptime(row.payment_date, "%Y-%m-%d").date()
        difference = payment_date - due_date
        value = calculate_value(difference.days)
        
        data.append(value * weight)
        
        totalWeight += weight
        weight += 1
    
    organization_value = sum(data)/totalWeight
            
    return organization_value