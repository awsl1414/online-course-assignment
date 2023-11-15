from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from models import User
from core import get_db, get_password_hash
from schemas import Response200, Response400, UserIn, UpdateUserIn
from crud import create_user, get_current_user, update_user


router_user = APIRouter(tags=["用户相关"])


@router_user.get("/get_current_user", summary="获取当前用户")
def get_current_user_api(db: Session = Depends(get_db)):
    return get_current_user(db=db)


@router_user.post("/create_user", summary="创建用户")
def create_user_api(user: UserIn, db: Session = Depends(get_db)):
    user = create_user(
        db=db,
        username=user.username,
        password=get_password_hash(user.password),
        job_number=user.job_number,
        permission=user.permission,
    )

    return user


@router_user.put("/update_user", summary="修改用户信息")
def user_update(
    user_obj: UpdateUserIn,
    db: Session = Depends(get_db),
):
    """
    修改当前用户信息
    """
    result = update_user(db=db, user_obj=user_obj)
    return result
