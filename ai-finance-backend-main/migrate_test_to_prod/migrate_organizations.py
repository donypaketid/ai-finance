from supabase import create_client, Client
from config.config import SUPABASE_URL, SUPABASE_KEY
from config.table_name_constants import TABLE_INVOICES
from core.tools import convert_to_isoformat

# Buat koneksi ke Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def _fetch_organization_test_data():
    response = (supabase
                .table("organizations_test")
                .select("*")
                .limit(10000)
                .execute())
    
    if response.data:
        return response.data
    else:
        print("No data found or an error occurred.")
        return None

def _remove_unwanted_keys(record):
    """Menghapus 'id' dan 'created_at' dari setiap record jika ada."""
    record.pop("id", None)  # Hapus id jika ada, jika tidak ada abaikan
    record.pop("created_at", None)  # Hapus created_at jika ada, jika tidak ada abaikan
    return record

def _convert_dates_in_record(record):
    """Mengonversi kolom tanggal dalam record menjadi format ISO 8601."""
    record = _remove_unwanted_keys(record)  # Hapus key yang tidak diinginkan
    record["join_date"] = convert_to_isoformat(record.get("join_date"), "%m/%d/%Y")
    record["last_payment"] = convert_to_isoformat(record.get("last_payment"), "%m/%d/%Y")
    return record

def migrate_organization_to_prod():
    # Ambil data dari organization_test
    organization_test_data = _fetch_organization_test_data()
    
    if organization_test_data is None:
        print("No data to migrate.")
        return
    
    # Konversi tanggal di setiap record
    organization_test_data = [_convert_dates_in_record(record) for record in organization_test_data]
    
    # Masukkan data ke tabel invoices
    supabase.table("organizations").insert(organization_test_data).execute()
    
    print(f"Successfully migrated {len(organization_test_data)} records to organizations.")