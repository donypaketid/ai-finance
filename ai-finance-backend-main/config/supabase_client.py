from supabase import create_client, Client
from config.config import SUPABASE_URL, SUPABASE_KEY

# Buat koneksi ke Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)