from src.repository.simulation_repository import SimulationRepository
from fastapi.responses import StreamingResponse

class SimulationController:
    def __init__(self, repository: SimulationRepository):
        self.repo = repository


    def stream_data(self, chunk_size):
        return StreamingResponse(
            self.repo.chunk_file(chunk_size),
            media_type="application/json",
            headers={
            "Content-Disposition": "attachment; filename=out.json",
            }
        )
   