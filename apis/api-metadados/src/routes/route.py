from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_connection import get_db
from controller.component_controller import ComponentController
from model.component import Component

route = APIRouter()

@route.get("/id/{component_id}")
def read_component(component_id: int, db: Session = Depends(get_db)):
    
    controller = ComponentController(db)
    component = controller.get_component_by_id(component_id)
    
    if component is None:
        raise HTTPException(status_code=404, detail="Componente não encontrado")
        
    return component