from fastapi import FastAPI
from src.routes.route import route as simulation_router
from fastapi.middleware.gzip import GZipMiddleware


app = FastAPI(title="API de Simulações de Séries Temporais")

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(
    simulation_router,
    tags=["simulation"]
)

@app.get("/")
def read_root():
    return {"message": "Olá, bem-vindo à API de Séries Temporais do Nexus!\nHello, welcome to the Nexus Series API", "status": "Online"}







