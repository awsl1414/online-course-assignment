from fastapi import APIRouter, Depends, Query

from typing import List, Optional
from sqlalchemy.orm import Session

from core import get_db
from crud import get_origin_course

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
        teacherName=teacherName,
        courseName=courseName,
        className=className,
        software=software,
        cycle=cycle,
        db=db,
    )
    if not result:
        return Response400(msg="记录不存在")
    return result


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
        teacherName=teacherName,
        courseName=courseName,
        className=className,
        software=software,
        cycle=cycle,
        db=db,
    )
    if not result:
        return Response400(msg="记录不存在")
    return result
