from pydantic import BaseModel


class Year(BaseModel):
    id: int
    year: int
