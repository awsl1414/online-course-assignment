from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Query, Depends

from models import OriginClass, MainClass
from core import get_db


def get_origin_course(
    db: Session,
    teacherName: Optional[str] = Query(None),
    courseName: Optional[str] = Query(None),
    className: Optional[str] = Query(None),
    software: Optional[str] = Query(None),
    cycle: Optional[str] = Query(None),
):
    query = db.query(OriginClass)

    filters = {
        OriginClass.teacherName: teacherName,
        OriginClass.courseName: courseName,
        OriginClass.className: className,
        OriginClass.software: software,
        OriginClass.cycle: cycle,
    }
    for column, value in filters.items():
        if value:
            query = query.filter(column == value)
    return query.all()


def get_main_course(
    db: Session,
    teacherName: Optional[str] = Query(None),
    courseName: Optional[str] = Query(None),
    className: Optional[str] = Query(None),
    population: Optional[int] = Query(None),
    software: Optional[str] = Query(None),
    computerRoomName: Optional[str] = Query(None),
    week: Optional[int] = Query(None),
    weekDay: Optional[int] = Query(None),
    lesson: Optional[str] = Query(None),
    littleLesson: Optional[str] = Query(None),
    cycle: Optional[str] = Query(None),
):
    query = db.query(MainClass)

    filters = {
        MainClass.teacherName: teacherName,
        MainClass.courseName: courseName,
        MainClass.className: className,
        MainClass.population: population,
        MainClass.software: software,
        MainClass.computerRoomName: computerRoomName,
        MainClass.week: week,
        MainClass.weekDay: weekDay,
        MainClass.lesson: lesson,
        MainClass.littleLesson: littleLesson,
        MainClass.cycle: cycle,
    }
    for column, value in filters.items():
        if value:
            query = query.filter(column == value)
    return query.all()
