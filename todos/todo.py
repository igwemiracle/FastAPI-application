from fastapi import APIRouter, Path, Response
from model import Todo, Employee, Item
from typing import Optional
import json


todo_router = APIRouter()
# todo_list = ["Black", "Blue", "Purple"]
todo_list = [
    {"id": 1, "name": "todo 1"},
    {"id": 2, "name": "todo 2"}
]

# @todo_router.post("/todo")
# async def AddTodo(todo: dict) -> dict:
#     todo_list.append(todo)
#     return {"Message": "Todo successfully added!"}


@todo_router.post("/todo")
async def AddTodo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "Message": "Todo successfully added!",
        "todo": todo_list
    }


@todo_router.get("/todo")
async def RetrieveTodos() -> dict:
    return {
        "Todos": todo_list
    }


@todo_router.get("/todo/{todo_id}")
async def GetSingleID(todo_id: int = Path(..., title="The id of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo["id"] == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }


@todo_router.post("/employee")
async def AddEmployee(employee: Employee):
    if (employee.Age > 18):
        new_emp = Employee(EmpId=employee.EmpId,
                           Name=employee.Name,
                           Age=employee.Age,
                           JobExperience=employee.JobExperience,
                           Nationality=employee.Nationality,
                           Color=employee.Color)
        return new_emp
    return {"Message": "Employee not up to age!"}


@todo_router.post("/items/")
async def MyItems(item_id: int, items: Item, QueryString: Optional[str] = None):
    result = {"ItemID": item_id, **items.dict()}
    if items.Price:
        ans = "$"
        result["Price"] = ans+items.Price
    if QueryString:
        result.update({"QueryString": QueryString})
    return result
