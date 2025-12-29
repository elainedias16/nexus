from repository.component_repository import ComponentRepository

class ComponentController:
    def __init__(self, db):
        self.repo = ComponentRepository(db)

    def get_component_by_id(self, component_id: int):
        component = self.repo.get_component_by_id(component_id)
        return component 

    # def get_all_components(self):
    #     return self.repo.get_all_components()

# from fastapi import APIRouter
# import repository.component_repository as repo

# router = APIRouter()
# repository = repo.ComponentRepository()


# class ComponentController:
#     def __init__:
#         pass

# # @router.get("/id/{component_id}")
# # def get_component_by_id(component_id: int):
# #     component = repository.get_component_by_id(component_id)
# #     return component

# # @router.get("/all")
# # def get_all_components():
# #     return repository.get_all_components()

# # @router.get("/search")
# # def get_components_by_criteria(component_type: str = None, install_timestamp: str = None, manufacterer: str = None):
# #     return repo.get_components_by_criteria(component_type, install_timestamp, manufacterer)