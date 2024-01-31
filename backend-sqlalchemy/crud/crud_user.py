from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer


from models import User
from core import get_password_hash, settings
from jose import JWTError, jwt
from schemas import Response400, UpdateUserIn, Response200

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


def get_current_user(token: str = Depends(oauth2_scheme)):
    print(token)
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWTError",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username


def get_permissioned_user(permissioned_user: User = Depends(get_current_user)):
    if User.permission == 2:
        return permissioned_user
    return HTTPException(status_code=400, detail="非管理员账户")
