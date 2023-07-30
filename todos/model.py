from pydantic import BaseModel
from fastapi import Body
from typing import Optional

# #previous work


class Todo(BaseModel):
    id: int
    Name: str

    class Config:
        schema_extra = {
            "Example": {
                "id": 1,
                "Name": "Jacob"
            }
        }


class Employee(BaseModel):
    EmpId: int = 12
    Name: str
    JobExperience: int = Body(None, ge=3)
    Age: int
    Nationality: str
    Color: Optional[str] = None


class Item(BaseModel):
    Drinks: str
    Fruits: str
    Books: int = Body(None, le=5)
    Price: str
