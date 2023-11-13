from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Query, Depends

from models import OriginClass, MainClass
from core import get_db

from schemas import Response400, MainClassIn, Response200


def get_origin_course(
    db: Session,
    teacherName: Optional[str] = Query(None),
    teacherRoom: Optional[str] = Query(None),
    courseName: Optional[str] = Query(None),
    className: Optional[str] = Query(None),
    software: Optional[str] = Query(None),
    cycle: Optional[str] = Query(None),
):
    query = db.query(OriginClass)

    filters = {
        OriginClass.teacherName: teacherName,
        OriginClass.teacherRoom: teacherRoom,
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
    teacherRoom: Optional[str] = Query(None),
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
        MainClass.teacherRoom: teacherRoom,
        MainClass.courseName: courseName,
        MainClass.className: className,
        MainClass.population: population,
        MainClass.software: software,
        MainClass.week: week,
        MainClass.weekDay: weekDay,
        MainClass.lesson: lesson,
        MainClass.littleLesson: littleLesson,
        MainClass.cycle: cycle,
    }
    for column, value in filters.items():
        if value:
            query = query.filter(column == value)
    if computerRoomName:
        return query.filter(
            MainClass.computerRoomName.ilike(f"%{computerRoomName}%")
        ).all()
    return query.all()


# def add_main_course(
#     db: Session,
#     teacherName: str,
#     teacherRoom: str,
#     courseName: str,
#     className: str,
#     population: int,
#     software: str,
#     computerRoomName: str,
#     week: int,
#     weekDay: int,
#     lesson: str,
#     littleLesson: str,
#     cycle: str,
# ):
#     if (
#         not db.query(MainClass)
#         .filter(MainClass.teacherName == teacherName)
#         .filter(MainClass.courseName == courseName)
#         .first()
#     ):
#         mainclass = MainClass(
#             teacherName=teacherName,
#             teacherRoom=teacherRoom,
#             courseName=courseName,
#             className=className,
#             population=population,
#             software=software,
#             computerRoomName=computerRoomName,
#             week=week,
#             weekDay=weekDay,
#             lesson=lesson,
#             littleLesson=littleLesson,
#             cycle=cycle,
#         )
#         db.add(mainclass)
#         db.commit()
#         db.refresh(mainclass)
#         return mainclass
#     return Response400(msg="用户已存在")


def add_main_course(db: Session, formData: MainClassIn):
    if (
        not db.query(MainClass)
        .filter(MainClass.teacherName == formData.teacherName)
        .filter(MainClass.courseName == formData.courseName)
        .first()
    ):
        mainclass = MainClass(**formData.model_dump())
        db.add(mainclass)
        db.commit()
        db.refresh(mainclass)
        return mainclass
    return Response400(msg="数据已存在")


def delete_main_course(db: Session, id: int):
    query = db.query(MainClass).get(id)
    if query:
        db.delete(query)
        db.commit()
        return Response200(msg="删除成功")
    return Response400(msg="数据不存在")


def delete_origin_course(db: Session, id: int):
    query = db.query(OriginClass).get(id)
    if query:
        db.delete(query)
        db.commit()
        return Response200(msg="删除成功")
    return Response400(msg="数据不存在")
