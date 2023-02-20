from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: str
    title: str
    description: str

class TodoBody(BaseModel):
    title: str
    description: str

class SuccessMsg(BaseModel):
    message: str

class UserBody(BaseModel):
    username: str
    email: str
    password: str
    birthday: str
    avatar: str
    gender: str
    agreement: bool

class UserInfo(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    birthday: str
    avatar: str
    gender: str