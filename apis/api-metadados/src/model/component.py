from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, Boolean, Float, BigInteger
from database.db_connection import Base


class Component(Base):
    __tablename__ = "well_components"

    id = Column(BigInteger, primary_key=True, index=True)
    well_name = Column(String)  
    component_type = Column(String)
    install_timestamp = Column(String)
    manufacturer = Column(String)
    phase_num = Column(Float)
    model = Column(String)  
    component_name = Column(String)
    outer_diameter = Column(Float)
    material = Column(String)
    screw = Column(String)
    linear_weight = Column(Float)
    length = Column(Float)
    lda = Column(Float)
    base_md = Column(Float)
    top_md = Column(Float)
    base_tvd = Column(Float)
    top_tvd = Column(Float)
    component_amount = Column(Float)
    substitution = Column(Boolean)
    removal_timestamp = Column(String)
    last_component = Column(Boolean)

     


