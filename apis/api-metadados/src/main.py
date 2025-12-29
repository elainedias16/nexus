from fastapi import FastAPI, Depends
from database.db_connection import engine, Base
from routes.route import route as component_router
from model.component import Component



Base.metadata.create_all(bind=engine)
app = FastAPI(title="API de Metadados")



app.include_router(
    component_router,
    prefix="/components",
    tags=["Components"]
)

@app.get("/")
def read_root():
    return {"message": "Olá, bem-vindo à API de Metadados do Nexus!\nHello, welcome to the Nexus Metadata API", "status": "Online"}


# @app.get("/test-db")
# def test_connection(db: Session =  Depends(get_db)):
#     return {"status": "Conectado ao nexus_project!"}## deu certo!!!