from sqlalchemy import and_
from sqlalchemy.orm import Session

from utils import general_found, general_not_found
from models import ModelsOriginClass
from schemas import SchemasOriginClassCreate, SchemasOriginClassUpdate


# OriginClass
def create_origin_class(db: Session, origin_class_data: SchemasOriginClassCreate):
    origin_class = (
        db.query(ModelsOriginClass)
        .filter(
            and_(
                ModelsOriginClass.teacher_name == origin_class_data.teacher_name,
                ModelsOriginClass.class_name == origin_class_data.class_name,
                ModelsOriginClass.course_name == origin_class_data.course_name,
            )
        )
        .first()
    )
    if origin_class:
        raise general_found()
    origin_class = ModelsOriginClass(**origin_class_data.model_dump())
    db.add(origin_class)
    db.commit()
    db.refresh(origin_class)
    return origin_class


def delete_origin_class(db: Session, origin_class_id: int):
    origin_class = (
        db.query(ModelsOriginClass)
        .filter(ModelsOriginClass.id == origin_class_id)
        .first()
    )
    if not origin_class:
        raise general_not_found()
    db.delete(origin_class)
    db.commit()
    return origin_class


def update_origin_class(
    db: Session, origin_class_id: int, origin_class_data: SchemasOriginClassUpdate
):
    origin_class = (
        db.query(ModelsOriginClass)
        .filter(ModelsOriginClass.id == origin_class_id)
        .first()
    )
    if not origin_class:
        raise general_not_found()
    update_data = origin_class_data.model_dump()
    for key, value in update_data.items():
        if hasattr(origin_class, key):
            setattr(origin_class, key, value)
    db.commit()
    return origin_class


def get_origin_class_by_field(db: Session, field_name: str, value: str):
    if hasattr(ModelsOriginClass, field_name):
        if value is None:
            return db.query(ModelsOriginClass).all()
        field = getattr(ModelsOriginClass, field_name)
        return db.query(ModelsOriginClass).filter(field == value).all()
    else:
        raise general_not_found()


def get_origin_class_all(db: Session):

    return db.query(ModelsOriginClass).all()
