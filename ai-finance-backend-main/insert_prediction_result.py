from config.supabase_client import supabase
from config.table_name_constants import TABLE_PREDICTION_RESULT
from core.tools import convert_to_isoformat

def insert_prediction_result_if_not_exists(data, organization_code):
    # 1. Cari data berdasarkan organization_code
    result = supabase.from_(TABLE_PREDICTION_RESULT).select("last_payment").eq("organization_code", organization_code).execute()

    records = result.data

    # 2. Filter hasil berdasarkan last_payment
    existing_record = next(
        (record for record in records if record["last_payment"] == data["last_payment"]),
        None,
    )

    # 3. Jika tidak ditemukan, lakukan INSERT
    if existing_record is None:
        supabase.from_(TABLE_PREDICTION_RESULT).insert(data).execute()
        
        return "Success";
    else:
        return "Data with the same last_payment already exists, skipping insert."