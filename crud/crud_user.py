from sqlalchemy.orm import Session

from utils import general_found, general_not_found
from models import ModelsUser
from schemas import SchemasUserCreate


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
