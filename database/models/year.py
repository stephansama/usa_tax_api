from enum import unique
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, Integer, String, Boolean, ForeignKey

from ..setup import Base
from .state import State


class Year(Base):
    __tablename__ = "year"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True)
    states = relationship(State, backref="states", uselist=True)
