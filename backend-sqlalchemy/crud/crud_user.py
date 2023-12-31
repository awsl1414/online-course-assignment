from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from models import User
from core import get_db, settings, get_password_hash
from schemas import Response400, UpdateUserIn, Response200

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    """
    # oauth2_scheme -> 从请求头中取到 Authorization 的value
    解析token 获取当前用户对象
    :param token: 登录之后获取到的token
    :return: 当前用户对象
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user


def create_user(
    db: Session, username: str, password: str, job_number: str, permission: int
):
    if not db.query(User).filter(User.username == username).first():
        user = User(
            username=username,
            hashed_password=password,
            job_number=job_number,
            permission=permission,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    return Response400(msg="用户已存在")


def update_user(db: Session, user_obj: UpdateUserIn):
    if user := db.query(User).filter(User.username == user_obj.username):
        updates = {
            "username": f"{user_obj.reUsername}",
            "hashed_password": f"{get_password_hash(user_obj.rePassword)}",
            "job_number": f"{user_obj.reJob_number}",
            "permission": f"{user_obj.rePermission}",
        }
        user.update(updates)
        db.commit()
        return Response200(msg="修改成功")
    return Response400(msg="用户不存在")
