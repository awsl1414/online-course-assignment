from fastapi import APIRouter, Depends, Query

from typing import List, Optional
from sqlalchemy.orm import Session

from core import get_db
from crud import get_origin_course, get_main_course

from schemas import Response200, Response400, OriginClassIn

router_course = APIRouter(tags=["课程相关"])


@router_course.get("/get_origin_course", summary="原始课表查询")
def get_origin_course_api(
    db: Session = Depends(get_db),
    teacherName: Optional[str] = Query(None),
    courseName: Optional[str] = Query(None),
    className: Optional[str] = Query(None),
    software: Optional[str] = Query(None),
    cycle: Optional[str] = Query(None),
):
    result = get_origin_course(
        db=db,
        teacherName=teacherName,
        courseName=courseName,
        className=className,
        software=software,
        cycle=cycle,
    )
    if not result:
        return Response400(msg="记录不存在")
    return result


@router_course.get("/get_main_course", summary="详细课表查询")
def get_main_course_api(
    db: Session = Depends(get_db),
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
    result = get_main_course(
        db=db,
        teacherName=teacherName,
        courseName=courseName,
        className=className,
        population=population,
        software=software,
        computerRoomName=computerRoomName,
        week=week,
        weekDay=weekDay,
        lesson=lesson,
        littleLesson=littleLesson,
        cycle=cycle,
    )
    if not result:
        return Response400(msg="记录不存在")
    return result
