from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import get_db
from crud import get_origin_course
from schemas import Response200, Response400

router_course = APIRouter(tags=["课程相关"])


@router_course.get("/get_origin_course")
def get_origin_course_api(teacher_name: str, db: Session = Depends(get_db)):
    result = get_origin_course(db=db, teacher_name=teacher_name)
    if not result:
        return Response400(msg="记录不存在")
    return 
