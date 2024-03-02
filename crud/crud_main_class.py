from sqlalchemy import and_
from sqlalchemy.orm import Session

from utils import general_found, general_not_found

from models import ModelsMainClass
from schemas import SchemasMainClassCreate, SchemasMainClassUpdate


# MainClass
def create_main_class(db: Session, main_class_data: SchemasMainClassCreate):
    main_class = (
        db.query(ModelsMainClass)
        .filter(
            and_(
                ModelsMainClass.computer_room_name
                == main_class_data.computer_room_name,
                ModelsMainClass.day == main_class_data.day,
                ModelsMainClass.lesson == main_class_data.lesson,
                ModelsMainClass.cycle == main_class_data.cycle,
            )
        )
        .first()
    )
    if main_class:
        raise general_found()
    main_class = ModelsMainClass(**main_class_data.model_dump())
    db.add(main_class)
    db.commit()
    db.refresh(main_class)
    return main_class


def delete_main_class(db: Session, main_class_id: int):
    main_class = (
        db.query(ModelsMainClass).filter(ModelsMainClass.id == main_class_id).first()
    )
    if not main_class:
        raise general_not_found()
    db.delete(main_class)
    db.commit()
    return main_class


def update_main_class(
    db: Session, main_class_id: int, main_class_data: SchemasMainClassUpdate
):
    main_class = (
        db.query(ModelsMainClass).filter(ModelsMainClass.id == main_class_id).first()
    )
    if not main_class:
        raise general_not_found()
    # 遍历update_data，如果有值，就更新
    update_data = main_class_data.model_dump()
    for key, value in update_data.items():
        if hasattr(main_class, key):
            setattr(main_class, key, value)
    db.commit()
    return main_class


def get_main_class_by_field(db: Session, field_name: str, value: str):
    if field_name is None or value is None:
        return db.query(ModelsMainClass).all()
    if hasattr(ModelsMainClass, field_name):
        field = getattr(ModelsMainClass, field_name)
        return db.query(ModelsMainClass).filter(field == value).all()
    else:
        raise general_not_found()


def get_main_class_all(db: Session):

    return db.query(ModelsMainClass).all()
