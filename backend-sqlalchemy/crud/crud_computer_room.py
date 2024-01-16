from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Query
from models import MainClass, Floors


def get_computer_room_software(
    db: Session,
    computerRoomName: Optional[str] = Query(None),
):
    query = (
        db.query(MainClass.software)
        .filter(MainClass.computerRoomName == computerRoomName)
        .all()
    )

    return query


def get_computer_room_floor(db: Session):
    query = db.query(Floors.classRoomName).all()

    floor_dict = {}
    for item in query:
        class_room = item.classRoomName
        floor_prefix = class_room[:1]
        floor_dict.setdefault(floor_prefix, []).append(class_room)

    return floor_dict
