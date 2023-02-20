from fastapi import APIRouter
from fastapi import Response, Request, Depends
from fastapi.encoders import jsonable_encoder
from schemas import UserBody, SuccessMsg, UserInfo
from database import (
    db_signup,
    db_login,
)
from auth_utils import AuthJwtCsrf

router = APIRouter()
auth = AuthJwtCsrf()


@router.post("/api/register", response_model=UserInfo)
async def signup(request: Request, user: UserBody):
    user = jsonable_encoder(user)
    new_user = await db_signup(user)
    return new_user


@router.post("/api/login", response_model=SuccessMsg)
async def login(request: Request, response: Response, user: UserBody):    
    user = jsonable_encoder(user)
    token = await db_login(user)
    response.set_cookie(
        key="access_token", value=f"Bearer {token}", httponly=True, samesite="none", secure=True)
    return {"message": "Successfully logged-in"}


@router.post("/api/logout", response_model=SuccessMsg)
def logout(request: Request, response: Response):
    response.set_cookie(key="access_token", value="",
                        httponly=True, samesite="none", secure=True)
    return {'message': 'Successfully logged-out'}


@router.get('/api/user', response_model=UserInfo)
def get_user_refresh_jwt(request: Request, response: Response):
    new_token, subject = auth.verify_update_jwt(request)
    return {'email': subject}