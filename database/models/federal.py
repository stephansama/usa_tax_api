from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, Integer, ForeignKey

from ..setup import Base


class TaxBracket(Base):
    __tablename__ = "tax_bracket"
    id = Column(Integer, primary_key=True, index=True)

    tax_rate = Column(Float, nullable=False)
    bracket_start = Column(Integer, nullable=False)
    bracket_end = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)

    federal_id = Column(Integer, ForeignKey("federal.id"))
    federal = relationship("Federal", backref="federal")


class Federal(Base):
    __tablename__ = "federal"
    id = Column(Integer, primary_key=True, index=True)

    year_id = Column(Integer, ForeignKey("year.id"))
    year = relationship("Year", backref="federal")

    tax_brackets = relationship(
        TaxBracket, backref="tax_bracket", uselist=True)
