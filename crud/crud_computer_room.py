from sqlalchemy.orm import Session

from models import ModelsComputerRoom
from schemas import SchemasComputerRoomCreate
from utils import general_not_found, general_found


def create_computer_room(db: Session, computer_room_data: SchemasComputerRoomCreate):
    computer_room = (
        db.query(ModelsComputerRoom)
        .filter(
            ModelsComputerRoom.computer_room_name
            == computer_room_data.computer_room_name
        )
        .first()
    )
    if computer_room:
        raise general_found()
    computer_room = ModelsComputerRoom(**computer_room_data.model_dump())
    db.add(computer_room)
    db.commit()
    db.refresh(computer_room)
    return computer_room


def delete_computer_room(db: Session, computer_room_id: int):
    computer_room = (
        db.query(ModelsComputerRoom)
        .filter(ModelsComputerRoom.id == computer_room_id)
        .first()
    )
    if not computer_room:
        raise general_not_found()
    db.delete(computer_room)
    db.commit()
    return computer_room


def update_computer_room(
    db: Session, computer_room_id: int, computer_room_data: SchemasComputerRoomCreate
):
    computer_room = (
        db.query(ModelsComputerRoom)
        .filter(ModelsComputerRoom.id == computer_room_id)
        .first()
    )
    if not computer_room:
        raise general_not_found()
    computer_room.software_name = computer_room_data.software_name
    computer_room.computer_room_name = computer_room_data.computer_room_name
    db.commit()
    return computer_room


def get_computer_room_by_field(db: Session, field_name: str, value: str):
    if value is None or field_name is None:
        return db.query(ModelsComputerRoom).all()
    if hasattr(ModelsComputerRoom, field_name):
        field = getattr(ModelsComputerRoom, field_name)
        return db.query(ModelsComputerRoom).filter(field == value).all()
    else:
        raise general_not_found()
