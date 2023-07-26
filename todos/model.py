from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    Name: str


class Item(BaseModel):
    item: str
    valid: str
