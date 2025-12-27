from fastapi import FastAPI
from controller.component_controller import router as component_router

app = FastAPI(title="API de Metadados")


app.include_router(
    component_router,
    prefix="/components",
    tags=["Components"]
)

@app.get("/")
def read_root():
    return {"message": "Olá, bem-vindo à API de Metadados do Nexus!\nHello, welcome to the Nexus Metadata API", "status": "Online"}