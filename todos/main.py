from fastapi import FastAPI
from todo import todo_router
from model import Todo, Item

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to my very own first fast api app"}

todo_list = []


@todo_router.post("/todo")
async def AddTodo(todo: Todo) -> dict:
    todo_list.append(todo)

    return {"Message": "Item successfully added!"}


@todo_router.get("/todo")
async def RetrieveTodos() -> dict:
    return {"todos": todo_list}

app.include_router(todo_router)
