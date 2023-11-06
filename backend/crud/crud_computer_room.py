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


def get_computer_room_floor(db: Session):
    query = db.query(OriginClass).with_entities(MainClass.computerRoomName).all()
    # print(query)

    b_set = set()
    c_set = set()
    floor_dict = {}
    for item in query:
        if item[0][:1] == "B":
            b_set.add(item[0])
            floor_dict.update({f"{item[0][:2]}": f"{list(b_set)}"})
        if item[0][:1] == "C":
            c_set.add(item[0])
            floor_dict.update({f"{item[0][:2]}": f"{list(c_set)}"})

    # print("b_set:", b_set)
    # print("c_set:", c_set)
    # print("floor_dict", floor_dict)
    return floor_dict
