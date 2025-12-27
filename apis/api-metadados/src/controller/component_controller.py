from fastapi import APIRouter
import repository.component_repository as repo

router = APIRouter()

@router.get("/id/{component_id}")
def get_component_by_id(component_id: int):
    return repo.get_component_by_id(component_id)

@router.get("/all")
def get_all_components():
    return repo.get_all_components()

@router.get("/search")
def get_components_by_criteria(component_type: str = None, install_timestamp: str = None, manufacterer: str = None):
    return repo.get_components_by_criteria(component_type, install_timestamp, manufacterer)