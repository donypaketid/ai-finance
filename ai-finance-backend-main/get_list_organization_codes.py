from supabase import create_client, Client
from config.config import SUPABASE_URL, SUPABASE_KEY
from config.table_name_constants import TABLE_ORGANIZATIONS
from core.tools import convert_to_isoformat

# Buat koneksi ke Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def _fetch_organization_data():
    response = (supabase
                .table(TABLE_ORGANIZATIONS)
                .select("organization_code")
                .limit(10000)
                .execute())
    
    if response.data:
        return response.data
    else:
        print("No data found or an error occurred.")
        return None

def get_list_organization_code():
    # Ambil data dari organization
    organization_data = _fetch_organization_data()
    
    if organization_data is None:
        print("No organization data.")
        return
    
    list_organization_code = [record["organization_code"] for record in organization_data]
    
    return list_organization_code