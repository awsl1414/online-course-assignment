import json, os
from sqlalchemy.orm import Session
from openpyxl import Workbook

# 解决循环导入
import models


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def insert_origin_courses_from_json(db: Session):
    with open(f"{BASE_DIR}/course_origin.json", "r", encoding="utf-8") as f:
        courses = json.load(f)["data"]

    for course in courses:
        # 检查是否存在相同的记录
        existing_course = (
            db.query(models.OriginClass)
            .filter(
                models.OriginClass.teacherName == course["teacherName"],
                models.OriginClass.courseName == course["courseName"],
                models.OriginClass.className == course["className"],
            )
            .first()
        )

        if not existing_course:
            new_course = models.OriginClass(**course)
            db.add(new_course)

    db.commit()


def insert_main_courses_from_json(db: Session):
    with open(f"{BASE_DIR}/course_main.json", "r", encoding="utf-8") as f:
        courses = json.load(f)["data"]

    for course in courses:
        # 检查是否存在相同的记录
        existing_course = (
            db.query(models.MainClass)
            .filter(
                models.MainClass.teacherName == course["teacherName"],
                models.MainClass.courseName == course["courseName"],
                models.MainClass.className == course["className"],
            )
            .first()
        )

        if not existing_course:
            new_course = models.MainClass(**course)
            db.add(new_course)

    db.commit()


def insert_origin_courses_from_xlsx(db: Session):
    # 创建一个工作簿
    wb = Workbook()
    # 获取当前活动的工作表
    ws = wb.active

    max_row = ws.max_row
    

    for rows in ws.iter_rows(min_row = 1, max_row=max_row):
        origin_data = []
        
    wb.save(f"{BASE_DIR}/course_origin.xlsx")
