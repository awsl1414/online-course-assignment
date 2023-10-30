from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from models import User
from core import verify_password, create_access_token, get_current_user, get_db
from schemas import Response200, Response400, ResponseToken, UserIn, UserInInfo

router_login = APIRouter(tags=["登录相关"])


@router_login.post("/login", summary="登录")
def user_login(
    response: Response,
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    if user := db.query(User).filter(User.username == form_data.username).first():
        if verify_password(form_data.password, user.hashed_password):
            token = create_access_token({"sub": user.username})
            response.set_cookie(
                key="token", value=token, httponly=True, samesite="strict"
            )
            return ResponseToken(token=token, msg="请求")
    return Response400(msg="请求失败")


@router_login.put("/logout", summary="注销")
def user_logout(response: Response):
    response.delete_cookie(key="token")
    return Response200()
