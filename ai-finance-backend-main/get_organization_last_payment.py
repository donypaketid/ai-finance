from fetch_invoices_data import fetch_invoices_data

def get_organization_last_payment(organization_code: str, limit: int):
    invoices_data = fetch_invoices_data(organization_code, limit)
    
    if invoices_data == None:
        return None
    
    return invoices_data[len(invoices_data)-1]["payment_date"]