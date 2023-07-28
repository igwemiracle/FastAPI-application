from fastapi import APIRouter, Path, Response
from model import Todo, Employee, Item
from typing import Optional
import json


todo_router = APIRouter()
# todo_list = ["Black", "Blue", "Purple"]
todo_list = []

# @todo_router.post("/todo")
# async def AddTodo(todo: dict) -> dict:
#     todo_list.append(todo)
#     return {"Message": "Todo successfully added!"}
# --------------------------------------------------------


@todo_router.post("/todo")
async def AddTodo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "Message": "Todo successfully added!"
        # "todo": todo_list
    }


@todo_router.get("/todo")
async def RetrieveTodos() -> dict:
    return {
        "Todos": todo_list
    }


@todo_router.get("/todo/{todo_id}")
async def GetSingleID(todo_id: int = Path(..., title="The id of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
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


@todo_router.put("/todo/{todo_id}")
async def UpdateTodoItem(todo_data: Todo,
                         todo_id: int = Path(..., title="Updata Todo ID")):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.Name = todo_data.Name
            return {
                "Message": "| Todo Updated Successfully |",

            }

    return {
        "Message": "Todo with supplied id does not exist!"
    }


@todo_router.delete("/delete/{todo_id}")
async def DeleteSingleTodo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "Message": "Todo deleted successfully"
            }
    return {"Message": "Todo with supplied ID does not exist"}
