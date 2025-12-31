from sqlalchemy.orm import Session
from database.model.component import ComponentModel 
from datetime import date

class ComponentRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_component_by_id(self, component_id: int):
        return self.db.query(ComponentModel).get(component_id)

    def get_component_by_criteria(self, type: str, install_timestamp: date):
        component_type_after_date = self.db.query(ComponentModel).filter(
            ComponentModel.component_type == type,
            ComponentModel.install_timestamp >= install_timestamp
        ).all()    
        return component_type_after_date


     




