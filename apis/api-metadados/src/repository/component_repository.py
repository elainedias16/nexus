from sqlalchemy.orm import Session
from model.component import Component


class ComponentRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_component_by_id(self, component_id: int):
        return self.db.query(Component).filter(Component.id == component_id).first()

    def get_all_components(self):
        return self.db.query(Component).all()




