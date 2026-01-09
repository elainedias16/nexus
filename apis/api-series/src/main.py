from fastapi import FastAPI
from src.routes.route import route as simulation_router

app = FastAPI(title="API de Simulações de Séries Temporais")


app.include_router(
    simulation_router,
    tags=["simulation"]
)

@app.get("/")
def read_root():
    return {"message": "Olá, bem-vindo à API de Séries Temporais do Nexus!\nHello, welcome to the Nexus Series API", "status": "Online"}







