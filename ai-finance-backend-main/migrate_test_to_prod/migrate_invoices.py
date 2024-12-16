from supabase import create_client, Client
from config.config import SUPABASE_URL, SUPABASE_KEY
from config.table_name_constants import TABLE_INVOICES
from core.tools import convert_to_isoformat

# Buat koneksi ke Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def _fetch_invoices_test_data():
    response = (supabase
                .table("invoices_test")
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
    payment_date = record.get("payment_date")
    if "#" in payment_date:
        return
    else:
        tgl, bulan, tahun = payment_date.split("/")
        if int(bulan) > 9:
            return
        
    record = _remove_unwanted_keys(record)  # Hapus key yang tidak diinginkan
    record["issue_date"] = convert_to_isoformat(record.get("issue_date"))
    record["due_date"] = convert_to_isoformat(record.get("due_date"))
    record["payment_date"] = convert_to_isoformat(record.get("payment_date"))
    return record

def migrate_invoices_to_prod():
    # Ambil data dari invoices_test
    invoices_test_data = _fetch_invoices_test_data()
    
    if invoices_test_data is None:
        print("No data to migrate.")
        return
    
    # Konversi tanggal di setiap record
    invoices_test_data = [_convert_dates_in_record(record) for record in invoices_test_data]
    invoices_test_data = [record for record in invoices_test_data if record is not None]

    # Masukkan data ke tabel invoices
    supabase.table("invoices").insert(invoices_test_data).execute()
    
    print(f"Successfully migrated {len(invoices_test_data)} records to invoices.")