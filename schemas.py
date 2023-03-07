from pydantic import BaseModel
from typing import Optional
from decouple import config

CSRF_KEY = config('CSRF_KEY')

class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY

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
    username: Optional[str] = None
    email: str
    birthday: Optional[str] = None
    avatar: Optional[str] = None
    gender: Optional[str] = None

class Csrf(BaseModel):
    csrf_token: str