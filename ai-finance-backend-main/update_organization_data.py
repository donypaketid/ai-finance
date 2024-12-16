from config.supabase_client import supabase
from config.table_name_constants import TABLE_ORGANIZATIONS

def update_organization_data(data, organization_code):
    (supabase
     .table(TABLE_ORGANIZATIONS)
     .update(data)
     .eq("organization_code", organization_code)
     .execute())
    
    return True;