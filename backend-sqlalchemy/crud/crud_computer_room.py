from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Query, Depends

from models import OriginClass, MainClass, Floors
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
    query = db.query(Floors).all()
    query_list = []
    for i in query:
        query_list.append(i.classRoomName)
    # print(query_list)
    b_set = set()
    c_set = set()
    floor_dict = {}
    for item in query_list:
        if computerRoom:
            if item[:2] == computerRoom[:2]:
                b_set.add(item)
                floor_dict.update({f"{item[:2]}": f"{list(b_set)}"})
        else:
            if item[:1] == "B":
                b_set.add(item)
                for i in b_set:
                    if i[:2] == item[:2]:
                        floor_dict.update({f"{item[:2]}": f"{list(b_set)}"})
            if item[:1] == "C":
                c_set.add(item)
                for i in c_set:
                    if i[:2] == item[:2]:
                        floor_dict.update({f"{item[:2]}": f"{list(c_set)}"})

    return floor_dict
