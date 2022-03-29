from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, Integer, Float, ForeignKey

from ..setup import Base


class State(Base):
    __tablename__ = "state"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    income_tax = Column(Float, nullable=False)
    sales_tax = Column(Float, nullable=False)
    property_tax = Column(Float, nullable=False)
    year_id = Column(Integer, ForeignKey("year.id"))
    
    year = relationship("Year", backref="year")
