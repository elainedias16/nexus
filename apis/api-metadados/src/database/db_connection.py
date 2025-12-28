import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")


engine = create_engine(
    f"postgresql://{user}:{password}@{host}:{port}/{db}"
)

local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = local_session() # new session for every request
    try:
        yield db
    finally:
        db.close()


# if __name__ == "__main__":  
#     try:
#         with engine.connect() as connection:
#             print("Conexão com o banco de dados estabelecida com sucesso.")
#     except Exception as e:
#         print("Falha ao conectar ao banco de dados!\n")
#         print("Erro:", str(e))
