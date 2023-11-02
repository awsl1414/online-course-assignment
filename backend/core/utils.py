import json


import os


from sqlalchemy.orm import Session

from models.models_originclass import OriginClass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def insert_courses_from_json(db: Session):
    with open(f"{BASE_DIR}/course.json", "r", encoding="utf-8") as f:
        courses = json.load(f)["data"]

    for course in courses:
        # 检查是否存在相同的记录
        existing_course = (
            db.query(OriginClass)
            .filter(
                OriginClass.teacherName == course["teacherName"],
                OriginClass.courseName == course["courseName"],
                OriginClass.className == course["className"],
            )
            .first()
        )

        if not existing_course:
            new_course = OriginClass(**course)
            db.add(new_course)

    db.commit()
