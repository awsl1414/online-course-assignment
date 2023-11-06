from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Query, Depends

from models import OriginClass, MainClass
from core import get_db


def get_computer_room_software(
    db: Session,
    computerRoomName: Optional[str] = Query(None),
):
    query = db.query(MainClass).with_entities(MainClass.software)

    filters = {
        MainClass.computerRoomName: computerRoomName,
    }
    for column, value in filters.items():
        if value:
            query = query.filter(column == value)

    return query.all()
