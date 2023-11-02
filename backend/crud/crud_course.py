from sqlalchemy.orm import Session

from models import OriginClass

def get_origin_course(db:Session, teacher_name:str):
    result = db.query(OriginClass).filter(OriginClass.teacherName == teacher_name).all()
    return result