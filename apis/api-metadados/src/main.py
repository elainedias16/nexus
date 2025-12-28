from fastapi import FastAPI, Depends
from controller.component_controller import router as component_router
from sqlalchemy.orm import Session
from database.db_connection import get_db

app = FastAPI(title="API de Metadados")


app.include_router(
    component_router,
    prefix="/components",
    tags=["Components"]
)

@app.get("/")
def read_root():
    return {"message": "Olá, bem-vindo à API de Metadados do Nexus!\nHello, welcome to the Nexus Metadata API", "status": "Online"}

@app.get("/test-db")
def test_connection(db: Session =  Depends(get_db)):
    return {"status": "Conectado ao nexus_project!"}## deu certo!!!