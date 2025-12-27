import pandas as pd
import os
from sqlalchemy import create_engine

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{user}:{password}@{host}:{port}/{db}"
)

df = pd.read_csv("/data/well_components.csv")

df.to_sql(
    "well_components",
    engine,
    if_exists="replace",
    index=False
)

print("Ingestão concluída com sucesso.")

