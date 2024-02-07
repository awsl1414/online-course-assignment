from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from utils import get_db, authenticate_user, create_access_token
from crud import get_current_user


router_login = APIRouter(tags=["登录路由"])


@router_login.post("/user_login", summary="登录")
def user_login(
    response: Response,
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = authenticate_user(
        db=db, username=form_data.username, password=form_data.password
    )
    token = create_access_token({"sub": user.username})
    response.set_cookie(
        key="token", value=f"Bearer {token}", httponly=True, samesite="strict"
    )
    return {"access_token": token, "token_type": "bearer"}


@router_login.put("/user_logout", summary="登出")
def user_logout(response: Response, current_user: str = Depends(get_current_user)):
    response.delete_cookie(key="token")
    return HTTPException(status_code=status.HTTP_200_OK, detail="登出成功")
