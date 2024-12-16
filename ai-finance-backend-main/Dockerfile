# Gunakan base image dengan Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Salin semua file ke container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port dinamis untuk Railway
EXPOSE ${PORT}

# Command untuk menjalankan aplikasi
CMD ["python", "main_api.py"]
