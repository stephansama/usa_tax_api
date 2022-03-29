from pydantic import BaseModel


class State(BaseModel):
    id: int
    name: str
    income_tax: float
    property_tax: float
    sales_tax: float
    year_id: int
    class Config:
        orm_mode = True
