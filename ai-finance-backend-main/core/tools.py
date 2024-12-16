from datetime import datetime

def convert_to_isoformat(date_str, input_format="%d/%m/%Y"):
    """
    Mengonversi string tanggal ke format ISO 8601 (YYYY-MM-DD).

    Args:
        date_str (str): Tanggal dalam format string.
        input_format (str): Format input tanggal. Defaultnya adalah "%d/%m/%Y".

    Returns:
        str: Tanggal dalam format ISO 8601 (YYYY-MM-DD).
    """
    try:
        return datetime.strptime(date_str, input_format).date().isoformat()
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")
