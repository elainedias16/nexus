from sqlalchemy import Column, Integer, String, Index, Boolean, Float, BigInteger, Date, PrimaryKeyConstraint, UniqueConstraint
from database.db_connection import Base


class ComponentModel(Base):
    __tablename__ = "well_components"

    id = Column(BigInteger, primary_key=True)
    well_name = Column(String)  
    component_type = Column(String)
    install_timestamp = Column(Date) #YYYY-MM-DD
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


    __table_args__ = (
        UniqueConstraint( #composite unique key
            'well_name',
            'component_name',
            'install_timestamp',
            name='uq_comp',
            postgresql_nulls_not_distinct=True
        ),
    )
        
