from pydantic import BaseModel, EmailStr
from typing import Optional, List, Union
from fastapi import APIRouter, HTTPException, status

user_router = APIRouter()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str


class UserOut(BaseUser):
    pass


fake_user_db = {}


@user_router.post("/user/", response_model=UserOut)
async def CreatUser(user: UserIn):
    fake_user_db[user.username] = user
    return user


@user_router.get("/user/{username}", response_model=UserOut)
async def RetrieveUser(UserName: str):
    if UserName in fake_user_db:
        return fake_user_db[UserName]
    raise HTTPException(status_code=404, detail="User not found")
