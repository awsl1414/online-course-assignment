from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import get_db
from crud import get_origin_course
from schemas import Response200, Response400

router_class = APIRouter()


@router_class.get("/get_origin_course")
def get_origin_course_api(teacher_name: str, db: Session = Depends(get_db)):
    return get_origin_course(db=db, teacher_name=teacher_name)
