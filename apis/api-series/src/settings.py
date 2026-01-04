import os

class Settings:
    def __init__(self):
        self.data_path = os.getenv("SIMULATION_DATA_PATH")
        self.chunk_size = 1 * 1024 * 1024 # 1MB 
       

settings = Settings()