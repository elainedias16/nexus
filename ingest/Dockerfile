FROM python:3.11-slim

WORKDIR /nexus

# COPY requirements.txt .
COPY ingest/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ingest/ingest_data_to_db.py .
COPY database/ ./database/

CMD ["python", "ingest_data_to_db.py"]
