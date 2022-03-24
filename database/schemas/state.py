from pydantic import BaseModel


class State(BaseModel):
    id: int
    name: str
    abbrev: str
    income_tax: float
    sales_tax: float
    property_tax: float
