from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from utils import settings, general_found, general_not_found
from models import ModelsUser
from schemas import SchemasUserCreate

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/user_login")


def get_current_user(token: str = Depends(oauth2_scheme)):
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


def create_user(db: Session, user_data: SchemasUserCreate):
    user_job_number = (
        db.query(ModelsUser)
        .filter(ModelsUser.job_number == user_data.job_number)
        .first()
    )
    if user_job_number:
        raise general_found()
    user = ModelsUser(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(ModelsUser).filter(ModelsUser.id == user_id).first()
    if not user:
        raise general_not_found()
    db.delete(user)
    db.commit()
    return user


def update_user(db: Session, user_id: int, user_data: SchemasUserCreate):
    user = db.query(ModelsUser).filter(ModelsUser.id == user_id).first()
    if not user:
        raise general_not_found()
    user.username = user_data.username
    user.hashed_password = user_data.hashed_password
    user.job_number = user_data.job_number
    user.permission = user_data.permission
    db.commit()
    return user


def get_user(db: Session, user_id: int):
    user = db.query(ModelsUser).filter(ModelsUser.id == user_id).first()
    if not user:
        raise general_not_found()
    return user
