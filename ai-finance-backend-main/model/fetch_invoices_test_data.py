from supabase import create_client, Client
from config.config import SUPABASE_URL, SUPABASE_KEY
from config.table_name_constants import TABLE_INVOICES

# Buat koneksi ke Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Query data dari tabel
def fetch_invoices_test_data():
    response = supabase.table(TABLE_INVOICES).select("*").execute()

    if response.data:
        print("Data retrieved successfully:")
        return response.data
    else:
        print("No data found or an error occurred.")
        return None