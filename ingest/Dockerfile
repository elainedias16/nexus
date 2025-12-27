FROM python:3.11-slim

WORKDIR /nexus

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ingest_data_to_db.py .

CMD ["python", "ingest_data_to_db.py"]
