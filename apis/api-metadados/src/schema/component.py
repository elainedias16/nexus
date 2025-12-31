from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ComponentSchema(BaseModel):
    id : int
    well_name : str 
    component_type : Optional[str] = None
    install_timestamp : datetime #YYYY-MM-DD
    manufacturer : Optional[str] = None
    phase_num : Optional[float] = None
    model : Optional[str] = None  
    component_name : Optional[str] = None
    outer_diameter : Optional[float] = None
    material : Optional[str] = None
    screw : Optional[str] = None
    linear_weight : Optional[float] = None
    length : Optional[float] = None
    lda : Optional[float] = None
    base_md : Optional[float] = None
    top_md : Optional[float] = None
    base_tvd : Optional[float] = None
    top_tvd : Optional[float] = None
    component_amount : Optional[float] = None
    substitution : Optional[bool] = None
    removal_timestamp : Optional[str] = None
    last_component : Optional[bool] = None

     


