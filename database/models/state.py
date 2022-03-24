from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, Integer, String, Boolean, ForeignKey

from ..setup import Base

from .year import Year


class State(Base):
    __tablename__ = "state"
    id = Column(Integer, primary_key=True, index=True)
