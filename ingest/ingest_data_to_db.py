from database.db_connection import engine, Base
import pandas as pd
from database.model.component import ComponentModel
from sqlalchemy.dialects.postgresql import insert

def insert_on_conflict_nothing(table, conn, keys, data_iter):
    data = [dict(zip(keys, row)) for row in data_iter]
    stmt = insert(table.table).values(data)
    
    stmt = stmt.on_conflict_do_nothing()
    
    result = conn.execute(stmt)
    return result.rowcount


def ingest_data_to_db():
    data_path = "/data/well_components.csv"

    df = pd.read_csv(data_path)

    Base.metadata.create_all(bind=engine)

    # Convert 'install_timestamp' to date format
    if 'install_timestamp' in df.columns:
        df['install_timestamp'] = pd.to_datetime(df['install_timestamp']).dt.date

    df.to_sql(
        ComponentModel.__tablename__,
        engine,
        if_exists="append",
        index=False,
        method=insert_on_conflict_nothing
    )
    
    print("Ingestão concluída com sucesso.")


if __name__ == "__main__":
    ingest_data_to_db()