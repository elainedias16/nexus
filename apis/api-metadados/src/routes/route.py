from src.database.db_connection import get_db
from src.controller.component_controller import ComponentController
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from src.schema.component import ComponentSchema
from sqlalchemy.orm import Session
from fastapi import Path
from fastapi import Query

route = APIRouter()


@route.get("/search", response_model=list[ComponentSchema], summary="Busca componentes pelo tipo e pela data de instalação",
            responses={200: {"description": "Components found successfully"}, 404: {"description": "No components found"}, 
                       500: {"description": "Internal server error"}})
def get_component_by_criteria(type: str,
                              install_timestamp: date = Query(...), db: Session = Depends(get_db)):
    """
    Busca componentes do mesmo tipo cuja data de instalação seja maior ou igual à data fornecida.
    - **type**: tipo do componente.
    - **install_timestamp**: data de instalação do componente no formato YYYY-MM-DD.
    """

    try:
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
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "error_code": "500_INTERNAL_SERVER_ERROR",
            "message": "Ocorreu um erro interno ao processar a solicitação.",
            "hint": str(e)
        }
    )

    

@route.get("/{component_id}", response_model=ComponentSchema, summary="Busca um componente pelo ID",
            responses={200: {"description": "Component found successfully"}, 404: {"description": "Component not found"}, 
                       500: {"description": "Internal server error"}})
def get_component_by_id(component_id: int = Path(..., ge=0), db: Session = Depends(get_db)): #ge=0 (greater or equal = 0) blocks negative ids
    """
    Procura um componente pelo seu ID.
    - **id**: id do componente. Deve ser um número inteiro não negativo.
    """

    try:       
        controller = ComponentController(db)
        component = controller.get_component_by_id(component_id)
        
        if component is None:
            print("componente nulo")
            raise HTTPException(status_code=404, detail={
            "error_code": "404_COMPONENT_NOT_FOUND",
            "message": "O componente com o ID especificado não foi encontrado no banco de dados.",
            "hint": "Verifique se o ID está correto e tente novamente."
            }
        )
            
        return component
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "error_code": "500_INTERNAL_SERVER_ERROR",
            "message": "Ocorreu um erro interno ao processar a solicitação.",
            "hint": str(e)
        }
    )
