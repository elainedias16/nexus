import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db = os.getenv("POSTGRES_DB")

engine = create_engine(
    f"postgresql://{user}:{password}@{host}:{port}/{db}"
)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal() # new session for every request
    try:
        yield db
        print("DB session yielded successfully.")
    finally:
        print("Closing DB session.")
        db.close()
