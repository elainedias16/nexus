class SimulationRepository:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def chunk_file(self, chunk_size: int):
        with open(self.data_path, "rb") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk


