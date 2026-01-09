FROM python:3.11-slim

WORKDIR /app

COPY apis/api-metadados/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apis/api-metadados/src ./src
COPY apis/api-metadados/tests ./tests

COPY data/well_components.csv ./data/well_components.csv

ENV PYTHONPATH=/app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
