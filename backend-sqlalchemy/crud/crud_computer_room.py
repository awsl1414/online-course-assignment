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


def get_computer_room_floor(db: Session):
    query = db.query(Floors).all()
    query_list = []
    b_set = set()
    c_set = set()
    bn_set = set()
    cn_set = set()
    floor_dict = {}
    tmp_litemst = []
    tmp_litemst2 = []
    c = ""
    b = ""
    for item in query:
        query_list.append(item.classRoomName)
        if item.classRoomName[:1] == "B":
            b_set.add(item.classRoomName)
            bn_set.add(item.classRoomName[:2])
        if item.classRoomName[:1] == "C":
            c_set.add(item.classRoomName)
            cn_set.add(item.classRoomName[:2])
    for i in bn_set:
        for j in b_set:
            if j[:2] == i:
                tmp_litemst2.append(j)
        floor_dict.update({f"{i}": f"{tmp_litemst2}"})
        if b != i:
            tmp_litemst2 = []
    for i in cn_set:
        for j in c_set:
            if j[:2] == i:
                tmp_litemst.append(j)
        floor_dict.update({f"{i}": f"{tmp_litemst}"})
        if c != i:
            tmp_litemst = []

    return floor_dict
