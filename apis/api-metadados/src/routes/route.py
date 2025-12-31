from database.db_connection import get_db
from controller.component_controller import ComponentController
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from schema.component import ComponentSchema
from sqlalchemy.orm import Session

route = APIRouter()

@route.get("/id/{component_id}", response_model=ComponentSchema, summary="Busca um componente pelo ID")
def get_component_by_id(component_id: int, db: Session = Depends(get_db)):
    """
    Procura um componente pelo seu ID.
    - **id**: id do componente. Deve ser um número inteiro não negativo.
    """
    
    controller = ComponentController(db)
    component = controller.get_component_by_id(component_id)
    
    if component is None:
        raise HTTPException(status_code=404, detail={
        "error_code": "404_COMPONENT_NOT_FOUND",
        "message": "O componente com o ID especificado não foi encontrado no banco de dados.",
        "hint": "Verifique se o ID está correto e tente novamente."
        }
       )
        
    return component


@route.get("/search", response_model=list[ComponentSchema], summary="Busca componentes pelo tipo e pela data de instalação")
def get_component_by_criteria(type: str, install_timestamp: date, db: Session = Depends(get_db)):
    """
    Busca componentes pelo tipo e pela data de instalação.
    - **type**: tipo do componente.
    - **install_timestamp**: data de instalação do componente no formato YYYY-MM-DD.
    """
    controller = ComponentController(db)
    filtered_components = controller.get_component_by_criteria(type, install_timestamp)
    
    if not filtered_components:
        raise HTTPException(status_code=404, detail={
        "error_code": "404_NO_COMPONENTS_FOUND",
        "message": "Nenhum componente correspondente aos critérios fornecidos foi encontrado no banco de dados.",
        "hint": "Verifique os critérios de busca e tente novamente."
        }
       )
        
    return filtered_components

