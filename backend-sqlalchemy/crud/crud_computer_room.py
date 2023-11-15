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


def get_computer_room_floor(db: Session, computerRoom: Optional[str] = Query(None)):
    query = db.query(OriginClass).with_entities(MainClass.computerRoomName).all()
    # print(query)

    floor_set = set()
    c_set = set()
    floor_dict = {}
    for item in query:
        if computerRoom:
            if item[0][:1] == computerRoom[:1]:
                floor_set.add(item[0])
                floor_dict.update({f"{item[0][:2]}": f"{list(floor_set)}"})
        else:
            if item[0][:1] == "B":
                floor_set.add(item[0])
                floor_dict.update({f"{item[0][:2]}": f"{list(floor_set)}"})
            if item[0][:1] == "C":
                floor_set.add(item[0])
                floor_dict.update({f"{item[0][:2]}": f"{list(floor_set)}"})

    return floor_dict
