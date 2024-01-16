from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from core import get_db, get_password_hash
from schemas import UserIn, UpdateUserIn
from crud import create_user, update_user


router_user = APIRouter(tags=["用户相关"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token")


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
