from core.calculate_value import calculate_value
from model.fetch_invoices_test_data import fetch_invoices_test_data
import pandas as pd
from datetime import datetime

invoices_test_data = fetch_invoices_test_data()

df = pd.DataFrame(invoices_test_data)

last_5_invoices_each_org = df.sort_values(by=["id"], ascending=[True]).groupby("organization_cde").head(5)

X = []
y = []
data1 = 0
data2 = 0
data3 = 0
data4 = 0
data5 = 0

for row in last_5_invoices_each_org.itertuples():
    due_date = datetime.strptime(row.due_date, "%d/%m/%Y").date()
    payment_date = datetime.strptime(row.payment_date, "%d/%m/%Y").date()
    difference = payment_date - due_date
    
    if data1 == 0:
        data1 = calculate_value(difference.days)
    elif data2 == 0:
        data2 = calculate_value(difference.days)
    elif data3 == 0:
        data3 = calculate_value(difference.days)
    elif data4 == 0:
        data4 = calculate_value(difference.days)
    elif data5 == 0:
        data5 = calculate_value(difference.days)
        summary = (data1*0.5 + data2*0.75 + data3*1 + data4*1.25 + data5*1.5)/5
        
        X.append([summary])
        
        if summary >= 3.5:
            y.append("Health")
        elif summary >= 2.5:
            y.append("Normal")
        elif summary >= 1.5:
            y.append("Warning")
        else:
            y.append("Danger")
            
        data1 = 0
        data2 = 0
        data3 = 0
        data4 = 0
        data5 = 0