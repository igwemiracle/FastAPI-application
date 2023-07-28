from pydantic import BaseModel, EmailStr
from typing import Optional, Any
from fastapi import APIRouter

user_router = APIRouter()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserInn(BaseUser):
    password: str


# @user_router.post("/userinput/", response_model=UserOut)
# async def userinput(user: UserIn) -> Any:
#     return user


@user_router.post("/user/")
async def create_user(user: UserInn) -> BaseUser:
    return user

# print(help(user_router.include_router))
