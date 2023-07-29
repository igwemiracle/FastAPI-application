from pydantic import BaseModel
from fastapi import Body
from typing import Optional, List


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


# class NewTodo(BaseModel):
#     Name: str


# class TodoItems(BaseModel):
#     todos: List[NewTodo]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "todos": [
#                     {
#                         "Name": "Will Biyers"
#                     },
#                     {
#                         "Name": "Dustin"
#                     }

#                 ]

#             }
#         }


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
