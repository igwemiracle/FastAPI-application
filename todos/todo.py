from fastapi import APIRouter, Path
from model import Todo, Item


todo_router = APIRouter()
# todo_list = ["Black", "Blue", "Purple"]
todo_list = [{"id": 1, "name": "todo 1"}, {"id": 2, "name": "todo 2"}]

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
