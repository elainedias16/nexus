from src.database.db_connection import engine, Base
import pandas as pd
from src.database.model.component import ComponentModel
from sqlalchemy.dialects.postgresql import insert

def insert_on_conflict_nothing(table, conn, keys, data_iter):
    """
    Insert rows into a PostgreSQL table ignoring conflicts.
    
    :param table: Object representing the table.
    :param conn: Active SQLAlchemy database connection.
    :param keys: List of column names (e.g. ["id", "component_name"]).
    :param data_iter: Iterator of data rows.
    :return: Number of rows successfully inserted.
    """
 
    # List of dicts of the data to be inserted in the database
    data = [dict(zip(keys, row)) for row in data_iter]

    # SQLAlchemy creates INSERT statement
    statement = insert(table.table).values(data)

    # Do not insert if conflict occurs
    statement = statement.on_conflict_do_nothing()
    
    result = conn.execute(statement)
    print(f"{result.rowcount} rows inserted, conflicts ignored.")
    return result.rowcount


# The method that ingest data needs to have access to the engine and Base directly.
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
        method=insert_on_conflict_nothing #pandas will use this function to handle conflicts
    )
    
    print("Ingestão concluída com sucesso.")


if __name__ == "__main__":
    ingest_data_to_db()