from datetime import date
from repository.component_repository import ComponentRepository

class ComponentController:
    def __init__(self, db):
        self.repo = ComponentRepository(db)

    def get_component_by_id(self, component_id: int):
        component = self.repo.get_component_by_id(component_id)
        return component 

    def get_component_by_criteria(self, type : str, install_timestamp: date):
        filtered_components = self.repo.get_component_by_criteria(type, install_timestamp)
        return filtered_components

        