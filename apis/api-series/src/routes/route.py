from fastapi import APIRouter, Path, HTTPException
from src.controller.simulation_controller import SimulationController
from src.settings import settings

route = APIRouter()


@route.get("/components/{component_id}/simulation", 
            responses={200: {"description": "Simulation completed successfully"},
                       500: {"description": "Internal server error"}} , summary = "Simula a série temporal de um componente específico")
def simulate_series(component_id: int = Path(..., ge=0)):
    """
    Retorna a simulação da série temporal para um componente específico.
    No caso do MVP, retorna o mesmo json para qualquer componente_id.
    - **component_id**: ID do componente para o qual a série temporal será simulada
    """
    try :
        controller = SimulationController(settings.data_path)
        return controller.stream_data(settings.chunk_size)
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "error_code": "500_INTERNAL_SERVER_ERROR",
            "message": "Ocorreu um erro interno ao processar a solicitação.",
            "hint": str(e)
        })  
    


