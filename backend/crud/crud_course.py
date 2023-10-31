from sqlalchemy.orm import Session

from models import Origin

def get_origin_course(db:Session, teacher_name:str):
    result = db.query(Origin).filter(Origin.teacherName == teacher_name).all()
    return result