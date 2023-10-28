from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from models import User
from core import get_current_user, get_db, get_password_hash
from schemas import Response200, Response400, UserIn, UserInInfo
from crud import create_user

router_user = APIRouter(tags=["用户相关"])


@router_user.post("/create_user", response_model=UserInInfo, summary="创建用户")
def create_user_api(user: UserInInfo, db: Session = Depends(get_db)):
    db_user = create_user(
        db,
        username=user.username,
        password=get_password_hash(user.password),
        # password="12345678",
        empno=user.empno,
        role=user.role
    )
    if not db_user:
        raise HTTPException(status_code=400, detail="用户名已存在")
    return db_user


@router_user.put("/user", summary="修改信息")
def user_update(
    user_form: UserIn,
    user_obj: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    修改当前用户信息
    """

    if result := db.query(User).filter(User.username == user_obj.username).first():
        result.username = user_form.username
        result.hashed_password = get_password_hash(user_form.password)
        db.commit(result)
        return Response200(data=result)
    return Response400(msg="更新失败")
