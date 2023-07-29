from pydantic import BaseModel, EmailStr
from typing import Optional, List, Union
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
'''
 With the function just below we are able to filter out
 the password element that is not decleared in the output
 model(using pydantic).But by using this method, we are not
 getting the support from  the editor and tools checking the function return type.
 BUT in most cases where we want to do something like this,we want the model
 just to filter/remove some of the data.
 WE can use classes and inheritance to our advantage.
'''


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str

# @user_router.post("/userinput/", response_model=UserOut)
# async def userinput(user: UserIn) -> Any:
#     return user


@user_router.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


@user_router.get("/user/")
async def view_user() -> List[BaseUser]:
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "full_name": "John Doe",
        "password": "*********"  # This field is omitted in the response
    }
    user = BaseUser(**user_data)
    return user
