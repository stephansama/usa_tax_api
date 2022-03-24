

from enum import Enum
from pydantic import BaseModel


class TaxBracket(BaseModel):
    id: int
    tax_rate: int
    bracket_start: int
    bracket_end: int


class Federal(BaseModel):
    id: int
    abbrev: str
    income_tax: float
    sales_tax: float
    property_tax: float
    tax_brackets: list(TaxBracket)


# Filing Status
class Status(Enum):
    single = 1
    married = 2
